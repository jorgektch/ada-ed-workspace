import streamlit as st
import subprocess
from inicio.inicio import *
from semana_01.semana_01 import *
from semana_02.semana_02 import *
from semana_03.semana_03 import *
from semana_04.semana_04 import *
from semana_05.semana_05 import *
from semana_06.semana_06 import *
from semana_09.semana_09 import *
from semana_11.semana_11 import *

# Aside menu
selectbox_values = ["Inicio",
                    "Semana 01",
                    "Semana 02",
                    "Semana 03",
                    "Semana 04",
                    "Semana 05",
                    "Semana 06",
                    "Semana 09",
                    "Semana 11",
                    ]

default_ix = selectbox_values.index("Semana 06")

add_selectbox = st.sidebar.selectbox(
          "Semana de clases",
          selectbox_values,
          index = default_ix,
)

# Contenido
st.title('Curso: Análisis y diseño de algoritmos')
st.divider()
if "Inicio" in add_selectbox:
  ejecutar_inicio()
if "Semana 01" in add_selectbox:
  ejecutar_semana_01()
elif "Semana 02" in add_selectbox:
  ejecutar_semana_02()
elif "Semana 03" in add_selectbox:
  ejecutar_semana_03()
elif "Semana 04" in add_selectbox:
  ejecutar_semana_04()
elif "Semana 05" in add_selectbox:
  ejecutar_semana_05()
elif "Semana 06" in add_selectbox:
  ejecutar_semana_06()
elif "Semana 09" in add_selectbox:
  ejecutar_semana_09()
elif "Semana 11" in add_selectbox:
  ejecutar_semana_11()