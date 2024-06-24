import os
import streamlit.components.v1 as components


parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
component = components.declare_component("stretch_component", path=build_dir)


def stretch_component(radius:int, speed:int, numberOfNodes: int, theme:str = "dark", key=None):
    component_value = component_func(radius=radius,speed=speed,numberOfNodes=numberOfNodes,theme=theme,key=key)
    
