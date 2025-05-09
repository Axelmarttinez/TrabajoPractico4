import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1
while adivinanza != numero_secreto:
    try:
        adivinanza = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1
        if adivinanza < 0 or adivinanza > 9:
            print("Número fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
print(f"5Correcto, Adivinaste el número en {intentos} intento(s).")