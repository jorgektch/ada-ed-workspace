import streamlit as st

def ejecutar_implementacion_mergesort():
  st.subheader("Mergesort")

  code = '''public static void mergesort(int a[]){
    mergesort(a,0,a.lenght-1);
}
 
public static void mergesort( int a[], int primero, int ultimo){
    int central;
    if(primero<ultimo){
        central=(primero+ultimo);
        mergesort(a,primero,central);
        mergesort(a,central+1,ultimo);
        mezcla(a,primero,central,ultimo);
    }
}

public static void mezcla(int[] a, int izda, int medio, int drcha){
    int[] tmp = new int[a.lenght];
    int i,k,z;
    i=z=izda;
    k=medio+1;
    while(i<=medio && k<=drcha){
        if(a[i] <= a[k]){
            tmp[z++]=a[i++];
        }else{
            tmp[z++]=a[k++];
        }
    }
    while(i<=medio){
        tmp[z++]=a[i++];
    }
    while(k<=drcha){
        tmp[z++]=a[k++];
    }
    System.arraycopy(tmp,izda,a,izda,drcha-izda+1);
}
 '''
  
  st.code(code, language='java')

def ejecutar_implementacion_quicksort():
  st.subheader("Quicksort")

  code = '''int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);
    int aux;
    for (int j = low; j <= high; j++) {
        if (arr[j] < pivot) {
            i++;
            aux = arr[i];
            arr[i] = arr[j];
            arr[j] = aux;
        }
    }
    aux = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = aux;
    return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}'''
  
  st.code(code, language='cpp')

def ejecutar_implementacion_heapsort():
  st.subheader("Heapsort")

  code = '''#include <iostream>
using namespace std;

void heapify(int arr[], int N, int i)
{
    int largest = i;
    int l = 2 * i + 1;  
    int r = 2 * i + 2;

    if (l < N && arr[l] > arr[largest])
        largest = l;

    if (r < N && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, N, largest);
    }
}

void heapSort(int arr[], int N)
{
    for (int i = N / 2 - 1; i >= 0; i--)
        heapify(arr, N, i);

    for (int i = N - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
'''
  st.code(code, language='cpp')

def ejecutar_implementacion_insertionsort():
  st.subheader("Insertion Sort")

  code = '''void insertionSort(int[] v, int n ){
    int aux;
    int key;
    int j;
    for(int i = 1;i<n;i++){
        key = v[i];
        j = i - 1;
        while(j >= 0 && key < v[j]){
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = key;
    }
}
'''
  st.code(code, language='cpp')

def ejecutar_implementacion_shellsort():
  st.subheader("Shell Sort")

  code = '''void shellSort(int[] v, int n){
    int aux,z;
    for(int i = n/2;i>0;i/=2){
        for(int j = i;j<n;j++){
            aux = v[j];
            for(z = j; z >= i && v[z - i] > aux;z-=i){
                v[z] = v[z-i];
            }
            v[z] = aux;
        }
    }
}
'''
  st.code(code, language='cpp')
