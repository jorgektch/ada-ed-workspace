import streamlit as st

def ejecutar_implementacion():
  st.subheader("Implementación")

  codeNode = '''
        class Nodo:     
            def __init__(self,value) -> None:
                self.value = value 
                self.left = None    
                self.right = None
                self.repetitions = 0
                self.height = 1
          '''
  
  with st.expander("Nodo", expanded=True ):
    st.code(codeNode, language='python')

  codeAvl = '''
            class ArbolAVL:

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


              def obtenerAltura(self,raiz):
                  if not raiz:
                      return 0
                  
                  return raiz.height

              def obtenerBalanceo(self, raiz): 
                  if not raiz: 
                      return 0
            
                  return self.obtenerAltura(raiz.left) - self.obtenerAltura(raiz.right) 

              def searchNodo(self,nodo,value):
                  if not nodo:
                      print(0)

                  if(value < nodo.value):
                      nodo.left = self.searchNodo(nodo.left,value)
                  elif(value > nodo.value):
                      nodo.right = self.searchNodo(nodo.right,value)
                  else:
                      print(nodo.repetitions)

              def imprimirArbol(self,raiz,value = 0):
                  if raiz:
                      self.imprimirArbol(raiz.left,value)
                      if(raiz.repetitions >= value):
                          print(str(raiz.value) + " " + str(raiz.repetitions))
                      self.imprimirArbol(raiz.right,value)
            '''
  
  with st.expander("Arbol AVL"):
    st.code(codeAvl, language='python')

  codeText = '''
            def obtenerTexto(texto):
              with open(texto,encoding="utf8") as f:
                  st = f.read()
                  st = re.sub('[^A-zÀ-ú\s]','',st)
                  return st.lower().split()
             '''
  
  with st.expander("Obtener texto"):
    st.code(codeText, language='python')

  codedMain = '''
              if __name__ == "__main__":
                  tree = ArbolAVL()
                  nodo = None
                  
                  wr = input("Ingrese un valor para empezar el analisis: ")
                  cadenaTexto = obtenerTexto('Laciudadylosperros.txt')
                  print("Texto analizado")
                  print(str(len(cadenaTexto)) + " palabras")
                  wr = input("Ingrese un valor para empezar el analisis: ")
                  
                  start = time.time()

                  for word in cadenaTexto:
                      nodo = tree.insert(nodo,word)

                  end = time.time()
                  print(end - start)
                  print("Texto analizado")
                  wr = input("Ingrese un valor para obtener las palabras que se repiten mas de 500 veces: ")
                  tree.imprimirArbol(nodo,500)

                  wr = input("Ingrese una palabra: ")
                  wr.lower()
                  print(wr)
                  tree.searchNodo(nodo,wr)
              '''
  
  with st.expander("Menu principal"):
    st.code(codedMain, language='python')
