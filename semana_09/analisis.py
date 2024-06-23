import streamlit as st
import pandas as pd

def ejecutar_analisis_mon():
  
  st.subheader("Análisis")
  st.markdown('''
              Para resolver este problema aplicando una estrategia voraz, colacamos el orden del vector que contiene las monedas en orden descendente,
              esto con el propósito de aplicar una estrategia voraz que permita solucionar el problema rápidamente. La implementación se ve en la función
              main.
              ''')
  
  with st.expander("Main"):
    st.code('''def main():
    monedas = [200, 100, 50, 20, 10, 5, 2, 1]
    cantidad = int(input("Ingrese la cantidad en soles: "))
    solucion = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            solucion.append(moneda)
    print("La cantidad se puede devolver con las siguientes monedas:", solucion)
            ''')
    
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("- **Función main**")
    st.markdown("Para el análisis, solo analizaremos la parte del código donde se realizan iteraciones que sería el bucle for y el bucle")
    oper = ["for moneda in monedas","cantidad >= moneda","cantidad -= moneda","solucion.append(moneda)","Total"]
    pasos = ["2 + 3n","n*k","2k","2k","(3+k)n + 4k + 2"]
    exp = ["Declaración y asignación del valor moneda; comparación, asignación, suma e iteración hasta la longitud máxima del vector monedas de manera implícita (3n), se repite una vez más para salir del bucle", "Comparación, se asume que se repite n*k veces por ambos bucles","Comparación y asignación, se repite k veces por el bucle while", "Asignación y acceso a elemento, se repite k veces por el bucle while",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = (3+k)n + 4k + 2
             ''')
    st.markdown('''Del T(n) anterior, la cantidad que se repite k veces se dará de acuerdo a la resta de elementos hasta llegar a la solución que es el vuelto solicitado. En el peor de los casos se seguirá
                repitiendo una cantidad constante, por lo tanto, el O(n) se puede inferir:''')
    st.latex('''
             T(n) = (3+k)n + 4k + 2 \equiv O(n)
             ''')

def ejecutar_analisis_moch1():
  
  st.subheader("Análisis")
  st.markdown('''
              Para resolver este problema, emplearemos dos funciones principales: "seleccion_por_valor" y "valor_total". Estas funciones nos 
              permitirán tanto calcular el valor total obtenido como elegir los artículos usando una estrategia voraz. Esta estrategia 
              consiste en seleccionar los artículos priorizando los que tienen mayor valor sin exceder la capacidad máxima de la mochila.
              ''')
  
  with st.expander("Seleccion por valor"):
    st.code('''def seleccion_por_valor():
    max_valor = -float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado'] and objetos[j]['valor'] > max_valor:
            max_valor = objetos[j]['valor']
            indice = j
    return indice
            ''')
    
  with st.expander("Valor total"):
    st.code('''def valor_total():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor
            ''')
    
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("- **Función seleccion_por_valor**")
    oper = ["max_valor=-float(\"inf\")","indice = -1","for j in range(len(objetos)):","not objetos[j]['tomado']","objetos[j]['peso'] < menor","menor = objetos[j]['peso']","indice = j","return indice","Total"]
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
            priorizando siempre los artículos más valiosos y asegurando que no se exceda la capacidad máxima. El uso de estas dos funciones se puede apreciar
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

    for i in range(n):
        objetos[i]['peso'] = float(input("Peso del objeto {}? ".format(i)))
        objetos[i]['valor'] = float(input("Valor del objeto {}? ".format(i)))

    PesoMax = float(input("¿Peso máximo de la mochila? "))

    suma_peso = 0

    while suma_peso < PesoMax:
        i = seleccion_por_valor()
        if i == -1:
            break
        peso_restante = PesoMax - suma_peso
        if objetos[i]['peso'] <= peso_restante:
            solucion[i] = 1.0
            suma_peso += objetos[i]['peso']
            objetos[i]['tomado'] = True
        else:
            solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
            suma_peso = PesoMax  # Alcanzamos el límite de peso
            objetos[i]['tomado'] = True
            ''')
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("En este apartado no se analizarán las entradas de datos dado que su análisis es simple (O(n)), por el contrario, se analizará el bucle iterativo while. Además, este bucle es afectado por la función \"seleccion_por_valor\"")
    oper = ["suma_peso < PesoMax","i = seleccion_por_peso()","i == -1","break", "peso_restante = PesoMax - suma_peso", "objetos[i]['peso'] <= peso_restante","solucion[i] = 1.0","suma_peso += objetos[i]['peso']","objetos[i]['tomado'] = True", "solucion[i] = peso_restante / objetos[i]['peso']", "suma_peso = PesoMax", "objetos[i]['tomado'] = True","Total"]
    pasos = ["2","2n + 1","1","1","2","2","2","3","2","4", "1", "2","2n + 23"]
    exp = ["Comparación","Asignación y acceso a función (O(n))","Comparación", "Finaliza el bucle", "Resta y asignación", "Acceso a valor, comparación", "Acceso a elemento y asignación", "Asignación, suma y acceso a elemento", "Asignación y acceso a valor", "Acceso a valor 2 veces, asignación y división", "Asignación", "Acceso a valor y asignación",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.markdown("Por último, la cantidad de operaciones anteriormente obtenida se va a repetir \"k\" veces por el bucle while, obteniendo:")
    st.latex('''
             T(n) = (2n + 23)k
             ''')
    st.markdown("- Para comprobar que se está aplicando un algoritmo voraz (A lo más la complejidad será cuadrática), los corroboramos con el peor de los casos que solo sucede cuando la suma del peso de todos elementos es igual al peso máximo, esto nos da un \"k = n\". Por lo tanto:")
    st.latex('''
             T(n) = (2n + 23)k \\
             T(n) = 2n^2 + 23n \equiv O(n^2)
             ''')
    
def ejecutar_analisis_moch2():
  
  st.subheader("Análisis")
  st.markdown('''
              Para resolver este problema, emplearemos dos funciones principales: "seleccion_por_peso" y "valor_total". Estas funciones nos 
              permitirán tanto calcular el valor total obtenido como elegir los artículos usando una estrategia voraz. Esta estrategia 
              consiste en seleccionar los artículos de menor peso en orden creciente, sin exceder la capacidad máxima de la mochila.
              ''')
  
  with st.expander("Seleccion por peso"):
    st.code('''def seleccion_por_peso():
    menor = float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado'] and objetos[j]['peso'] < menor:
            menor = objetos[j]['peso']
            indice = j
    return indice
            ''')
    
  with st.expander("Valor total"):
    st.code('''def valor_total():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor
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
  
def ejecutar_analisis_moch3():
  
  st.subheader("Análisis")
  st.markdown('''
              Para resolver este problema, emplearemos dos funciones principales: "seleccion_por_valor_peso" y "valor_total". Estas funciones nos 
              permitirán tanto calcular el valor total obtenido como elegir los artículos usando una estrategia voraz. Esta estrategia 
              consiste en seleccionar los artículos priorizando el objeto que tenga mayor valor según su peso, sin exceder la capacidad máxima de la mochila.
              ''')
  
  with st.expander("Seleccion por valor peso"):
    st.code('''def seleccion_por_valor_peso():
    max_valor_peso = -float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado']:
            valor_peso = objetos[j]['valor'] / objetos[j]['peso']
            if valor_peso > max_valor_peso:
                max_valor_peso = valor_peso
                indice = j
    return indice
            ''')
    
  with st.expander("Valor total"):
    st.code('''def valor_total():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor
            ''')
    

  st.markdown('''
            En este caso no realizaremos un análisis detallado del T(n) y BigO dado que sería muy similar a los anteriores análisis. De acuerdo a lo que hemos aprendido
            de los anteriores problemas de la mochila, podemos inferir que las funciones tendrán una complejidad de O(n).
            ''')
  
  st.markdown('''
            Al utilizar estas dos funciones de manera combinada, seguimos una metodología que asegura que la mochila se llena de una manera muy eficiente, 
            priorizando siempre los artículos más valiosos de acuerdo al peso y asegurando que no se exceda la capacidad máxima. El uso de estas dos funciones se puede apreciar
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

    for i in range(n):
        objetos[i]['peso'] = float(input(f"Peso del objeto {i}? "))
        objetos[i]['valor'] = float(input(f"Valor del objeto {i}? "))

    PesoMax = float(input("¿Peso máximo de la mochila? "))

    suma_peso = 0

    while suma_peso < PesoMax:
        i = seleccion_por_valor_peso()
        if i == -1:
            break
        peso_restante = PesoMax - suma_peso
        if objetos[i]['peso'] <= peso_restante:
            solucion[i] = 1.0
            suma_peso += objetos[i]['peso']
            objetos[i]['tomado'] = True
        else:
            solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
            suma_peso = PesoMax  # Alcanzamos el límite de peso
            objetos[i]['tomado'] = True
            ''')
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    st.markdown("En este apartado no se analizarán las entradas de datos dado que su análisis es simple (O(n)), por el contrario, se analizará el bucle iterativo while. Además, este bucle es afectado por la función \"seleccion_por_valor_peso\"")
    oper = ["suma_peso < PesoMax","i = seleccion_por_valor_peso()","i == -1","break", "peso_restante = PesoMax - suma_peso", "objetos[i]['peso'] <= peso_restante","solucion[i] = 1.0","suma_peso += objetos[i]['peso']","objetos[i]['tomado'] = True", "solucion[i] = peso_restante / objetos[i]['peso']", "suma_peso = PesoMax", "objetos[i]['tomado'] = True","Total"]
    pasos = ["2","2n + 1","1","1","2","2","2","3","2","4", "1", "2","2n + 23"]
    exp = ["Comparación","Asignación y acceso a función (O(n))","Comparación", "Finaliza el bucle", "Resta y asignación", "Acceso a valor, comparación", "Acceso a elemento y asignación", "Asignación, suma y acceso a elemento", "Asignación y acceso a valor", "Acceso a valor 2 veces, asignación y división", "Asignación", "Acceso a valor y asignación",""]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.markdown("Por último, la cantidad de operaciones anteriormente obtenida se va a repetir \"k\" veces por el bucle while, obteniendo:")
    st.latex('''
             T(n) = (2n + 23)k
             ''')
    st.markdown("- Para comprobar que se está aplicando un algoritmo voraz (A lo más la complejidad será cuadrática), los corroboramos con el peor de los casos que solo sucede cuando la suma del peso de todos elementos es igual al peso máximo, esto nos da un \"k = n\". Por lo tanto:")
    st.latex('''
             T(n) = (2n + 23)k \\
             T(n) = 2n^2 + 23n \equiv O(n^2)
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