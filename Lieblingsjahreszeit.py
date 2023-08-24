import streamlit as st
import pandas as pd
import altair as alt

st.header("Lieblingsjahreszeit der Deutschen")
st.subheader("Winter? Nein, danke!")

source = pd.DataFrame({
        'Anteil(%)': [44, 34, 12, 7, 3],
        'Jahreszeit': ['Sommer', 'Frühling', 'Herbst', 'Winter', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Jahreszeit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=2079; 2021; in Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")