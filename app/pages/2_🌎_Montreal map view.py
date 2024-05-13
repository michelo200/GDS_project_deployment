# basic map viz + emmas distance calc plotting goes in here

import streamlit as st
import pandas as pd
import osmnx as ox
import geopandas as gpd 

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


st.subheader("Map view analysis")

# basic map viz


st.divider()
# distance by amenity and district plotting
amenity_distances_map()

st.write("*If the distance is 0, no such amenity is located in the district.*")