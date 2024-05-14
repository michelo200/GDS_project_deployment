import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
st.subheader("Statistics analysis - Montreal")
st.write("Make your data input in the sidebar and wait for the analysis to run.")

amenity_plot()



st.sidebar.write("Choose different site options above.")

amenity_dataframe()