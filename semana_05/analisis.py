import streamlit as st

def ejecutar_analisis_mergesort():
  with st.expander("Análisis"):
    st.markdown('''
                Cada vez que se llama la función mergesort, el arreglo original se divide en dos subarreglos partiendo de su mitad:
                ''')
    st.markdown('''
                Hasta que nos dé una cantidad de “n” elementos independientes que es el caso base.
                1. Al sumar cada fila de manera independiente, nos da una cantidad “n”.
                2. La función se va a dividir una cantidad de k veces, suponiendo que n es una potencia 2, la función acabará cuando solo quede un elemento:
                ''')
    st.latex(r'''
        \frac{n}{2^{k}} = 1 \\
        n = 2^k \\
        \log_{2}( n) =k
            ''')
    st.markdown('''
                Entonces, la función mergeSort se repetirá:
                ''')
    st.latex(r'''
        n*\log_{2}( n)
        ''')
    st.markdown('''
                Por lo tanto, su complejidad será la siguiente:
                ''')
    st.latex(r'''
        T( n) =O( n*\log_{2}( n))
        ''')

def ejecutar_analisis_quicksort():
  with st.expander("Análisis"):
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

def ejecutar_analisis_heapsort():
  with st.expander("Análisis"):
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

def ejecutar_analisis_insertionsort():
  with st.expander("Análisis"):
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
    
def ejecutar_analisis_shellsort():
  with st.expander("Análisis"):
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')