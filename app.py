import streamlit as st
from PIL import Image
import base64
import io

# Image paths (relative to app.py) and corresponding links for the last page
images = [
    ("1.png", None),
    ("2.png", None),
    ("3.png", None),
    ("4.png", None),
    ("5.png", None),
    ("6.png", {
        "instagram": "https://www.instagram.com/rosalindaloveshair_12/",
        "booking": "https://square.site/book/HW1YNE3B0FZ67/rosalinda-cruz-at-salon-bella-donna-corpus-christi-tx?fbclid=PAZXh0bgNhZW0CMTEAAabRjSFT30xtjXx2JwnlKrdyQv6J_4G-WAeo3L3TkVFRjrAPXyKqR4J431M_aem_ErJY2t3JTZ-oYEt5DUlSEA"
    })
]

# Session state to track current page
if "page" not in st.session_state:
    st.session_state.page = 0

# Navigation functions
def next_page():
    if st.session_state.page < len(images) - 1:
        st.session_state.page += 1

def previous_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

# Add smooth fade-in CSS animation
st.markdown("""
    <style>
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Display current image with fade-in effect
current_image_path, links = images[st.session_state.page]
try:
    with open(current_image_path, "rb") as img_file:
        image_bytes = img_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        st.markdown(f"""
            <img src='data:image/png;base64,{encoded_image}' class='fade-in' style='width:100%; border-radius:10px;' />
        """, unsafe_allow_html=True)
except FileNotFoundError:
    st.error(f"Image file not found: {current_image_path}")

# If on last page, add clickable elements under the image
if links:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Visit Instagram 📷", key="insta"):
            st.markdown(f"[Click here to visit Instagram]({links['instagram']})", unsafe_allow_html=True)
    with col2:
        if st.button("Book Appointment 📅", key="book"):
            st.markdown(f"[Click here to book]({links['booking']})", unsafe_allow_html=True)

    # Clickable image for booking link ONLY (not shown twice)
    st.markdown(f"""
        <a href='{links['booking']}' target='_blank'>
            <img src='data:image/png;base64,{encoded_image}' style='width:100%; border-radius:10px;' />
        </a>
    """, unsafe_allow_html=True)

# Navigation Buttons (Back and Next)
nav_col1, nav_col2 = st.columns([0.15, 0.85])
with nav_col1:
    if st.session_state.page > 0:
        if st.button("⬅️ Back", key="back_button"):
            previous_page()
with nav_col2:
    if st.session_state.page < len(images) - 1:
        if st.button("Next ➡️", key="next_button"):
            next_page()

# Progress dots
dot_container = ""
for i in range(len(images)):
    if i == st.session_state.page:
        dot_container += "<span style='font-size: 24px; color: pink;'>●</span> "
    else:
        dot_container += "<span style='font-size: 20px; color: lightgray;'>●</span> "
st.markdown(f"<div style='text-align:center; margin-top:10px;'>{dot_container}</div>", unsafe_allow_html=True)

