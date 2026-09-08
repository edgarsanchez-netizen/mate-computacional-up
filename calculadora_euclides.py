def calculadora_euclides_paso_a_paso(a, b):
    print(f"\n--- INICIANDO EL ALGORITMO DE EUCLIDES ENTRE {a} Y {b} ---")
    
    # Asegurar que 'a' sea el mayor para empezar ordenados
    if b > a:
        print(f"Nota: Como {b} es mayor que {a}, los intercambiamos para empezar.")
        a, b = b, a
    
    paso = 1
    
    # El algoritmo corre mientras el divisor no sea 0
    while b != 0:
        cociente = a // b  # División entera (cuántas veces cabe b en a)
        residuo = a % b    # El resto de la división
        
        print(f"\n[Paso {paso}]:")
        print(f"  -> Dividimos {a} entre {b}")
        print(f"  -> Operación: {a} = ({b} * {cociente}) + {residuo}")
        print(f"  -> El cociente es {cociente} y el residuo es {residuo}")
        
        if residuo == 0:
            print(f"  -> ¡El residuo es 0! Hemos terminado.")
            mcd = b
        else:
            print(f"  -> Como el residuo no es 0, el nuevo dividendo será {b} y el nuevo divisor será {residuo}")
        
        # Avanzamos al siguiente paso del algoritmo
        a = b
        b = residuo
        paso += 1
        
    return mcd

# Solicitar datos al usuario
try:
    num1 = int(input("Ingresa el primer número entero positivo: "))
    num2 = int(input("Ingresa el segundo número entero positivo: "))

    if num1 <= 0 or num2 <= 0:
        print("Por favor, ingresa números mayores a cero.")
    else:
        resultado_mcd = calculadora_euclides_paso_a_paso(num1, num2)
        print(f"\n=========================================")
        print(f"RESULTADO FINAL: El MCD es {resultado_mcd}")
        print(f"=========================================")

except ValueError:
    print("Error: Debes ingresar únicamente números enteros.")


