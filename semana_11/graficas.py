import streamlit as st
import pandas as pd
import numpy as np
from math import factorial
from semana_11.dibujarGrafico import crearDiagrama

def ejecutar_grafica(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función de la cantidad de personas/colores ingresados. Para este análisis se consideró la regla del ejemplo: el rojo no puede sentarse primero y el amarillo no puede sentarse segundo.")
    
    # Datos del análisis empírico
    variable = [3, 4, 5, 6, 7, 8, 9]
    tiempos_ms = [0.0058499000, 0.1057998743, 0.2492000349, 1.1702000629,
                        8.7876999751, 78.7734999321, 777.8373998590]
    
    data = {
        "Cantidad": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n_fac = np.array([factorial(n) for n in variable]) * (tiempos_ms[0] / factorial(variable[0]))
    
    crearDiagrama(xpoints, ypoints, y_O_n_fac, "Cantidad vs Tiempo de respuesta", theme, logx=False, logy=False)