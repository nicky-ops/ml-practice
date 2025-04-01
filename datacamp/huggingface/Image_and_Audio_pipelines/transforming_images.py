from transformers import image_transforms
import numpy as np
from PIL import Image

# Load an image from the file system
image = Image.open("my_image.jpg")

# Apply a transformation to the image
image_array = np.array(image)
cropped_image = image_transforms.center_crop(image=np.ndarray, size=(1000, 1000))