# 🧠 FocusBuddy AI

> **Study Smarter, Not Harder.**
> An empathetic, AI-powered study coach that adapts your schedule to your real-time energy levels.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## 💡 Inspiration
Traditional study planners are rigid. They treat students like robots with constant energy. But in reality, some days we are ready for deep calculus, and other days we are barely running on 10% battery.

**FocusBuddy AI** solves burnout by acting as a compassionate coach. It uses the latest **Google Gemini 2.5 Flash** model to generate a psychological study strategy based on your current energy level (Low, Medium, or High).

## ✨ Features
* **Energy-Adaptive Planning:**
    * ⚡ **High Energy:** Generates deep-work sessions (Active Recall, Feynman Technique).
    * 🔋 **Low Battery:** Generates gentle, low-friction tasks (Video reviews, scanning notes).
* **Real-Time AI Generation:** Custom prompts ensure every plan is unique to the specific subject and timeframe.
* **Universal AI Connector:** Built with a custom HTTP implementation to bypass library versioning issues and access experimental Gemini models.
* **Clean UI:** Distraction-free interface built with Bootstrap 5 and Markdown rendering.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **AI Model:** Google Gemini 2.5 Flash (via direct REST API)
* **Frontend:** HTML5, Bootstrap 5, Custom CSS
* **Utilities:** `requests` (API handling), `markdown` (Text formatting)

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/focusbuddy-ai.git](https://github.com/YOUR_USERNAME/focusbuddy-ai.git)
cd focusbuddy-ai

```

### 2. Install Dependencies

You need Django and the requests library.

```bash
pip install django requests markdown

```

### 3. Set Up Your API Key

To keep the project secure, the API key is not included in the code.

1. Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Open `focusbuddy/core/views.py`.
3. Find the line `GENAI_API_KEY` and paste your key:
```python
GENAI_API_KEY = "PASTE_YOUR_REAL_KEY_HERE"

```

Navigate to the inner folder where `manage.py` is located:

```bash
cd focusbuddy
python manage.py runserver

```

### 5. Access the App

Open your browser and go to:
`http://127.0.0.1:8000/`

---

## 📂 Project Structure

```text
focusbuddy_ai/
│
├── focusbuddy/            # Main Project Folder
│   ├── core/              # The App Logic
│   │   ├── migrations/    # Database migrations
│   │   ├── templatetags/  # Custom Markdown filters
│   │   ├── models.py      # Database structure
│   │   ├── views.py       # AI Logic & Universal Connector
│   │   └── urls.py        # Routing
│   ├── templates/         # HTML Files (index.html)
│   └── manage.py          # Django Command Tool
│
└── README.md              # Documentation

```

## 🧠 The "Universal Connector"

During the hackathon, we encountered deprecation issues with the standard Python client libraries for the newest Gemini models.

To solve this, we wrote a **custom HTTP handler** in `views.py` using the `requests` library. This allows FocusBuddy to:

1. Connect directly to Google's `v1beta` REST endpoints.
2. Bypass library compatibility errors.
3. Utilize the bleeding-edge **Gemini 2.5 Flash** model reliably.

##  What's Next?

* **Pomodoro Timer:** Embedding a live timer into the generated plan.
* **User Accounts:** Saving study history to track progress over time.
* **Voice Mode:** Speech-to-text integration for hands-free coaching.

---
