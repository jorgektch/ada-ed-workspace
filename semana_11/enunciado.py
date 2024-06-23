import streamlit as st

def ejecutar_enunciado_silla():
  st.subheader("Tres personas en tres sillas")
  st.markdown('''
              Deseamos sentar a tres personas en tres sillas, ¿Cuántas formas existen para ubicar a las personas en las 3 sillas?
              Considerar:
              - La estructura del código brindado por el profesor
              - La persona amarilla no puede sentarse en el asiento 2
              - La persona roja no se puede sentar en el primer asiento
              ''')