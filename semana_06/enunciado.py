import streamlit as st

def ejecutar_enunciado():
  st.subheader("Enunciado")
  st.markdown('''
              Escriba un programa para ejecutar las apariciones de cada palabra en un archivo grande
              - Permita que el usuario escriba una palabra e informe cuantas veces aparecio esa palabra en el libro.
              - Informe todas las palabras que aparecieron en el libro al menos 500 veces, en orden alfabetico.
              - ¿Como almacenaremos los datos para resolver este problema? ''')