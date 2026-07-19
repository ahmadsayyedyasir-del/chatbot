import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


SYSTEM_PROMPT = """
You are Neurofive Solutions Support Assistant.

Rules:
- Be friendly and professional.
- Help students with Python, AI, FastAPI, Docker, LangChain, LangGraph and Machine Learning.
- If asked something unrelated, politely say that your role is to assist with technical learning.
- Keep answers concise.
"""


while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    response = client.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", user)
        ]
    )

    print("\nBot:", response.content)