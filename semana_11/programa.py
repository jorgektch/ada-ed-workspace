import streamlit as st

def EsSolucion(nodo):
    return len(nodo) == 3

def Expandir(nodo, personas):
    nuevos_nodos = []
    for persona in personas:
        if persona not in nodo:
            nuevo_nodo = nodo + [persona]
            nuevos_nodos.append(nuevo_nodo)
    return nuevos_nodos

def EsFactible(nodo, regla_inicio, regla_medio, regla_final):
    if len(nodo) > 0 and nodo[0] == regla_inicio:
        return False
    if len(nodo) > 1 and nodo[1] == regla_medio:
        return False
    if len(nodo) > 2 and nodo[2] == regla_final:
        return False
    return True

def backtracking(nodo, personas, regla_inicio, regla_medio, regla_final):
    lista_soluciones = []
    if EsSolucion(nodo):
        lista_soluciones.append(nodo)
    for v in Expandir(nodo, personas):
        if EsFactible(v, regla_inicio, regla_medio, regla_final):   
            ls = backtracking(v, personas, regla_inicio, regla_medio, regla_final)
            lista_soluciones.extend(ls)
    return lista_soluciones

def main_silla():
    st.title("Backtracking con Reglas Personalizadas")
    personas = ['amarilla', 'roja', 'negra']
    num_reglas = st.number_input("Seleccione el número de reglas a aplicar (1 o 2)", min_value=1, max_value=2, step=1)
    regla_inicio = regla_medio = regla_final = None

    if num_reglas >= 1:
        regla_1 = st.selectbox("Seleccione la primera regla", ["", "No se sienta al inicio", "No se sienta en el medio", "No se sienta al final"])
        if regla_1 == "No se sienta al inicio":
            regla_inicio = st.selectbox("Persona para la primera regla", personas)
        elif regla_1 == "No se sienta en el medio":
            regla_medio = st.selectbox("Persona para la primera regla", personas)
        elif regla_1 == "No se sienta al final":
            regla_final = st.selectbox("Persona para la primera regla", personas)

    if num_reglas == 2:
        regla_2 = st.selectbox("Seleccione la segunda regla", ["", "No se sienta al inicio", "No se sienta en el medio", "No se sienta al final"])
        if regla_2 == "No se sienta al inicio" and not regla_inicio:
            regla_inicio = st.selectbox("Persona para la segunda regla", personas, key="regla_2_inicio")
        elif regla_2 == "No se sienta en el medio" and not regla_medio:
            regla_medio = st.selectbox("Persona para la segunda regla", personas, key="regla_2_medio")
        elif regla_2 == "No se sienta al final" and not regla_final:
            regla_final = st.selectbox("Persona para la segunda regla", personas, key="regla_2_final")

    if st.button("Generar Soluciones"):
        if regla_inicio or regla_medio or regla_final:
            nodo_inicial = []
            soluciones = backtracking(nodo_inicial, personas, regla_inicio, regla_medio, regla_final)
            
            st.header("Soluciones")
            if soluciones:
                for solucion in soluciones:
                    st.write(solucion)
            else:
                st.write("No hay soluciones posibles con las reglas seleccionadas.")
        else:
            st.warning("Seleccione al menos una regla para generar soluciones.")