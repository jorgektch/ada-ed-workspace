import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_05():
  st.header(f"Semana 05")
  ejecutar_enunciado()
  ejecutar_implementacion()
  ejecutar_analisis()
  ejecutar_graficas()
