import streamlit as st

# Using object notation
selectbox_values = ['<select>',
          "Semana 01",
          "Semana 02",
          "Semana 03",
          "Semana 04",
          "Semana 05",
         ]

default_ix = selectbox_values.index("Semana 05")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    selectbox_values,
    index = default_ix,
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
