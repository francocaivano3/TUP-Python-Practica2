from abc import ABC, abstractmethod
from datetime import date
from tipo_documento import TipoDocumento

class Persona(ABC): 
    @abstractmethod
    def __init__(self, nombre:str, apellido:str, fechaNacimiento:date, edad:int, nroDocumento:int, tipoDocumento:tipoDocumento) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._fechaNacimiento = fechaNacimiento
        self._nroDocumento = nroDocumento
        self._tipoDocumento = tipoDocumento

    def getEdad(self) -> int:
        return date.today().year - self._fechaNacimiento().year
    
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, newNombre:str):
        self._nombre = newNombre
    
    def getApellido(self) -> str:
        return self._apellido

    def setApellido(self, newApellido:str):
        self._apellido = newApellido
    
    def getFechaNacimiento(self) -> date:
        return self._fechaNacimiento

    def setFechaNacimiento(self, newFechaNacimiento:date):
        self._fechaNacimiento = newFechaNacimiento
    
    def getNroDocumento(self) -> int:
        return self._nroDocumento
    
    def setNroDocumento(self, newNroDocumento: )
