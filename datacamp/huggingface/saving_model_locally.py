from transformers import AutoModel

modelId = "bert-base-uncased"

# Download the model from the Hub using the modelId
model = AutoModel.from_pretrained(modelId)

# Save the model locally
model.save_pretrained("model")