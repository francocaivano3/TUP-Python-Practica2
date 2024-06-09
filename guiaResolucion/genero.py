class Genero():
    def __init__(self, nombre:str):
        self.__nombre = nombre
    
    def __str__(self):
        return f'El género es: {self.__nombre}'

