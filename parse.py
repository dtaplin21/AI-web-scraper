from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "you are tasked with extrcting specific information from the following text content: {dom_content}"
)

model = OllamaLLM(model="llama3")

def parse_with_ollama(dom_chunks, parse_description):
    