import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .programa import *

def ejecutar_Prim(theme):
  st.header(f"Semana 09")
  st.write("#")
  ejecutar_enunciado_silla()
  st.write("#")
  ejecutar_analisis_silla()
  st.write("#")
  ejecutar_implementacion_silla()
  st.write("#")
  ejecutar_programa(theme)
  st.write("#")