from transformers import GPT2Tokenizer, DistilBertTokenizer

text = "I'm so excited to be working with Hugging Face today! 🤗"
# Download the gpt tokenizer
gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# Tokenize the text
gpt_tokens=gpt_tokenizer.tokenize(text)
print(gpt_tokens)

# Download the distilbert tokenizer
distilbert_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
# Tokenize the text
distilbert_tokens=distilbert_tokenizer.tokenize(text)
print(distilbert_tokens)