from flask import Flask, request, jsonify
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import requests
import os

app = Flask(__name__)

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(image):
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

@app.route("/caption", methods=["POST"])
def generate_caption():
    if 'image' in request.files:
        image = Image.open(request.files['image']).convert('RGB')
    elif 'url' in request.json:
        img_url = request.json['url']
        image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
    else:
        return jsonify({'error': 'No image or URL provided'}), 400

    caption = caption_image(image)
    return jsonify({'caption': caption})

from flask_cors import CORS
CORS(app)
