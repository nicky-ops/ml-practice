from huggingface_hub import HfApi, ModelFilter
# Create the instance of the API
api = HfApi()

# Return the filtered list from the Hub
models = api.list_models(
    task="text-classification",
    sort="downloads",
    direction=-1,
  	limit=1
)

# Store as a list
modelList = list(models)

print(modelList[0].modelId)