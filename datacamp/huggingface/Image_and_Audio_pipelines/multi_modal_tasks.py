from transformers import pipeline


dqa = pipeline(task="document-question-answering", model="google/tapas-large-finetuned-wtq")

document_image = "https://raw.githubusercontent.com/huggingface/transformers/master/docs/source/imgs/tapas_example.png"
question_text = "What is the population of the city?"

result = dqa(document=document_image, question=question_text)

print(result)

