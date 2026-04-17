#  AI Text to Image Generator

A web application that generates images from text descriptions using AI.

## 🛠️ Built With
- [Streamlit](https://streamlit.io/) - Web framework
- [Pollinations AI](https://pollinations.ai/) - Free image generation API
- [Pillow](https://pillow.readthedocs.io/) - Image processing
- [Requests](https://requests.readthedocs.io/) - HTTP requests

## ✨ Features
- Enter any text description and generate an image
- No API key or login required
- Download generated image as PNG
- Fast and free image generation
- Clean and simple user interface

##📁 Project Structure
text--image/
├── App.py
└── requirements.txt


## ⚙️ How to Run Locally
1. Clone the repository
bash
git clone https://github.com/yourusername/your-repo-name
cd your-repo-name


2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
bash
streamlit run App.py


## 🧠 How It Works
User enters text description
        ↓
Text sent to Pollinations AI API
        ↓
AI generates image from text
        ↓
Image displayed on screen
        ↓
User can download as PNG

## 📦 Requirements
streamlit
requests
Pillow

## 🆓 Why Pollinations AI?
- 100% Free forever
- No API key needed
- No login required
- No token expiry issues
- High quality image generation

## 📸 Screenshot
![App Screenshot](screenshot.png)

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
