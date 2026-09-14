import streamlit as st

# Configuración visual de la página web (Estilo laboratorio)
st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides Extendido")
st.write("Calcula el Máximo Común Divisor (MCD) y encuentra su combinación lineal (Identidad de Bézout).")

# --- NÚCLEO MATEMÁTICO TRADUCIDO EXACTAMENTE DE TU PYGAME ---
def calcular_euclides_extendido_completo(dividendo_orig, divisor_orig):
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
            
            # Si el MCD se encontró en el primer paso, la combinación es directa
            if len(historial_divisiones) == 1:
                bitacora.append("### ⬅️ Fase de Combinación Lineal")
                bitacora.append(rf"$$\,{mcd} = {dividendo_orig}(0) + {divisor_orig}(1)\,$$")
                return bitacora
            break
        else:
            a = b
            paso_actual += 1

    # --- FASE 3: SUSTITUCIÓN HACIA ATRÁS (COMBINACIÓN LINEAL) ---
    bitacora.append("### ⬅️ Fase de Combinación Lineal (Identidad de Bézout)")
    bitacora.append("**--- Despejes y Sustitución hacia atrás ---**")
    
    # Quitamos la última división (la que dio residuo 0) ya que no sirve para despejar
    if historial_divisiones[-1][3] == 0:
        historial_divisiones.pop()
        
    # Comenzamos desde el último residuo no nulo (el MCD)
    a_act, b_act, q_act, r_act = historial_divisiones.pop()
    mcd = r_act
    
    bitacora.append(f"Despejamos el MCD ({mcd}) de la última ecuación útil:")
    bitacora.append(f"$$\,{mcd} = {a_act} - {b_act}({q_act})\,$$")
    
    # Coeficientes iniciales de la combinación lineal: mcd = a_act * x + b_act * y
    x, y = 1, -q_act
    
    # Vamos sustituyendo hacia arriba usando las ecuaciones previas guardadas
    while historial_divisiones:
        a_prev, b_prev, q_prev, r_prev = historial_divisiones.pop()
        
        # En la expresión actual 'x*dividendo + y*divisor', el 'divisor' actual (b_act) 
        # es el residuo (r_prev) de la ecuación de arriba. Lo sustituimos.
        bitacora.append(f"Sustituimos el residuo **{b_act}** = {a_prev} - {b_prev}({q_prev}):")
        
        # Mostramos el paso intermedio algebraico para el estudiante
        bitacora.append(rf"$$\,{mcd} = {x}({a_act}) + {y}({a_prev} - {b_prev}({q_prev}))\,$$")
        
        # Al distribuir, el nuevo 'a_act' se convierte en el 'a_prev'
        # Los nuevos coeficientes se recalculan exactamente como en tu Pygame:
        nuevo_x = y
        nuevo_y = x + y * (-q_prev)
        
        a_act = a_prev
        b_act = b_prev
        x = nuevo_x
        y = nuevo_y
        
        bitacora.append(rf"$$\,{mcd} = {x}({a_act}) + ({y})({b_act})\,$$")
        
    bitacora.append("🎉 **Resultado Final:**")
    bitacora.append(rf"🏆 $$\,{mcd} = {dividendo_orig}({x}) + {divisor_orig}({y})\,$$")
    return bitacora

# --- INTERFAZ DE USUARIO EN STREAMLIT ---
st.sidebar.markdown("## Parámetros de entrada")
num1 = st.sidebar.number_input("Introduce el primer número (Dividendo):", min_value=1, value=48, step=1)
num2 = st.sidebar.number_input("Introduce el segundo número (Divisor):", min_value=1, value=18, step=1)

if st.sidebar.button("Calcular Euclides Extendido"):
    # Validación: Dividendo debe ser estrictamente mayor que el divisor
    if num1 <= num2:
        st.error("Error: El dividendo debe ser mayor que el divisor.")
    else:
        # Ejecutar el algoritmo y renderizar las líneas guardadas en la bitácora
        lineas_resultado = calcular_euclides_extendido_completo(num1, num2)
        for linea in lineas_resultado:
            st.markdown(linea)


