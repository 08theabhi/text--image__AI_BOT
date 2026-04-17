import streamlit as st
import requests
from PIL import Image
import io

API_URL = "API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0""
HEADERS = {"Authorization": "Bearer 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"}  # your HF token here

def generate_image(prompt):
    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json={"inputs": prompt},
            timeout=60
        )
        if response.status_code == 401:
            return None, "❌ Invalid HuggingFace token. Please check your token."
        elif response.status_code == 503:
            return None, "⏳ Model is loading, please wait 20 seconds and try again."
        elif response.status_code == 429:
            return None, "⚠️ Too many requests. Please wait and try again."
        elif response.status_code == 404:
            return None, "❌ Model not found. Check the API URL."
        elif response.status_code != 200:
            return None, f"❌ API Error: Status code {response.status_code} — {response.text[:200]}"

        image = Image.open(io.BytesIO(response.content))
        return image, None

    except requests.exceptions.Timeout:
        return None, "❌ Request timed out. Please try again."
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# ---- UI ----
st.set_page_config(page_title="Text to Image AI", layout="centered")
st.title("🎨 AI Text to Image Generator")
st.write("Enter a description and AI will generate an image for you!")

prompt = st.text_area("Describe the image you want:", height=100,
                       placeholder="Example: A beautiful sunset over mountains with snow...")

if st.button("🎨 Generate Image"):
    if prompt.strip():
        with st.spinner("Generating image... this may take 20-30 seconds..."):
            image, error = generate_image(prompt)
        if error:
            st.error(error)
        else:
            st.subheader("🖼️ Generated Image:")
            st.image(image, use_column_width=True)
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            st.download_button(
                label="⬇️ Download Image",
                data=buf.getvalue(),
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.warning("⚠️ Please enter a description first.")
