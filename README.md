# 👟 NorthernStar Customer Support AI (https://northernstar-ai-email-support.streamlit.app) 

An AI-powered customer support assistant built with **Python**, **Streamlit**, and **Ollama**.

This project demonstrates how Generative AI can help customer support teams analyze incoming emails, classify requests, determine urgency, and draft professional replies while keeping a human in the approval loop.

---

## 🚀 Features

- 📧 Analyze customer emails
- 🏷️ Classify support requests
- ⚡ Detect urgency
- 😊 Detect customer sentiment
- 📝 Generate professional reply drafts
- 👨‍💼 Human review recommendation
- 💾 Download drafted response

---

## Architecture

```text
Customer Email
        │
        ▼
 Streamlit Web UI
        │
        ▼
 Prompt Builder
        │
        ▼
 Ollama (llama3.2)
        │
        ▼
 Structured JSON
        │
        ▼
 Display Analysis
```

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web UI |
| Ollama | Local LLM |
| Requests | HTTP Client |

---

## Project Structure

```text
northerStar-support-ai/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/sunnystep-support-ai.git

cd sunnystep-support-ai
```

Create virtual environment

```bash
python3 -m venv .venv
```

Activate

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```cmd
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Install Ollama

https://ollama.com

Download the model

```bash
ollama pull llama3.2
```

Verify

```bash
ollama list
```

---

## Run the Application

Start Ollama

```bash
ollama serve
```

> If you see "address already in use", Ollama is already running.

Run Streamlit

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

## Example Workflow

Customer Email

```
Hi,

I ordered size 10 but received size 8.

Can you help me exchange it?

Thanks.
```

↓

AI Analysis

- Category: Return
- Urgency: Medium
- Sentiment: Negative

↓

AI Reply Draft

```
Hello,

Thank you for contacting NorthernStar.

We're sorry to hear that you received the wrong size.

Please reply with your order number and we will assist you with the exchange process.

Kind regards,
NorthernStar Support
```

---

## Future Improvements

- RAG Knowledge Base
- Product Catalog Search
- Order Tracking API
- CRM Integration
- Email Automation
- Multi-Agent Workflow
- Analytics Dashboard
- Authentication
- Docker Deployment
- Cloud LLM Support

---

## Production Architecture

```text
Customer
      │
      ▼
Streamlit
      │
      ▼
API Gateway
      │
      ▼
LLM
      │
      ├──────────► Order API
      │
      ├──────────► Product Database
      │
      ├──────────► Company Knowledge Base
      │
      └──────────► CRM
      │
      ▼
Human Approval
      │
      ▼
Customer Reply
```

---

## Current Limitations

This MVP uses a **local Ollama server**.

When deploying to Streamlit Community Cloud, replace the local LLM with a hosted provider such as:

- OpenAI
- Google Gemini
- Groq
- Azure OpenAI

---

## Author

**Zun**

AI Engineer Portfolio Project

Built for the NorthernStar AI Platform Engineer Interview.
