import streamlit as st
import pandas as pd

def ejecutar_analisis_moch2():
  
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
    st.markdown("- **Función seleccion_por_peso**")
    oper = ["menor=float(\"inf\")","indice = -1","for j in range(len(objetos)):","not objetos[j]['tomado']","objetos[j]['peso'] < menor","menor = objetos[j]['peso']","indice = j","return indice","Total"]
    pasos = ["2","2","3 + 3n","2n","2n","2","1","1","7n + 11"]
    exp = ["Declaración y Asignación","Declaración y asignación","Declaración y asignación del valor j; comparación, asignación, suma e iteración hasta la longitud n de manera implícita (3n), se repite una vez más para salir del bucle", "Evaluación y acceso a elemento (2), se repite n veces por el bucle", "Comparación y acceso a elemento (2)", "Asignación y acceso a elemento", "Asignación", "Devuelve el resultado",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = 7n + 11 \equiv O(n)
             ''')
    st.write("#")
    st.markdown("- **Función valor_total**")
    oper = ["valor = 0","for i in range(len(objetos)):","valor += objetos[i]['valor'] * solucion[i]","return valor","Total"]
    pasos = ["2", "3 + 3n","5n","1","8n + 6"]
    exp = ["Declaración y Asignación","Declaración y asignación del valor i; comparación, asignación, suma e iteración hasta la longitud n de manera implícita (3n), se repite una vez más para salir del bucle", "Asignación, suma, multiplicación y doble acceso a elementos, se repite n veces por el bucle","Devuelve el resultado",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = 8n + 11 \equiv O(n)
             ''')
    
  st.markdown('''
            Al utilizar estas dos funciones de manera combinada, seguimos una metodología que asegura que la mochila se llena de una manera muy eficiente, 
            priorizando siempre los artículos más ligeros y asegurando que no se exceda la capacidad máxima. El uso de estas dos funciones se puede apreciar
            en la función "main" del programa. 
            ''')
  
  with st.expander("Main"):
    st.code('''def main():
  global objetos, solucion

  n = int(input("Colocar la cantidad de objetos: "))

  objetos = [{'peso': 0, 
          'valor': 0, 
          'tomado': False} 
          for _ in range(n)]

  solucion = [0] * n

  suma = 0
  for i in range(n):
      objetos[i]['peso'] = float(input("Peso del objeto {}? ".format(i)))
      objetos[i]['valor'] = float(input("Valor del objeto {}? ".format(i)))
  
  PesoMax = float(input("¿Peso máximo de la mochila? "))

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

  print("El valor máximo obtenido es:", valor_total())
  print("Y el vector solución es:")
  print(solucion)
  input("...")
            ''')
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("En este apartado no se analizarán las entradas de datos dado que su análisis es simple (O(n)), por el contrario, se analizará el bucle iterativo while. Además, este bucle es afectado por la función \"seleccion_por_peso\"")
    oper = ["suma < PesoMax","i = seleccion_por_peso()","i == -1","break","(suma + objetos[i]['peso']) <= PesoMax","solucion[i] = 1","suma += objetos[i]['peso']","objetos[i]['tomado'] = True", "break","Total"]
    pasos = ["2","2n + 1","1","1","3","2","3","2","1","2n + 14"]
    exp = ["Comparación","Asignación y acceso a función (O(n))","Comparación", "Finaliza el bucle", "Suma, acceso a valor, comparación", "Acceso a elemento y asignación", "Asignación, suma y acceso a elemento", "Asignación y acceso a valor", "Finaliza el bucle",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.markdown("Por último, la cantidad de operaciones anteriormente obtenida se va a repetir \"k\" veces por el bucle while, obteniendo:")
    st.latex('''
             T(n) = (2n + 14)k
             ''')
    st.markdown("- Para comprobar que se está aplicando un algoritmo voraz (A lo más la complejidad será cuadrática), los corroboramos con el peor de los casos que solo sucede cuando la suma del peso de todos elementos es igual al peso máximo, esto nos da un \"k = n\". Por lo tanto:")
    st.latex('''
             T(n) = (2n + 14)k \\
             T(n) = 2n^2 + 14n \equiv O(n^2)
             ''')
  
def ejecutar_analisis_est():
  
  st.subheader("Análisis")
  st.markdown('''
              Para la solución del problema mediante un algoritmo voraz, hemos seleccionado con prioridad las estaciones de radio que cubren más estados de manera iterativa hasta
              que se cubran todas las estaciones requeridas; de esta manera se gastará invertirá menos tiempo en la búsqueda de estaciones. El código de solución solo emplea una función,
              la función "mayor" que devuelve el índice o posición de la estación que cubre la mayor cantidad de estados.
              ''')
  
  with st.expander("Mayor"):
    st.code('''def mayor(total):
    max_size = 0
    index = -1
    for i, item in enumerate(total):
        if not item.tomado and len(item.vec) > max_size:
            max_size = len(item.vec)
            index = i
    return index
            ''')
    
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("- **Función mayor**")
    oper = ["max_size = 0","index = -1","for i, item in enumerate(total):","not item.tomado","len(item.vec) > max_size","max_size = len(item.vec)","index = i","return index","Total"]
    pasos = ["2","2","3 + 3n","2n","2n","2","1","1","7n + 11"]
    exp = ["Declaración y Asignación","Declaración y asignación","Declaración y asignación del valor i; comparación, asignación, suma e iteración hasta la longitud n de manera implícita (3n), se repite una vez más para salir del bucle", "Evaluación y acceso a elemento (2), se repite n veces por el bucle", "Comparación y acceso a elemento (2)", "Asignación y acceso a elemento", "Asignación", "Devuelve el resultado",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = 7n + 11 \equiv O(n)
             ''')
    
  st.markdown('''
            Esta función será llamada en el main del programa; por esta razón, debemos evaluar el Big(O) del main teniendo en cuenta la función "mayor". 
            ''')
  
  with st.expander("Main"):
    st.code('''if __name__ == "__main__":
    total = []
    
    num = int(input("Ingrese la cantidad de elementos del total: "))

    for _ in range(num):
        name = input("Ingrese el nombre del elemento: ")
        vec = input("Ingrese los elementos del vector separados por espacios: ").split()
        total.append(KTotal(name=name, vec=vec, tomado=False))

    estados = set().union(*(item.vec for item in total))
    
    actual = []
    estaciones_tomadas = []

    while True:
        i = mayor(total)
        if i != -1 and set(actual) != estados:
            estaciones_tomadas.append(total[i].name)
            actual.extend(total[i].vec)
            total[i] = total[i]._replace(tomado=True)
            actual = list(set(actual))
        else:
            break

    print("Estaciones tomadas:", estaciones_tomadas)
    print("Vector actual:", actual)
    input("Presiona Enter para salir...")
            ''')
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("En este apartado no se analizarán las entradas de datos dado que su análisis es simple (O(n)), por el contrario, se analizará solo el bucle iterativo while dado que el resto del código serían constante a excepción del bucle. Recordemos que este bucle es afectado por la función \"mayor\"")
    oper = ["i = mayor(total)","i != -1","set(actual) != estados","estaciones_tomadas.append(total[i].name)","actual.extend(total[i].vec)","total[i] = total[i]._replace(tomado=True)","actual = list(set(actual))", "break","Total"]
    pasos = ["1 + n","1","2","2","2","5","3","1","n + 17"]
    exp = ["Asignación y llamada a la función con complejidad O(n)","Comparación", "Acceso a función y comparación", "Acceso a elemento y asignación", "Acceso a elemento y asignación", "Asignación (3) y acceso a elemento (2)", "Asignación y llamada a función(2)", "Finaliza el bucle",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.markdown("Por último, la cantidad de operaciones anteriormente obtenida se va a repetir \"k\" veces por el bucle while, obteniendo:")
    st.latex('''
             T(n) = (n + 17)k
             ''')
    st.markdown("- Para comprobar que se está aplicando un algoritmo voraz (A lo más la complejidad será cuadrática), los corroboramos con el peor de los casos que solo sucede cuando es necesario comprar todas las estaciones de radio para abarcar todos los estados, esto nos da un \"k = n\". Por lo tanto:")
    st.latex('''
             T(n) = (n + 17)k \\
             T(n) = n^2 + 17n \equiv O(n^2)
             ''')