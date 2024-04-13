import streamlit as st
import pandas as pd
from tools.ui_utils import (
    add_logo,
    ui_setup
)

add_logo()
ui_setup()

st.subheader("Map view of Montreal")
st.write("Make your data input in the sidebar and wait for the analysis to run.")

montreal_map = pd.DataFrame({
    'lat': [45.5017],
    'lon': [-73.5673]
})

with st.sidebar:
    st.selectbox("Mode of transportation",("Walking", "Biking", "Driving", "Public transport"))
    st.selectbox("Amenity",("Supermarket", "Pharmacy", "General practitioner", "School/university", "Café", "Park/green area", "Public water access", "Library", "Place of worship", "Bar", "Restaurants"))
    
    start_button = st.button("Use these choices.")
    
if start_button:
    with st.spinner("Your analysis is running in the background."):
        import time
        time.sleep(10)
        st.success("Finished - let's have a look at your best living location in Montreal.")
        
        # map: change of zoom and color possible
        st.map(montreal_map, zoom=10) 
        

st.sidebar.write("Choose different site options above.")


# import json
# with open("montreal_geojson.txt", "r") as file:
#     montreal_geojson = json.load(file)
# # GET TO KNOW HOW TO DISPLAY THIS IN STREAMLIT!!! ######################################
# fig = px.choropleth(montreal_data,
#                     geojson=montreal_geojson,
#                     locations='District',  # This should match the IDs in your GeoJSON
#                     color='Supermarkets',  # The DataFrame column you want to color by
#                     featureidkey="properties.District",  # Path to the feature ID in the GeoJSON
#                     projection="mercator",
#                     title="Supermarkets in Montreal's Districts")

# # Update the map's layout
# fig.update_geos(fitbounds="locations", visible=False)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# st.pyplot(fig)