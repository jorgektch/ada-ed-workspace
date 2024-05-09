import streamlit as st
import pandas as pd
def ejecutar_analisis10():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  data={
    "Operacion": ["int count = 0", "int i = 0", "i < arr.length", "i++", "sum++", "if(arr[i])", "count++", "return count >= 2"],
    "Número de operaciones": ["2", "2", "n+1", "2 * n = 2n", "2 * n = 2n", "2n", "2", "2"],
    "¿Por qué?": [
                  "Declaración y asignación", 
                  "Declaración y asignación", 
                  "Se realiza una comparación. La acción se repite n veces. Se realiza una vez más como falsa", 
                  "Acción suma y asignación. Se repite n veces.", 
                  "Acción suma y asignación. Se repite n veces por el bucle.", 
                  "Condición y acceso a valor del vector, se repite n veces.", 
                  "Declaración y asignación", 
                  "Comparación y devolver valor"]
  }
  df=pd.DataFrame(data)
  st.table(df)
  st.markdown("**El T(n) es:**")
  st.latex(r'''
      T(n) = 5n + 9
      ''')
  st.markdown("**Suposición:** BigO es O(n)")
  st.latex(r'''
      \text{Hallar una constante c y un valor } n_0 \text{ tal que:} \\
      T(n) \leq cn \text{, para todo } n \geq n_0
      ''')
  st.markdown("**Con c=6:**")
  st.latex(r'''
      5n + 9 \leq 6n \\
      9 \leq n
      ''')
  st.write("Se obtiene:")
  st.latex(r'''c = 6 \text{ y } n_0 = 3''')
  st.markdown("**T(n) = O(n):**")
  st.latex(r'''
      \text{Dado un } c = 6 \text{ para todo } n \geq 9: \\
      5n + 9 \leq 6n \text{, para todo } n \geq 9
      ''')

def ejecutar_analisis11():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  st.markdown("**Peor caso:** No hay valores verdaderos")
  data={
    "Operacion": ["int i = 0", "i < arr.length", "i++", "int j = i + 1", "j < arr.length", "j++", "if(arr[i] && arr[j])", "return true", "return false"],
    "Número de operaciones": ["2", "n+1", "2 * n = 2n", "3 * (n - 1) = 3n - 3", "n * (n - 1) / 2", "2 * n * (n - 1) / 2", "3 * n * (n - 1) / 2", "0", "1"],
    "¿Por qué?": [
                  "Declaración y asignación",
                  "Se realiza una comparación. La acción se repite n veces. Se realiza una vez más como falsa", 
                  "Acción suma y asignación. Se repite n veces.", 
                  "Declaración, acción suma y asignación. Se repite n - 1 veces", 
                  "Se realiza una comparación. Por el bucle externo, se repetirá como una sumatoria de n - 1 a 1", 
                  "Declaración y asignación. Por el bucle externo, se repetirá como una sumatoria de n - 1 a 1", 
                  "Condición y acceso a valor de los vectores, por el bucle externo, se repetirá como una sumatoria de n - 1 a 1",
                  "No se considera trabajo",
                  "Se considera trabajo"]
  }
  df=pd.DataFrame(data)
  st.table(df)
  st.markdown("**Por lo tanto el T(n):**")
  st.latex(r'''
      T(n) = 3n^2 + 3n + 1 \\
      \text{ } \\
      \text{Demostrando que } 3n^2 + 3n + 1 \text{ es } O(n^2): \\
      \text{ } \\
      3n^2 \leq 3n^2 \\
      3n \leq 3n^2 \text{ para } n \geq 1 \\
      1 \leq n^2 \\
      3n^2 + 3n + 1 \leq 7n^2 \\
      c=7 \text{ y } n=1
      ''')
  
def ejecutar_analisis12():
  st.subheader("Análisis")
  st.write("Analizando el algoritmo")
  data={
    "Operacion": ["int i = 0", "i < arr.length", "i++", "if(array[i])", "int j = i + 1", "j < arr.length", "j++", "if(arr[j])", "return true", "return false"],
    "Número de operaciones": ["2", "n + 1", "2n", "2n", "3", "n", "2n - 2", "2n - 2", "0", "1"],
    "¿Por qué?": [
                  "Declaración y asignación",
                  "Se realiza una comparación. La acción se repite (n-1 + 0 + 1) veces. Se realiza una vez más como falsa", 
                  "Acción suma y asignación. Se repite (n-1 + 0 + 1) veces.", 
                  "Acción condicional y acceso. Se repite n veces", 
                  "Acción suma, asignación y declaración.", 
                  "Se realiza una comparación. La acción se repite (n -1 -1 + 1) veces. Se realiza una vez más como falsa. Esta iteración sólo se produce una única vez debido a que solo existe un valor positivo que desencadene la condición. ", 
                  "Acción suma y asignación. Se repite (n-1 - 1 + 1) veces.",
                  "Acción concisión y acceso. Se repite (n-1 - 1 + 1) veces.",
                  "Esta acción nunca se ejecuta",
                  "Acción llamar función"]
  }
  df=pd.DataFrame(data)
  st.table(df)
  st.markdown("**Por lo tanto el T(n) es:**")
  st.latex(r'''
      T(n) = 10n + 3
      ''')
  st.markdown("**Suposición:** El BigO es O(n)")
  st.latex(r'''
      \raggedright \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
      T(n) \leq cn \text{, para todo } n \geq n_0 \\
      ''')
  st.markdown("**Escogemos c = 11")
  st.latex(r'''
      10n + 3 \leq 11n \\
      3 \leq n \\
      \raggedright \text{Un valor válido para } n_0 \text{ sería: } 4
      ''')
