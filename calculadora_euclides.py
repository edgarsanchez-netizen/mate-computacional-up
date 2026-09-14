import streamlit as st

# Configuración obligatoria al inicio para modo extendido y activar el menú lateral
st.set_page_config(
    page_title="Algoritmo de Euclides",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título de tu aplicación principal
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Bienvenido al Simulador del Algoritmo de Euclides")
st.write("Usa la barra lateral de la izquierda para navegar entre el cálculo directo y el extendido.")

# --- TU FUNCIÓN DEL ALGORITMO DIRECTO CORREGIDA ---
def calcular_euclides_directo(a, b):
    bitacora = []
    # Usamos 'rf' al inicio de la cadena para que no marque el error de escape con '\,'
    bitacora.append(rf" ➔ Operación:  $$\,{a} = ({b} \times {cociente}) + {residuo}\,$$")
    return bitacora

# --- INFORMACIÓN INICIAL ---
st.info("Selecciona '1 calculador euclides extendido' en el menú de la izquierda para usar la versión avanzada.")




