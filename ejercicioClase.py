#Ejercicio de bucle for y lista:
#Escribe un programa que tome una lista de números y calcule la suma de todos los elementos.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = 0

for i in range(len(lista)):
    resultado += lista[i]

print(resultado)