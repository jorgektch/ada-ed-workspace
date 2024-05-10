import streamlit as st

def ejecutar_implementacion1_0():
  st.subheader("Algoritmo versión 1")

  code = '''public boolean hasTwoTrueValues( boolean [ ] arr ){
	int count = 0;
	
	for( int i = 0; i < arr.length; i++ )
		if( arr[ i ] )
			count++;

	return count >= 2;
 }'''
  st.code(code, language='java')

def ejecutar_implementacion1_1():
  st.subheader("Algoritmo versión 2")

  code = '''public boolean hasTwoTrueValues( boolean [ ] arr ){
	for( int i = 0; i < arr.length; i++ )
		for( int j = i + 1; j < arr.length; j++ )
			if( arr[ i ] && arr[ j ] )
				return true;

	return false;
 }'''
  st.code(code, language='java')

def ejecutar_implementacion1_2():
  st.subheader("Algoritmo versión 3")

  code = '''public boolean hasTwoTrueValues( boolean [ ] arr ){
	for( int i = 0; i < arr.length; i++ )
  		if( arr[ i ])
		for( int j = i + 1; j < arr.length; j++ )
			if( arr[ j ] )
				return true;
	return false;
 }'''
  st.code(code, language='java')

def ejecutar_implementacion2():

  code = '''for( int i = 0; i < n; i++ )
	sum++;
 '''
  st.code(code, language='java')

def ejecutar_implementacion3():

  code = '''for( int i = 0; i < n; i+=2 )
	sum++;
 '''
  st.code(code, language='java')

def ejecutar_implementacion4():

  code = '''for( int i = 0; i < n; i++ )
	for( int j = 0; j < n; j++ )
		sum++;
 '''
  st.code(code, language='java')

def ejecutar_implementacion5():

  code = '''for( int i = 0; i < n; i++)
	sum++
for( int j = 0; j < n; j++)
	sum++

 '''
  st.code(code, language='java')
