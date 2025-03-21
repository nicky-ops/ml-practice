from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai = OpenAI(os.getenv("OPENAI_API_KEY"))

