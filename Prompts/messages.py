from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini_v2024-07-18")

messages = [
    SystemMessage(content="You are a helpful assistance"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages).content
messages.append(AIMessage(content=result))
print(messages)
