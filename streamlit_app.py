# 0. TITULO Y DESCRIPCION DEL PROYECTO
st.title('Análisis de casos positivos registrados en Perú')
st.markdown("""
---
### 1. Descripción del proyecto
El proyecto consiste en análisis exploratorio de un dataset que registra información
de los casos positivos detectados en Perú durante el mes de mayo del año 2022.

Fuente de datos: [https://ejemplo.com/](https://ejemplo.com/)

### 2. Origen de los datos
El conjunto de dato se obtuvo del portal de datos abiertos del MINSA.
| Variable        |	Descripción                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------- |
| FECHA_CORTE     |	Fecha de corte de información                                                                       |
| UUID            |	ID de la persona como caso positivo de covid-19 confirmada con cualquier tipo de prueba.            |
| UBIGEO          |	Código de Ubicación Geografica que denotan "DDppdd" (Departamento, provincia,distrito), fuente INEI |
| DEPARTAMENTO    |	Departamento donde reside la persona confirmada como caso positivo de covid-19                      |
| PROVINCIA       |	Provincia donde reside la persona confirmada como caso positivo de covid-19                         |
| DISTRITO        |	Distrito donde reside la persona confirmada como caso positivo de covid-19                          |
| METODODX        |	Metodo de laboratorio a la que es sometida una prueba de covid-19                                   |
| EDAD            |	Edad de la persona confirmada como caso positivo de covid-19                                        |
| SEXO            |	Sexo de la persona confirmada como caso positivo de covid-19                                        |
| FECHA_RESULTADO |	Fecha del resultado de la prueba de covid-19                                                        |

&nbsp;
### 3. Herramientas utilizadas
A continuación se listan los paqueyes de Python utilizaron durant el desarrollo del proyecto.
```
gdown==4.4.0
numpy==1.22.4
pandas==1.4.2
pyecharts==1.9.1
streamlit==1.10.0
streamlit_echarts==0.4.0
```
