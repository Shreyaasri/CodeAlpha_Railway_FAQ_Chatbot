# 🚆 RailBot AI — Railway Inspection FAQ Chatbot

**RailBot AI** is a Python-based FAQ chatbot designed to answer common questions about railway track inspection robots, crack detection, sensors, GPS-based localization, and railway safety.

## ✨ Features

- 💬 Interactive chatbot interface built with Streamlit
- 🤖 FAQ matching using Python text processing
- 🚆 Railway inspection and crack detection information
- 📡 Information about sensors, GPS, and wheel encoders
- ⚡ Quick question suggestions for easy interaction
- 🛡️ Safety-focused answers explaining the role of human inspectors

## 🛠️ Technologies Used

- Python
- Streamlit
- JSON
- Regular expressions
- `difflib` for FAQ similarity matching

## 📂 Project Structure

```text
Railway_FAQ_Chatbot/
├── app.py
├── chatbot.py
├── faqs.json
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/Shreyaasri/RailBot-AI.git
   ```

2. Open the project folder:

   ```bash
   cd RailBot-AI
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## 🧠 How It Works

1. The user enters a question about railway inspection.
2. The chatbot processes the question and compares it with stored FAQs.
3. It returns the answer for the closest matching question.
4. If no suitable match is found, it displays a fallback response.

## 🎯 Purpose

The project demonstrates how a lightweight FAQ chatbot can make information about railway inspection robots accessible through a simple, user-friendly interface.

**Note:** This is an informational FAQ chatbot. It does not independently inspect real railway tracks or diagnose actual track defects.

## 👩‍💻 Author

**Shreya Kumari**


## 📄 License

This project is intended for educational and demonstration purposes.

