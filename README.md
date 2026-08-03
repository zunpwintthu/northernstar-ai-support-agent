# 👟 NorthernStar AI Support Agent (https://northernstar-ai-email-support.streamlit.app)

An AI-powered customer support assistant built with **Python**, **Streamlit**, and **Google Gemini**.

This project demonstrates how Generative AI can help customer support teams analyze customer emails, classify requests, determine urgency, detect sentiment, and generate professional reply drafts while keeping humans in the approval workflow.

> **Note:** This is a portfolio project created for learning and demonstration purposes. It is not affiliated with any specific company.

## ✨ Features

- 📧 Customer email analysis
- 🏷️ Email classification
- ⚡ Urgency detection
- 😊 Sentiment analysis
- 📝 AI-generated reply drafts
- 👨‍💼 Human review recommendation
- 💾 Download reply

---

# 🏗️ Architecture

```text
Customer Email
        │
        ▼
 Streamlit Web Application
        │
        ▼
 Prompt Engineering
        │
        ▼
 Google Gemini API
        │
        ▼
 Structured JSON Response
        │
        ▼
 Customer Support Dashboard
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web UI |
| Google Gemini | Large Language Model |
| Google GenAI SDK | Gemini Integration |

---

# 📂 Project Structure

```text
northernstar-ai-support-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/zunpwintthu/northernstar-ai-support-agent.git

cd northernstar-ai-support-agent
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate

macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Google Gemini

Create the folder

```text
.streamlit/
```

Create

```text
.streamlit/secrets.toml
```

Add your API key

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

Get a free API key from Google AI Studio:

https://aistudio.google.com/

---

# ▶️ Run

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 📧 Example

### Input

```
Hi,

I ordered size 10 but received size 8.

Can you help me exchange it?

Thanks.
```

### Output

**Category**

Return

**Urgency**

Medium

**Sentiment**

Negative

**Summary**

Customer received the wrong shoe size and requests an exchange.

**Suggested Reply**

```
Hello,

Thank you for contacting us.

We're sorry that you received the wrong shoe size.

Please provide your order number so our support team can assist you with the exchange.

Kind regards,
Customer Support
```

---

# 🔒 Human-in-the-loop

The AI **does not** automatically send emails.

High-risk cases such as:

- Refund requests
- Payment disputes
- Legal issues
- Safety concerns

are flagged for manual review.

---

# 🚀 Future Improvements

- RAG Knowledge Base
- Product Catalog Search
- Order Tracking API
- CRM Integration
- Email Automation
- LangGraph Agent Workflow
- Confidence Score
- Authentication
- Docker Deployment
- Monitoring Dashboard

---

# 📷 Screenshot

> Add a screenshot here after deployment.

```text
assets/demo.png
```

```markdown
![Application Screenshot](assets/demo.png)
```

---

# 🎯 Skills Demonstrated

- Prompt Engineering
- Google Gemini API
- Streamlit Development
- JSON Structured Output
- Human-in-the-loop AI
- Python
- AI Application Development
- Customer Support Automation

---

# 👨‍💻 Author

**Zun**

AI Engineer Portfolio Project

Built to demonstrate practical AI engineering skills using Python, Streamlit, and Google Gemini.
