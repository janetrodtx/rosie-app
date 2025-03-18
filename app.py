import streamlit as st
from PIL import Image
import base64
import io

# Image paths and corresponding links for the last page
images = [
    ("/mnt/data/1.png", None),
    ("/mnt/data/2.png", None),
    ("/mnt/data/3.png", None),
    ("/mnt/data/4.png", None),
    ("/mnt/data/5.png", None),
    ("/mnt/data/6.png", {
        "instagram": "https://www.instagram.com/rosalindaloveshair_12/",
        "booking": "https://square.site/book/HW1YNE3B0FZ67/rosalinda-cruz-at-salon-bella-donna-corpus-christi-tx?fbclid=PAZXh0bgNhZW0CMTEAAabRjSFT30xtjXx2JwnlKrdyQv6J_4G-WAeo3L3TkVFRjrAPXyKqR4J431M_aem_ErJY2t3JTZ-oYEt5DUlSEA"
    })
]

# Session state to track current page
if "page" not in st.session_state:
    st.session_state.page = 0

# Function to go to next page
def next_page():
    if st.session_state.page < len(images) - 1:
        st.session_state.page += 1

# Display current image
current_image_path, links = images[st.session_state.page]
try:
    image = Image.open(current_image_path)
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.error(f"Image file not found: {current_image_path}")

# If on last page, add clickable elements
if links:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Visit Instagram 📷", key="insta"):
            st.markdown(f"[Click here to visit Instagram]({links['instagram']})", unsafe_allow_html=True)
    with col2:
        if st.button("Book Appointment 📅", key="book"):
            st.markdown(f"[Click here to book]({links['booking']})", unsafe_allow_html=True)

    # Clickable image for booking link using Streamlit markdown and base64
    with open(current_image_path, "rb") as img_file:
        image_bytes = img_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()

    st.markdown(f"""
        <a href='{links['booking']}' target='_blank'>
            <img src='data:image/png;base64,{encoded_image}' style='width:100%; border-radius:10px;'/>
        </a>
    """, unsafe_allow_html=True)

# Pink "Next" arrow button
if st.session_state.page < len(images) - 1:
    col = st.columns([0.85, 0.15])[1]
    with col:
        if st.button("Next ➡️", key="next_button"):
            next_page()
