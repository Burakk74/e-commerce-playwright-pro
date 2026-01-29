import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    USER_EMAIL = os.getenv("VALID_USER_EMAIL")
    PASSWORD = os.getenv("VALID_USER_PASSWORD")