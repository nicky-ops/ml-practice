from openai import OpenAI
import os


# Set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

client = OpenAI(api_key="your_api_key_here")
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            "role": "user",
            "content": "Who developed ChatGPT?",
        }
    ],
    response_format="json",
)

print(response.choices[0].message.content)