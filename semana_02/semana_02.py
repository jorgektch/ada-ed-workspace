import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_02():
  st.header(f"Semana 02")
  # Ejercicio 1
  ejecutar_enunciado()
  ejecutar_implementacion1_0()
  ejecutar_analisis1_0()
  ejecutar_implementacion1_1()
  ejecutar_analisis1_1()
  ejecutar_implementacion1_2()
  ejecutar_analisis1_2()
  # Ejercicio 2
  ejecutar_enunciado2()
  ejecutar_implementacion2()
  ejecutar_analisis2()
  # Ejercicio 3
  ejecutar_enunciado3()
  ejecutar_implementacion3()
  ejecutar_analisis3()
  # Ejercicio 4
  ejecutar_enunciado4()
  ejecutar_implementacion4()
  ejecutar_analisis4()
  # Ejercicio 5
  ejecutar_enunciado5()
  ejecutar_implementacion5()
  ejecutar_analisis5()
