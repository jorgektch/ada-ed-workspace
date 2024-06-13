import streamlit as st
import re
import pandas as pd
from io import StringIO
from collections import namedtuple
import streamlit as st

## Estaciones

KTotal = namedtuple('KTotal', ['name', 'vec', 'tomado'])

def mayor(total):
    max_size = 0
    index = -1
    for i, item in enumerate(total):
        if not item.tomado and len(item.vec) > max_size:
            max_size = len(item.vec)
            index = i
    return index

def main_est():
    st.header("Programa")

    total = []
    
    num = st.number_input("Ingrese la cantidad de estaciones en total:", min_value=1, step=1)

    for i in range(num):
        name = st.text_input(f"Nombre de la estación {i + 1}:")
        vec_input = st.text_input(f"Estados de la estación {i + 1} separados por espacios:")
        vec = vec_input.split()
        total.append(KTotal(name=name, vec=vec, tomado=False))

    estados = set().union(*(item.vec for item in total))
    
    actual = []
    estaciones_tomadas = []

    if st.button("Calcular", key="calc_estaciones"):
        while True:
            i = mayor(total)
            if i != -1 and set(actual) != estados:
                estaciones_tomadas.append(total[i].name)
                actual.extend(total[i].vec)
                total[i] = total[i]._replace(tomado=True)
                actual = list(set(actual))
            else:
                break

        st.write("Estaciones tomadas:", estaciones_tomadas)
        st.write("Vector actual:", actual)

## Mochila - Caso minimizar peso

def seleccion_por_peso():
    menor = float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado'] and objetos[j]['peso'] < menor:
            menor = objetos[j]['peso']
            indice = j
    return indice

def valor_total():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor

def main_moch2():
    global objetos, solucion

    st.header("Programa")
    
    n = st.number_input("Colocar la cantidad de objetos:", min_value=1, step=1)

    objetos = [{'peso': 0, 'valor': 0, 'tomado': False} for _ in range(n)]
    solucion = [0] * n

    suma = 0
    for i in range(n):
        objetos[i]['peso'] = st.number_input(f"Peso del objeto {i+1}:", min_value=0.0, step=0.1)
        objetos[i]['valor'] = st.number_input(f"Valor del objeto {i+1}:", min_value=0.0, step=0.1)
    
    PesoMax = st.number_input("¿Peso máximo de la mochila?", min_value=0.0, step=0.1)

    if st.button("Calcular", key="calc_mochila"):
        while suma < PesoMax:
            i = seleccion_por_peso()
            if i == -1:
                break
            if (suma + objetos[i]['peso']) <= PesoMax:
                solucion[i] = 1
                suma += objetos[i]['peso']
                objetos[i]['tomado'] = True
            else:
                break

        st.write("El valor máximo obtenido es:", valor_total())
        st.write("Y el vector solución es:")
        st.write(solucion)