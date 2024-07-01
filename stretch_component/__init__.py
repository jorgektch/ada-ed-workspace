import os
import streamlit.components.v1 as components


parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
component_func = components.declare_component("stretch_component", path=build_dir)

def stretch_component(id:str, type:str, theme:str, radius, speed, numberOfNode = 6, key=None):
    topSort = component_value = component_func(id = id, type=type,theme=theme, radius=radius, speed = speed, numberOfNode = numberOfNode ,key=key)
    if(topSort):
        return topSort
    else:
        return []
    
