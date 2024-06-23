import streamlit as st
def ejecutar_implementacion_mon():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
    st.code('''def main():
    monedas = [200, 100, 50, 20, 10, 5, 2, 1]
    cantidad = int(input("Ingrese la cantidad en soles: "))
    solucion = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            solucion.append(moneda)
    print("La cantidad se puede devolver con las siguientes monedas:", solucion)

if __name__ == "__main__":
    main()
            ''')
    
def ejecutar_implementacion_moch1():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
    st.code('''def seleccion_por_valor():
    max_valor = -float('inf')
    indice = -1
    for j in range(len(objetos)):
        if not objetos[j]['tomado'] and objetos[j]['valor'] > max_valor:
            max_valor = objetos[j]['valor']
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
            solucion[i] = 1.0  # Tomar el objeto completo
            suma_peso += objetos[i]['peso']
            objetos[i]['tomado'] = True
        else:
            solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
            suma_peso = PesoMax  # Alcanzamos el límite de peso
            objetos[i]['tomado'] = True

    print("El valor máximo obtenido es:", valor_total())
    print("Y el vector solución es:")
    print(solucion)
    input("...")

if __name__ == "__main__":
    main()
            ''')

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
    
def ejecutar_implementacion_moch3():
  st.subheader("Implementación")
  
  with st.expander("Codigo completo"):
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
            solucion[i] = 1.0  # Tomar el objeto completo
            suma_peso += objetos[i]['peso']
            objetos[i]['tomado'] = True
        else:
            solucion[i] = peso_restante / objetos[i]['peso']  # Tomar parte del objeto
            suma_peso = PesoMax  # Alcanzamos el límite de peso
            objetos[i]['tomado'] = True

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