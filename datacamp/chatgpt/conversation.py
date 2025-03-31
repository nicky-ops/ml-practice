from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": 'system',
        'content': "You are a data science tutor who provides short, simple explanations."
    }
]

user_questions = ["Why is Python so popular?", "Summarize this in one sentence."]

for question in user_questions:
    print("User:", question)
    user_dict = {"role": 'user', 'content': question}
    messages.append(user_dict)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_dict = {"role": 'assistant', 'content': response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant:", response.choices[0].message.content)
                  