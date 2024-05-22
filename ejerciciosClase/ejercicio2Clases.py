from abc import ABC
class Persona(ABC):
    def __init__(self, nombre, apellido, fechaNacimiento, edad, nroDocumento):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.nroDocumento = nroDocumento
    
