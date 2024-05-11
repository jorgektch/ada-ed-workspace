import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .dibujarGrafico import *
from streamlit_theme import st_theme

def getLog(arr):
  return np.array(arr) * np.log2(arr) * 2.234

def ejecutar_graficas():
  st.subheader("Gráficas")
  st.write("Se presenta el analisis empirico, hecho en python, realizado sobre la insercion de n elementos dentro de un set usando un arbol AVL para su implementacion.")
  nsize = ["10","100","1000","10000","100000","1000000"]
  time = ["0 ms","1001.3580 ms","11964.5595 ms","161956.3102 ms","2345753.6697 ms","35468925.9529 ms"]
  data = {
    "n" : nsize,
    "tiempo de ejecucion (ms)" : time 
  }
  df = pd.DataFrame(data)
  st.table(df)

  theme = st_theme()
  theme = theme["base"]

  xpoints = np.array([10,100,1000,10000,100000,1000000])
  ypoints = np.array([98,1001.3580,11964.5595,161956.3102,2345753.6697,35468925.9529])

  x_log = [10,100,1000,10000,100000,1000000] 
  y_log = getLog(x_log)
  x_log = np.array(x_log)

  crearDiagrama(x_log,ypoints,y_log,"n vs t(ns) Escala Lineal",theme,True)
  plt.close()
  crearDiagrama(x_log,ypoints,y_log,"n vs t(ns) Escala Logaritmica",theme,True,True)
