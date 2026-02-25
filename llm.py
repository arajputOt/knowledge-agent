from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

response = llm.invoke("Say hello in one sentence")

print(response.content)
