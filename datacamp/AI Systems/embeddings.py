from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

request = client.embeddings.create(
    model="text-embedding-ada-002",
    input="The food was delicious and the waiter...",
)

response = request["data"][0]["embedding"]
print(response)

# Embedding Multiple headlines
articles = [
    {
        'headline': 'Economic growth in the US',
        'topic': 'Economy',
    },
    {
        'headline': 'New advancements in AI technology',
        'topic': 'Technology',
    },
    {
        'headline': 'The impact of climate change on agriculture',
        'topic': 'Environment',
    },
    {
        'headline': 'The future of electric vehicles',
        'topic': 'Transportation',
    },
]

headline_text = [article['headline'] for article in articles]

response = client.embeddings.create(
    model="text-embedding-ada-002",
    input=headline_text,
)

for i, articles in enumerate(articles):
    articles['embedding'] = response['data'][i]['embedding']

print(articles)