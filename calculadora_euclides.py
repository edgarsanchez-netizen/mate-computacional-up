import streamlit as st

# Configuración visual de la página web
st.set_page_config(page_title="Laboratorio UP", page_icon="🧮", layout="centered")

st.title("🧮 Laboratorio de Matemática Computacional - UP")
st.markdown("### Simulador interactivo: Algoritmo de Euclides")

# --- SU NÚCLEO MATEMÁTICO ADAPTADO PARA WEB ---
def calculadora_euclides_paso_a_paso(a, b):
    # En lugar de prints sueltos, guardamos los pasos en una lista para la web
    bitacora = []
    bitacora.append(f"**INICIANDO EL ALGORITMO DE EUCLIDES ENTRE {a} Y {b}**")
    
    if b > a:
        bitacora.append(f" *Nota: Como {b} es mayor que {a}, los intercambiamos para empezar.*")
        a, b = b, a
    
    paso = 1
    
    while b != 0:
        cociente = a // b  # Su misma división entera
        residuo = a % b    # Su mismo residuo
        
        # Guardamos sus mismos textos informativos paso a paso
        bitacora.append(f"**[Paso {paso}]:**")
        bitacora.append(f" ➔ Dividimos {a} entre {b}")
        bitacora.append(f" ➔ Operación:  $$\,{a} = ({b} \\times {cociente}) + {residuo}\,$$")
        bitacora.append(f" ➔ El cociente es **{cociente}** y el residuo es **{residuo}**")
        
        if residuo == 0:
            bitacora.append(f" ➔ ¡El residuo es 0! Hemos terminado.")
            mcd = b
        else:
            bitacora.append(f" ➔ Como el residuo no es 0, el nuevo dividendo será {b} y el nuevo divisor será {residuo}")
        
        a = b
        b = residuo
        paso += 1
        
    return mcd, bitacora  # Retornamos el MCD y toda la bitácora de pasos

# --- INTERFAZ GRÁFICA (Sustituye a sus inputs de consola) ---
st.sidebar.header("Parámetros de Entrada")
num1 = st.sidebar.number_input("Ingresa el primer número entero positivo:", min_value=1, value=240, step=1)
num2 = st.sidebar.number_input("Ingresa el segundo número entero positivo:", min_value=1, value=46, step=1)

if st.sidebar.button("Ejecutar Algoritmo"):
    # Llamamos a su función con los números que el alumno puso en la web
    resultado_mcd, pasos_calculados = calculadora_euclides_paso_a_paso(num1, num2)
    
    # Desplegamos el resultado final de forma elegante
    st.success(f"### RESULTADO FINAL: El MCD es {resultado_mcd}")
    
    # Mostramos el desglose paso a paso idéntico al de sus prints
    st.markdown("### 📋 Desglose del procedimiento paso a paso:")
    with st.container(border=True):
        for linea in pasos_calculados:
            st.write(linea)



