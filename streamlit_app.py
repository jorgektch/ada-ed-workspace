import streamlit as st
import subprocess
from inicio import *
from semana_01.semana_01 import *
from semana_02 import *
from semana_03 import *
from semana_04 import *
from semana_05 import *

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
st.title('Curso: Análisis y diseño de algoritmos')
if "Inicio" in add_selectbox:
  ejecutar_inicio()
if "Semana 01" in add_selectbox:
  semana_01.ejecutar()
elif "Semana 02" in add_selectbox:
  ejecutar_semana_02()
elif "Semana 03" in add_selectbox:
  ejecutar_semana_03()
elif "Semana 04" in add_selectbox:
  ejecutar_semana_04()
elif "Semana 05" in add_selectbox:
  ejecutar_semana_05()
