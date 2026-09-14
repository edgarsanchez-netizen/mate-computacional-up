import streamlit as st

# 1. SIEMPRE LA CONFIGURACIÓN PRIMERO
st.set_page_config(
    page_title="Caja de Herramientas UP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SECCIÓN DE BIENVENIDA (El código nuevo, adaptado)
st.title("🧮 Caja de Herramientas de Matemática Computacional - UP")
st.write("Bienvenido al laboratorio. Selecciona una herramienta en el menú de la izquierda o usa el módulo directo aquí abajo:"

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




