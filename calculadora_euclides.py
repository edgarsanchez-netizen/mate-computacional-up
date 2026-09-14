import streamlit as st

# 1. Configuración de página obligatoria (Debe ir al inicio)
st.set_page_config(
    page_title="Algoritmo de Euclides",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Título de la aplicación principal
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides Directo")
st.write("Calcula el Máximo Común Divisor (MCD) mediante divisiones sucesivas.")

# --- NÚCLEO MATEMÁTICO ---
def calcular_euclides_directo(dividendo, divisor):
    bitacora = []
    a = dividendo
    b = divisor
    paso = 1
    
    while b != 0:
        cociente = a // b
        residuo = a % b
        # Nota el uso de 'rf' para evitar errores de escape con '\,' en LaTeX
        bitacora.append(rf"**Paso {paso}:**  ➔ Operación:  $$\,{a} = ({b} \times {cociente}) + {residuo}\,$$")
        a = b
        b = residuo
        paso += 1
        
    mcd = a
    bitacora.append(f"🏆 **El Máximo Común Divisor (MCD) es: {mcd}**")
    return mcd, bitacora

# --- INTERFAZ DE USUARIO ---
st.sidebar.markdown("## Parámetros de entrada")
num1 = st.sidebar.number_input("Introduce el primer número (Dividendo):", min_value=1, value=48, step=1)
num2 = st.sidebar.number_input("Introduce el segundo número (Divisor):", min_value=1, value=18, step=1)

if st.sidebar.button("Calcular MCD"):
    mcd_resultado, logs_directo = calcular_euclides_directo(num1, num2)
    
    # Mostrar resultados en pantalla
    for linea in logs_directo:
        st.markdown(linea)

st.info("💡 Usa la barra lateral de la izquierda para alternar entre esta pantalla y el 'Calculador Euclides Extendido'.")




