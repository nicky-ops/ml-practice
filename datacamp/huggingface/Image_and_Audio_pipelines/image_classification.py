from transformers import pipeline

classifier = pipeline(task="image-classification", model='google/vit-base-patch16-224-in21k')

image = "https://images.pexels.com/photos/59989/elephant-herd-of-elephants-african-bush-elephant-africa-59989.jpeg?auto=compress&cs=tinysrgb&w=600"

results = classifier(image, top_k=2)

print(results[0]['label'])