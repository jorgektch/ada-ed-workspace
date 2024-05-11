import streamlit as st
import pandas as pd
def ejecutar_analisis1_0():
  with st.expander("Análisis"):
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

def ejecutar_analisis1_1():
  with st.expander("Análisis"):
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
  
def ejecutar_analisis1_2():
  with st.expander("Análisis"):
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
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Escogemos c = 11:**")
    st.latex(r'''
        10n + 3 \leq 11n \\
        3 \leq n \\
        \text{Un valor válido para } n_0 \text{ sería: } 4 \\
        ''')
  
def ejecutar_analisis2():
  with st.expander("Análisis"):
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "sum++"],
        "Número de operaciones": ["2", "n + 1", "2n", "2n"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite n veces. Se realiza una vez más como falsa", 
                    "Acción suma y asignación. Se repite n veces.", 
                    "Acción suma y asignación. Se repite n veces."]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 5n + 3
        ''')
    st.markdown("**Suposición:** BigO es O(n)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Con c = 6:**")
    st.latex(r'''
        5n + 3 \leq 6n \\
        3 \leq n \\
        ''')
    st.markdown("**Se obtiene:**")
    st.latex(r'''
        c = 6 \text{ y } n_0 = 3
        ''')
    st.markdown("**T(n) = O(n):**")
    st.latex(r'''
        \text{Dado un c= 6 para todo } n \geq 3 \\
        5n + 3 \leq 6n \text{, para todo } n \geq 3 \\
        ''')
  
def ejecutar_analisis3():
  with st.expander("Análisis"):
    st.markdown("**Peor caso:** Que n sea impar")
    data={
        "Operacion": ["int i = 0", "i < n", "i+=2", "sum++"],
        "Número de operaciones": ["2", "2 + n/2", "n + 2", "n + 2"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n/2 - 0 + 1) veces. Se hace una vez más como falsa si n es impar", 
                    "Acción suma y asignación. Se repite (n/2 - 0 + 1) veces.", 
                    "Acción suma y asignación. Se repite (n/2 - 0 + 1) veces por el bucle."]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 8 + \frac{n}{2} + 2n
        ''')
    st.markdown("**Suposición:** BigO es O(n)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Escogemos c = 3:**")
    st.latex(r'''
        8 + \frac{n}{2} + 2n \leq 3n \\
        8 + \frac{n}{2} \leq n \\
        8 \leq \frac{n}{2} \\
        16 \leq n \\
        \text{ } \\
        \text{Un valor válido para } n_0 \text{ sería: } 17 \\
        ''')

def ejecutar_analisis4():
  with st.expander("Análisis"):
    st.markdown("**Peor caso:** Que n sea impar")
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "int j = 0", "j < n", "j++", "sum++"],
        "Número de operaciones": ["2", "n + 1", "2n", "2n", "n^2 + 1", "2n^2", "2n^2"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n veces por el bucle externo.",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa. Se repite n veces por el bucle externo.",
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces. Se repite n veces por el bucle externo. ",
                    "Acción suma y asignación. Se repite n veces por el bucle interno. Se repite n veces por el bucle externo."]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 5n^2 + 6n + 3
        ''')
    st.markdown("**Suposición:** BigO es O(n^2)")
    st.markdown("**Sea:**")
    st.latex(r'''
        5n^2 \leq 5n^2 \text{...(1)} \\
        6n \leq 6n^2 \text{...(2)} \\
        3 \leq 3n^2 \text{...(3)} \\
        ''')
    st.markdown("**Sumando (1) , (2) y (3):**")
    st.latex(r'''
        5n^2 + 6n + 3 \leq 14n^2 \\
        6n + 3 \leq 9n^2 \\
        0 \leq 9n^2 - 6n - 3 \\
        0 \leq 3n^2 - 2n - 1 \\
        ''')
    st.markdown("**Resolviendo se tiene: **")
    st.latex(r'''
        n \leq \frac{-1}{3} \text{ y } n \geq 1 \\
        c = 14 \\
        n_0 = 1 \\
        ''')
    st.markdown("**T(n) = O(n^2):**")
    st.latex(r'''
        \text{Dado un c= 14 para todo } n \geq 1 \\
        5n^2 + 6n + 3 \leq 14n^2 \text{, para todo } n \geq 1 \\
        ''')
    
def ejecutar_analisis5():
  with st.expander("Análisis"):
    st.markdown("**Peor caso:** Que n sea impar")
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "sum++", "int j = 0", "j < n", "j++", "sum++"],
        "Número de operaciones": ["2", "n + 1", "2n", "2n", "2", "n + 1", "2n", "2n"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n veces por el bucle externo.",
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n veces por el bucle externo."]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 10n + 6
        ''')
    st.markdown("**Suposición:** BigO es O(n)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Con c = 11:**")
    st.latex(r'''
        10n + 6 \leq 11n \\
        6 \leq n \\
        ''')
    st.markdown("**Se obtiene:**")
    st.latex(r'''
        c = 11 \text{ y } n_0 = 6
        ''')
    st.markdown("**T(n) = O(n):**")
    st.latex(r'''
        \text{Dado un c= 11 para todo } n \geq 6 \\
        10n + 6 \leq 11n \text{, para todo } n \geq 6 \\
        ''')

