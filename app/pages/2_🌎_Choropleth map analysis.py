import streamlit as st

from tools.ui_utils import (
    add_logo,
    ui_setup
)

from tools.utils import (
    amenity_distances_map
)

add_logo()
ui_setup()
st.sidebar.write("Choose different site options above.")


st.subheader("Choropleth map analysis")
st.write("In this page you get introduced to the **amenities across the neighbourhood map** and their **distances from the respective neighbourhood centres**.")
st.write("This will give you a first indication about your favourite neighbourhoods and their neighbouring neighbourhoods.")

st.divider()

# basic map viz
st.write("COMING SOON FROM EMMAS CODE...")


st.divider()

# distance by amenity and district plotting
amenity_distances_map()

st.write("*Note: If the distance is 0, no such amenity is located in the district.*")