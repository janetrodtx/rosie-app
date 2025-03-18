import streamlit as st
from PIL import Image
import base64
import io
import os

# Image paths (relative to app.py) and corresponding links for the last page
images = [
    ("1.png", None),
    ("2.png", None),
    ("3.png", None),
    ("4.png", None),
    ("5.png", None),
    ("6.png", {
        "instagram": "https://www.instagram.com/rosalindaloveshair_12/",
        "facebook": "https://m.facebook.com/RosalindaClarrissaCruz/",
        "booking": "https://square.site/book/HW1YNE3B0FZ67/rosalinda-cruz-at-salon-bella-donna-corpus-christi-tx?fbclid=PAZXh0bgNhZW0CMTEAAabRjSFT30xtjXx2JwnlKrdyQv6J_4G-WAeo3L3TkVFRjrAPXyKqR4J431M_aem_ErJY2t3JTZ-oYEt5DUlSEA"
    })
]

# Add custom CSS for glam
st.markdown("""
    <style>
        body, .stApp {
            cursor: url('https://cur.cursors-4u.net/cursors/cur-9/cur830.cur'), auto;
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .pink-button {
            color: pink;
            font-weight: bold;
            text-align: center;
            font-size: 16px;
            transition: text-shadow 0.3s ease-in-out;
        }
        .pink-button:hover {
            text-shadow: 0 0 10px pink;
        }
        .sparkle {
            animation: shimmer 1.2s infinite;
        }
        @keyframes shimmer {
            0% { filter: drop-shadow(0 0 5px pink); }
            50% { filter: drop-shadow(0 0 15px hotpink); }
            100% { filter: drop-shadow(0 0 5px pink); }
        }
    </style>
""", unsafe_allow_html=True)

# Load and play sound
sound_file_path = "hairdryer.mp3"
if os.path.exists(sound_file_path):
    with open(sound_file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3', start_time=0)

# Display all images vertically
for idx, (img_path, links) in enumerate(images):
    try:
        with open(img_path, "rb") as img_file:
            image_bytes = img_file.read()
            encoded_image = base64.b64encode(image_bytes).decode()
    except FileNotFoundError:
        st.error(f"Image file not found: {img_path}")
        continue

    if links:
        st.markdown(f"""
            <a href='{links['booking']}' target='_blank'>
                <img src='data:image/png;base64,{encoded_image}' class='fade-in sparkle' style='width:100%; border-radius:10px;' />
            </a>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style='text-align:center; margin-top: 20px;'>
                <a href='{instagram}' target='_blank' class='pink-button'>📷 Visit Instagram</a> |
                <a href='{facebook}' target='_blank' class='pink-button'>📘 Visit Facebook</a> |
                <a href='{booking}' target='_blank' class='pink-button'>📅 Book Appointment</a>
            </div>
        """.format(instagram=links['instagram'], facebook=links['facebook'], booking=links['booking']), unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <img src='data:image/png;base64,{encoded_image}' class='fade-in' style='width:100%; border-radius:10px;' />
        """, unsafe_allow_html=True)


