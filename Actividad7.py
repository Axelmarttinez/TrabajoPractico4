#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#úmero entero positivo indicado por el usuario. 

numero=int(input("Ingreese un numero entero positivo: "))
suma=0
for i in range(numero+1):
    suma +=1
print(F"suma de los numeros desde 0 hasta {numero} es :{suma}")

    

