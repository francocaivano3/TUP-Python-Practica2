# """Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como 
# responsabilidades la carga por teclado y su impresión.
# En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

# Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
# También en el bloque principal del programa crear un objeto de la clase Empleado."""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(f"Nombre: {self.nombre} \n apellido: {self.apellido}")
    
    def Empleado(Persona): 
        def __init__(self, sueldo):
            self.sueldo = sueldo

persona1 = 