import streamlit as st

# Using object notation
selectbox_values = ["Inicio",
                    "Semana 01",
                    "Semana 02",
                    "Semana 03",
                    "Semana 04",
                    "Semana 05",
                    ]

default_ix = selectbox_values.index("Semana 05")

add_selectbox = st.sidebar.selectbox(
          "Semana de clases",
          selectbox_values,
          index = default_ix,
)

