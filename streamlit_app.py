import streamlit as st

# Aside menu
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

# Contenido
if "Semana 01" in add_selectbox:
  st.write(f"S1")
elif "Semana 01" in add_selectbox:
  st.write(f"S2")
else:
  st.write(f"Another")

        
