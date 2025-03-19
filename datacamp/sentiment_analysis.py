from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(os.getenv("OPENAI_API_KEY"))

prompt = """
Classify the sentiment of the following statments as either negative, positive, or neutral:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!
"""
# A request to the Chat completions endpoint
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": prompt,
    }],
    max_tokens=100
)

print(response.choices[0].message.content)