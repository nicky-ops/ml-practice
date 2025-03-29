"""
Creating a pipeline using the transformers library
Use case: Sentiment Analysis
"""
# Import pipeline
from transformers import pipeline

# Create the task pipeline
task_pipeline = pipeline("sentiment-analysis")

# Create the model pipeline
model_pipeline = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")

# Predict the sentiment
task_output = task_pipeline(input)
model_output = model_pipeline(input)

print(f"Sentiment from task_pipeline: {task_output[0]['label']}; Sentiment from model_pipeline: {model_output[0]['label']}")