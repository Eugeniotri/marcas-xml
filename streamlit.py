import streamlit as st
st.set_page_config(page_title="Practica1", page_icon=":favicon_ico:", layout="wide")

# Example Streamlit app
st.title("Pagina de Prueba")
st.write("Esta es una pagina de prueba para Streamlit.")
st.write("Puedes agregar texto, imágenes, gráficos y más.")
st.header("Esto es un h2")
st.subheader("Esto es un h3")   
st.text("Esto es un texto sin formato.")
st.markdown("Esto es un texto en **negrita** y _cursiva_.") 
st.code("print('Hola, mundo!')", language='python')
st.image("https://via.placeholder.com/150", caption="Imagen de ejemplo")    
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", caption="Video de ejemplo")
st.write("Puedes agregar formularios y entradas de usuario.")   
st.text_input("Ingresa tu nombre:")
st.number_input("Ingresa un número:", min_value=0, max_value=100, value=50)
st.date_input("Selecciona una fecha:")
st.time_input("Selecciona una hora:")   
st.file_uploader("Sube un archivo:")
st.button("Haz clic aquí")  
if st.button("Haz clic aquí"):
    st.write("¡Botón clickeado!")   
st.text_area("Ingresa un texto largo:") 
st.selectbox("Selecciona una opción:", ["Opción 1", "Opción 2", "Opción 3"])
seleccion=st.selecbox("Selecciona una opción:", ["Opción 1", "Opción 2", "Opción 3"])
st.write(f"Has seleccionado: {seleccion}")
st.checkbox("Acepto los términos y condiciones")    
st.multiselect("Selecciona varias opciones:", ["Opción 1", "Opción 2", "Opción 3"])
st.slider("Selecciona un número:", 0, 100, 50)
col1, col2, col3 = st.columns(2)
with col1:
    st.write("Columna 1")
    st.button("Botón en columna 1") 
with col2:
    st.write("Columna 2")
    st.button("Botón en columna 2") 
st.write("Puedes agregar gráficos y visualizaciones.")

