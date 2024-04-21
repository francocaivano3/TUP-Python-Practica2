# 6. Escribe un programa que itere sobre un diccionario e imprima solo las claves que sean
# strings

diccionario = {"nombre": "Franco", 21: "Veintiuno", "materia favorita": "Programación", 3: "Tres"}

for clave in diccionario:
    if isinstance(clave, str):
        print(clave)