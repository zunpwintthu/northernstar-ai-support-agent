import json
from typing import Any
import streamlit as st

from google import genai

GEMINI_MODEL = "gemini-flash-latest"
##OLLAMA_URL = "http://localhost:11434/api/generate"
## OLLAMA_MODEL = "llama3.2"


def build_prompt(customer_email: str) -> str:
    return f"""
You are a customer-support assistant for NorthenStar, a footwear company.

Analyze the customer email and return exactly one valid JSON object.

Use this exact structure:

{{
  "category": "delivery",
  "urgency": "medium",
  "sentiment": "negative",
  "summary": "Short summary of the customer issue",
  "draft_reply": "Professional and empathetic reply",
  "requires_human_review": true,
  "review_reason": "Reason for human review"
}}

Allowed category values:
delivery, return, refund, product_question, complaint, damaged_product, other

Allowed urgency values:
low, medium, high

Allowed sentiment values:
positive, neutral, negative

Business rules:
1. Never promise a refund.
2. Never claim that an order was found, updated, cancelled, or refunded.
3. Never invent delivery dates, prices, stock levels, policies, or customer details.
4. Require human review for refunds, payment disputes, legal threats,
   safety issues, severe complaints, or actions involving an order.
5. Keep the draft reply friendly, professional, and concise.
6. Ask for missing order information when necessary.
7. Return JSON only.
8. Do not use Markdown.
9. Do not add explanations before or after the JSON.
10. Put every required field at the top level.

Customer email:

{customer_email}
""".strip()


def extract_result(result: Any) -> dict[str, Any]:
    if not isinstance(result, dict):
        raise RuntimeError("The AI response was not a JSON object.")

    required_fields = {
        "category",
        "urgency",
        "sentiment",
        "summary",
        "draft_reply",
        "requires_human_review",
        "review_reason",
    }

    if required_fields.issubset(result.keys()):
        return result

    wrapper_names = [
        "analysis",
        "result",
        "response",
        "output",
        "data",
    ]

    for wrapper_name in wrapper_names:
        nested_value = result.get(wrapper_name)

        if isinstance(nested_value, dict):
            if required_fields.issubset(nested_value.keys()):
                return nested_value

    for value in result.values():
        if isinstance(value, dict):
            if required_fields.issubset(value.keys()):
                return value

    available_fields = ", ".join(result.keys())

    raise RuntimeError(
        "The AI returned an unexpected JSON structure. "
        f"Available fields: {available_fields}. "
        f"Full response: {json.dumps(result, indent=2)}"
    )


def validate_result(result: dict[str, Any]) -> None:
    required_fields = {
        "category",
        "urgency",
        "sentiment",
        "summary",
        "draft_reply",
        "requires_human_review",
        "review_reason",
    }

    missing_fields = required_fields - result.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise RuntimeError(f"Missing required fields: {missing}")

    valid_categories = {
        "delivery",
        "return",
        "refund",
        "product_question",
        "complaint",
        "damaged_product",
        "other",
    }

    valid_urgencies = {"low", "medium", "high"}
    valid_sentiments = {"positive", "neutral", "negative"}

    if result["category"] not in valid_categories:
        result["category"] = "other"

    if result["urgency"] not in valid_urgencies:
        result["urgency"] = "medium"

    if result["sentiment"] not in valid_sentiments:
        result["sentiment"] = "neutral"

    if not isinstance(result["requires_human_review"], bool):
        value = str(result["requires_human_review"]).lower()
        result["requires_human_review"] = value in {
            "true",
            "yes",
            "1",
        }


def call_gemini(customer_email: str) -> dict[str, Any]:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except KeyError as exc:
        raise RuntimeError(
            "GEMINI_API_KEY is missing from Streamlit secrets."
        ) from exc

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=build_prompt(customer_email),
            config={
                "temperature": 0.1,
                "response_mime_type": "application/json",
            },
        )

    except Exception as exc:
        raise RuntimeError(
            f"Gemini API request failed: {exc}"
        ) from exc

    model_output = response.text

    if not model_output:
        raise RuntimeError("Gemini returned an empty response.")

    try:
        parsed_output = json.loads(model_output)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Gemini did not return valid JSON: {model_output}"
        ) from exc

    result = extract_result(parsed_output)
    validate_result(result)

    return result


def load_example_email() -> str:
    return """
Hi NorthenStar Support,

I ordered a pair of running shoes last week, but I received the wrong
size. I ordered size 10, but received size 8.

Can you please help me get the correct size as soon as possible?

Thanks,
Amanda
""".strip()


st.set_page_config(
    page_title="NorthenStar Support AI",
    page_icon="👟",
    layout="wide",
)

st.title("👟 NorthenStar Customer Support AI")

st.caption(
    "Analyze customer emails, prioritize requests, and prepare reply drafts."
)

with st.sidebar:
    st.header("MVP Features")

    st.write("• Email classification")
    st.write("• Urgency detection")
    st.write("• Sentiment analysis")
    st.write("• AI-generated reply")
    st.write("• Human review flagging")

    st.divider()

    st.info(
        "The assistant drafts responses only. "
        "A support employee approves customer-facing actions."
    )

if "customer_email" not in st.session_state:
    st.session_state.customer_email = ""

if st.button("Load sample email"):
    st.session_state.customer_email = load_example_email()

customer_email = st.text_area(
    "Customer email",
    key="customer_email",
    height=220,
    placeholder="Paste the customer's email here...",
)

analyze_button = st.button(
    "Analyze email",
    type="primary",
    use_container_width=True,
)

if analyze_button:
    if not customer_email.strip():
        st.warning("Please enter a customer email.")

    else:
        with st.spinner("Analyzing customer email..."):
            try:
                result = call_gemini(customer_email)

            except RuntimeError as error:
                st.error(f"Error during analysis: {error}")

            else:
                st.success("Email analyzed successfully.")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Category",
                        result["category"].replace("_", " ").title(),
                    )

                with col2:
                    st.metric(
                        "Urgency",
                        result["urgency"].title(),
                    )

                with col3:
                    st.metric(
                        "Sentiment",
                        result["sentiment"].title(),
                    )

                st.subheader("Issue summary")
                st.write(result["summary"])

                if result["requires_human_review"]:
                    st.warning("Human review required")
                else:
                    st.success("Standard support review")

                st.write(result["review_reason"])

                st.subheader("Suggested reply")

                edited_reply = st.text_area(
                    "Review and edit the reply",
                    value=result["draft_reply"],
                    height=220,
                )

                st.download_button(
                    label="Download reply",
                    data=edited_reply,
                    file_name="customer_reply.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

                with st.expander("View structured AI result"):
                    st.json(result)
