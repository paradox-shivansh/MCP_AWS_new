import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = llm.invoke(user_input)

    print("AI:", response.content)