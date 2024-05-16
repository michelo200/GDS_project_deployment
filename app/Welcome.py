import streamlit as st
import pandas as pd
from tools.ui_utils import (
    add_logo,
    ui_setup,
)

from tools.utils import (
    neighbourhood_map
)

st.set_page_config(page_title='Montreal-15-minute-city', page_icon=":earth_americas:",layout="wide")


montreal_map = pd.DataFrame({
'lat': [45.5017],
'lon': [-73.5673]
})

add_logo()

st.title("MONTREAL - A 15-MINUTE CITY?")
st.subheader("A Geospatial Data Science project at ITU Copenhagen")

ui_setup()

st.write("**May 2024**")
st.write("**Authors:** Emma Stoklund Lee, Carolina Branas Soria, and Michel Poesze")
st.write("This project serves as a inspiration for people, who want to move or relocate in Montreal. Based on the concept of the 15-minute city we want to help finding the best address to live within the city. In the different pages, users are able to choose their **amenity of interest** and the **mode of transportation** they want to use. Visualisations and our conclusions will help to find the best neighbourhoods to live in Montreal.")

st.divider()
st.write("Now it's up to you - walk through the app pages and analyse the city. We'll provide you with the best living locations.")

neighbourhood_map()


st.sidebar.write("Choose different site options above.")