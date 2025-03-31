from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "system",
        "content": "You are a data science tutor who speaks concisely."
    },
    {
        "role": 'user',
        'content': 'How do you define  a python list?'
    },
    {
        'role': "assistant",
        "content": 'Lists are defined by enclosing comma-seperated values in square brackets [ ].'
    },
    {
        "role": "user",
        'content': "What is the difference between mutable and immutable objects?"
    }
    ]
)