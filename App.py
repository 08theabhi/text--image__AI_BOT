import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Text to Image AI", layout="centered")

def generate_image(prompt):
    try:
        url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            return image, None
        else:
            return None, f"❌ Error: Status code {response.status_code}"
    except requests.exceptions.Timeout:
        return None, "❌ Request timed out. Please try again."
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# ---- UI ----
st.title("🎨 AI Text to Image Generator")
st.write("Enter a description and AI will generate an image for you!")

prompt = st.text_area(
    "Describe the image you want:",
    height=100,
    placeholder="Example: A beautiful sunset over mountains with snow..."
)

if st.button("🎨 Generate Image"):
    if prompt.strip():
        with st.spinner("Generating image... please wait..."):
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
