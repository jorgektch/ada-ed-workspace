import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_01():
  st.header(f"Semana 01")
  ejecutar_enunciado()
  ejecutar_implementacion()
  ejecutar_analisis()
  ejecutar_graficas()
