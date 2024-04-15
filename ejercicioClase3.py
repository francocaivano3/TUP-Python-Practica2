# Supongamos que tenemos una lista de números y queremos filtrar solo los números pares.
# Supongamos que queremos calcular el cuadrado de cada número en una lista.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaPares = []
listaCuadrado = []

def numerosPares(lista):
    for i in listaNumeros:
        if i % 2 == 0:
            listaPares.append(i)
    
    print(listaPares)

numerosPares(listaNumeros)
################################################
def cuadrado(lista):
    for i in listaNumeros:
        listaCuadrado.append(i ** 2)

    print(listaCuadrado)
    
cuadrado(listaNumeros)


# # Solicitar al usuario que ingrese los elementos de la lista separados por espacios
# entrada = input("Ingrese los elementos de la lista separados por espacios: ")

# # Dividir la entrada en una lista de cadenas
# elementos = entrada.split()

# # Convertir cada cadena en un entero
# lista = [int(elemento) for elemento in elementos]

# print("La lista ingresada es:", lista)

# ## Supongamos que queremos calcular el cuadrado de cada número en una list

lista = [1,2,3,4,5,6,7,8,9]
def cuadrado(elemento):
    return elemento ** 2

cuadrados = list(map(cuadrado, lista))
print(cuadrados)