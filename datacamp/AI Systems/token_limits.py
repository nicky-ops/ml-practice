from openai import OpenAI
import os
import tiktoken

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
num_tokens = len(encoding.encode("Hello, how are you?"))

if num_tokens > 4096:
    raise ValueError("The number of tokens exceeds the limit.")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)
print(response.choices[0].message.content)

