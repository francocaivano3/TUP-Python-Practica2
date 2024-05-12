
# ¡Claro! Aquí tienes otro ejercicio para practicar:

# Ejercicio: Crear una clase de Empleado
# Crea una clase llamada Empleado que tenga los siguientes atributos y métodos:

# Atributos:

# nombre - Nombre del empleado
# edad - Edad del empleado
# cargo - Cargo que ocupa el empleado en la empresa
# salario - Salario del empleado
# Métodos:

# informacion() - Método que imprime un resumen de la información del empleado, incluyendo nombre, edad, cargo y salario.
# aumentar_salario(porcentaje) - Método que aumenta el salario del empleado en un porcentaje especificado.
# Luego, instancia un objeto de la clase Empleado, configura sus atributos y llama a los métodos para probar su funcionamiento. ¡Buena suerte!

class Empleado():
    def __init__(self, nombre, edad, cargo, salario):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    def informacion(self):
        print(f"Nombre: {self.nombre} \n Edad: {self.edad} \n Cargo: {self.cargo} \n Salario: {self.salario}")
    
    def aumentarSalario(self, porcentaje):
        self.salario = self.salario + (self.salario * porcentaje) / 100
    
empleado1 = Empleado("Franco Caivano", 21, "Backend Developer", 1000000)

empleado1.informacion()
empleado1.aumentarSalario(10)
empleado1.informacion()

