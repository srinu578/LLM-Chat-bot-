# LLM-Chat-bot-
# 🌐 Language Learning Chatbot with Mistake Tracking

This project is a conversational chatbot designed to help users practice and improve their skills in a foreign language by simulating real-life scenarios. It gives real-time feedback, corrects mistakes gently, and tracks user progress using a local SQLite database.

---

## 📌 Features

- 🔤 **Multi-language Setup**: Choose your known language and the one you're learning.
- 🧠 **OpenAI-Powered**: Uses GPT via LangChain to simulate realistic conversations.
- 🎭 **Scene-based Conversations**: Roleplay with the bot in realistic contexts (e.g., ordering at a café).
- ✍️ **Mistake Detection & Feedback**: AI detects mistakes, provides corrections, and explains them.
- 💾 **SQLite Integration**: Logs user mistakes with explanations for later review.
- 🧾 **End-of-Session Summary**: Displays a full list of all mistakes and explanations made during the session.

---

## ⚙️ Technologies Used

- Python 3.12
- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/) (`langchain-openai`, `langchain-community`)
- SQLite for local data logging


---

## 📦 How to Run

1. **Install dependencies**  
```bash
pip install -U openai langchain langchain-openai langchain-community


export OPENAI_API_KEY="your-api-key-here"  # for Linux/macOS
set OPENAI_API_KEY=your-api-key-here       # for Windows CMD


Run the Script:
python Ass.py