def ejecutar_analisis6():
  with st.expander("Análisis"):
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "int j = 0", "j < n*n", "j++", "sum++", "Bucle interno"],
        "Número de operaciones": ["2", "n + 1", "2n", "2", "n^2 + 1", "2n^2", "2n^2", "(3 + 5n^2) * n"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n*n - 1 + 0 + 1) veces. Se hace una vez más como falsa.",
                    "Acción suma y asignación. Se repite (n*n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n*n veces por el bucle interno.", 
                    "El bucle interno es ejecutado n veces por el bucle externo"]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 5n^3 + 6n + 3
        ''')
    st.markdown("**Suposición:** BigO es O(n^3)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Sea:**")
    st.latex(r'''
        5n^3 \leq 5n^3 \text{ ...(1)} \\
        6n \leq 6n^3 \text{ ...(2)} \\
        3 \leq 3n^3 \text{ ...(3)} \\
        ''')
    st.markdown("**Sumando (1), (2), (3):**")
    st.latex(r'''
        5n^3 + 6n + 3 \leq 14n^3 \\
        6n + 3 \leq 9n^3 \\
        0 \leq 9n^3 - 6n +3 \\
        0 \leq 3n^3 - 2n + 1\\
        ''')
    st.markdown("**Resolviendo se tiene:**")
    st.latex(r'''
        n \geq \frac{-\sqrt{2}}{3} \land n \geq \frac{\sqrt{2}}{3} \\
        ''')
    st.write("- Significa:")
    st.latex(r'''
        n \geq 1 \geq \frac{\sqrt{2}}{3} \\
        c = 14 \\
        n_0 = 1
        ''')
    st.markdown("**T(n) = O(n^3):**")
    st.latex(r'''
        \text{Dado un c= 14 para todo } n \geq 1 \\
        5n^3 + 6n + 3 \leq 14n^3 \text{, para todo } n \geq 1 \\
        ''')
    
def ejecutar_analisis7():
  with st.expander("Análisis"):
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "int j = 0", "j < i", "j++", "sum++"],
        "Número de operaciones": ["2", "n + 1", "2n", "2n", "n^2/2 + n/2", "n^2 + n", "n^2 + n"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n veces por el bucle externo. ",
                    "Se realiza una comparación. Se repite [n * (n + 1)]/2 veces por el bucle externo.",
                    "Acción suma y asignación. Se repite [n * (n - 1)]/2 veces por el bucle externo.", 
                    "Acción suma y asignación. Se repite [n * (n - 1)]/2 veces por el bucle externo."]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = \frac{5n^2}{2} + \frac{15n}{2} + 3
        ''')
    st.markdown("**Suposición:** BigO es O(n^2)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Sea:**")
    st.latex(r'''
        \frac{5n^2}{2} \leq \frac{5n^2}{2} \text{ ...(1)} \\
        \frac{15n}{2} \leq \frac{15n^2}{2} \text{ ...(2)} \\
        3 \leq 3n^3 \text{ ...(3)} \\
        ''')
    st.markdown("**Sumando (1), (2), (3):**")
    st.latex(r'''
        \frac{5n^2}{2} + \frac{15n}{2} + 3 \leq 13n^2 \\
        \frac{15n}{2} + 3 \leq \frac{21n^2}{2} \\
        0 \leq \frac{21n^2}{2} - \frac{15n}{2} - 3\\
        0 \leq 21n^2 - 15n - 6 \\
        0 \leq 7n^2 - 5n - 2 \\
        0 \leq (n - 1)(7n + 2) \\
        ''')
    st.markdown("**Resolviendo se tiene:**")
    st.latex(r'''
        1 \leq n \land \frac{-2}{7} \leq n\ \\
        ''')
    st.write("- Significa:")
    st.latex(r'''
        c = 13 \\
        n_0 = 1
        ''')
    st.markdown("**T(n) = O(n^2):**")
    st.latex(r'''
        \text{Dado un c= 13 para todo } n \geq 1 \\
        \frac{5n^2}{2} + \frac{15n}{2} + 3 \leq 13n^2 \text{, para todo } n \geq 1 \\
        ''')
    
