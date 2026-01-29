from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    
    ALLOWED_MODEL_NAMES=[
        "openai/gpt-oss-20b",
        "llama-3.1-8b-instant",
        "openai/gpt-oss-120b"
    ]
    
settings=Settings()
