# 🧮 Gradio Calculator App

A simple and interactive calculator web app built using **Gradio** with dynamic branding support via a JSON configuration file.

---

## 🚀 Features

* Perform basic arithmetic operations:

  * Addition (+)
  * Subtraction (-)
  * Multiplication (*)
  * Division (/)
* Clean UI powered by **Gradio Soft Theme**
* Dynamic branding using `branding.json`
* Modular code structure (separation of logic and UI)

---

## 🏗️ Project Structure

```
project/
│
├── app.py              # Main Gradio app
├── calculator.py       # Calculation logic
├── branding.json       # Branding configuration
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ How It Works

### 1. Branding System

The app reads branding details from `branding.json`:

```json
{
  "brand": {
    "organizationShortName": "Your App Name",
    "slogan": "Your tagline here"
  }
}
```

These values dynamically update:

* App title
* App description

---

### 2. Core Logic

The calculation is handled in `calculator.py`:

```python
def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
```

---

### 3. UI Layer (Gradio)

The UI is built using Gradio:

* Inputs:

  * First Number
  * Operator (Radio buttons)
  * Second Number
* Output:

  * Result textbox

---

## 🛠️ Installation & Setup

### Step 1: Clone the repository

```bash
git clone <your-repo-url>
cd project
```

---

### Step 2: Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the app

```bash
python app.py
```

---

## 🌐 Access the App

After running, Gradio will provide a local URL like:

```
http://127.0.0.1:7860
```

Open it in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```
gradio
```

---

## 🔐 Important Notes

* Do **not** push `venv/` to Git
* Keep sensitive data out of `branding.json`
* Use `.env` for secrets if needed

---

## 🚀 Future Improvements

* Add advanced operations (%, power, etc.)
* Input validation (division by zero handling)
* History tracking
* Deploy on Hugging Face / Render / AWS

---

## 💡 Learning Outcome

This project demonstrates:

* UI building with Gradio
* Clean code separation
* Config-driven design (branding system)
* Basic production practices

---

## 👨‍💻 Author

Yash Gupta

---
