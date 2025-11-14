# rarefood_senegal/style_manager.py
import streamlit as st

def inject_style():
    st.markdown("""
        <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #007B5E;
            color: white;
            border-radius: 5px;
        }
        .stTextInput>div>input {
            border: 1px solid #007B5E;
        }
        .stMarkdown {
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)
