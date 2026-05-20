from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()

class AgentSettings(BaseSettings):
    GROQ_API_KEY:str
    DOCUMENT_DIR:str
    VECTOR_STORAGE_DIR:str
    COLLECTION_NAME:str
    MODEL_NAME:str
    MODEL_TEMPERATURE:float

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra= "allow"