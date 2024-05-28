import streamlit as st

def ejecutar_implementacion_moch2():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
    st.code('''def seleccion_por_peso():
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

def main():
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

if __name__ == "__main__":
    main()
            ''')

def ejecutar_implementacion_est():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
    st.code('''from collections import namedtuple

KTotal = namedtuple('KTotal', ['name', 'vec', 'tomado'])

def mayor(total):
    max_size = 0
    index = -1
    for i, item in enumerate(total):
        if not item.tomado and len(item.vec) > max_size:
            max_size = len(item.vec)
            index = i
    return index

if __name__ == "__main__":
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