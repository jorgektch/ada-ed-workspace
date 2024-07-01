import streamlit as st
import pandas as pd
import numpy as np

from semana_09.dibujarGrafico import crearDiagrama,crearDiagrama_moch

def ejecutar_grafica_mon(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función del vuelto a recibir.")
    
    # Datos del análisis empírico
    variable = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    tiempos_ms = [2.8361, 5.8405, 8.4223, 10.9453, 13.4263, 15.727, 18.1328, 20.6156, 22.9159, 26.4889]
    
    data = {
        "Vuelto": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n = np.array(variable) * (tiempos_ms[0] / variable[0])
    
    crearDiagrama(xpoints, ypoints, y_O_n, "Vuelto vs Tiempo de respuesta", theme, logx=False, logy=False)

def ejecutar_grafica_moch1(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función de la cantidad de objetos. Se tomaron valores aleatorios para el peso del 1 al 10 y para el valor del objeto 1 al 100; además, se tomó valores aleatorios para el peso máximo de 50 a 200.")
    
    # Datos del análisis empírico
    variable = [100, 200, 300, 400, 500, 600, 700, 800]
    tiempos_ms = [0.2901, 0.5569, 0.7604, 1.1550, 1.3379, 1.9416, 2.0343, 2.0806]
    
    data = {
        "Cantidad de objetos": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n = np.array(variable) * (tiempos_ms[0] / variable[0])
    
    crearDiagrama_moch(xpoints, ypoints, y_O_n, "Cantidad de objetos vs Tiempo de respuesta", theme, logx=False, logy=False)

def ejecutar_grafica_moch2(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función de la cantidad de objetos. Se tomaron valores aleatorios para el peso del 1 al 10 y para el valor del objeto del 1 al 100; además, se tomó valores aleatorios para el peso máximo de 50 a 200. Recordemos que la complejidad puede variar aún más y depende del valor  \"k\". En este caso lo compararemos con O(n)")
    
    # Datos del análisis empírico
    variable = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tiempos_ms = [0.2587421001, 0.7305288999, 1.6838513000, 2.0565911999, 3.0094851998, 
              3.5597130999, 4.2046327002, 5.4716113000, 6.2232400000, 5.6627360000]
    
    data = {
        "Cantidad de objetos": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n = np.array(variable) * (tiempos_ms[0] / variable[0])
    
    crearDiagrama_moch(xpoints, ypoints, y_O_n, "Cantidad de objetos vs Tiempo de respuesta", theme, logx=False, logy=False)

def ejecutar_grafica_moch3(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función de la cantidad de objetos. Se tomaron valores aleatorios para el peso del 1 al 10 y para el valor del objeto del 1 al 100; además, se tomó valores aleatorios para el peso máximo de 50 a 200. Recordemos que la complejidad puede variar aún más y depende del valor  \"k\". En este caso lo compararemos con O(n)")
    
    # Datos del análisis empírico
    variable = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    tiempos_ms = [0.0220, 0.0547396000, 0.0973685002, 0.1445450999, 0.1465846000,
                     0.1616026000, 0.2525341001, 0.3482474000, 0.3612130999, 0.4835645999]
    
    data = {
        "Cantidad de objetos": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n = np.array(variable) * (tiempos_ms[0] / variable[0])
    
    crearDiagrama_moch(xpoints, ypoints, y_O_n, "Cantidad de objetos vs Tiempo de respuesta", theme, logx=False, logy=False)

def ejecutar_grafica_est(theme):
    st.subheader("Gráficas")
    st.write("Análisis empírico del tiempo de respuesta en función de los cantidad de elementos de KTotal, es decir, el número de estaciones y estados que abarca.")
    
    # Datos del análisis empírico
    variable = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tiempos_ms = [0.1755460999, 0.3536501999, 0.5290986001, 0.7425073001, 
                        0.9350974001, 1.1042399998, 1.3007725000, 1.4840988000, 
                        1.6546958999, 1.8991705000]
    
    data = {
        "Estado": variable,
        "Tiempo de respuesta (ms)": tiempos_ms
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    xpoints = np.array(variable)
    ypoints = np.array(tiempos_ms)
    
    # Cálculo de O(n)
    y_O_n = np.array(variable) * (tiempos_ms[0] / variable[0])
    
    crearDiagrama_moch(xpoints, ypoints, y_O_n, " Estado vs Tiempo de respuesta", theme, logx=False, logy=False)