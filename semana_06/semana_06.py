import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *
from .programa import *

def ejecutar_semana_06():
  st.header(f"Semana 06")
  st.write("#")
  ejecutar_enunciado()
  st.write("#")
  ejecutar_implementacion()
  st.write("#")
  ejecutar_analisis()
  st.write("#")
  ejecutar_graficas()
  st.write("#")
  ejecutar_programa()
