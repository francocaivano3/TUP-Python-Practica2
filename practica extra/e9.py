# 9. Escribe una función llamada eliminar_duplicados que tome una lista como argumento y
# devuelva una nueva lista con los elementos únicos de la lista original, manteniendo el
# orden.

def eliminarDuplicados(lista):
    listaUnica = []

    for elemento in lista:
        if elemento not in listaUnica:
            listaUnica.append(elemento)
    
    print(listaUnica)


lista = [1, 1, 2, 2, 3, 3, 4, 4]
eliminarDuplicados(lista)
