import streamlit as st

# Using object notation
selectbox_values = ['Seleccionar',
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

values2 = ['Select', 10, 15, 20, 25, 30]
default_ix2 = values.index(10)
if values2 == 'Select':
    st.warning("Choose the integers from the list in the dropdown")
else:
    components = st.selectbox("Select the components below⤵️", values2, 
    index=default_ix2)
