# 8. Escribe una función llamada contador_letras que tome una cadena como argumento y
# devuelva un diccionario donde las claves sean las letras de la cadena y los valores sean
# la cantidad de veces que aparece cada letra.

def contadorLetras(cadena):
    diccionario = {}

    for letra in cadena:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    
    print(diccionario)

contadorLetras("CARC CAMPEÓN")