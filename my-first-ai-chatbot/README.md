# 🤖 ChatBot AI — Beginner-Friendly AI Teacher Chatbot

An interactive AI chatbot built using **LangChain, Groq, and Gradio** that teaches AI concepts in a **simple, conversational, beginner-friendly way**.

---

## 🚀 What This Project Does

ChatBot AI acts like a **friendly teacher** who:

* Explains AI concepts in very simple language
* Teaches like you're a beginner (even a 10-year-old)
* Uses examples and analogies
* Asks follow-up questions to keep learning interactive

---

## 🧠 Core Idea

Instead of giving complex technical explanations, this chatbot:

* Breaks concepts into **small, easy steps**
* Uses **short sentences**
* Keeps the conversation **engaging and interactive**

---

## 🏗️ Project Structure

```bash
project/
│
├── app.py              # Main chatbot app
├── .env                # API keys (NOT pushed to Git)
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Tech Stack

* **LangChain** → Prompt + LLM chaining
* **Groq API** → Fast LLM inference
* **Gradio** → Web UI for chatbot
* **Python dotenv** → Environment variable management

---

## 🛠️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd project
```

---

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Create `.env` File

```bash
touch .env
```

Add the following:

```env
MODEL_NAME=your_model_name
GROQ_API_KEY=your_api_key
```

⚠️ Never push `.env` to GitHub

---

### Step 5: Run the App

```bash
python app.py
```

---

## 🌐 Access the App

After running, open:

```
http://127.0.0.1:7860
```

---

## 🧩 How It Works

### 1. AI Personality

The chatbot is guided by a system prompt:

* Acts like a **teacher**
* Explains simply
* Encourages users
* Asks questions after each response

---

### 2. LangChain Flow

```python
prompt → LLM → Response
```

* User input is passed into a prompt template
* Sent to Groq LLM
* Response is returned to UI

---

### 3. Gradio Interface

* Chat-style UI
* Real-time responses
* Simple and interactive

---

## 📦 Requirements

Example `requirements.txt`:

```txt
gradio
python-dotenv
langchain
langchain-core
langchain-groq
```

---

## 🔐 Important Notes

* Do NOT push:

  * `.env`
  * `venv/`
* Keep API keys secure
* Use `.gitignore`

---

## 🚀 Future Improvements

* Add memory (chat history understanding)
* Add voice input/output
* Deploy on Hugging Face Spaces or Render
* Multi-language support
* Save learning progress

---

## 💡 Learning Outcomes

This project helps you understand:

* LLM integration in real apps
* Prompt engineering
* Building chat interfaces
* API-based AI systems

---

## 👨‍💻 Author

Yash Gupta

---
