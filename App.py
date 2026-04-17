import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.set_page_config(page_title="Text to Image AI", layout="centered")

client = InferenceClient(
    provider="hf-inference",
    api_key="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"  # your HF token here
)

def generate_image(prompt):
    try:
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-dev"
        )
        return image, None
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
