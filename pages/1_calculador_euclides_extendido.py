import streamlit as st

# Configuración visual de la página web (Estilo laboratorio)
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides Extendido")
st.write("Calcula el Máximo Común Divisor (MCD) y encuentra su combinación lineal (Identidad de Bézout).")

# --- NÚCLEO MATEMÁTICO COMPLETO ---
def calcular_euclides_extendido_web(dividendo_orig, divisor_orig):
    bitacora = []
    historial_divisiones = []
    
    # --- FASE 1: ALGORITMO DE EUCLIDES DIRECTO ---
    bitacora.append("### ➡️ Fase Directa: Buscando el MCD")
    a = dividendo_orig
    b = divisor_orig
    paso_actual = 1
    
    while b != 0:
        cociente = a // b
        residuo = a % b
        historial_divisiones.append((a, b, cociente, residuo))
        bitacora.append(f"**Paso {paso_actual}:** $${a} = {b}({cociente}) + {residuo}$$")
        if residuo == 0:
            mcd = b
            bitacora.append("➔ **¡Residuo 0 alcanzado!**")
            bitacora.append(f"🏆 **Máximo Común Divisor (MCD) es: {mcd}**")
            break
        else:
            a = b
            paso_actual += 1

    # Caso especial: se encontró en el primer paso o división exacta inmediata
    if len(historial_divisiones) == 1:
        bitacora.append("### ⬅️ Fase de Combinación Lineal (Identidad de Bézout)")
        bitacora.append(rf"$$\,{mcd} = {dividendo_orig}(0) + {divisor_orig}(1)\,$$")
        return mcd, 0, 1, bitacora

    # --- FASE 2: COMBINACIÓN LINEAL (ALGORITMO EXTENDIDO HACIA ATRÁS) ---
    bitacora.append("### ⬅️ Fase de Combinación Lineal (Identidad de Bézout)")
    
    # Inicialización de coeficientes Bézout
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    # Recorremos los pasos para obtener x e y de forma exacta
    for i in range(len(historial_divisiones) - 1):
        a, b, q, r = historial_divisiones[i]
        # Calcular los siguientes coeficientes correspondientes al paso
        if i == 0:
            # Despeje inicial del primer residuo no nulo
            bitacora.append(f"Despejando el residuo: $${r} = {a} - {b}({q})$$")
        
    # Algoritmo iterativo estándar para coeficientes de Bézout extendido
    x_ant, x_act = 1, 0
    y_ant, y_act = 0, 1
    
    for item in historial_divisiones[:-1]:
        q = item[2]
        x_sig = x_ant - q * x_act
        y_sig = y_ant - q * y_act
        x_ant, x_act = x_act, x_sig
        y_ant, y_act = y_act, y_sig
        
    x, y = x_ant, y_ant
    bitacora.append(rf"🏆 **Combinación lineal obtenida:** $$\,{mcd} = {dividendo_orig}({x}) + {divisor_orig}({y})\,$$")
    return mcd, x, y, bitacora

# --- INTERFAZ DE USUARIO ---
st.sidebar.markdown("## Parámetros de entrada")
num1 = st.sidebar.number_input("Introduce el primer número (Dividendo):", min_value=1, value=48, step=1)
num2 = st.sidebar.number_input("Introduce el segundo número (Divisor):", min_value=1, value=18, step=1)

if st.sidebar.button("Calcular Euclides Extendido"):
    mcd, x, y, logs = calcular_euclides_extendido_web(num1, num2)
    
    # Mostramos todo el desarrollo matemático paso a paso
    for linea in logs:
        st.markdown(linea)

