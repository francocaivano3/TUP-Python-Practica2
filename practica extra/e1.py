# #1. Escribe un programa que pida al usuario ingresar su edad y luego imprima un mensaje
# indicando si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))

result = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(result)