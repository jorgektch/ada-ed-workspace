import streamlit as st

def ejecutar_implementacion():
  st.subheader("Implementación")

  code = '''public boolean hasTwoTrueValues( boolean [ ] arr ){
	int count = 0;
	
	for( int i = 0; i < arr.length; i++ )
		if( arr[ i ] )
			count++;

	return count >= 2;
 }'''
  st.code(code, language='java')

