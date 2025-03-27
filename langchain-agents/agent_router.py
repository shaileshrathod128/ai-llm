import os
from dotenv import load_dotenv
from langchain.llms import OpenAI, Replicate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
import replicate

# Load environment variables from .env
load_dotenv()

# Assign API keys from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

# Initialize OpenAI model for general-purpose Q&A
openai_llm = OpenAI(temperature=0.5)

# Initialize Mistral (via Replicate) for summarization
mistral_llm = Replicate(
    model="mistralai/mistral-7b-instruct-v0.1",
    model_kwargs={
        "temperature": 0.3,
        "max_new_tokens": 512,
        "top_p": 0.95
    }
)

# Prompt for OpenAI (general Q&A)
general_prompt = PromptTemplate.from_template(
    "You are a helpful assistant. Answer the following question:\n{input}"
)

# Prompt for Mistral (summarization tasks)
summarization_prompt = PromptTemplate.from_template(
    "You are a summarization assistant. Summarize the following text:\n\n{input}"
)

# LLM chains for each task
general_chain = LLMChain(llm=openai_llm, prompt=general_prompt)
summary_chain = LLMChain(llm=mistral_llm, prompt=summarization_prompt)

# Route query to appropriate model
def route_query(user_input):
    trigger_words = ["summarize", "summary", "tl;dr", "reduce", "compress"]
    if any(word in user_input.lower() for word in trigger_words):
        return summary_chain.run(user_input)
    else:
        return general_chain.run(user_input)

# Run interactively
if __name__ == "__main__":
    print("🧠 Multi-Model LangChain Agent (OpenAI + Mistral for Summarization)\n")
    while True:
        query = input("Ask something (or type 'exit'): ")
        if query.lower() == "exit":
            break
        try:
            response = route_query(query)
            print("\n🤖 Response:\n", response)
        except Exception as e:
            print("⚠️ Error:", str(e))
