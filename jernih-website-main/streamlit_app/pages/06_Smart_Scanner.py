import streamlit as st
import sys
from pathlib import Path

root_path = Path(__file__).parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

import os
import base64
import io
from datetime import datetime

from src.config import OPENROUTER_URL, SITE_URL, SITE_TITLE

# Ambil API Key
try:
    OPENROUTER_KEY = os.environ.get("OPENAI_API_KEY", "") or st.secrets["OPENAI_API_KEY"]
except Exception:
    OPENROUTER_KEY = ""

st.set_page_config(
    page_title="Smart Scanner - JERNIH OS",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded",
)

from src.ui_components import inject_css
inject_css()

from PIL import Image
import io

# ── OCR PAKAI OPENROUTER LANGSUNG ──

def ocr_via_openrouter(image_bytes: bytes) -> str | None:
    """OCR pake OpenRouter Vision API (langsung, tanpa fallback)"""
    if not OPENROUTER_KEY:
        st.error("❌ OpenRouter API Key TIDAK DITEMUKAN! Set di Secrets.")
        return None
    
    try:
        b64 = base64.b64encode(image_bytes).decode("utf-8")
        mime = "image/jpeg"  # default
        data_url = f"data:{mime};base64,{b64}"
        
        from openai import OpenAI
        
        client = OpenAI(
            api_key=OPENROUTER_KEY,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": SITE_URL,
                "X-Title": SITE_TITLE,
            },
        )
        
        # Pake model yang paling stabil
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",  # ini model vision
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Extract ALL text from this image exactly as written. Return ONLY the raw text with no extra words, no explanation."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url
                            }
                        }
                    ]
                }
            ],
            max_tokens=2048,
            temperature=0.0,
        )
        
        result = response.choices[0].message.content
        if result and result.strip():
            return result.strip()
        else:
            return None
            
    except Exception as e:
        st.error(f"❌ Error OpenRouter: {str(e)}")
        return None

# ── UI ──

def render_page():
    st.markdown("""
    <div class="main-header fade-in">
        <h1>📸 Smart Scanner</h1>
        <p>AI-Powered Picture-to-Text OCR — Extract, Copy & Download</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<p style='color: #888;'>Upload gambar untuk mengekstrak semua teks secara otomatis menggunakan AI Vision.</p>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Gambar (JPG, PNG, JPEG, BMP, WEBP)",
        type=["jpg", "png", "jpeg", "bmp", "webp"],
    )

    if uploaded_file is None:
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown("""
                <div style="text-align: center; padding: 3rem 1rem; color: rgba(255,255,255,0.3);">
                    <div style="font-size: 4rem; margin-bottom: 1rem;">📄</div>
                    <p style="font-size: 1.1rem;">Upload gambar untuk memulai</p>
                    <p style="font-size: 0.85rem;">Dukung format JPG, PNG, JPEG, BMP, WEBP</p>
                </div>
                """, unsafe_allow_html=True)
        return

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='color: #667eea;'>📷 Gambar Asli</h3>", unsafe_allow_html=True)
        st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)

    with col2:
        st.markdown("<h3 style='color: #2ed573;'>📝 Hasil Ekstraksi Teks</h3>", unsafe_allow_html=True)

        scan_btn = st.button("🔍 Scan Text dari Gambar", type="primary", use_container_width=True)

        if "ocr_text" not in st.session_state:
            st.session_state.ocr_text = ""
        if "ocr_done" not in st.session_state:
            st.session_state.ocr_done = False

        if scan_btn:
            with st.spinner("🧠 AI Vision sedang mengekstrak teks..."):
                # Tampilkan status API Key
                st.info(f"🔑 API Key Status: {'✅ ADA' if OPENROUTER_KEY else '❌ TIDAK ADA'}")
                
                image_bytes = uploaded_file.getvalue()
                extracted_text = ocr_via_openrouter(image_bytes)
                
                if extracted_text:
                    st.session_state.ocr_text = extracted_text
                    st.session_state.ocr_done = True
                    st.success("✅ Teks berhasil diekstrak oleh AI Vision!")
                else:
                    st.session_state.ocr_text = "Gagal mengekstrak teks. Pastikan API Key benar dan gambar jelas."
                    st.session_state.ocr_done = True
                    st.error("❌ Gagal mengekstrak teks!")

        if st.session_state.ocr_done:
            edited_text = st.text_area(
                "Edit teks jika perlu:",
                value=st.session_state.ocr_text,
                height=300,
                key="text_editor",
            )
            st.session_state.ocr_text = edited_text

            word_count = len(edited_text.split()) if edited_text else 0
            char_count = len(edited_text) if edited_text else 0

            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("Kata", word_count)
            with col_m2:
                st.metric("Karakter", char_count)
            with col_m3:
                st.metric("Sumber", "AI Vision")

            st.markdown("<div style='margin: 0.5rem 0;'>", unsafe_allow_html=True)

            with st.expander("📋 Teks Hasil Scan (bisa dicopy dari sini)", expanded=True):
                st.code(edited_text if edited_text else "(kosong)", language="text")

            st.markdown("</div>", unsafe_allow_html=True)

            btn_col1, btn_col2, btn_col3 = st.columns(3)

            with btn_col1:
                if edited_text:
                    st.download_button(
                        label="📋 Salin sebagai TXT",
                        data=edited_text.encode("utf-8"),
                        file_name=f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True,
                    )

            with btn_col2:
                if edited_text:
                    st.download_button(
                        label="📄 Download DOC",
                        data=f"<html><body><pre>{edited_text}</pre></body></html>".encode("utf-8"),
                        file_name=f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                        mime="text/html",
                        use_container_width=True,
                    )

            with btn_col3:
                if st.button("🔄 Reset", use_container_width=True):
                    st.session_state.ocr_text = ""
                    st.session_state.ocr_done = False
                    st.rerun()

if __name__ == "__main__":
    render_page()
