import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi primera aplicación de Streamlit", page_icon="👑")

# -------- ÁREA PRINCIPAL --------
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.write("Esta es una aplicación simple")
st.image("logo_uss.png", width=300)

if st.button("Haz clic"):
    st.success("¡Hiciste clic en el botón!")

mensaje = st.text_input("Escribe algo:")
st.write("Escribiste:", mensaje)

# -------- BARRA LATERAL --------
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra lateral!")
st.sidebar.write("Esta es una barra lateral")
st.sidebar.image("logo_uss.png", width=220)

if st.sidebar.button("Haz clic para la barra lateral"):
    st.sidebar.success("¡Hiciste clic en el botón de la barra lateral!")

mensaje_lateral = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write("Escribiste en la barra:", mensaje_lateral)
