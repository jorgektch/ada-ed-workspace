import streamlit as st
import pandas as pd
def ejecutar_analisis():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  data={
    "Operacion": ["int count = 0"],
    "Número de operaciones": ["2"],
    "¿Por qué?": ["Declaración y asignación"]
  }
  df=pd.DataFrame(data)
  st.table(df)
  st.latex(r'''
      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
      \sum_{k=0}^{n-1} ar^k =
      a \left(\frac{1-r^{n}}{1-r}\right)
      ''')
