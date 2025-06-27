# 🧠 BLIP Image Captioning with Transformers

This project demonstrates how to generate natural language captions for images using the **BLIP (Bootstrapped Language Image Pretraining)** model from Salesforce, powered by Hugging Face's `transformers` library.

Using a pretrained model, this script can take an image (local file or URL) and output a human-like caption describing the image content.

## ✨ Features

- 🖼️ Accepts both image URLs and local image files
- 🤖 Uses the powerful BLIP model (`Salesforce/blip-image-captioning-base`)
- ⚡ Fast and efficient inference with PyTorch
- 🔁 Easily extendable for batch processing, web apps, or AI-powered galleries

---

## 📸 Example Output

```bash
> python main.py
A bird is standing on a rock
A colorful bird is sitting on a branch
```

---

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.7+
* PyTorch
* Hugging Face Transformers
* PIL (Pillow)
* Requests

Install dependencies using:

```bash
pip install -r requirements.txt
```

### 🧪 Running the Code

```bash
git clone https://github.com/HirthikBalaji/ImageCaptioning.git
cd ImageCaptioning
python main.py
```

Make sure to replace the sample image paths (`download.jpeg`, `bird.jpeg`) with valid file paths or image URLs.

---

## 🧠 How It Works

1. **Load BLIP Processor and Model**
   The script loads a pretrained processor and model from Hugging Face.

2. **Input Image (URL or Local)**
   It supports both local images and remote images via URL.

3. **Image Preprocessing & Caption Generation**
   The image is preprocessed using the processor, passed to the model, and the generated output tokens are decoded into a human-readable sentence.

4. **Display the Result**
   The script prints a caption describing the image content.

---

## 📚 References

* [BLIP: Bootstrapped Language-Image Pretraining](https://github.com/salesforce/BLIP)
* [Hugging Face Model Card](https://huggingface.co/Salesforce/blip-image-captioning-base)
* [Transformers Documentation](https://huggingface.co/docs/transformers/index)

---

## 💡 Ideas for Extension

* Integrate with a Flask or Streamlit app for a web UI
* Add batch processing for datasets
* Save and display images with their captions
* Use in accessibility tools or educational software

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project uses models and tools that are open source. Check individual dependencies for their respective licenses.

---