import streamlit as st

def ejecutar_implementacion1():
  st.subheader("Implementación")

  code = '''def div_Entera(numerador, denominador):
    if numerador < denominador:
        return 0
    else:
        return 1 + div_Entera(numerador - denominador, denominador)
        
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))

    resultado = div_Entera(numerador, denominador)

    print("La división entera es:", resultado)
    '''
  st.code(code, language='python')

def ejecutar_implementacion2():
  st.subheader("Implementación")

  code = '''def invertir_Numero(num, pos):
    if num < 10:
        return num
    else:
        ultimo_digito = num % 10
        return ultimo_digito * (10*pos) + invertir_Numero(num / 10, pos - 1)

    numero = int(input("Ingrese un número a invertir: "))
    num_Digitos = len(str(numero)) - 1

    resultado = invertir_Numero(numero, num_Digitos)
    print("El número invertido es:", resultado)
    '''
  st.code(code, language='python')

def ejecutar_implementacion3():
  st.subheader("Implementación")

  code = '''public class Main {
    
    public static int sumarDigitos(int numero) {
        if(numero < 10) {
            return numero;
        } else {
            return (numero % 10) + sumarDigitos(numero / 10);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresar numero: ");
        int num = scanner.nextInt();
        int suma = sumarDigitos(num);
        System.out.println("Suma: " + suma);
        scanner.close();
    }
  }
  '''
  st.code(code, language='java')

def ejecutar_implementacion4():
  st.subheader("Implementación")

  code = '''public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese num1: ");
        int num1 = scanner.nextInt();
        System.out.print("Ingrese num2: ");
        int num2 = scanner.nextInt();
        int resultado = multiplicar(num1, num2);
        System.out.println("Resultado: " + resultado);
    }

    public static int multiplicar(int a, int b) {
        if (a == 0 || b == 0) {
            return 0;
        } else if (b == 1) {
            return a;
        } else if (a == 1) {
            return b;
        } else {
            return a + multiplicar(a, b - 1);
        }
      }
    }
    '''
  st.code(code, language='java')

def ejecutar_implementacion5():
  st.subheader("Implementación")

  code = '''public class Problema5 {
    
    public static void main(String[] args) {
        int[] vector = {1, 2, 3, 4, 7};
        int resultado = sumaVector(vector, 5);
        System.out.println("La suma de los elementos del vector es: " + resultado);
    }
    
    public static int sumaVector(int[] vector, int indice) {     

   //Funcion recursiva
        if (indice == 1) {
            return vector[indice-1]; //Caso base, operaciones primitivas c1
        } else {
            return vector[indice-1] + sumaVector(vector, indice - 1);
        }  
      }
    }
    '''
  st.code(code, language='java')

def ejecutar_implementacion6():
  st.subheader("Implementación")

  code = '''package problema6;
import java.util.Scanner;

public class Problema6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa un numero: ");
        double numero = scanner.nextDouble();

        if (esPositivo(numero)) {
            System.out.println(numero + " es positivo.");
        } else if (esNegativo(numero)) {
            System.out.println(numero + " es negativo.");
        } else {
            System.out.println(numero + " es cero.");
        }
    }

    public static boolean esPositivo(double numero) {
        if (numero > 0) {
            return true;
        } else if (numero == 0) {
            return false;
        } else {
            return esPositivo(numero + 1);
        }
    }

    public static boolean esNegativo(double numero) {
        if (numero < 0) {
            return true;
        } else if (numero == 0) {
            return false;
        } else {
            return esNegativo(numero - 1);
        }
      }
    }
    '''
  st.code(code, language='java')

def ejecutar_implementacion7():
  st.subheader("Implementación")

  code = ''' static int digitSum (int n) {
    if (n < 10) { 
                  return n;
    } else {
                return n % 10 + digitSum(n / 10); 
    }
  }
    '''
  st.code(code, language='python')

def ejecutar_implementacion8():
  st.subheader("Implementación")

  code = '''#include <bits/stdc++.h>

    using namespace std;

    string getBin(int n, string bin){
        string ans = bin;
        if(n != 0){
          if(n & (1 << 0)){
              ans = "1" + ans;
          }else{
              ans = "0" + ans;
          }
          return getBin(n>>1,ans);
        }else{
          return ans;
        }

    }

    int main(){
        int n;
        cin>>n;
        cout<<getBin(n,"")<<endl;
    }
    '''
  st.code(code, language='cpp')

def ejecutar_implementacion9():
  st.subheader("Implementación")

  code = '''def div_Entera(numerador, denominador):
    if numerador < denominador:
        return 0
    else:
        return 1 + div_Entera(numerador - denominador, denominador)
        
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))

    resultado = div_Entera(numerador  , denominador)

    print("La división entera es:", resultado)
    '''
  st.code(code, language='python')

def ejecutar_implementacion10():
  st.subheader("Implementación")

  code = '''#include <bits/stdc++.h>
    using namespace std;

    double potencia(double n,double x){
   	 	if(x <= 1){
   		 	return n;
   	 	}else{
   			return n*potencia(n,x-1);
   	 	}
    }
    
    int main(){
    		double n,x;
   	 	cin>>n>>x;
   	 	cout<<potencia(n,x)<<endl;
    }
    '''
  st.code(code, language='cpp')

def ejecutar_implementacion11():
  st.subheader("Implementación")

  code = '''#include <bits/stdc++.h>
    using namespace std;

    int GCD(int a, int b, int factor){
        if(a % factor == 0 && b % factor == 0){
          return factor;
        }else{
          return max(1,GCD(a,b,factor-1));
        }
    }

    int main(){
        int a,b;
        cin>>a>>b;
        cout<<GCD(a,b,a)<<endl;
    }
    '''
  st.code(code, language='cpp')