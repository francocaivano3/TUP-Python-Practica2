from datetime import date

class Usuario:
    def __init__(self, userName:str, nombre:str, apellido:str, password:str) -> None:
        self.__userName:str = userName
        self.__estado