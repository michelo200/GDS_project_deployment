import streamlit as st


from tools.ui_utils import (
    add_logo,
    ui_setup
)

from tools.utils import (
    neighbourhood_characteristics,
    neighbourhoods_by_group
)

add_logo()
ui_setup()
st.sidebar.write("Choose different site options above.")

st.subheader("Conclusions & Winning neighbourhoods")

st.divider()

neighbourhoods_by_group()

st.divider()

neighbourhood_characteristics()