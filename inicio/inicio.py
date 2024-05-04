import streamlit as st
from .grupo import *
from .metodologia import *
from .tecnologias import *

def ejecutar_inicio():
  st.header(f"Inicio")
  ejecutar_grupo()
  ejecutar_metodologia()
  ejecutar_tecnologias()
