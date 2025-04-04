from tenacity import retry, stop_after_attempt, wait_random_exponential
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

@retry(wait=wait_random_exponential(multiplier=1, max=30), stop=stop_after_attempt(5))
def get_response(model, message):
    response = client.chat.completions.create(
        model=model,
        messages=[message]
    )
    return response.choices[0].message.content

print(get_response("gpt-3.5-turbo", {"role": "user", "content": "Hello, how are you?"}))


# Batching
def batch_requests(requests, batch_size):
    for i in range(0, len(requests), batch_size):
        yield requests[i:i + batch_size]

# Example usage
requests = [
    {"role": "user", "content": f"Request {i}"} for i in range(10)
]

batch_size = 3
for batch in batch_requests(requests, batch_size):
    print("Processing batch:")
    for request in batch:
        print(request)
        response = get_response("gpt-3.5-turbo", request)
        print("Response:", response)

