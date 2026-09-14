import streamlit as st

# Configuración visual de la página web (Estilo laboratorio)
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides Extendido")
st.write("Calcula el Máximo Común Divisor (MCD) y encuentra su combinación lineal (Identidad de Bézout).")

# --- NÚCLEO MATEMÁTICO (Adaptado de tu lógica de Pygame) ---
def calcular_euclides_extendido_web(dividendo_orig, divisor_orig):
    bitacora = []
    historial_divisiones = []
    
    # --- FASE 2: ALGORITMO DE EUCLIDES DIRECTO ---
    bitacora.append("### ➡️ Fase Directa: Buscando el MCD")
    
    a = dividendo_orig
    b = divisor_orig
    paso_actual = 1
    
    while b != 0:
        cociente = a // b
        residuo = a % b
        
        # Guardamos el paso en el historial idéntico a tu lógica
        historial_divisiones.append((a, b, cociente, residuo))
        
        bitacora.append(f"**Paso {paso_actual}:** $${a} = {b}({cociente}) + {residuo}$$")
        
        if residuo == 0:
            mcd = b
            bitacora.append("➔ **¡Residuo 0 alcanzado!**")
            bitacora.append(f"🏆 **Máximo Común Divisor (MCD) es: {mcd}**")
            
            # Caso especial: se encontró en el primer paso
            if len(historial_divisiones) == 1:
                bitacora.append("### ⬅️ Fase de Combinación Lineal")
                bitacora.append(f"$$\,{mcd} = {dividendo_orig}(0) + {divisor_orig}(1)\,$$")
                return mcd, 0, 1, bitacora
        else:
            a = b
            b = residuo
            paso_actual += 1

    # --- FASE 3: SUSTITUCIÓN HACIA ATRÁS (COMBINACIÓN LINEAL) ---
    bitacora.append("### ⬅️ Fase de Sustitución Hacia Atrás")
    
    # Quitamos la última división (la que dio residuo 0)
    if historial_divisiones[-1][3] == 0:
        historial_divisiones.pop()
        
    # Comenzamos desde el último residuo no nulo (el MCD)
    a_act, b_act, q_act, r_act = historial_divisiones.pop()
    mcd = r_act
    
    bitacora.append(f"Despejamos el MCD ({mcd}) de la última ecuación útil:")
    bitacora.append(f"➔ $${mcd} = {a_act} - {b_act}({q_act})$$")
    
    # Coeficientes iniciales
    x, y = 1, -q_act
    
    # Vamos sustituyendo hacia arriba usando las ecuaciones previas guardadas
    while historial_divisiones:
        a_prev, b_prev, q_prev, r_prev = historial_divisiones.pop()
        
        bitacora.append(f"Sustituimos el residuo {b_act} por la expresión: $${b_act} = {a_prev} - {b_prev}({q_prev})$$")
        bitacora.append(f"➔ $${mcd} = {x}({a_act}) + {y}({a_prev} - {b_prev}({q_prev}))$$")
        
        # Redistribución de coeficientes (Tus fórmulas matemáticas exactas)
        nuevo_x = y
        nuevo_y = x + y * (-q_prev)
        
        a_act = a_prev
        b_act = b_prev
        x = nuevo_x
        y = nuevo_y
        
        bitacora.append(f"Reagrupando términos queda:")
        bitacora.append(f"➔ $${mcd} = {x}({a_act}) + ({y})({b_act})$$")
        bitacora.append("---")
        
    return mcd, x, y, bitacora

# --- INTERFAZ GRÁFICA EN STREAMLIT (Sustituye las entradas de Pygame) ---
st.sidebar.header("Parámetros de Entrada")
num1 = st.sidebar.number_input("Ingresa el Dividendo (Mayor):", min_value=1, value=240, step=1)
num2 = st.sidebar.number_input("Ingresa el Divisor (Menor):", min_value=1, value=46, step=1)

if st.sidebar.button("Ejecutar Algoritmo Extendido"):
    # Validación: Dividendo debe ser estrictamente mayor que el divisor
    if num1 <= num2:
        st.error("❌ Error: El dividendo debe ser mayor que el divisor. Modifica los parámetros en la barra lateral.")
    else:
        # Ejecutamos la función
        mcd_final, x_final, y_final, pasos_consola = calcular_euclides_extendido_web(num1, num2)
        
        # Cuadro destacado con el resultado final
        st.success("### 📊 RESULTADO FINAL")
        st.markdown(f"**MCD encontrado:** `{mcd_final}`")
        st.markdown(f"**Combinación Lineal (Identidad de Bézout):**")
        st.info(f"$${mcd_final} = {num1}({x_final}) + {num2}({y_final})$$")
        st.markdown(f"Donde los coeficientes son: **x = {x_final}** , **y = {y_final}**")
        
        # Desglose completo del procedimiento en un contenedor estético
        st.markdown("### 📋 Bitácora detallada del procedimiento:")
        with st.container(border=True):
            for elemento in pasos_consola:
                # Si el elemento tiene fórmulas matemáticas $$, Streamlit las renderiza hermoso
                st.write(elemento)
