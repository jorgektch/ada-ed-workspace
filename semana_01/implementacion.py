import streamlit as st

def ejecutar_implementacion1():
  st.subheader("Algoritmo")

  code = '''def sumPair0(vector):
    count = 0
    n = len(vector)
    for i in range(n):
        for j in range(i + 1, n):
            if vector[i] + vector[j] == 0:
                count += 1
    return count
 }'''
  st.code(code, language='python')

def ejecutar_implementacion2():
  st.subheader("Algoritmo")

  code = '''def sumTriple0(vector):
    count = 0
    n = len(vector)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if vector[i] + vector[j] + vector[k] == 0:
                    count += 1
    return count
 }'''
  st.code(code, language='python')
