from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

responce = model.invoke("Hello, I am learning langhcain, Who are you?")

print(responce)