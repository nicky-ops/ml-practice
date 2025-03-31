from transformers import AutoTokenizer

# Download the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Normalize the text
text = "I'm so excited to be working with Hugging Face today! 🤗"

output = tokenizer.backend_tokenizer.normalizer.normalize_str(text)