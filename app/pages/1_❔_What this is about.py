import streamlit as st
import pandas as pd
from tools.ui_utils import (
    add_logo,
    ui_setup
)


montreal_map = pd.DataFrame({
'lat': [45.5017],
'lon': [-73.5673]
})

add_logo()
ui_setup()

st.title("Project in Geospatial Data Science")
st.write("**Authors:** Emma, Caro, and Michel")
st.write("This project serves as a inspiration for people, who want to move or relocate in Montreal. Based on the concept of the 15-minute city we want to help you find the best spot within the city. You are able to choose which **mode of transportation** you want to use and which **amenity** is most important to you.")
st.write("Bring your data and we'll provide your best living locations.")

st.map(montreal_map, zoom=10)

st.sidebar.write("Choose different site options above.")