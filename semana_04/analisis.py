import streamlit as st

def ejecutar_analisis1():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es numerador (n) y denominador (m).")
    st.write("Paso 2: Tamaño de la entrada es “n y m”.")
    st.write("Paso 3: Definir recurrencia para T(n).")
    st.latex(r'''
        T(n,m)= 
        \begin{cases} 
        c_{1} & \text{si } n < m \\ 
        c_{2} + T(n-m, m) & \text{si } n \geq m 
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(n,m)")
    st.write("Peor caso m = 1;")
    st.latex(r'''
        \begin{align*}
        T(n,1) &= c_{2} + T(n-1,1) \\
        T(n,1) &= 2c_{2} + T(n-2,1) \\
        T(n,1) &= ic_{2} + T(n-i,1) \\
        \end{align*}
    ''')
    st.latex(r'''
        \text{Finaliza cuando } n - i \leq 1 \\
        n - 1 \leq i \\
        i = n \\
        T(n,1) = nc_{2} + c_{1}
    ''')

def ejecutar_analisis2():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es numerador (n).")
    st.write("Paso 2: Tamaño de la entrada es “n”.")
    st.write("Paso 3: Definir recurrencia para T(n).")
    st.latex(r'''
        T(n)= 
        \begin{cases} 
        c_{1} & \text{si } n < 10 \\ 
        c_{2} + T\left(\frac{n}{10}\right) & \text{si } n \geq 10 
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(n)")
    st.write("Caso: n es potencia de 10")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T\left(\frac{n}{10}\right) \\
        &= c_{2} + \left(c_{2} + T\left(\frac{n}{100}\right)\right) \\
        &= 2c_{2} + T\left(\frac{n}{100}\right) \\
        &= 3c_{2} + T\left(\frac{n}{1000}\right) \\
        &= ic_{2} + T\left(\frac{n}{10^i}\right)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Finaliza cuando } n = 1 \text{ en este caso} \\
        \frac{n}{10^i} = 1 \\
        \log_{10}n = i \\
        T(n) = \log_{10}n \cdot c_{2} + c_{1}
    ''')

def ejecutar_analisis3():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es “n”.")
    st.write("Paso 2: Tamaño de la entrada es “n”.")
    st.write("Paso 3: Definir recurrencia para T(n).")
    st.latex(r'''
        T(n)= 
        \begin{cases} 
        c_{1} & \text{si } n < 10 \\ 
        c_{2} + T\left(\frac{n}{10}\right) & \text{si } n \geq 10 
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(n)")
    st.write("Caso: n es potencia de 10")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T\left(\frac{n}{10}\right) \\
        &= c_{2} + \left(c_{2} + T\left(\frac{n}{100}\right)\right) \\
        &= 2c_{2} + T\left(\frac{n}{100}\right) \\
        &= 3c_{2} + T\left(\frac{n}{1000}\right) \\
        &= ic_{2} + T\left(\frac{n}{10^i}\right)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Finaliza cuando } n = 1 \text{ en este caso} \\
        \frac{n}{10^i} = 1 \\
        \log_{10}n = i \\
        T(n) = \log_{10}n \cdot c_{2} + c_{1}
    ''')

def ejecutar_analisis4():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es “a”, “b”.")
    st.write("Paso 2: Tamaño de la entrada es “a”, “b”.")
    st.write("Paso 3: Definir recurrencia para T(a,b).")
    st.latex(r'''
        T(a,b)= 
        \begin{cases} 
        0 & \text{si } a=0 \text{ o } b=0 \\ 
        c_{1} & \text{si } b=1 \\ 
        c_{2} & \text{si } a=1 \\ 
        c_{3} + T(a, b-1) & \text{si no se cumple lo anterior} \\
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(a,b)")
    st.latex(r'''
        \begin{align*}
        T(a,b) &= c_{3} + T(a, b-1) \\
        &= c_{3} + c_{3} + T(a, b-2) \\
        &= 2c_{3} + T(a, b-2) \\
        &= 2c_{3} + c_{3} + T(a, b-3) \\
        &= 3c_{3} + T(a, b-3) \\
        & \quad \vdots \\
        &= ic_{3} + T(a, b-i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } b-i=1, \text{luego } i=b-1
    ''')
    st.latex(r'''
        \text{Reemplazando en la ecuación:}
    ''')
    st.latex(r'''
        \begin{align*}
        T(a,b) &= (b-1)c_{3} + T(a, b-(b-1)) \\
               &= bc_{3} - c_{3} + T(a,1)
        \end{align*}
    ''')
    st.latex(r'''
        T(a,1) \text{ retorna } a, \text{ además, recordemos que } c_{3}=a
    ''')
    st.latex(r'''
        \begin{align*}
        T(a,b) &= bc_{3} - c_{3} + c_{3} \\
        &= bc_{3}
        \end{align*}
    ''')

    st.write("Paso 5: Tiempo de ejecución (b=n)")
    st.latex(r'''
        T(n) = nc_{3}
    ''')

