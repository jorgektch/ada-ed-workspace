import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *
from .programa import *

def ejecutar_semana_06(theme:str):
  st.header(f"Semana 06")
  st.write("#")
  ejecutar_enunciado()
  st.write("#")
  ejecutar_analisis(theme)
  st.write("#")
  ejecutar_implementacion()
  st.write("#")
  ejecutar_graficas(theme)
  st.write("#")
  ejecutar_programa()
