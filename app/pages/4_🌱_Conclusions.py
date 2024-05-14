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