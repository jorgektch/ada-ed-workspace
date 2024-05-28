import streamlit as st

def ejecutar_enunciado_moch2():
  st.subheader("Mochila versión 3")
  st.markdown('''
              Se tiene un conjunto de "n" objetos, cada uno con un peso determinado, y una mochila con capacidad "C".
              Se solicita crear un programa que permita maximizar el peso de los objetos que se introducen en la mochila sin sobrepasar la capacidad "C".
              - El programa debe mostrar:
                - El valor total obtenido de los objetos
                - La vector solución''')
  
def ejecutar_enunciado_est():
  st.subheader("Estaciones")
  st.markdown('''
              Supón que estas creando un programa de radio. Quieres llegar a
              oyentes en n estados de EEUU. Tienes que decidir en qué
              estaciones de radio pasarás tu programa para llegar a todos los
              oyentes. Cuesta dinero poner tu programa en cada estación, así
              que intentarás minimizar el número de estaciones. 
              - Cada estación cubre una región y hay cierto solapamiento. ¿Cómo
                encuentras el menor conjunto de estaciones con las cuales cubres
                los n estados?''')