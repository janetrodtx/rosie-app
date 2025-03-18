import streamlit as st

# Image paths
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
current_image, links = images[st.session_state.page]
st.image(current_image, use_column_width=True)

# If on last page, add clickable elements
if links:
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Visit Instagram", key="insta"):
            st.markdown(f"[Click here to visit Instagram]({links['instagram']})")
    with col2:
        if st.button("Book Appointment", key="book"):
            st.markdown(f"[Click here to book]({links['booking']})")

    # Make image clickable for booking
    st.markdown(f"<a href='{links['booking']}' target='_blank'><img src='data:image/png;base64,{st.image(current_image, use_column_width=True)}' style='display:none;'/></a>", unsafe_allow_html=True)

# Pink "Next" arrow button
if st.session_state.page < len(images) - 1:
    st.markdown("""
        <div style='text-align: right; padding: 20px;'>
            <button onclick='window.location.reload()' style='background-color: pink; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;'>
                Next ➡️
            </button>
        </div>
    """, unsafe_allow_html=True)
    st.button("", on_click=next_page, key="next_button")