def ejecutar_analisis5():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es “n”.")
    st.write("Paso 2: Tamaño de la entrada es “n”.")
    st.write("Paso 3: Definir recurrencia para T(n).")
    st.latex(r'''
        T(n)= 
        \begin{cases} 
        c_{1} & \text{si } n = 1 \\ 
        c_{2} + T(n-1) & \text{si } n \ne 1 
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(n)")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n-1) \\
             &= c_{2} + \left[c_{2} + T((n-1)-1)\right] \\
             &= 2c_{2} + T(n-2) \\
             &= 2c_{2} + \left[c_{2} + T((n-2)-1)\right] \\
             &= 3c_{2} + T(n-3) \\
             &= 3c_{2} + \left[c_{2} + T((n-3)-1)\right] \\
             &= 4c_{2} + T(n-4) \\
             & \quad \vdots \\
             &= ic_{2} + T(n-i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } n - i = 1 \\
        \text{entonces } i = n - 1
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = (n-1)c_{2} + c_{1}
    ''')
    st.write("Por lo tanto:")
    st.latex(r'''
        \text{Tiene complejidad } O(n)
    ''')

def ejecutar_analisis6():
    st.subheader("Análisis")
    st.write("Calculando el T(n)")

    st.write("Para esPositivo(double numero):")
    st.latex(r'''
        \begin{cases} 
        T(n) = c_{1} & \text{si } n > 0 \\ 
        T(n) = c_{2} + T(n+1) & \text{si } n \le 0 
        \end{cases}
    ''')
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n+1) \\
             &= c_{2} + \left[c_{2} + T((n+1)+1)\right] \\
             &= 2c_{2} + T(n+2) \\
             &= 2c_{2} + \left[c_{2} + T((n+2)+1)\right] \\
             &= 3c_{2} + T(n+3) \\
             &= 3c_{2} + \left[c_{2} + T((n+3)+1)\right] \\
             &= 4c_{2} + T(n+4) \\
             & \quad \vdots \\
             &= ic_{2} + T(n+i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } n + i = 0 \\
        \text{entonces } -n = i
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = -n \cdot c_{2} + T(0) = -n \cdot c_{2} + c_{1}
    ''')
    st.write("Por lo tanto:")
    st.latex(r'''
        \text{Tiene complejidad } O(n)
    ''')

    st.write("Para esNegativo(double numero):")
    st.latex(r'''
        \begin{cases} 
        T(n) = c_{1} & \text{si } n \le 0 \\ 
        T(n) = c_{2} + T(n-1) & \text{si } n > 0 
        \end{cases}
    ''')
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n-1) \\
             &= c_{2} + \left[c_{2} + T((n-1)-1)\right] \\
             &= 2c_{2} + T(n-2) \\
             &= 2c_{2} + \left[c_{2} + T((n-2)-1)\right] \\
             &= 3c_{2} + T(n-3) \\
             &= 3c_{2} + \left[c_{2} + T((n-3)-1)\right] \\
             &= 4c_{2} + T(n-4) \\
             & \quad \vdots \\
             &= ic_{2} + T(n-i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } n - i = 0 \\
        \text{entonces } n = i
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = n \cdot c_{2} + T(0) = n \cdot c_{2} + c_{1}
    ''')
    st.write("Por lo tanto:")
    st.latex(r'''
        \text{Tiene complejidad } O(n)
    ''')

