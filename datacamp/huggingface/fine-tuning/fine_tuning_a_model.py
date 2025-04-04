from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments, pipeline

model_name = 'bert-base-cased'
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# Prepare the dataset
tokenizer = AutoTokenizer.from_pretrained(model_name)
dataset = dataset.map(
    lambda x: tokenizer(x['text'], padding="max_length", truncation=True),
    batched=True
)

# Define the training arguments
training_args = TrainingArguments(
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir='./logs',
    logging_steps=10,
    save_steps=10,
    output_dir='./output'
)

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['validation']
)

# Train the model
trainer.train()

local_model_path = './output'

# Save the model
trainer.save_model(local_model_path)


# Load the model
classifier = pipeline(task="text-classification", model=local_model_path)
classifier(dataset['text'])