from genero import Genero
from autor import Autor
from datetime import date 

class Libro():
    def __init__(self, nombre:str, fechaPublicacion:date, autor: Autor = 'Unknown') -> None:
        self.__nombre = nombre
        self.__fechaPublicacion = fechaPublicacion
        self.__autor = autor
        self.__generosLibro = []


    def __str__(self) -> str:
        return f'Nombre del libro: {self.__nombre}\nFecha publicación: {self.__fechaPublicacion}'

    @property
    def generos(self):
        return self.__generosLibro 

    @generos.setter
    def generos(self, genero: Genero):
        self.__generosLibro.append(genero)
        print(f'Libro: {self.__nombre}\nFecha de publicación: {self.__fechaPublicacion}\nGénero: {genero}')
        print(f'Este es el array: {self.__generosLibro}')

    @generos.setter
    def generoEliminado(self, genero: Genero):
        self.__generosLibro.remove(genero)
        print (self.__generosLibro)
    

extranjero = Libro('the outsider', '10/06/1940')

