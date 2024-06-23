import streamlit as st
from collections import namedtuple

#Monedas

def main_mon():
    st.header("Programa de cambio con la menor cantidad de monedas")

    cantidad = st.number_input("Ingrese el vuelto a recibir (Número entero):", min_value=0, step=1)
    monedas = [200, 100, 50, 20, 10, 5, 2, 1]

    if st.button("Calcular"):
        solucion = []
        for moneda in monedas:
            while cantidad >= moneda:
                cantidad -= moneda
                solucion.append(moneda)
        st.write("La cantidad se puede devolver con las siguientes monedas:", solucion)


# Mochila - Caso escoger según su factor valor/peso

def seleccion_por_valor_peso():
    max_valor_peso = -float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado']:
            valor_peso = objetos[j]['valor'] / objetos[j]['peso']
            if valor_peso > max_valor_peso:
                max_valor_peso = valor_peso
                indice = j
    return indice

def valor_total():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor

def main_moch3():
    global objetos, solucion

    st.header("Programa de selección de objetos para mochila (Factor valor/peso)")

    n = st.number_input("Colocar la cantidad de objetos:", min_value=1, step=1)

    objetos = [{'peso': 0, 'valor': 0, 'tomado': False} for _ in range(n)]
    solucion = [0] * n

    for i in range(n):
        objetos[i]['peso'] = st.number_input(f"Peso del objeto {i+1}:", min_value=0.0, step=0.1, key=f"peso_{i}")
        objetos[i]['valor'] = st.number_input(f"Valor del objeto {i+1}:", min_value=0.0, step=0.1, key=f"valor_{i}")

    PesoMax = st.number_input("¿Peso máximo de la mochila?", min_value=0.0, step=0.1, key="peso_max")

    if st.button("Calcular", key="calc_mochila3"):
        suma_peso = 0

        while suma_peso < PesoMax:
            i = seleccion_por_valor_peso()
            if i == -1:
                break
            peso_restante = PesoMax - suma_peso
            if objetos[i]['peso'] <= peso_restante:
                solucion[i] = 1.0  # Tomar el objeto completo
                suma_peso += objetos[i]['peso']
                objetos[i]['tomado'] = True
            else:
                solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
                suma_peso = PesoMax  # Alcanzamos el límite de peso
                objetos[i]['tomado'] = True

        st.write("El valor máximo obtenido es:", valor_total())
        st.write("Y el vector solución es:")
        st.write(solucion)

# Mochila - Caso escoger los de mayor valor

def seleccion_por_valor():
    max_valor = -float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado'] and objetos[j]['valor'] > max_valor:
            max_valor = objetos[j]['valor']
            indice = j
    return indice

def valor_total1():
    valor = 0
    for i in range(len(objetos)):
        valor += objetos[i]['valor'] * solucion[i]
    return valor

def main_moch1():
    global objetos, solucion

    st.header("Programa de selección de objetos para mochila (Mayor valor)")

    n = st.number_input("Colocar la cantidad de objetos:", min_value=1, step=1, key="num_objs1")

    objetos = [{'peso': 0, 'valor': 0, 'tomado': False} for _ in range(n)]
    solucion = [0] * n

    for i in range(n):
        objetos[i]['peso'] = st.number_input(f"Peso del objeto {i+1}:", min_value=0.0, step=0.1, key=f"peso_{i}_1")
        objetos[i]['valor'] = st.number_input(f"Valor del objeto {i+1}:", min_value=0.0, step=0.1, key=f"valor_{i}_1")

    PesoMax = st.number_input("¿Peso máximo de la mochila?", min_value=0.0, step=0.1, key="peso_max1")

    if st.button("Calcular", key="calc_mochila1"):
        suma_peso = 0

        while suma_peso < PesoMax:
            i = seleccion_por_valor()
            if i == -1:
                break
            peso_restante = PesoMax - suma_peso
            if objetos[i]['peso'] <= peso_restante:
                solucion[i] = 1.0  # Tomar el objeto completo
                suma_peso += objetos[i]['peso']
                objetos[i]['tomado'] = True
            else:
                solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
                suma_peso = PesoMax  # Alcanzamos el límite de peso
                objetos[i]['tomado'] = True

        st.write("El valor máximo obtenido es:", valor_total1())
        st.write("Y el vector solución es:")
        st.write(solucion)

# Estaciones

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
    st.header("Programa de selección de estaciones")

    total = []
    
    num = st.number_input("Ingrese la cantidad de estaciones en total:", min_value=1, step=1, key="num_estaciones")

    for i in range(num):
        name = st.text_input(f"Nombre de la estación {i + 1}:", key=f"name_{i}")
        vec_input = st.text_input(f"Estados de la estación {i + 1} separados por espacios:", key=f"vec_input_{i}")
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

# Mochila - Caso minimizar peso

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

    st.header("Programa de selección de objetos para mochila (Menor peso)")
    
    n = st.number_input("Colocar la cantidad de objetos:", min_value=1, step=1, key="num_objs2")

    objetos = [{'peso': 0, 'valor': 0, 'tomado': False} for _ in range(n)]
    solucion = [0] * n

    for i in range(n):
        objetos[i]['peso'] = st.number_input(f"Peso del objeto {i+1}:", min_value=0.0, step=0.1, key=f"peso_{i}_2")
        objetos[i]['valor'] = st.number_input(f"Valor del objeto {i+1}:", min_value=0.0, step=0.1, key=f"valor_{i}_2")
    
    PesoMax = st.number_input("¿Peso máximo de la mochila?", min_value=0.0, step=0.1, key="peso_max2")

    if st.button("Calcular", key="calc_mochila2"):
        suma = 0
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