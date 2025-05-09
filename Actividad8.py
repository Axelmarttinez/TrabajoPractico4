#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad_numeros):
    try:
        numero = int(input(f"Ingrese el número {i+1}/{cantidad_numeros}: "))
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entero.")
        i -= 1
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

