import streamlit as st
import pandas as pd
from stretch_component import stretch_component

def ejecutar_analisis(theme:str):
  
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
  
  stretch_component('stretch',True,theme,30,1000,6,"5")

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
    
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    oper = ["if not nodo","return Nodo(value)","if value < nodo.value","nodo.left = self.insert(nodo.left,value)","elif value > nodo.value","nodo.right = self.insert(nodo.right,value)","nodo.height = 1 + max(self.obtenerAltura(nodo.left), self.obtenerAltura(nodo.right))","balance = self.obtenerBalanceo(nodo)"]
    oper.append("if balance > 1 and value < nodo.left.value")
    oper.append("return self.rotacionDerecha(nodo)")
    oper.append("if balance < -1 and value > nodo.right.value")
    oper.append("return self.rotacionIzquierda(nodo)")
    oper.append("if balance > 1 and value > nodo.left.value")
    oper.append("nodo.left = self.rotacionIzquierda(nodo.left)")
    oper.append("return self.rotacionDerecha(nodo)")
    oper.append("if balance < -1 and value < nodo.right.value")
    oper.append("nodo.right = self.rotacionDerecha(nodo.right)")
    oper.append("return self.rotacionIzquierda(nodo) ")
    oper.append("return nodo")
    pasos = ["2","2","3","4","3","4","8","2","6","2","6","2","6","4","2","6","4","2","1"]
    exp = ["Operador negacion y Condicionak","Llamado a constructor Nodo y Llamado a funcion retorno","Acceso, Operacion menor que y Condicional","Llamado funcion insert, Acceso, Asignacion y Acceso"]
    exp.append("Acceso, Operador mayor que y Condicional")
    exp.append("Llamaado funcion insert, Acceso, Asignacion y Acceso")
    exp.append("Llamado funcion max, Doble llamado funcion obtenerAltura, Doble acceso, Suma y Acceso")
    exp.append("Llamado funcion obtenerBalance y Asignacion")
    exp.append("Operador mayor que, Operador and, Operador menor que, Doble acceso y Condicional")
    exp.append("Llamado funcion rotacionDerecha y Llamado funcion retorno")
    exp.append("Operador menor que, Operador and, Operador mayor que, Doble acceso y Condicional")
    exp.append("Llamado funcion rotacionIzquierda y Llamado funcion retorno")
    exp.append("Operador mayor que, Operador and, Operador mayor que, Doble acceso y Condicional")
    exp.append("Llamando funcion rotacionIzquierda, Acceso, Asignacion y Acceso")
    exp.append("Llamado funcion rotacionDerecha, Llamado funcion retorno")
    exp.append("Operador menor que, Operador and, Operador menor que, Doble acceso y Condicional")
    exp.append("Llamando funcion rotacionDerecha, Acceso, Asignacion y Acceso")
    exp.append("Llamado funcion rotacionIzquierda, Llamado funcion retorno")
    exp.append("Llamado funcion retorno")
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.write("**Peor caso:** \n - Nos encontramos en un arbol binario perfecto")
    st.write("Definicion recursiva:")
    st.latex(r'''
             T(n) = \begin{cases} 4 &,\ Si\quad n < 1\\ 50 + T(n/2) &,\ Si\quad n \geq 1 \end{cases}
             ''')
    st.write("Definicion no recursiva:")
    st.latex(r'''
             \begin{align*}
              T(n) &= 50 + T(n/2) = 50 + (50 + T((n/2)/2)) \\
              T(n) &= 100 + T(n/4) = 100 + (50 + T((n/4)/2)) \\
              T(n) &= 150 + T(n/8) = \dots \\
              T(n) &= 50i + T(n/2^i)
             \end{align*}
             ''')
    st.write("Finaliza cuando:")
    st.latex(r'''
            \begin{align*}
              n/2^i &< 1 \\
                  n &< 2^i \\
                log_2n &< i  \\
                \phantom{.} \\
                i = log_2n &+ 1
            \end{align*}\\
             \phantom{.} \\
             T(n) = 50log_2n + 54 \equiv O(logn)
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
                return

              if(value < nodo.value):
                  self.searchNodo(nodo.left,value)
              elif(value > nodo.value):
                  self.searchNodo(nodo.right,value)

            ''')
  
  with st.container(border = True):
    st.info("**Analisis T(n) y BigO**")
    oper = ["if not nodo","return","if value < nodo.value","self.searchNodo(nodo.left,value)","elif(value > nodo.value)","self.searchNodo(nodo.right,value)"]
    pasos = ["2","1","3","2","3","2"]
    exp = ["Operador negador y Condicional","Llamada funcion retorno","Operacion menor que, Acceso y Condicional","Llamado a funcion searchNodo y Acceso","Operador mayor que, Acceso y Condicional","Llamado a funcion searchNodo y Acceso"]
    data = {
        "Operaciones" : oper,
        "Pasos": pasos,
        "Fundamento": exp
    }   
    df = pd.DataFrame(data)
    st.table(df)
    st.write("**Peor caso:** \n - Nos encontramos en un arbol binario perfecto \n - El elemento que se busca no se encuentra en el arbol")
    st.write("Definicion recursiva:")
    st.latex(r'''
             T(n) = \begin{cases} 3 &,\ Si\quad n < 1\\ 5 + T(n/2) &,\ Si\quad n \geq 1 \end{cases}
             ''')
    st.write("Definicion no recursiva:")
    st.latex(r'''
             \begin{align*}
              T(n) &= 5 + T(n/2) = 5 + (5 + T((n/2)/2)) \\
              T(n) &= 10 + T(n/4) = 10 + (5 + T((n/4)/2)) \\
              T(n) &= 15 + T(n/8) = \dots \\
              T(n) &= 5i + T(n/2^i)
             \end{align*}
             ''')
    st.write("Finaliza cuando:")
    st.latex(r'''
            \begin{align*}
              n/2^i &< 1 \\
                  n &< 2^i \\
                log_2n &< i  \\
                \phantom{.} \\
                i = log_2n &+ 1
            \end{align*}\\
             \phantom{.} \\
             T(n) = 5log_2n + 8 \equiv O(logn)
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
    st.write("**Peor caso:** \n - Nos encontramos en un arbol binario perfecto")
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
             \begin{align*}
             log_B(A) > C \Rightarrow \ T(n) &\equiv O(n ^{log_B(A)}) \\
             T(n) &\equiv O(n)
             \end{align*}
             ''')

  hide_img_fs = '''
  <style>
  button[title="View fullscreen"]{
      visibility: hidden;}
  </style>
  '''

  st.markdown(hide_img_fs, unsafe_allow_html=True)

