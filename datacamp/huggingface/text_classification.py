from transformers import pipeline


# Text classification
classifier = pipeline(task="text-classification")

result = classifier("I'm so excited to be working with Hugging Face today! 🤗")

print(result)

# QNLI (Question Natural Language Inference) is a dataset for the task of Question Answering
# The model is trained to predict whether the answer to a question is yes or no
result = classifier("I'm so excited to be working with Hugging Face today! 🤗", task="question-answering")
print(result)