def ejecutar_analisis8():
  with st.expander("Análisis"):
    data={
        "Operacion": ["int i = 0", "i < n", "i++", "int j = 0", "j < n * n", "j++", "int k = 0", "k < j", "k++", "sum++", "Suma de operaciones del segund bucle", "Suma (1)", "Suma de operaciones del primer bucle interno (Suma(2))", "Suma(3)", "Suma de operaciones del bucle externo (Suma(4))", "Suma total"],
        "Número de operaciones": ["2", "n + 1", "2n", "2n", "n^2 + 1", "2n^2", "2", "n^2 + 2", "2n^2 + 2", "2n^2 + 2", "5n^2 + 8", "5n^4 + 8n^2", "3n^2 + 3", "5n^5 + 11n^3 + 3n", "3n + 3", "5n^5 + 11n^3 + 6n + 3"],
        "¿Por qué?": [
                    "Declaración y asignación",
                    "Se realiza una comparación. La acción se repite (n - 1 + 0 + 1) veces. Se hace una vez más como falsa.", 
                    "Acción suma y asignación. Se repite (n - 1 + 0 + 1) veces.", 
                    "Acción y declaración. Se repite n veces por el bucle externo. ",
                    "Acción multiplicación y comparación. Se repite n*n veces por el bucle interno y termina con otra comparación +1.",
                    "Acción suma y asignación. Se repite n*n veces por el primer bucle interno.", 
                    "Acción y declaración.",
                    "Se realiza una comparación. El j al final se repitió n*n+1 veces, por lo tanto, para el segundo bucle interno se repetirá (n*n+1)+1 veces, el último +1 es para que salga del bucle.",
                    "Acción suma y asignación.Se repite n*n+1 veces por el segundo bucle interno.",
                    "Acción suma y asignación.Se repite n*n+1 veces por el segundo bucle interno.",
                    "",
                    "Por el primer bucle interno, la suma anterior se repite n*n veces",
                    "",
                    "Por el bucle externo, la suma(1) y (2) que conforman una sola, se repite n veces",
                    "",
                    "Se debe sumar la suma(3) y la suma(4)"]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**El T(n) es:**")
    st.latex(r'''
        T(n) = 5n^5 + 11n^3 + 6n + 3
        ''')
    st.markdown("**Suposición:** BigO es O(n^5)")
    st.latex(r'''
        \text{Hallar una cosntante c u valor } n_0 \text{tal que: }\\
        T(n) \leq cn \text{, para todo } n \geq n_0 \\
        ''')
    st.markdown("**Sea:**")
    st.latex(r'''
        5n^5 \leq 5n^5 \text{ ...(1)} \\
        11n^3 \leq 11n^5 \text{ ...(2)} \\
        6n \leq 6n^5 \text{ ...(3)} \\
        3 \leq 3n^5 \text{ ...(3)} \\
        ''')
    st.markdown("**Sumando (1), (2), (3) y (4):**")
    st.latex(r'''
        5n^5 + 11n^3 + 6n + 3 \leq 25n^5 \\
        11n^3 + 6n + 3 \leq 20n^5 \\
        0 \leq 20n^5 - 11n^3 - 6n - 3\\
        0 \leq (n - 1)(20n^4 - 11n^3 - 6n - 3)\\
        ''')
    st.markdown("**Resolviendo se tiene:**")
    st.latex(r'''
        1 \leq n \land n \geq 1\ \\
        ''')
    st.write("- Significa:")
    st.latex(r'''
        c = 25 \\
        n_0 = 1
        ''')
    st.markdown("**T(n) = O(n^5):**")
    st.latex(r'''
        \text{Dado un c= 25 para todo } n \geq 1 \\
        5n^5 + 11n^3 + 6n + 3 \leq 25n^3 \text{, para todo } n \geq 1 \\
        ''')
    
def ejecutar_analisis9():
  with st.expander("Análisis"):
    data={
        "Operacion": ["for (int i = 1; i < n; i = i*2)", "sum++", "Total"],
        "Número de operaciones": ["2 + log2(n) + 1 +  2(log2(n))", "2Log2(n)", "T(n) = 3 +  5Log2(n)"]
    }
    df=pd.DataFrame(data)
    st.table(df)
    st.markdown("**Número de operaciones según n asignado**")
    st.latex(r'''
        n: 1 \text{ - operaciones: } 3 \\
        n: 2 \text{ - operaciones: } 8 \\
        n: 3 \text{ - operaciones: } 13 \\
        n: 4 \text{ - operaciones: } 13 \\
        n: 5 \text{ - operaciones: } 18 \\
        n: 6 \text{ - operaciones: } 18 \\
        n: 7 \text{ - operaciones: } 18 \\
        n: 8 \text{ - operaciones: } 23 \\
        n: 9 \text{ - operaciones: } 23 \\
        n: 10 \text{ - operaciones: } 23 \\
        n: 11 \text{ - operaciones: } 23 \\
        n: 12 \text{ - operaciones: } 23 \\
        n: 13 \text{ - operaciones: } 23 \\
        ''')
    st.markdown("**Demostrando que tiene BigO O(log(n)):**")
    st.latex(r'''
        5 \log{2}{n} \leq 5 \log{2}{n} \\
        3 \leq 3 \log{2}{n} \text{, para todo } n \geq 1\\
        ''')
    st.markdown("**Se tiene:**")
    st.latex(r'''
        5 \log{2}{n} + 3 \leq 8 \log{2}{n} \\
        ''')
    st.write("- Por lo tanto: ")
    st.latex(r'''
        c = 8 \\
        n_0 = 1
        ''')