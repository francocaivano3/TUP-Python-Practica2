# 11. Escribe una función para contar vocales en una cadena

vocales = ["a", "e", "i", "o", "u"]

def contarVocales(cadena):
    contador = 0
    for letra in cadena.lower(): 
        if letra in vocales:
            contador += 1
    
    print(contador)

contarVocales("CARC CAMPEON")