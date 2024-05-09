import streamlit as st
import pandas as pd
def ejecutar_analisis():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  data={
    "Operacion": ["int count = 0", "int i = 0", "i < arr.length", "i++", "sum++", "if(arr[i])", "count++", "return count >= 2"],
    "Número de operaciones": ["2", "2", "n+1", "2 * n = 2n", "2n", "2", "2"],
    "¿Por qué?": [
                  "Declaración y asignación", 
                  "Declaración y asignación", 
                  "Se realiza una comparación. La acción se repite n veces. Se realiza una vez más como falsa", 
                  "Acción suma y asignación. Se repite n veces.", 
                  "Acción suma y asignación. Se repite n veces por el bucle.", 
                  "Condición y acceso a valor del vector, se repite n veces.", 
                  "Declaración y asignación", 
                  "Comparación y devolver valor"]
  }
  df=pd.DataFrame(data)
  st.table(df)
  st.latex(r'''
      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
      \sum_{k=0}^{n-1} ar^k =
      a \left(\frac{1-r^{n}}{1-r}\right)
      ''')
