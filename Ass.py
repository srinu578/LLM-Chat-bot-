import sqlite3
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# os.environ['OPENAI_API_KEY'] = "your-api-key-here"
# Set this in your environment before running

# Initialize the ChatOpenAI instance
chat = ChatOpenAI(temperature=0.7, openai_api_key=os.environ["OPENAI_API_KEY"])
# Setup SQLite database
conn = sqlite3.connect("mistakes.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS mistakes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    correction TEXT,
    explanation TEXT
)
""")
conn.commit()

# Helper function to log mistakes
def log_mistake(user_input, correction, explanation):
    cursor.execute("INSERT INTO mistakes (user_input, correction, explanation) VALUES (?, ?, ?)",
                   (user_input, correction, explanation))
    conn.commit()

# Scene setup
learning_language = "Spanish"
known_language = "English"
level = "Beginner"

scene = f"You are a friendly waiter at a Spanish cafe helping a customer (beginner) practice Spanish. Only use simple Spanish and correct their mistakes gently."

conversation = [
    SystemMessage(content=scene),
    HumanMessage(content="¡Hola! ¿Qué te gustaría pedir hoy?")
]
print("👋 Welcome to the Spanish Language Learning Chatbot!")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    if not user_input.strip():
        print("Please enter something.")
        continue

    conversation.append(HumanMessage(content=user_input))
    response = chat(conversation)
    bot_reply = response.content

    print(f"Bot: {bot_reply}")

    # Ask OpenAI to detect mistakes (simple version)
    mistake_check = chat([
        SystemMessage(content="You are a language tutor."),
        HumanMessage(content=f"The user said: '{user_input}' in Spanish. Are there any mistakes? If so, give a correction and brief explanation. If not, say 'No mistakes.'")
    ])

    feedback = mistake_check.content
    print(f"Feedback: {feedback}\n")

    if "No mistakes" not in feedback:
        # Basic parsing (not foolproof)
        parts = feedback.split("Correction:")
        if len(parts) > 1:
            correction = parts[1].strip()
            explanation = feedback.replace(parts[0], "").replace(correction, "").strip()
            log_mistake(user_input, correction, explanation)

# At end of session, show mistakes
print("\nSummary of your mistakes:")
cursor.execute("SELECT user_input, correction, explanation FROM mistakes")
rows = cursor.fetchall()
for i, (ui, corr, expl) in enumerate(rows, 1):
    print(f"{i}. You said: '{ui}' | Correction: '{corr}' | Explanation: {expl}")

conn.close()
