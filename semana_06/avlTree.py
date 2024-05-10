from .nodo import Nodo
import streamlit as st
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
      T2 = y.left 

      y.left = z 
      z.right = T2 

      z.height = 1 + max(self.obtenerAltura(z.left), 
                      self.obtenerAltura(z.right)) 
      y.height = 1 + max(self.obtenerAltura(y.left), 
                      self.obtenerAltura(y.right)) 

      return y 

  def rotacionDerecha(self, z): 

      y = z.left 
      T3 = y.right 

      y.right = z 
      z.left = T3 

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
          st.error("Palabra no encontrada")
          return

      if(value < nodo.value):
          self.searchNodo(nodo.left,value)
      elif(value > nodo.value):
          self.searchNodo(nodo.right,value)
      else:
          st.success("Palabra encontrada "+str(nodo.repetitions)+" veces")
          return

  def imprimirArbol(self,raiz,strs,rpt,val = 0):
        if raiz:
            self.imprimirArbol(raiz.left,strs,rpt,val)

            if(raiz.repetitions >= val):
                strs.append(raiz.value)
                rpt.append(str(raiz.repetitions))

            self.imprimirArbol(raiz.right,strs,rpt,val)      
