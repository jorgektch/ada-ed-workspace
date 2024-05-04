import streamlit as st

def ejecutar_semana_01_implementacion():
  st.subheader("Implementación")

  code = '''def hello():
    print("Hello, Streamlit!")'''
  st.code(code, language='python')

