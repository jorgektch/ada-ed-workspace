import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *

def ejecutar_semana_05():
  st.header(f"Semana 05")
  ejecutar_enunciado()
  ejecutar_implementacion_mergesort()
  ejecutar_analisis_mergesort()
  ejecutar_implementacion_quicksort()
  ejecutar_analisis_quicksort()
  ejecutar_implementacion_heapsort()
  ejecutar_analisis_heapsort()
  ejecutar_implementacion_insertionsort()
  ejecutar_analisis_insertionsort()
  ejecutar_implementacion_shellsort()
  ejecutar_analisis_shellsort()
  ejecutar_graficas()
