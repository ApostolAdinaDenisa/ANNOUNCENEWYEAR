import streamlit as st

st.set_page_config(page_title="Revelion 2025-2026", layout="centered")

# Pink background
st.markdown("""
<style>
body {
    background-color: #f7c1d9;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center; color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.4);'>"
    "Revelion 2025 - 2026"
    "</h1>",
    unsafe_allow_html=True
)

# One test image
st.image("https://upload.wikimedia.org/wikipedia/commons/5/5f/Cannabis_plant.jpg", use_column_width=True)

if st.button("REVELION 2025-2026 TAP HERE"):
    st.markdown(
        "<h2 style='color:white; font-weight:bold; text-align:center;'>"
        "SORRY GUYS BUT THIS NEW YEAR WE WILL NOT BE TOGETHER"
        "</h2>",
        unsafe_allow_html=True
    )
