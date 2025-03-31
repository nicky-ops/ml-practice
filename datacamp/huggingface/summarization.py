from transformers import pipeline
import random

model = "sshleifer/tiny-mbart"
summarizer = pipeline(task="summarization", model=model)

text = """It was a very long story he gave. He talked about his adventures in the mountains, where he encountered wild animals and survived harsh weather. He shared his experiences of traveling across the world, meeting new people, and learning about different cultures. The story revolved around a mysterious treasure hidden in an ancient castle, guarded by riddles and traps. He recounted his childhood memories of growing up in a small village surrounded by lush green fields and rivers. The tale was about a futuristic world where humans and robots coexisted, facing challenges together."""

result = summarizer(text, max_length=50, min_length=10, do_sample=True, temperature=0.7)
