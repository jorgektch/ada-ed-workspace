import streamlit as st
import pandas as pd
def ejecutar_analisis1():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  st.latex(r'''
        T(n) = 
        \begin{cases} 
        c_{1} & \text{Si } n = 0 \\
        c_{2} \cdot n(n-1)/2 & \text{Si } n \geq 1
        \end{cases}
    ''')
  st.write("Paso 4: Derivar la función recursiva de \( T(n) \)")
  st.latex(r'''
        T(n) = c_{2} \cdot \frac{n(n-1)}{2}
        ''')
  st.write("Por lo tanto, la complejidad es:")
  st.latex(r'''
      T(n) = O(n^2)
  ''')

def ejecutar_analisis2():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  st.latex(r'''
      T(n) = 
      \begin{cases} 
      c_{1} & \text{Si } n = 0 \\
      c_{2} \cdot \frac{n(n-1)(n-2)}{6} & \text{Si } n \geq 1
      \end{cases}
  ''')
  st.write("Paso 4: Derivar la función recursiva de \( T(n) \)")
  st.latex(r'''
      T(n) = c_{2} \cdot \frac{n(n-1)(n-2)}{6}
  ''')
  st.write("Por lo tanto, la complejidad es:")
  st.latex(r'''
      T(n) = O(n^3)
  ''')