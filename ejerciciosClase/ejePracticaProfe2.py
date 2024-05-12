# Ejercicio 2: Evaluación de Clientes en una Tienda

# Para cada cliente de una tienda, es necesario evaluar su historial de compras y determinar si cumple con ciertos criterios de fidelidad establecidos por el negocio. Un cliente con al menos 5 compras realizadas en los últimos 3 meses cumple con los estándares propuestos por la tienda.

# Se desconoce la cantidad de clientes a evaluar. De cada cliente se conoce: nombre, número de cliente y detalle de compras realizadas.

# Mostrar un menú principal con las siguientes opciones:

# Registrar Cliente:
# Se registra a un cliente con los siguientes datos: nombre y número de cliente. Se debe validar que el número de cliente no esté duplicado en la lista de clientes registrados.
# Agregar Compra:
# Se ingresa el número de cliente y se lo busca. En caso de que el número de cliente no sea encontrado, se muestra un mensaje aclaratorio. Si el cliente es encontrado, se solicita ingresar los detalles de una nueva compra para agregar a su historial de compras.
# Mostrar Resumen:
# Se muestra un resumen que lista a los clientes evaluados, ordenados de mayor a menor por cantidad de compras realizadas en los últimos 3 meses. El resumen incluye el nombre del cliente, su número de cliente, sus detalles de compras y la cantidad de compras realizadas en los últimos 3 meses. Se indica también si el cliente cumple o no con los estándares de fidelidad de la tienda.
# Salir.
# Consideraciones:

# Cada cliente registrado es un diccionario que se agrega a la lista de clientes.
# Codificar la función validar_fidelidad(cliente: dict) -> bool en un módulo aparte. 

from ejerciciosPropios.ejerciciosClase.cumpleEstandar import cumpleEstandar 

listaClientes = []

def registrarCliente():
    duplicado = True
    nombre = input("Ingrese el nombre del cliente: ")
    numCliente = input("Ingrese el número de cliente: ")
    

    for elemento in listaClientes:
        if elemento["numCliente"] == numCliente:
            print("El número de cliente ya está registrado")
            break
        else:
            print("paso por aca")
            duplicado = False
    
    if len(listaClientes) == 0: 
        cliente = {"nombre": nombre, "numCliente": numCliente, "historialCompras": []}
        listaClientes.append(cliente)

    if duplicado == False:
        cliente = {"nombre": nombre, "numCliente": numCliente, "historialCompras": []}
        listaClientes.append(cliente)
        print(listaClientes) 


def agregarCompra():
    numClienteCompra = input("Ingrese el número de cliente: ")
    encontrado = False
    for cliente in listaClientes:
        if numClienteCompra == cliente["numCliente"]:
            compra = input("Ingrese el producto comprado: ")
            cliente["historialCompras"].append(compra)
            encontrado = True
            break
    
    if not encontrado:
        print("No se ha encontrado al cliente") 
            
            
def mostrarResumen():
    listaOrdenada = sorted(listaClientes, key=lambda x: len(x["historialCompras"]), reverse=True)

    for cliente in listaOrdenada:
        cumple = "Si" if cumpleEstandar(cliente) == True else "No"
        print(f"Nombre: {cliente['nombre']} - Nro cliente: {cliente['numCliente']} \n Detalle de compras:\n")
        for compra in cliente["historialCompras"]:
            print(compra)
        print(f"Cantidad de compras realizadas: {len(cliente['historialCompras'])} \n Cumple con el estándar: {cumple}")
        

while True:
    print("1. Registrar cliente")
    print("2. Agregar compra")
    print("3. Mostrar resumen")
    print("4. Salir")
    opt = input("Ingrese una opción: ")

    if opt == "1":
        registrarCliente()
    elif opt == "2":
        agregarCompra()
    elif opt == "3":
        mostrarResumen()
    elif opt == "4":
        print("Gracias por utilizar nuestro sistema de Franco²")
        break
    else: 
        print("Opción no válida")