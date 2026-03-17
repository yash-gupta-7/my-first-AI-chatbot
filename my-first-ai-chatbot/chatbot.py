from dotenv import load_dotenv
from os import getenv
from langchain_groq import ChatGroq

load_dotenv()
llm= ChatGroq(model=getenv("MODEL_NAME"), api_key=getenv("GROQ_API_KEY"))

print("MY FIRST CHATBOT! Type 'exit' to quit.\n")
while True:
    user_input = input("You: \n")
    if user_input.lower() == "exit":
        break
    response = llm.invoke(user_input)
    print(f"CHATBOT : {response.content}\n")