# ¡Por supuesto! Aquí tienes otro ejercicio:

# Ejercicio: Crear una clase de Coche
# Crea una clase llamada Coche que tenga los siguientes atributos y métodos:

# Atributos:

# marca - Marca del coche
# modelo - Modelo del coche
# color - Color del coche
# velocidad - Velocidad actual del coche (en km/h)
# encendido - Estado del motor del coche (True si está encendido, False si está apagado)
# Métodos:

# informacion() - Método que imprime un resumen de la información del coche, incluyendo marca, modelo, color, velocidad y estado del motor.
# encender() - Método que enciende el motor del coche.
# apagar() - Método que apaga el motor del coche.
# acelerar(velocidad) - Método que recibe una velocidad como parámetro y aumenta la velocidad del coche en esa cantidad.
# frenar(velocidad) - Método que recibe una velocidad como parámetro y reduce la velocidad del coche en esa cantidad.
# Luego, instancia un objeto de la clase Coche, configura sus atributos y llama a los métodos para probar su funcionamiento. ¡Buena suerte!

class Coche():
    def __init__(self, marca, modelo, color, velocidad, encendido):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.encendido = encendido
    
    def informacion(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nVelocidad: {self.velocidad}\nEstado: {'Encendido' if self.encendido == True else 'Apagado'}")

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def acelerar(self, velocidad):
        self.velocidad += velocidad

    def frenar(self, velocidad):
        self.velocidad -= velocidad


coche1 = Coche("BMW", "ABC", "Negro", 120, False)

coche1.informacion()
coche1.encender()
coche1.informacion()
coche1.apagar()
coche1.informacion()
coche1.acelerar(10)
coche1.informacion()
coche1.frenar(20)
coche1.informacion()
