import streamlit as st
import subprocess
import sys

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
if "Inicio" in add_selectbox:
  subprocess.run([f"{sys.executable}", "inicio.py"])
if "Semana 01" in add_selectbox:
  subprocess.run([f"{sys.executable}", "semana-01.py"])
elif "Semana 01" in add_selectbox:
  subprocess.run([f"{sys.executable}", "semana-02.py"])
else:
  st.write(f"Another")

        
