from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import torch


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def caption_image(image_path_or_url):
    if image_path_or_url.startswith('http'):
        image = Image.open(requests.get(image_path_or_url, stream=True).raw).convert('RGB')
    else:
        image = Image.open(image_path_or_url).convert('RGB')

    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


img_url = "download.jpeg"
print(caption_image(img_url))
img = "bird.jpeg"
print(caption_image(img))