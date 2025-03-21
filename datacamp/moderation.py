from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# a request to the moderation endpoint
response = openai.moderation.create(
    model="text-moderation-latest",
    input="My favorite book is To Kill a Mockingbird"
)

# print category scores
print(response.results[0].category_scores)