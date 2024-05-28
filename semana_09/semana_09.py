import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *
from .programa import *

def ejecutar_semana_09():
  st.header(f"Semana 09")
  st.write("#")
  ejecutar_enunciado_moch2()
  st.write("#")
  ejecutar_analisis_moch2()
  st.write("#")
  ejecutar_implementacion_moch2()
  st.write("#")
  main_moch2()
  st.write("#")
  ejecutar_enunciado_est()
  st.write("#")
  ejecutar_analisis_est()
  st.write("#")
  ejecutar_implementacion_est()
  st.write("#")
  main_est()