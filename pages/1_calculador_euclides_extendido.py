import streamlit as st

# Configuración visual de la página web (Estilo laboratorio)
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides Extendido")
st.write("Calcula el Máximo Común Divisor (MCD) y encuentra su combinación lineal (Identidad de Bézout).")

# --- NÚCLEO MATEMÁTICO CORREGIDO ---
def calcular_euclides_extendido_completo(dividendo_orig, divisor_orig):
    bitacora = []
    historial_divisiones = []
    
    # --- FASE 1: ALGORITMO DE EUCLIDES DIRECTO (CORREGIDO) ---
    bitacora.append("### ➡️ Fase Directa: Buscando el MCD")
    a = dividendo_orig
    b = divisor_orig
    paso_actual = 1
    
    while b != 0:
        cociente = a // b
        residuo = a % b
        
        # Guardamos la división real antes de avanzar variables
        historial_divisiones.append((a, b, cociente, residuo))
        bitacora.append(f"**Paso {paso_actual}:** $${a} = {b}({cociente}) + {residuo}$$")
        
        # AVANCE CORRECTO DE VARIABLES
        a = b
        b = residuo
        paso_actual += 1

    # El MCD real es el último residuo no nulo (que quedó guardado en 'a')
    mcd = a
    bitacora.append("➔ **¡Residuo 0 alcanzado!**")
    bitacora.append(f"🏆 **Máximo Común Divisor (MCD) es: {mcd}**")
            
    # Si el MCD se encontró en el primer paso (división exacta inmediata)
    if len(historial_divisiones) == 1:
        bitacora.append("### ⬅️ Fase de Combinación Lineal")
        bitacora.append(rf"$$\,{mcd} = {dividendo_orig}(1) + {divisor_orig}(0)\,$$")
        return bitacora

    # --- FASE 2: SUSTITUCIÓN HACIA ATRÁS (COMBINACIÓN LINEAL) ---
    bitacora.append("### ⬅️ Fase de Combinación Lineal (Identidad de Bézout)")
    bitacora.append("**--- Despejes y Sustitución hacia atrás ---**")
    
    # Quitamos la última división (la que dio residuo 0) ya que no se despeja
    if historial_divisiones[-1][3] == 0:
        historial_divisiones.pop()
        
    # Comenzamos desde la última ecuación útil (donde el residuo es el MCD)
    a_act, b_act, q_act, r_act = historial_divisiones.pop()
    
    bitacora.append(f"Despejamos el MCD ({mcd}) de la última ecuación útil:")
    bitacora.append(f"$$\,{mcd} = {a_act} - {b_act}({q_act})\,$$")
    
    # Coeficientes iniciales de la combinación lineal: mcd = a_act * x + b_act * y
    x, y = 1, -q_act
    
    # Inicializamos el divisor actual para el rastreo del texto
    b_actual_texto = b_act
    
    # Sustitución hacia arriba
    while historial_divisiones:
        a_prev, b_prev, q_prev, r_prev = historial_divisiones.pop()
        
        bitacora.append(f"Sustituimos el residuo **{b_actual_texto}** = {a_prev} - {b_prev}({q_prev}):")
        bitacora.append(rf"$$\,{mcd} = {x}({a_act}) + {y}({a_prev} - {b_prev}({q_prev}))\,$$")
        
        # Fórmulas algebraicas de tus coeficientes
        nuevo_x = y
        nuevo_y = x + y * (-q_prev)
        
        # Actualizamos variables para el siguiente ciclo
        a_act = a_prev
        b_act = b_prev
        b_actual_texto = b_prev
        x = nuevo_x
        y = nuevo_y
        
        bitacora.append(rf"$$\,{mcd} = {x}({a_act}) + ({y})({b_act})\,$$")
        
    bitacora.append("🎉 **Resultado Final:**")
    bitacora.append(rf"🏆 $$\,{mcd} = {dividendo_orig}({x}) + {divisor_orig}({y})\,$$")
    return bitacora

# --- INTERFAZ DE USUARIO EN STREAMLIT ---
st.sidebar.markdown("## Parámetros de entrada")
num1 = st.sidebar.number_input("Introduce el primer número (Dividendo):", min_value=1, value=53, step=1)
num2 = st.sidebar.number_input("Introduce el segundo número (Divisor):", min_value=1, value=15, step=1)

if st.sidebar.button("Calcular Euclides Extendido"):
    if num1 <= num2:
        st.error("Error: El dividendo debe ser mayor que el divisor.")
    else:
        lineas_resultado = calcular_euclides_extendido_completo(num1, num2)
        for linea in lineas_resultado:
            st.markdown(linea)



