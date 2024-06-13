import streamlit as st

def ejecutar_enunciado_moch2():
  st.subheader("Mochila versión 3")
  st.markdown('''
              Deseamos sentar a tres personas en tres sillas, ¿Cuántas formas existen para ubicar a las personas en las 3 sillas?
              Considerar:
              - La persona amarilla no puede sentarse en el asiento 2
              - La persona roja no se puede sentar en el primer asiento
              ''')