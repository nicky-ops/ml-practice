from transformers import pipeline

vqa = pipeline(task="visual-question-answering", model="google/vit-base-patch16-224-in21k")

result = vqa(image="https://raw.githubusercontent.com/huggingface/transformers/master/docs/source/imgs/tapas_example.png", question="What is the population of the city?")