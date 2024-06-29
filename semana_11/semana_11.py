import streamlit as st

from semana_11.graficas import ejecutar_grafica
from .enunciado import *
from .implementacion import *
from .analisis import *
from .programa import *

def ejecutar_semana_11(theme):
  st.header(f"Semana 11")
  st.write("#")
  ejecutar_enunciado_silla()
  st.write("#")
  ejecutar_analisis_silla()
  st.write("#")
  ejecutar_implementacion_silla()
  st.write("#")
  main_silla()
  st.write("#")
  ejecutar_grafica(theme)