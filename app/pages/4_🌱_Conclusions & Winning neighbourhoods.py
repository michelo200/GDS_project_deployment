import streamlit as st


from tools.ui_utils import (
    add_logo,
    ui_setup
)


add_logo()
ui_setup()
st.sidebar.write("Choose different site options above.")


st.subheader("Conclusions & Winning neighbourhoods")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
st.write("**The best neighbouhoods for:**")

group_radio = st.radio("Select your group", ["Young people", "Families", "Business people", "Elderly"])
if group_radio == "Young people":
    st.write("**Young people**")

if group_radio == "Families":
    st.write("**Families**")

if group_radio == "Business people":
    st.write("**Business people**")

if group_radio == "Elderly":
    st.write("**Elderly**")
    



st.write("Neighbourhoods and their characteristics")
details_toggle = st.toggle("Show neighbourhood details", False)
if details_toggle:
    st.write("**Ahuntsic-Cartierville**: Known for its family-friendly environment, this neighborhood boasts riverside parks, bike paths, and sports facilities. It offers a mix of action and tranquility, with a significant presence of green spaces and a variety of birds and aquatic wildlife")
    st.write("**Anjou**: Strategically located at the crossroads of major highways, Anjou features quiet streets, an abundance of single-family homes, and shopping centers like Place Versailles and Les Galeries d’Anjou, providing convenience and a suburban feel")
    st.write("**Côte-des-Neiges–Notre-Dame-de-Grâce**: This neighborhood offers a multicultural experience with a diverse range of homes, including historical houses. It is known for its vibrant community, educational institutions, and healthcare facilities, making it ideal for students and individuals seeking quality education and healthcare")
    st.write("**L'Île-Bizard–Sainte-Geneviève / Pierrefonds-Roxboro**: Characterized by tranquility and a wide range of outdoor activities, this area is suitable for families looking for a peaceful environment. It has space for new residential buildings and offers a suburban lifestyle close to nature")
    st.write("**LaSalle**: Located between the St. Lawrence River and the Lachine Canal, LaSalle provides a variety of homes, including condominiums and retirement homes. It is known for its waterfront living and recreational opportunities")
    st.write("**Lachine**: With a rich arts and recreational scene, Lachine offers a quality of life with rental homes and new buildings, appealing to young families. It is known for its historical significance and industrial heritage")
    st.write("**Le Plateau-Mont-Royal**: This neighborhood is known for its intense neighborhood life, urban charm, and proximity to busy streets. It features multiplexes with colorful staircases and a network of green lanes, attracting a diverse population including students and artists")
    st.write("**Le Sud-Ouest**: Appreciated for its urban yet friendly lifestyle, Le Sud-Ouest is known for its converted industrial buildings and recent developments along the Lachine Canal. It offers a blend of historic charm and modern amenities")
    st.write("**Mercier–Hochelaga-Maisonneuve**: This neighborhood is experiencing renewal with a rich industrial history. It offers a wide range of homes, commercial streets, and amenities like a public market, appealing to a diverse community")
    st.write("**Montréal-Nord**: Undergoing transformation, Montréal-Nord offers affordable housing options and is located on the shores of the Rivière des Prairies. It is known for its cultural diversity and community engagement")
    st.write("**Outremont**: Known for its beautiful historical homes and urban forest, Outremont offers a vast choice of housing and a delightful neighborhood life, appealing to those seeking upscale living")
    st.write("**Rivière-des-Prairies–Pointe-aux-Trembles**: With stunning settings on the shores of rivers, this neighborhood offers regional parks and affordable housing, attracting couples, families, and businesspeople looking for a suburban lifestyle")
    st.write("**Rosemont–La Petite-Patrie**: Features a number of distinct neighborhoods with lively atmospheres. It offers a vast choice of homes and is known for its family-friendly environment and community events")
    st.write("**Saint-Laurent**: Home to one of Canada’s largest industrial centers, Saint-Laurent offers diverse housing options and is close to public transportation. It is recognized for its multicultural community and economic development")
    st.write("**Saint-Léonard**: Known for its multiplexes and apartment towers, Saint-Léonard has a lively neighborhood life with a strong sense of community and cultural diversity")
    st.write("**Verdun**: An ideal place for young families, Verdun offers green spaces, family homes, rentals, co-owned homes, and a stunning beach, providing a waterfront lifestyle")
    st.write("**Ville-Marie**: Offers peaceful residential neighborhoods next to downtown's hustle and bustle. It is a hub of arts, culture, and economic activity, appealing to those seeking a vibrant urban environment")
    st.write("**Villeray–Saint-Michel–Parc-Extension**: Known for its unique vibe, parks, and rental homes, this neighborhood is accessible and filled with commercial streets at the heart of real neighborhoods, attracting a diverse population")