import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Red Ribbon Profile Generator", page_icon="🎗️")

st.title("🎗️ Red Ribbon Profile Picture Generator")
st.write("Upload your profile picture and adjust the ribbon position.")

# Upload profile picture
uploaded_file = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open uploaded image
    profile_pic = Image.open(uploaded_file).convert("RGBA")

    # Load ribbon overlay (transparent PNG file in your project folder)
    ribbon = Image.open("red_ribbon.png").convert("RGBA")

    # Resize ribbon relative to profile picture size
    ribbon_size = int(profile_pic.width * 0.25)  # 25% of width
    ribbon = ribbon.resize((ribbon_size, ribbon_size))

    # --- Slider controls for position ---
    st.sidebar.header("Ribbon Position Controls")
    x_offset = st.sidebar.slider("Horizontal offset (from right)", 0, profile_pic.width, 10)
    y_offset = st.sidebar.slider("Vertical position", 0, profile_pic.height, int(profile_pic.height * 0.65))

    # Calculate position
    x_pos = profile_pic.width - ribbon.width - x_offset
    y_pos = y_offset
    position = (x_pos, y_pos)

    # Overlay ribbon
    profile_pic.paste(ribbon, position, ribbon)

    # Show result
    st.image(profile_pic, caption="Your new profile picture with ribbon")

    # Save to bytes for download
    buf = BytesIO()
    profile_pic.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Download button
    st.download_button(
        label="📥 Download Image",
        data=byte_im,
        file_name="profile_with_ribbon.png",
        mime="image/png"
    )
else:
    st.info("Please upload a profile picture to get started.")