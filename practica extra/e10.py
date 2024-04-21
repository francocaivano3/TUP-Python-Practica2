# 10. Escribe un programa que pida al usuario ingresar una lista de números y luego imprima
# el mayor de ellos utilizando una función llamada encontrar_mayor.
lista = input("Ingrese números separados por espacios: ")
listaSeparada = [int(numero) for numero in lista.split()]

def encontrarMayor(listaDeNumeros):
    print(max(listaDeNumeros))

encontrarMayor(listaSeparada)