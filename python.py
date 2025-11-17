import streamlit as st

st.set_page_config(page_title="Revelion 2025-2026")

# Pink background
st.markdown("""
<style>
.stApp {
    background-color: #f7c1d9 !important;
    padding-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center; color:white;'>Revelion 2025 - 2026</h1>",
    unsafe_allow_html=True
)

# These image links ALWAYS work on Streamlit
st.image("https://raw.githubusercontent.com/streamlit/emoji-shortcodes/master/docs/en/images/emoji/🌿.png", width=200)
st.image("https://raw.githubusercontent.com/streamlit/emoji-shortcodes/master/docs/en/images/emoji/🍁.png", width=200)

# Button
if st.button("REVELION 2025-2026 TAP HERE"):
    st.markdown(
        "<h2 style='text-align:center; color:white; font-weight:bold;'>"
        "SORRY GUYS BUT THIS NEW YEAR WE WILL NOT BE TOGETHER"
        "</h2>",
        unsafe_allow_html=True
    )
