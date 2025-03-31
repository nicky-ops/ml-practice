'''
Zero shot classification
'''
from transformers import pipeline

text = "Wikipedia earlier this month released its list of the 25 most viewed ..."

candidate_labels = ["science", "sports", "politics", "business", "technology"]
model = "facebook/bart-large-mnli"
classifier = pipeline(task="zero-shot-classification", model=model)

result = classifier(text, candidate_labels)
print(result)
