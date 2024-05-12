
# ¡Claro! Aquí tienes otro ejercicio:

# Ejercicio: Crear una clase de Cuenta Bancaria
# Crea una clase llamada CuentaBancaria que tenga los siguientes atributos y métodos:

# Atributos:

# titular - Titular de la cuenta bancaria
# saldo - Saldo actual de la cuenta bancaria
# tipo - Tipo de cuenta bancaria (por ejemplo, "corriente", "ahorros", etc.)
# Métodos:

# mostrar_informacion() - Método que imprime un resumen de la información de la cuenta bancaria, incluyendo titular, saldo y tipo.
# depositar(monto) - Método que recibe un monto como parámetro y lo suma al saldo de la cuenta bancaria.
# retirar(monto) - Método que recibe un monto como parámetro y lo resta al saldo de la cuenta bancaria. Asegúrate de verificar si hay suficiente saldo antes de realizar el retiro.
# Luego, instancia un objeto de la clase CuentaBancaria, configura sus atributos y llama a los métodos para probar su funcionamiento. ¡Buena suerte!

class CuentaBancaria():
    def __init__(self, titular, saldo, tipo):
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo
    
    def mostrarInformacion(self):
        print(f"Titular: {self.titular}\nSaldo: {self.saldo}\nTipo: {self.tipo}")
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, retirar):
        self.saldo -= retirar
    

cliente1 = CuentaBancaria("Franco Caivano", 4000, "Ahorros")

cliente1.mostrarInformacion()
cliente1.depositar(1000)
cliente1.mostrarInformacion()
cliente1.retirar(1000)
cliente1.mostrarInformacion()