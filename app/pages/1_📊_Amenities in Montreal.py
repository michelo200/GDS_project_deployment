import streamlit as st

from tools.ui_utils import (
    add_logo,
    ui_setup
)

from tools.utils import (
    amenity_dataframe,
    amenity_plot
)

# ui
add_logo()
ui_setup()
st.subheader("Amenities in Montreal")
st.write("In this page you can get a feeling for the distribution of amenities across the neighbourhoods of Montreal.")
st.write("**The barplot** below shows the number of amenities per neighbourhood.")
st.write("**The dataframe** gives you the opportunity to look into single amenities and even look them up on google maps, if you are interested in more information about the location.")


st.divider()

# barplot for neighbourhood and amenity
amenity_plot()



st.sidebar.write("Choose different site options above.")

# dataframe lookup with same logic
amenity_dataframe()