from datetime import date

class Autor():
    def __init__(self, nombre:str, apellido:str, fechaNacimiento:date):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
    
    @property
    def nombre(self):
        print(self.__nombre)
    
    @property
    def apellido(self):
        print(self.__apellido)

    @property
    def fecha(self):
        print(self.__fechaNacimiento)

    def __str__(self):
        return f'Nombre del autor: {self.__nombre}\nApellido: {self.__apellido}\nFecha de nacimiento: {self.__fechaNacimiento}'

    

juan = Autor("Pedro", "Ruiz", "03/10/2002")
print(juan)