import streamlit as st
from algoPages.ASearch.ASearch import *
from algoPages.BFS.BFS import *
from algoPages.DFS.DFS import *
from algoPages.Prim.Prim import *
from algoPages.Kruskal.Kruskal import *
from algoPages.topologicSort.topologicSort import *
from algoPages.Dijkstra.Dijkstra import *



# Contenido
def ejecutar_algoritmos(add_selectboxAlg, theme):
  if "DFS" in add_selectboxAlg:
    ejecutar_DFS(theme)
  elif "BFS" in add_selectboxAlg:
    ejecutar_BFS(theme)
  elif "Ordenamiento topologico" in add_selectboxAlg:
    ejecutar_topologicSort(theme)
  elif "Prim" in add_selectboxAlg:
    ejecutar_Prim(theme)
  elif "Kruskal" in add_selectboxAlg:
    ejecutar_Kruskal(theme)
  elif "Dijkstra" in add_selectboxAlg:
    ejecutar_Dijkstra(theme)
  elif "A* Search" in add_selectboxAlg:
    ejecutar_ASearch(theme)

  