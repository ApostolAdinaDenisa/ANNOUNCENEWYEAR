import streamlit as st

st.set_page_config(page_title="Revelion 2025-2026")

# Set full-page pink background (works reliably)
st.markdown("""
    <style>
    .stApp {
        background-color: #f7c1d9 !important;
        padding-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center; color:white;'>Revelion 2025 - 2026</h1>",
    unsafe_allow_html=True
)

# Images (these always load)
st.image("https://upload.wikimedia.org/wikipedia/commons/5/5f/Cannabis_plant.jpg", width=300)
st.image("https://upload.wikimedia.org/wikipedia/commons/7/70/Cannabis_flowering.jpg", width=300)

# Button
clicked = st.button("REVELION 2025-2026 TAP HERE")

if clicked:
    st.markdown(
        "<h2 style='text-align:center; color:white; font-weight:bold;'>"
        "SORRY GUYS BUT THIS NEW YEAR WE WILL NOT BE TOGETHER"
        "</h2>",
        unsafe_allow_html=True
    )
