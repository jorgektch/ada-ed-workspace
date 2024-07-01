import streamlit as st
from .enunciado import *
from .implementacion import *
from .analisis import *
from .graficas import *
from .programa import *

def ejecutar_semana_09(theme:str):
  st.header(f"Semana 09")

  ## Monedas

  st.write("#")
  ejecutar_enunciado_mon()
  st.write("#")
  ejecutar_analisis_mon()
  st.write("#")
  ejecutar_implementacion_mon()
  st.write("#")
  main_mon()
  st.write("#")
  ejecutar_grafica_mon(theme)
  st.write("#")

  ## Mochila - Maximizar por valor
  
  ejecutar_enunciado_moch1()
  st.write("#")
  ejecutar_analisis_moch1()
  st.write("#")
  ejecutar_implementacion_moch1()
  st.write("#")
  main_moch1()
  st.write("#")
  ejecutar_grafica_moch1(theme)
  st.write("#")

  ## Mochila - Maximizar por peso

  ejecutar_enunciado_moch2()
  st.write("#")
  ejecutar_analisis_moch2()
  st.write("#")
  ejecutar_implementacion_moch2()
  st.write("#")
  main_moch2()
  st.write("#")
  ejecutar_grafica_moch2(theme)
  st.write("#")

  ## Mochila - Maximizar por factor valor/peso

  ejecutar_enunciado_moch3()
  st.write("#")
  ejecutar_analisis_moch3()
  st.write("#")
  ejecutar_implementacion_moch3()
  st.write("#")
  main_moch3()
  st.write("#")
  ejecutar_grafica_moch3(theme)
  st.write("#")

  ## Estaciones

  ejecutar_enunciado_est()
  st.write("#")
  ejecutar_analisis_est()
  st.write("#")
  ejecutar_implementacion_est()
  st.write("#")
  main_est()
  ejecutar_grafica_est(theme)
  st.write("#")