# Ejercicio: Crear una clase de Estudiante
# Crea una clase llamada Estudiante que tenga los siguientes atributos y métodos:

# Atributos:

# nombre - Nombre del estudiante
# edad - Edad del estudiante
# curso - Curso en el que está inscrito el estudiante
# Métodos:

# presentarse() - Método que imprime un mensaje con el nombre y la edad del estudiante.
# cambiar_curso(nuevo_curso) - Método que cambia el curso del estudiante al curso especificado.
# Luego, instancia un objeto de la clase Estudiante, configura sus atributos y llama a los métodos para probar su funcionamiento. ¡Buena suerte!

class Estudiante():
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre 
        self.edad = edad
        self.curso = curso
    
    def presentarse(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad}")

    def cambiarCurso(self):
        nuevoCurso = input("Ingrese el curso al que desea cambiarse: ")
        self.curso = nuevoCurso
        print(f"El estudiante ahora se encuentra en el curso: {self.curso}")
     

estudiante1 = Estudiante("Franco", 21, "1TUP7")

estudiante1.presentarse()
estudiante1.cambiarCurso()