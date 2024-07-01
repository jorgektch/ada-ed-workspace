import streamlit as st
import pandas as pd

def ejecutar_analisis_silla():
  
  st.subheader("Análisis")
  st.markdown('''
              En el código de resolución del problema, se ha implementado la estructura proporcionada por el profesor,
              sin embargo, hemos realizado unos cuántos cambios siguiendo con la estructura funcional.
              ''')
  
  with st.expander("Estructura"):
    st.code('''def backtracking(nodo):
    if EsSolucion(nodo):
        return nodo
    for v in Expandir(nodo):
        if EsFactible(v):   
            s = backtracking(v)
            if s! = None
                return s
    return None
            ''')
    
  with st.expander("Estructura modificada"):
    st.code('''def backtracking(nodo):
    lista_soluciones = []
    if EsSolucion(nodo):
        lista_soluciones.append(nodo)
    for v in Expandir(nodo):
        if EsFactible(v):   
            ls = backtracking(v)
            lista_soluciones.extend(ls)
    return lista_soluciones
            ''')
    
  st.markdown('''
              Las tres funciones: EsSolucion(nodo), Expandir(nodo), EsFactible(v); se han modificado a nuestor criterio, en este caso, EsSolucion retornaría un
                valor booleano cuando se haya detectado una solución de tamaño 3 para la lista_soluciones. Expandir, evaluaría si el nodo es expandible, si lo es, devolvería
                la lista de expansiones o combinaciones que todavía no se han probado en la que resta de la lista. Finalmente, EsFactible evaluaría si las listas de expansión
                brindadas por la función Expandir son soluciones, si lo es, se realiza backtracking de nuevo hasta que llegue a la solución esperada y verificada por EsSolucion y termine
                retornando lista_soluciones.
              ''')
    
  with st.expander("EsSolucion"):
        st.code('''def EsSolucion(nodo):
    return len(nodo) == 3
                ''')
    
  with st.expander("Expandir"):
        st.code('''personas = ['amarilla', 'roja', 'negra']
    nuevos_nodos = []
    for persona in personas:
        if persona not in nodo:
            nuevo_nodo = nodo + [persona]
            nuevos_nodos.append(nuevo_nodo)
    return nuevos_nodos
                ''')
        
  with st.expander("EsFactible"):
        st.code('''def EsFactible(nodo):
    if len(nodo) > 1 and nodo[1] == 'amarilla':
        return False
    if len(nodo) > 0 and nodo[0] == 'roja':
        return False
    return True
                ''')

  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("Para este análisis, se descartó las funciones EsSolucion y EsFactible dado que tienen una complejidad O(1), sin embargo, sí se consideró las otras funciones.")
    st.markdown("- **Función Expandir**")
    oper = ["for persona in personas", "persona not in nodo", "nuevo_nodo = nodo + [persona]", "nuevos_nodos.append(nuevo_nodo)", "return nuevos_nodos", "Total"]
    pasos = ["3 + 3n","n","3n","2n","1","9n + 4"]
    exp = ["Declaración y asignación del valor persona; comparación, asignación, suma e iteración hasta la longitud del vector personas de manera implícita (3n), se repite una vez más para salir del bucle", "Comparación con los elementos del nodo, se repite n veces", "Suma, acceso a valor y asignación, se repite n veces", "Acceso a valor y asignación, se repite n veces", "Devuelve el resultado",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = 9n + 4 \equiv O(n)
             ''')
    
    st.write("#")
    st.markdown("- **Función backtracking**")
    st.markdown('''
            En este caso, es una función recursiva, no iterativa, por lo tanto el análisis que se aplicará a continuación es distinto. Primero hay que entender lo siguiente: 
            La función Expandir itera sobre un conjunto fijo de N elementos (personas o colores) y genera nuevos nodos. Por cada persona no presente en el nodo actual, se crea un nuevo nodo.
            En el peor de los casos, la función itera sobre todos los elementos en personas.
            ''')
    st.markdown('''
            Como segundo punto a analizar: backtracking es la función recursiva que hace el trabajo principal. En el peor de los casos, explora todos los nodos posibles que pueden ser generados.
            El número total de nodos en el árbol de recursión es el número de permutaciones de N elementos tomados de 3 en 3 (Ya que en este caso la longitud máxima del nodo es 3). Por lo tanto, considerando
            que la recursión puede ser visualizada como un árbol donde cada nodo puede tener hasta "N-len(nodo)" hijos:
            ''')
    st.write("#")
    st.markdown('''
            Nivel 0: 1 nodo \\
            Nivel 1: N nodos \\
            Nivel 2: N * (N-1) nodos \\
            Nivel 3: N * (N-1) * (N-2) nodos \\
            ''')
    
    st.markdown('''
            Como se puede visualizar, el algoritmo de backtracking nos generaría una complejidad, para este caso, de O(N^3), sin embargo, consderando la estructura, de manera general,
            se puede deducir que el algoritmo generará una complejidad de O(N!).
            ''')