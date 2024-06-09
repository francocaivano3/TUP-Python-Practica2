from guiaResolucion.libro import Libro

class ListaLectura():
    codigos = []

    def __init__(self, codigo:int, nombre:str) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__libros = [nombre]
        


    def __str__(self) -> str:
        return f'Nombre del libro: {self.__nombre}\nCódigo del libro: {self.__codigo}'

    @property 
    def codigo(self):
        return self.__codigo

    @property
    def libro(self):
        return self.__libros

    @libro.setter
    def libro(self, libro:Libro):
        self.__libros.append(libro)
        print(self.__libros)
    
    @libro.setter
    def quitarLibro(self, libro:Libro):
        self.__libros.remove(libro)
        print(self.__libros)
    
    @property
    def cantLibros(self):
        print(len(self.__libros))

hola = ListaLectura(1234, 'theoutsider')
hola.libro = 'La peste'
hola.cantLibros