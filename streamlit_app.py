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
from algoritmos.algoritmos import *
from streamlit_theme import st_theme

theme = st_theme()
if(theme is not None):
  theme = theme["base"]



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
                    "Algoritmos"
                    ]

default_ix = selectbox_values.index("Semana 06")

add_selectbox = st.sidebar.selectbox(
          "Semana de clases",
          selectbox_values,
          index = default_ix,
)

if "Algoritmos" in add_selectbox:
  selectbox_valuesAlg = ["DFS",
                      "BFS",
                      "Ordenamiento topologico",
                      "Prim",
                      "Kruskal",
                      "Dijkstra",
                      "A* Search",
                      ]

  default_ixAlg = selectbox_valuesAlg.index("DFS")

  add_selectboxAlg = st.sidebar.selectbox(
            "Algoritmos",
            selectbox_valuesAlg,
            index = default_ixAlg,
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
  ejecutar_semana_06(theme)
elif "Semana 09" in add_selectbox:
  ejecutar_semana_09()
elif "Semana 11" in add_selectbox:
  ejecutar_semana_11()
elif "Algoritmos" in add_selectbox:
  ejecutar_algoritmos(add_selectboxAlg, theme)
