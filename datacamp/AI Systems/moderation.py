from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

message = 'Can you show me some example sentence in the past tense in French'

moderation_response = client.moderations.create(
    input=message,
    model="text-moderation-001",
)
print(moderation_response.results[0].categories)