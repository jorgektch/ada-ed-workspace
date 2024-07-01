import streamlit as st
import pandas as pd

def ejecutar_analisis_mergesort_1():
  with st.container(border = True):
    st.info("Análisis 1")
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
                Por lo tanto
                ''')
    st.latex(r'''
        T( n) =O( n*\log_{2}( n))
        ''')

def ejecutar_analisis_mergesort_2():
  with st.expander("Análisis 2"):
    st.markdown('''
                De la función: `public static void mezcla(int[] a, int izda, int medio, int drcha)`  
                El número de comparaciones para ordenar y mezclar la lista se repetiría constantemente n-1:
                ''')
    # IMAGEN
    st.markdown('''
                El número de operaciones que hará la función mezclar, será c*(n-1)  
                Del análisis 1 y el previo análisis se infiere el T(n):
                ''')
    st.latex(r'''
            T(n) = T( 1) =0; si n = 1, \text{no hace trabajo} \\
            T( n) =2T\left(\frac{n}{2}\right) +c_{1}( n-1) ;\ si\ n >1
             ''')
    st.markdown('''
                Desarrollando:
                ''')
    st.latex(r'''
            T( n) =2\left[ 2T\left(\frac{n}{4}\right) +c_{1}\left(\frac{n}{2-1}\right)\right] +c_{1}( n-1) \\
            T( n) =4T\left(\frac{n}{4}\right) +c_{1}( n-2+( n-1)) \\
            T( n) =4\left[ 2T\left(\frac{n}{8}\right) +c_{1}\left(\frac{n}{4-1}\right)\right] +c_{1}( n-2+( n-1)) \\
            T( n) =8T\left(\frac{n}{8}\right) +c_{1}( n-4+( n-2) +( n-1)) \\
            T( n) =2^{i} T\left(\frac{n}{2^{i}}\right) +c_{1}\left(\left( n-2^{i-1}\right) +...+( n-4) +( n-2) +( n-1)\right)
            ''')
    st.markdown('''
                Recordemos que la función acaba cuando:
                ''')
    st.latex(r'''
            T( n) =2^{i} T( 1) +c_{1}\left(\left( n-2^{i-1}\right) +...+( n-4) +( n-2) +( n-1)\right) \\
            T( n) =c_{1}\left(\left( n-2^{\log_{2}( n) -1}\right) +...+( n-4) +( n-2) +( n-1)\right) \\
            T( n) =c_{1}\left(\sum _{i=0}^{\log_{2}( n) -1}\left( n-2^{i}\right)\right) =c_{1}\left(\sum _{i=0}^{\log_{2}( n) -1} n\ -\sum _{i=0}^{\log_{2}( n) -1} 2^{i}\right) \\
            T( n) =c_{1}\left( n\log_{2}( n) -\frac{2^{\log_{2}( n) -1+1} -1}{2-1}\right) \\
            T( n) =c_{1}\left( n\log_{2}( n) -2^{\log_{2}( n)} -1\right) \\
            T( n) =c_{1}( n\log_{2}( n) -n-1) \\
            T( n) =c_{1} n\log_{2}( n) -c_{1} n-c_{1}
            ''')
    st.markdown('''
                Por lo tanto
                ''')
    st.latex(r'''
            T( n) =O( n\log( n))
            ''')

def ejecutar_analisis_quicksort_1():
  with st.container(border=True):
    st.info("Análisis de la definición recursiva")
    st.markdown('''
                $T( low,high):$
                ''')
    st.latex(r'''
            c_{1} \ +\ T( low,piv\ -\ 1) \ +\ T( piv\ +\ 1,hight) \\  \\
            \text{Si}\ low\ < \ high\ \text{o}\ \text{Si}\ low\ \geqslant \ high \\
            c_{1} \ =\ O( n) \\  \\
            hight\ =\ n \\
            low\ =\ 1
            ''')
    st.markdown('''Para el primer fragmento de la función partition''')
    code_b1 = '''
            int pivot = arr[high];
            int i = (low - 1);
            int aux;
            ...
            aux = arr[i+1];
            arr[i+1] = arr[high];
            arr[high] = aux;
            return (i + 1);
            '''
    st.code(code_b1, language="cpp")
    operacion_b1 = [
            "pivot = arr[high]",
            "i = (low - 1)", 
            "aux",
            "aux = arr[i+1]",
            "arr[i+1] = arr[high]",
            "arr[high] = aux",
            "return (i + 1)"
        ]
    pasos_b1 = [
            "2", "2", "1", "2", "2", "1", "2"
        ]
    exp_b1 = [
            "Acceso y asignación", "Resta y asignación", "Asignación", "Acceso y asignación", "Acceso y asignación", "Asignación", "Suma y llamado a la función de retorno"
        ]
    data_b1 = {
        "Expresion": operacion_b1,
        "Pasos": pasos_b1,
        "Fundamento": exp_b1
    }
    df_b1 = pd.DataFrame(data_b1)
    st.table(df_b1)
    st.markdown('''Para el segundo fragmento de la función partition''')
    code_b2 = '''
            for (int j = low; j <= high; j++) {
                ...
            }
            '''
    st.code(code_b2, language="cpp")

    operacion_b2 = [
            "for (int j = low; j <= high; j++)",
        ]
    pasos_b2 = [
            "n"
        ]
    exp_b2 = [
            "Repetición"
        ]
    data_b2 = {
        "Expresion": operacion_b2,
        "Pasos": pasos_b2,
        "Fundamento": exp_b2
    }
    df_b2 = pd.DataFrame(data_b2)
    st.table(df_b2)
    st.markdown('''Para el tercer fragmento de la función partition''')
    code_b3 = '''
            if (arr[j] < pivot) {
                ...
            }
            '''
    st.code(code_b3, language="cpp")
    operacion_b3 = [
            "if (arr[j] < pivot)"
        ]
    pasos_b3 = [
            "2"
        ]
    exp_b3 = [
            "Operador menor y condicional"
        ]
    data_b3 = {
        "Expresion": operacion_b3,
        "Pasos": pasos_b3,
        "Fundamento": exp_b3
    }
    df_b3 = pd.DataFrame(data_b3)
    st.table(df_b3)
    st.markdown('''Para el cuarto fragmento de la función partition''')
    code_b4 = '''
            i++;  
            aux = arr[i];
            arr[i] = arr[j];
            arr[j] = aux;
            '''
    st.code(code_b4, language="cpp")
    operacion_b4 = [
            "i++",  
            "aux = arr[i]",
            "arr[i] = arr[j]",
            "arr[j] = aux"
        ]
    pasos_b4 = [
            "k",
            "2",
            "2",
            "1"
        ]
    exp_b4 = [
            "Incremento",
            "Acceso y asignación",
            "Acceso y asignación",
            "Asignación"
        ]
    data_b4 = {
        "Expresion": operacion_b4,
        "Pasos": pasos_b4,
        "Fundamento": exp_b4
    }
    df_b4 = pd.DataFrame(data_b4)
    st.table(df_b4)
    st.markdown('''
                Luego
                ''')
    st.latex(r'''
            T( n) =\ b_{1}\ +\ b_{2}\ +\sum _{i\ =\ low}^{hight} b_{3} \\
            T( n) \ =\ b_{1}\ +\ b_{2}\ +\sum _{i=1}^{n} b_{3} \\
            T( n) =\ b_{1}\ +\ b_{2}\ +nb_{3}
            ''')
    st.markdown('''Teniendo a''')
    st.latex(r'''
             \begin{array}{l}
            b_{1}\ =\ 14 \\
            b_{2}\ =\ 3n\ +\ 3 \\
            b_{3}\ =\ 3
            \end{array}
            ''')
    st.latex(r'''
            T( n) \ =\ 14\ +\ 3n\ +\ 3\ +3n
            T( n) \ =\ \ 6n\ +\ 17
            c_{1} \ =\ O( n)
            ''')
def ejecutar_analisis_quicksort_2():
  with st.expander("Análisis de la definición no recursiva"):
    st.markdown('''
                **Peor caso:** El pivote siempre será el valor más grande en el arreglo.  
                Ejm: El arreglo se encuentra ordenado crecientemente
                ''')
    st.latex(r'''
            \begin{array}{l}
            T( 1,n)  = c_{1}  + T( 1,n-1)  + T( n+1,n)  = c_{1}  + T( 1,n-1)  + 0 \\
            T( 1,n)  = c_{1}  + c_{1}  + T( 1,n-2)  + T( n,n-1)  = 2c_{1}  + T( 1,n-2) \\
            T( 1,n)  = i( c_{1})  + T( 1,n-i)
            \end{array}
             ''')
    st.markdown('''
                Finalizando cuando:
                ''')
    st.latex(r'''
            \begin{array}{l}
            1  >= n - i \\
            i  >= n - 1\\
            i = n - 1
            \end{array}
            ''')
    st.markdown('''
                Luego
                ''')
    st.latex(r'''
            T( 1,n)  = ( n-1) c_{1}  = ( n-1) n  = n^{2}  - n
            ''')
    st.markdown('''
                Por lo tanto
                ''')
    st.latex(r'''
            T( 1,n) \ =\ O\left( n^{2}\right)
            ''')

def ejecutar_analisis_heapsort_1():
  with st.container(border = True):
    st.info("Análisis")
    st.markdown('''
                Debido a que el HeapSort se basa en un heap tree, que a su vez se basa en árboles binarios, tomaremos como pero caso un árbol binario que tenga como cantidad total de nodos una potencia de dos.
                ''')
    st.latex(r'''n = 2^{m}''')
    st.markdown('''En primer lugar, analizaremos el algoritmo para crear el heap tree.''')
    code = '''
        for (int i = N / 2 - 1; i >= 0; i--)
            heapify(arr, N, i);
        '''
    st.code(code, language="cpp")
    st.markdown('''
            Como podemos ver, analizamos N/2 - 1 + 1 veces la función `heapify`.
            ''')
    st.latex(r'''
            \begin{array}{l}
            T( 1,n)  = c_{1}  + T( 1,n-1)  + T( n+1,n)  = c_{1}  + T( 1,n-1)  + 0 \\
            T( 1,n)  = c_{1}  + c_{1}  + T( 1,n-2)  + T( n,n-1)  = 2c_{1}  + T( 1,n-2) \\
            T( 1,n)  = i( c_{1})  + T( 1,n-i)
            \end{array}
             ''')
    st.markdown('''
                Analizaremos ahora, el algoritmo heapify en sus dos definiciones.
                ''')
def ejecutar_analisis_heapsort_2():
  with st.expander("Análisis de la definición recursiva"):
    st.latex(r'''
            T( a) \ =\ c_{1} \ +\ T( 2a) ,\ si\ 2a\ < =\ n \\
            T( a) \ =\ c_{1} \ \ \ \ \ \ \ \ \ \ ,\ si\ 2a\  >\ n
            ''')
    st.markdown('''
                Donde a es cualquier posición en el arreglo.  
                El 2a se considera debido a la naturaleza que tiene el arreglo heap tree donde los hijos para un nodo n se encontrará en la ubicación 2n y 2n + 1.
                ''')
    
def ejecutar_analisis_heapsort_3():
  with st.expander("Análisis de la definición no recursiva"):
    st.latex(r'''
             \begin{array}{l}
            T( a) \ =\ c1+T( 2a) \ =c1\ +( c1\ +T( 4a)) =\\
            .\\
            .\\
            .\\
            =ic_{1} \ +T\left( 2^{i} a\right)
            \end{array}
             ''')
    st.markdown('''
                La función termina cuando:
                ''')
    st.latex(r'''
            \begin{array}{l}
            2^{i}  >n\\
            i\  >m\ 
            \end{array}
            ''')
    st.markdown('''Por lo tanto:''')
    st.latex(r'''
            i\ =\ m\ +\ 1 \\
            m\ =\ \log_{2}( n)
            ''')
    st.markdown('''
            Reemplazamos:
            ''')
    st.latex(r'''
             \begin{array}{l}
            T( a) =\ ( m\ +\ 1) c_{1} \ +\ c_{1}\\
            T( a) =\ (\log_{2}( n) \ +\ 2) c_{1}
            \end{array}
            ''')
    st.markdown('''
                Entonces, la complejidad para crear el heaptree es: 
                ''')
    st.latex(r'''
            T(a)*(\frac{n}{2}- 1) =(\log_{2}( n) + 2)c_{1} * (\frac{n}{2} - 1) = O(n\log n)
            ''')
    st.markdown('''
                Ahora hallaremos la complejidad para ordenar el arreglo:
                ''')
    code = '''
            for (int i = N - 1; i > 0; i--) {
                swap(arr[0], arr[i]);
                heapify(arr, i, 0);
            }
            '''
    st.code(code, language="cpp")
    st.markdown('''
                Vemos que este código repite la operación heapify $n - 1 - 1 + 1$ veces.  
                Entonces la complejidad de esta operación será:
                ''')
    st.latex(r'''
            T(a)* (n-1)= (\log_{} n + 2)c_{1} *(n-1) = O(n\log n)
            ''')
    st.markdown('''
                Sumando los BigO de ambas operaciones tendremos:
                ''')
    st.latex(r'''
            O(n\log n) + O(n\log n) = O(n\log n)
            ''')

def ejecutar_analisis_insertionsort():
  with st.container(border= True):
    st.info("Análisis")
    st.markdown('''
                $T( n)$  
                **Peor caso:** El arreglo se encuentra ordenado de forma decreciente
                ''')
    st.markdown('''Para el primer fragmento de la función insertionSort''')
    code_c1 = '''
            int aux;
            int key;
            int j;
            '''
    st.code(code_c1, language="cpp")
    operacion_c1 = ["aux","key", "j"]
    pasos_c1 = ["1","1","1"]
    exp_c1 = ["Declaración","Declaración","Declaración"]
    data_c1 = {
        "Operación": operacion_c1,
        "Pasos": pasos_c1,
        "Fundamento": exp_c1
    }   
    df_c1 = pd.DataFrame(data_c1)
    st.table(df_c1)
    st.markdown('''Para el segundo fragmento de la función insertionSort''')
    code_c2 = '''
            for(int i = 1;i<n;i++){
                ...
            }
            '''
    st.code(code_c2, language="cpp")
    operacion_c2 = ["for(int i = 1;i<n;i++)"]
    pasos_c2 = ["n"]
    exp_c2 = ["Repetición"]
    data_c2 = {
        "Operación": operacion_c2,
        "Pasos": pasos_c2,
        "Fundamento": exp_c2
    }   
    df_c2 = pd.DataFrame(data_c2)
    st.table(df_c2)
    st.markdown('''Para el tercer fragmento de la función insertionSort''')
    code_c3 = '''
            key = v[i];
            j = i - 1;
            ...
            v[j + 1] = key;
            '''
    st.code(code_c3, language="cpp")
    operacion_c3 = ["key = v[i]","j = i - 1","v[j + 1] = key"]
    pasos_c3 = ["2","2", "1"]
    exp_c3 = ["Acceso y asignación","Resta y asignación", "Asignación"]
    data_c3 = {
        "Operación": operacion_c3,
        "Pasos": pasos_c3,
        "Fundamento": exp_c3
    }   
    df_c3 = pd.DataFrame(data_c3)
    st.table(df_c3)
    st.markdown('''Para el cuarto fragmento de la función insertionSort''')
    code_c4 = '''
            while(j >= 0 && key < v[j]){
                ...
            }
            '''
    st.code(code_c4, language="cpp")
    operacion_c4 = ["while(j >= 0 && key < v[j])"]
    pasos_c4 = ["n"]
    exp_c4 = ["Repetición"]
    data_c4 = {
        "Operación": operacion_c4,
        "Pasos": pasos_c4,
        "Fundamento": exp_c4
    }   
    df_c4 = pd.DataFrame(data_c4)
    st.table(df_c4)
    st.markdown('''Para el quinto fragmento de la función insertionSort''')
    code_c5 = '''
            v[j + 1] = v[j];
            j--;
            '''
    st.code(code_c5, language="cpp")
    operacion_c5 = ["v[j + 1] = v[j]","j--"]
    pasos_c5 = ["2","k"]
    exp_c5 = ["Acceso y asignación","Decremento"]
    data_c5 = {
        "Operación": operacion_c5,
        "Pasos": pasos_c5,
        "Fundamento": exp_c5
    }   
    df_c5 = pd.DataFrame(data_c5)
    st.table(df_c5)
    st.markdown('''Entonces''')
    st.latex(r'''
        \begin{array}{l}
        T( n) \ =c_{1} +c_{2} +\ \sum _{i=1}^{n-1}( c_{3} +c_{4} +ic_{5})\\
        T( n) \ =c_{1} +c_{2} +\ \sum _{i=1}^{n-1} c_{3} +\sum _{i=1}^{n-1} c_{4} +\sum _{i=1}^{n-1} ic_{5}\\
        T( n) \ =c_{1} +c_{2} +\ ( n-1) c_{3} +( n-1) c_{4} +c_{5}\sum _{i=1}^{n-1} i\\
        T( n) \ =c_{1} +c_{2} +\ ( n-1) c_{3} +( n-1) c_{4} +c_{5}\left(\frac{n( n-1)}{2}\right)\\
        T( n) \ =c_{1} +c_{2} +\ ( n-1)( c_{3} +c_{4}) +c_{5}\left(\frac{n( n-1)}{2}\right)
        \end{array}
        ''')
    
def ejecutar_analisis_shellsort():
  with st.expander("Análisis"):
    st.markdown('''
                $T(n):$  
                Analizando en $T(n)$ para un caso general:
                ''')
    st.markdown('''Para el primer fragmento de la función shellSort''')
    code_c1 = '''
            int aux,z;
            '''
    st.code(code_c1, language="cpp")
    operacion_c1 = ["aux","z"]
    pasos_c1 = ["1","1"]
    exp_c1 = ["Declaración","Declaración"]
    data_c1 = {
        "Operación": operacion_c1,
        "Pasos": pasos_c1,
        "Fundamento": exp_c1
    }   
    df_c1 = pd.DataFrame(data_c1)
    st.table(df_c1)
    st.markdown('''Para el segundo fragmento de la función shellSort''')
    code_c2 = '''
            for(int i = n/2;i>0;i/=2){
                ...
            }
            '''
    st.code(code_c2, language="cpp")
    operacion_c2 = ["for(int i = n/2;i>0;i/=2)"]
    pasos_c2 = ["n"]
    exp_c2 = ["Repetición"]
    data_c2 = {
        "Operación": operacion_c2,
        "Pasos": pasos_c2,
        "Fundamento": exp_c2
    }   
    df_c2 = pd.DataFrame(data_c2)
    st.table(df_c2)
    st.markdown('''Para el tercer fragmento de la función shellSort''')
    code_c3 = '''
            for(int j = i;j<n;j++){
                ...
            }
            '''
    st.code(code_c3, language="cpp")
    operacion_c3 = ["for(int j = i;j<n;j++)"]
    pasos_c3 = ["n"]
    exp_c3 = ["Repetición"]
    data_c3 = {
        "Operación": operacion_c3,
        "Pasos": pasos_c3,
        "Fundamento": exp_c3
    }   
    df_c3 = pd.DataFrame(data_c3)
    st.table(df_c3)
    st.markdown('''Para el cuarto fragmento de la función shellSort''')
    code_c4 = '''
            aux = v[j];
            ...
            v[z] = aux;
            '''
    st.code(code_c4, language="cpp")
    operacion_c4 = ["aux = v[j]","v[z] = aux"]
    pasos_c4 = ["2","1"]
    exp_c4 = ["Acceso y asignación","Asignación"]
    data_c4 = {
        "Operación": operacion_c4,
        "Pasos": pasos_c4,
        "Fundamento": exp_c4
    }   
    df_c4 = pd.DataFrame(data_c4)
    st.table(df_c4)
    st.markdown('''Para el quinto fragmento de la función shellSort''')
    code_c5 = '''
            for(z = j; z >= i && v[z - i] > aux;z-=i){
                ...
            }
            '''
    st.code(code_c5, language="cpp")
    operacion_c5 = ["for(z = j; z >= i && v[z - i] > aux;z-=i)"]
    pasos_c5 = ["n"]
    exp_c5 = ["Repetición"]
    data_c5 = {
        "Operación": operacion_c5,
        "Pasos": pasos_c5,
        "Fundamento": exp_c5
    }   
    df_c5 = pd.DataFrame(data_c5)
    st.table(df_c5)
    st.markdown('''Para el sexto fragmento de la función shellSort''')
    code_c6 = '''
            v[z] = v[z-i];
            '''
    st.code(code_c6, language="cpp")
    operacion_c6 = ["v[z] = v[z-i];"]
    pasos_c6 = ["2"]
    exp_c6 = ["Acceso y asignación"]
    data_c6 = {
        "Operación": operacion_c6,
        "Pasos": pasos_c6,
        "Fundamento": exp_c6
    }   
    df_c6 = pd.DataFrame(data_c6)
    st.table(df_c6)