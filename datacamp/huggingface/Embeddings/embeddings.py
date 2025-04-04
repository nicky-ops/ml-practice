from sentence_transformers import SentenceTransformer


model_name = 'bert-base-nli-mean-tokens'
embedder = SentenceTransformer(model_name)

sentence = 'I love programming'
embedding = embedder.encode([sentence])
print(embedding)