"""
This script demonstrates how to use the AutoClasses to load the model and tokenizer
Use case: Sentiment Analysis
"""
# Download the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
sentimentAnalysis = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)

# Predict the sentiment
output = sentimentAnalysis(input)

print(f"Sentiment using AutoClasses: {output[0]['label']}")