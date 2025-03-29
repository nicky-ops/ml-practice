from datasets import load_dataset_builder

data_builder = load_dataset_builder("glue", "mrpc")

print(data_builder.info.description)
print(data_builder.info.features)

# Dpwload the dataset
data = load_dataset("imdb", split="train")

# Mutating the dataset
# Filter the dataset
filtered = data.filter(lambda row: row["label"] == 1)

# Slicing the dataset
sliced = data.select(range(5))

print(sliced)