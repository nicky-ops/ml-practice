from openai import OpenAI
import os
import uuid


unique_id = str(uuid.uuid4())

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    message=[
        {'role': 'user', 'content': 'Hello!'},
        {'role': 'user', 'content': 'What is your name?'},
        {'role': 'user', 'content': 'What is your favorite color?'}
    ],
    user=unique_id,
)