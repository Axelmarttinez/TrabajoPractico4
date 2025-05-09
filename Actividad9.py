cantidad_numeros = 100
suma = 0
for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i + 1}/{cantidad_numeros}: "))
            suma += numero
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
media = suma / cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números es: {media}")