def ejecutar_analisis7():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada es “n”.")
    st.write("Paso 2: Tamaño de la entrada es “n”.")
    st.write("Paso 3: Definir recurrencia para T(n).")
    st.latex(r'''
        T(n)= 
        \begin{cases} 
        c_{1} & \text{si } n < 10 \\ 
        c_{2} + T\left(\frac{n}{10}\right) & \text{si } n \geq 10 
        \end{cases}
    ''')

    st.write("Paso 4: Derivar la función recursiva de T(n)")
    st.write("Caso: n es potencia de 10")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T\left(\frac{n}{10}\right) \\
             &= c_{2} + \left(c_{2} + T\left(\frac{n}{100}\right)\right) \\
             &= 2c_{2} + T\left(\frac{n}{100}\right) \\
             &= 3c_{2} + T\left(\frac{n}{1000}\right) \\
             &= ic_{2} + T\left(\frac{n}{10^i}\right)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Finaliza cuando } n = 1 \text{ en este caso} \\
        \frac{n}{10^i} = 1 \\
        \log_{10}n = i
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = \log_{10}n \cdot c_{2} + c_{1}
    ''')
    st.write("Por lo tanto:")
    st.latex(r'''
        \text{Tiene complejidad } O(\log_{10}n)
    ''')

def ejecutar_analisis8():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada: número entero positivo n")
    st.write("Paso 2: Tamaño de entrada n")
    st.write("Paso 3: Definición recursiva para T(n)")
    st.latex(r'''
        \begin{cases}
        T(n) = c_{1} & \text{Si } n = 0 \\
        T(n) = c_{2} + T(n \gg 1) & \text{Si } n \geq 1
        \end{cases}
    ''')

    st.write("Paso 4: Derivar definición no recursiva de T(n)")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n \gg 1) \\
             &= c_{2} + (c_{2} + T((n \gg 1) \gg 1)) \\
             &= 2c_{2} + T(n \gg 2) \\
             &= 3c_{2} + T(n \gg 3) \\
             &= 4c_{2} + T(n \gg 4) \\
             &\quad \vdots \\
             &= ic_{2} + T(n \gg i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } n \gg i = 0 \\
        i = \log_{2}n + 1
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = (\log_{2}n + 1)c_{2} + c_{1}
    ''')
    st.write("Paso 5: Obtener el orden de tiempo de ejecución:")
    st.latex(r'''
        T(n) \text{ es } O(\log n)
    ''')

    st.write("Paso 6: Prueba por inducción de T(n)")
    st.latex(r'''
        T(n) = (\log_{2}n + 1)c_{2} + c_{1}
    ''')
    st.write("Caso inductivo:")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n \gg 1) \\
             &= c_{2} + (\log_{2}(n \gg 1) + 1)c_{2} + c_{1}
        \end{align*}
    ''')
    st.latex(r'''
        \log_{2}n = k \\
        \log_{2}(n \gg 1) = k - 1
    ''')
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + ((k - 1 + 1)c_{2}) + c_{1} \\
             &= c_{2} + (k)c_{2} + c_{1} \\
             &= (k + 1)c_{2} + c_{1} \\
             &= (\log_{2}n + 1)c_{2} + c_{1}
        \end{align*}
    ''')

def ejecutar_analisis9():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada: número entero positivo a, número entero positivo b")
    st.write("Paso 2: Tamaño de entrada b")
    st.write("Paso 3: Definición recursiva para T(a,b)")
    st.latex(r'''
        T(a,b) = 
        \begin{cases} 
        c_{1} & \text{Si } b = 0 \\
        c_{2} & \text{Si } b = 1 \\
        c_{3} + T(2a,\frac{b}{2}) & \text{Si } b \text{ es par y } b > 1 \\
        c_{4} + T(2a,\frac{b}{2}) & \text{Si } b \text{ es impar y } b > 1
        \end{cases}
    ''')

    st.write("Paso 4: Derivar definición no recursiva de T(a,b)")
    st.write("Caso: b es una potencia de 2")
    st.latex(r'''
        (b = 2^m)
    ''')
    st.latex(r'''
        \begin{align*}
        T(a,b) &= c_{3} + T(2a, \frac{b}{2}) \\
               &= c_{3} + (c_{3} + T(2(2a), \frac{b}{4})) \\
               &= 2c_{3} + T(4a, \frac{b}{4}) \\
               &= 3c_{3} + T(8a, \frac{b}{8}) \\
               &\quad \vdots \\
               &= ic_{3} + T(2^i a, \frac{b}{2^i})
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } b = 1 \text{ en este caso} \\
        \frac{b}{2^i} = 1 \\
        b = 2^i \\
        \log_{2}b = i
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(a,b) = \log_{2}b \cdot c_{3} + c_{2}
    ''')

    st.write("Paso 5: Prueba por inducción de T(a,b)")
    st.write("Caso base:")
    st.latex(r'''
        b = 0; \\
        T(a,b) = c_{1}
    ''')
    st.write("Caso inductivo:")
    st.latex(r'''
        \begin{align*}
        T(a,b) &= c_{3} + T(2a, \frac{b}{2}) \\
               &= c_{3} + (\log_{2}(\frac{b}{2}) \cdot c_{3} + c_{2}) \\
               &= c_{3} + \log_{2}(b) \cdot c_{3} - \log_{2}(2) \cdot c_{3} + c_{2} \\
               &= \log_{2}b \cdot c_{3} + c_{2}
        \end{align*}
    ''')

