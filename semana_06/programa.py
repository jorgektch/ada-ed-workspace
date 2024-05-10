import streamlit as st
import re
import pandas as pd
from io import StringIO
from .avlTree import *
from .nodo import *

@st.experimental_fragment()
def buscador(tree,node):
    st.write("Ingrese una palabra que desee encontrar dentro de su texto")
    searchWord = st.text_input("",label_visibility="collapsed")
    tree.searchNodo(node, searchWord)

def obtenerTabla(tree,node):
    st.write("Lista de palabras que aparecen mas de 500 veces en el texto")
    rpts = []
    vals = []
    tree.imprimirArbol(node,vals,rpts,500)
    data = {
        "Palabras" : vals,
        "Repeticiones": rpts
    }   
    df = pd.DataFrame(data)
    st.dataframe(df,use_container_width=True)

def ejecutar_programa():
      
    st.subheader("Programa")
    st.write("Seleccione el archivo de texto que desee analizar")
    myFile = st.file_uploader("",accept_multiple_files=False,type=['txt'],label_visibility="collapsed")      
    if myFile:

        stringio=StringIO(myFile.getvalue().decode('utf-8'))
        read_data=stringio.read()
        read_data=re.sub('[^A-zÀ-ú\s]','',read_data)
        read_data=read_data.lower().split()
        tree = ArbolAVL()
        node = None 

        with st.spinner():
            for word in read_data:
                node = tree.insert(node,word)    
            buscador(tree,node)
            obtenerTabla(tree,node)
    else:
        st.error("Ingrese un archivo con extension .txt")