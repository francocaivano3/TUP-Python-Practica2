# 5. Escribe un programa que tome dos tuplas e imprima un diccionario donde las primeras
# tuplas sean las claves y las segundas tuplas sean los valores correspondientes.

tuplaNombre = ("Nombre")
tuplaValor = ("Franco")

def tupla(tuplaClave, tuplaValor):
    diccionario = {tuplaClave: tuplaValor}
    print(diccionario)

tupla(tuplaNombre, tuplaValor)