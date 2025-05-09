
inicio=int(input("Introduce el primer número entero: "))
fin=int(input("Introduce el segundo número entero: "))
menor=min(inicio, fin)
mayor=max(inicio, fin)
suma=0
for i in range(menor + 1, mayor):
    suma+=i
print("La suma de los números entre", menor, "y", mayor, "es:", suma)