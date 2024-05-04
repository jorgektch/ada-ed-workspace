import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_03():
  st.header(f"Semana 03")
  ejecutar_enunciado()
  ejecutar_implementacion()
  ejecutar_analisis()
  ejecutar_graficas()
