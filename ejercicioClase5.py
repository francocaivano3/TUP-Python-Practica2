# Crear una clase llamada "Producto" con los siguientes atributos:

# nombre (String): El nombre del producto.
# precio (Float): El precio del producto.
# stock (Int): La cantidad de unidades disponibles en el inventario.
# disponible (Booleano, por defecto True): Indica si el producto está disponible para la venta.
# La clase debe tener los siguientes métodos de instancia:

# Constructor: Para inicializar los atributos del producto.
# agregarStock: Para incrementar la cantidad de unidades disponibles en el inventario.
# vender: Para disminuir la cantidad de unidades disponibles al realizar una venta.
# tipoProducto: Para determinar si el producto es de tipo electrónico o de tipo alimenticio, considerando que si el nombre del producto contiene la palabra "electrónico" será considerado de tipo electrónico, de lo contrario será de tipo alimenticio.
# mostrarInfo: Para mostrar por pantalla todos los atributos del producto.
# El programa principal debe crear una instancia de la clase Producto, llamar a algunos métodos del producto y mostrar su información por pantalla.

from user import Vehiculo

# Crear un objeto de tipo Vehiculo
vehiculo1 = Vehiculo("Toyota", 4, "Rojo")

# Llamar a métodos de la clase Vehiculo
vehiculo1.arrancar()
print("Tipo de vehículo:", vehiculo1.tipoVehiculo())
vehiculo1.mostrar()

