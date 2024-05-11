import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def crearDiagrama(l1,l2,l3,tittle,theme,logx = False,logy = False):
   
    if theme == "dark":
        plt.style.use("default")
        plt.figure(facecolor='#0E1117')
    else:
        plt.style.use("default")
        plt.figure(facecolor='#FFFFFF')

    ax = plt.axes()
    plt.plot(l1,l2,label ='T(n)')
    plt.plot(l1,l3, label='O(nLogn)', linestyle='--')
    
    if theme == "dark":
        plt.title(tittle,color='white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('#262730')
        ax.spines['top'].set_color('#262730')
        ax.spines['bottom'].set_color('white')
        ax.set_facecolor("#0E1117")
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis.label.set_color('white') 
        ax.yaxis.label.set_color('white') 
    else:
        plt.title(tittle,color='black')
        ax.spines['left'].set_color('black')
        ax.spines['right'].set_color('#F0F2F6')
        ax.spines['top'].set_color('#F0F2F6')
        ax.spines['bottom'].set_color('black')
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')
        ax.xaxis.label.set_color('black') 
        ax.yaxis.label.set_color('black') 


    if logx:
        plt.xscale('log')

    if logy:
        plt.yscale('log')
    else:
        plt.ticklabel_format(style='plain', axis='y')
        
    plt.xlabel("tamano n")
    plt.ylabel("tiempo (ms)")
    plt.legend()

    st.pyplot(plt.gcf(),use_container_width=True)