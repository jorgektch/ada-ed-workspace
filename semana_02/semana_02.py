import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_02():
  st.header(f"Semana 02")
  ejecutar_enunciado()
  ejecutar_implementacion10()
  ejecutar_analisis()
  ejecutar_implementacion11()
  ejecutar_implementacion12()
  ejecutar_graficas()
