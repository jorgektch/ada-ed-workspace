import streamlit as st
import pandas as pd

def ejecutar_analisis():
  
  st.subheader("Análisis")
  st.markdown('''
              Para resolver este problema, almacenaremos los datos dentro de una estructura de datos de tipo **set**.

              Los sets son conocidos por permitir almacenar una unica instancia de un objeto y podemos agruparlos en dos tipos:
              - Sets ordenados
              - Sets no ordenados

              Para solucionar este problema usaremos especificamente los sets ordenados. Este tipo de sets nos 
              proveen la caracteristica de mantener a todos los elementos ordenados crecientemente, 
              decrecientemente o como lo requiramos al ejecutar los metodos de insercion y eliminacion de elementos.

              La manera mas comun de implementar sets que mantengan un orden es mediante el uso de arboles de busquedda binaria
              combinados con algoritmos de balanceo, siendo el mas utilizado el arbol rojo-negro por su menor numero de rotaciones
              necesarias para mantener al arbol con un balanceo decente. 

              > Si el arbol no se encuentra balanceado, es posible que las operaciones de busqueda ocurran con complejidad O(n) en los peores casos,
                debido a la siguiente estructura:
              ''')
  co1,co2,co3,co4,co5 = st.columns(5)
  with co2:
    st.image('semana_06/skewdTree.jpg',width=400) 
  st.markdown('''
              En este caso, a modo de muestra, haremos la implementacion de un set ordenado mediante arbol de busqueda binaria haciendo uso 
              de un arbol AVL para el balanceo. A diferencia de los arboles rojo-negro, los arboles AVL realizan las operaciones de rotacion
              hasta que el arbol se encuentre estrictamente balanceado, por lo que los metodos de insercion y eliminacion pueden resultar
              menos eficientes, pero garantizamos que las operaciones de busqueda siempre ocurran en un menor tiempo.
              
              Para asegurar que el arbol se encuentre balanceado, se ejecutan las operaciones de rotacion izquierda o derecha dependiendo de la
              diferencia de alturas entre los nodos. 
              ''')
  with st.expander("Rotacion izquierda"):
    st.code('''
            def rotacionIzquierda(self, z): 

                y = z.right 
                son = y.left 

                y.left = z 
                z.right = son 

                z.height = 1 + max(self.obtenerAltura(z.left), 
                                self.obtenerAltura(z.right)) 
                y.height = 1 + max(self.obtenerAltura(y.left), 
                                self.obtenerAltura(y.right)) 

                return y 
            ''')
  with st.expander("Rotacion derecha"):
    st.code('''
            def rotacionDerecha(self, z): 

                y = z.left 
                son = y.right 

                y.right = z 
                z.left = son 

                z.height = 1 + max(self.obtenerAltura(z.left), 
                                self.obtenerAltura(z.right)) 
                y.height = 1 + max(self.obtenerAltura(y.left), 
                                self.obtenerAltura(y.right)) 

                return y 
            ''')
  
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    oper = ["y=z.left","son=y.right","y.right=z","z.left = son","z.height = 1 + max(self.obtenerAltura(z.left), self.obtenerAltura(z.right))","y.height = 1 + max(self.obtenerAltura(y.left), self.obtenerAltura(y.right))","return y",""]
    pasos = ["2","2","2","2","8","8","1","25"]
    exp = ["Acceso y Asignacion","Acceso y Asignacion","Acceso y Asignacion","Acceso y Asignacion","Llamada a funcion max, 2 veces llamada a funcion obtenerAltura con llamadas a acceso, Suma, Asignacion y Acceso","Llamada a funcion max, 2 veces llamada a funcion obtenerAltura con llamadas a acceso, Suma, Asignacion y Acceso","Llamada a funcion retorno","Total"]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.latex('''
             T(n) = 25 \equiv O(1)
             ''')


  st.markdown('''
              Las inserciones de nuevos elementos se haran deacuerdo a su orden relativo al nodo padre hasta que el
              nuevo nodo sea una hoja del arbol. Si el nuevo elemento es menor al nodo padre, se colocara como hijo izquierdo; si
              es mayor, se colocara como hijo derecho del nodo padre. 

              Para garantizar que el arbol se encuetre balanceado, se haran las rotaciones necesarias desde el nuevo nodo hasta 
              el nodo raiz. 
              ''')
  
  with st.expander("Insercion AVL"):
    st.code('''
            def insert(self,nodo,value):

                  if(nodo is None):
                      return Nodo(value)

                  if(value < nodo.value):
                      nodo.left = self.insert(nodo.left,value)
                  elif(value > nodo.value):
                      nodo.right = self.insert(nodo.right,value)
                  else:
                      nodo.repetitions+=1
                      return nodo

                  nodo.height = 1 + max(self.obtenerAltura(nodo.left), 
                                    self.obtenerAltura(nodo.right)) 

                  balance = self.obtenerBalanceo(nodo) 

                  if balance > 1 and value < nodo.left.value: 
                      return self.rotacionDerecha(nodo) 

                  if balance < -1 and value > nodo.right.value: 
                      return self.rotacionIzquierda(nodo) 

                  if balance > 1 and value > nodo.left.value: 
                      nodo.left = self.rotacionIzquierda(nodo.left) 
                      return self.rotacionDerecha(nodo) 

                  if balance < -1 and value < nodo.right.value: 
                      nodo.right = self.rotacionDerecha(nodo.right) 
                      return self.rotacionIzquierda(nodo) 

                  return nodo
            ''')
    
  st.markdown('''
              Realizar la busuqeda dentro de esta arbol se hara usando parte de la logica seguida en la
              insercion. Nos desplazaremos por el arbol mediante las comparaciones hechas con el node padre
              hasta que encontramos el valor que estamos buscando.
              ''')
  
  with st.expander("Busqueda AVL"):
    st.code('''
            def searchNodo(self,nodo,value):
            
              if not nodo:
                  print(0)

              if(value < nodo.value):
                  nodo.left = self.searchNodo(nodo.left,value)
              elif(value > nodo.value):
                  nodo.right = self.searchNodo(nodo.right,value)
              else:
                print(nodo.repetitions)
            ''')
  
  st.markdown('''
              Para obtener un arreglo de los elementos en orden creciente, haremos uso
              de un recorrido prefijo en el arbol.
              ''')
  with st.expander("Recorrido prefijo"):
    st.code('''
            def imprimirArbol(self,raiz):
              if raiz:
                  self.imprimirArbol(raiz.left)
                  print(str(raiz.value))
                  self.imprimirArbol(raiz.right)
            ''')
    
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    oper = ["if raiz:","self.imprimirArbol(raiz.left)","self.imprimirArbol(raiz.right)"]
    pasos = ["1","2","2"]
    exp = ["Condicional","Llama a funcion recursiva y Acceso","Llamada a funcion recursiva y Acceso"]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.write("**Peor caso:** Nos encontramos en un arbol binario perfecto")
    st.write("Definicion recursiva:")
    st.latex(r'''
             T(n) = \begin{cases} 1 &,\ Si\quad n = 0\\ 5 + T(n/2) + T(n/2) &,\ Si\quad n > 0 \end{cases}
             ''')
    st.latex(r'''
             T(n) = 5 + 2(T(n/2)) = 2(T(n/2)) + O(1)
             ''')
    st.write("Por teorema del maestro:")
    st.latex(r'''
             T(n) = AT(n/B) + O(n^C)\\ \phantom{.} \\
             \bullet \ A = 2\\
             \bullet \ B = 2\\
             \bullet \ C = 0\\
             \bullet \ log_B(A) = log_2(2) = 1\\ \phantom{.} \\
             log_B(A) > C \Rightarrow \ T(n) \equiv O(n ^{log_B(A)}) \\
             T(n) \equiv O(n)
             ''')

  hide_img_fs = '''
  <style>
  button[title="View fullscreen"]{
      visibility: hidden;}
  </style>
  '''

  st.markdown(hide_img_fs, unsafe_allow_html=True)

