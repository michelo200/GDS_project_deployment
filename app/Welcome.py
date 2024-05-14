import streamlit as st
import pandas as pd
from tools.ui_utils import (
    add_logo,
    ui_setup
)
from tools.utils import (
    init_walking_dist
)

st.set_page_config(page_title='Montreal-15-minute-city', page_icon=":earth_americas:",layout="wide")


montreal_map = pd.DataFrame({
'lat': [45.5017],
'lon': [-73.5673]
})

add_logo()

st.title("MONTREAL - A 15-MINUTE CITY?")
st.subheader("A Geospatial Data Science project at ITU Copenhagen")

with st.spinner("Initializing the application. This takes 2 minutes 🧘‍♂️"):
    if "walking_distances" not in st.session_state:
        st.session_state.walking_distances = init_walking_dist()

ui_setup()

st.write("**May 2024**")
st.write("**Authors:** Emma, Caro, and Michel")
st.write("This project serves as a inspiration for people, who want to move or relocate in Montreal. Based on the concept of the 15-minute city we want to help finding the best spot within the city. Users are able to choose which **mode of transportation** they want to use and which **amenity** is most important to them.")

st.divider()
st.write("Now it's up to you - walk through the app pages and analyse the city. We'll provide you with the best living locations.")

st.map(montreal_map, zoom=10)

st.sidebar.write("Choose different site options above.")