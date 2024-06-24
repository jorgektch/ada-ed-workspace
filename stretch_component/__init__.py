import os
import streamlit.components.v1 as components


absolute_path  = os.path.dirname(os.path.abspath(__file__))
frontend_path = absolute_path
component_func = components.declare_component(
    "stretch_component",
    path=frontend_path
)


def stretch_component(radius:int, speed:int, numberOfNodes: int, theme:str = "dark", key=None):
    component_value = component_func(radius=radius,speed=speed,numberOfNodes=numberOfNodes,theme=theme,key=key)
    
