from sentence_transformers import SentenceTransformer, util

encoder = SentenceTransformer('bert-base-nli-mean-tokens')

documents = ['I love programming', 'I love coding', 'I love to code']
document_embeddings = encoder.encode(documents)

query = 'I love programming'

query_embedding = encoder.encode([query])


hits = util.semantic_search(query_embedding, document_embeddings, top_k=2)

for hit in hits[0]:
    print(documents[hit['corpus_id']], hit['score'])