def ejecutar_analisis10():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada: número entero positivo n, potencia: x")
    st.write("Paso 2: Tamaño de entrada x")
    st.write("Paso 3: Definición recursiva para T(x)")
    st.latex(r'''
        T(n,x) = 
        \begin{cases} 
        c_{1} & \text{Si } x \leq 1 \\
        c_{2} + T(n,x-1) & \text{Si } x > 1
        \end{cases}
    ''')

    st.write("Paso 4: Derivar definición no recursiva de T(x)")
    st.latex(r'''
        \begin{align*}
        T(n,x) &= c_{2} + T(n, x-1) \\
               &= c_{2} + (c_{2} + T(n, (x-1)-1)) \\
               &= 2c_{2} + T(n, x-2) \\
               &= 3c_{2} + T(n, x-3) \\
               &\quad \vdots \\
               &= ic_{2} + T(n, x-i)
        \end{align*}
    ''')
    st.latex(r'''
        \text{Termina cuando } x - i = 0 \\
        x = i
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n,x) = x c_{2} + c_{1}
    ''')

    st.write("Paso 5: Obtener el orden de tiempo de ejecución:")
    st.latex(r'''
        T(n,x) \text{ es } O(x)
    ''')

    st.write("Paso 6: Prueba por inducción de T(n,x)")
    st.latex(r'''
        T(n,x) = x c_{2} + c_{1}
    ''')
    st.write("Caso base:")
    st.latex(r'''
        x = 0; \\
        T(n,0) = c_{1}
    ''')
    st.write("Caso inductivo:")
    st.latex(r'''
        \begin{align*}
        T(n,x) &= c_{2} + T(n, x-1) \\
               &= c_{2} + ((x-1) c_{2} + c_{1}) \\
               &= c_{2} + (x-1) c_{2} + c_{1} \\
               &= x c_{2} + c_{1}
        \end{align*}
    ''')

def ejecutar_analisis11():
    st.subheader("Análisis")
    st.write("Paso 1: Entrada: número entero positivo a, número entero positivo b, factor n = a")
    st.write("Paso 2: Tamaño de entrada n = a")
    st.write("Paso 3: Definición recursiva para T(n)")
    st.latex(r'''
        T(n) = 
        \begin{cases} 
        c_{1} & \text{Si } n \text{ es factor de } a \text{ y } b \\
        c_{2} + T(n-1) & \text{Si } n \geq 1
        \end{cases}
    ''')
    st.write("Paso 4: Derivar definición no recursiva de T(n)")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n-1) \\
             &= c_{2} + (c_{2} + T(n-2)) \\
             &= 2c_{2} + T(n-2) \\
             &= 3c_{2} + T(n-3) \\
             &\quad \vdots \\
             &= ic_{2} + T(n-i)
        \end{align*}
    ''')
    st.write("Peor caso: a y b poseen un único factor en común.")
    st.latex(r'''
        \text{Termina cuando } n - i = 1 \\
        i = n - 1
    ''')
    st.latex(r'''
        \text{Reemplazamos:} \\
        T(n) = (n-1)c_{2} + c_{1}
    ''')

    st.write("Paso 5: Obtener el orden de tiempo de ejecución:")
    st.latex(r'''
        T(n) \text{ es } O(n)
    ''')

    st.write("Paso 6: Prueba por inducción de T(n)")
    st.latex(r'''
        T(n) = (n-1)c_{2} + c_{1}
    ''')
    st.write("Caso inductivo:")
    st.latex(r'''
        \begin{align*}
        T(n) &= c_{2} + T(n-1) \\
             &= c_{2} + ((n-2)c_{2} + c_{1}) \\
             &= c_{2} + (n-2)c_{2} + c_{1} \\
             &= (n-1)c_{2} + c_{1}
        \end{align*}
    ''')