from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image

processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")

model = AutoModelforCausalLM.from_pretrained("microsoft/git-base-coco")

image = Image.open("https://huggingface.co/front/thumbnails/roberta-large.png")

pixel_values = processor(images=img, return_tensors="pt").pixel_values
generate_ids = model.generate(pixel_values, max_length=100, num_return_sequences=1)

generated_caption = processor.batch_decode(generate_ids, skip_special_tokens=True)

print(generated_caption[0])