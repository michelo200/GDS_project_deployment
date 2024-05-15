import streamlit as st
import pandas as pd

# deploy button removal
def ui_setup():
    # Removing 'Deploy' button from the top right corner for cooler demo experience
    st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)

# itu logo
def add_logo():
    image_path = "visuals/itu-logo.png"
    left, middle, right = st.columns([10,1,5])
    with right:
        st.image(image_path, use_column_width=True)