import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_01():
  st.header(f"Semana 01")
  ejecutar_enunciado1()
  ejecutar_implementacion1()
  ejecutar_analisis1()

  ejecutar_enunciado2()
  ejecutar_implementacion2()
  ejecutar_analisis2()
