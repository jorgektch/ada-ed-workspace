import streamlit as st

def ejecutar_implementacion_moch2():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
    st.code('''def EsSolucion(nodo):
    return len(nodo) == 3

def Expandir(nodo):
    personas = ['amarilla', 'roja', 'negra']
    nuevos_nodos = []
    for persona in personas:
        if persona not in nodo:
            nuevo_nodo = nodo + [persona]
            nuevos_nodos.append(nuevo_nodo)
    return nuevos_nodos

def EsFactible(nodo):
    if len(nodo) > 1 and nodo[1] == 'amarilla':
        return False
    if len(nodo) > 0 and nodo[0] == 'roja':
        return False
    return True

def backtracking(nodo):
    lista_soluciones = []
    if EsSolucion(nodo):
        lista_soluciones.append(nodo)
    for v in Expandir(nodo):
        if EsFactible(v):   
            ls = backtracking(v)
            lista_soluciones.extend(ls)
    return lista_soluciones

nodo_inicial = []

soluciones = backtracking(nodo_inicial)

for solucion in soluciones:
    print(solucion)
           ''')