import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="SpineWatch",
    page_icon="🩻",
    layout="centered",
)

# Streamlit adds its own page padding/margins around embedded content.
# This trims that so the embedded app's own #app max-width/centering looks right.
st.markdown(
    """
    <style>
        .block-container {padding-top: 0rem; padding-bottom: 0rem; max-width: 480px;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "spinewatch.html"
html_content = html_path.read_text(encoding="utf-8")

# height is a starting guess — the app itself scrolls internally (#app / body),
# so scrolling=True lets the iframe grow a scrollbar if content is taller.
components.html(html_content, height=950, scrolling=True)

st.caption(
    "หมายเหตุ: ฟีเจอร์กล้อง (ถ่ายภาพ) ต้องอนุญาตสิทธิ์กล้องในเบราว์เซอร์ "
    "และต้องเปิดหน้านี้ผ่าน https หรือ localhost มิฉะนั้นเบราว์เซอร์จะบล็อกการเข้าถึงกล้อง"
)
