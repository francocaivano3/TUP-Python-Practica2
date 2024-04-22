# Ejercicio 1: Evaluación de Estudiantes en una Escuela

# Para cada estudiante de una escuela, es necesario evaluar su desempeño académico y determinar si cumple con los estándares de rendimiento establecidos por la institución. Un estudiante con un promedio de calificaciones igual o superior a 7 cumple con los estándares propuestos por la escuela.

# Se conoce la cantidad de estudiantes a evaluar, los cuales son 60. De cada estudiante se conoce: nombre, número de identificación estudiantil y calificaciones obtenidas.

# Mostrar un menú principal con las siguientes opciones:
# [2:39 PM]
# Registrar Estudiantes:
# Se cargan todos los estudiantes de una vez. Para cada estudiante, se ingresan los siguientes datos: nombre, número de identificación estudiantil y calificaciones obtenidas en diferentes materias. Se debe validar que el número de identificación estudiantil tenga una longitud de 6 caracteres.
# Agregar Calificación:
# Se ingresa el número de identificación estudiantil del estudiante y se lo busca. En caso de que el número de identificación estudiantil no sea encontrado, se muestra un mensaje aclaratorio. Si el estudiante es encontrado, se solicita ingresar una nueva calificación para agregar a la lista de calificaciones del estudiante.
# Mostrar Resumen:
# Se muestra un resumen que lista a los estudiantes evaluados, ordenados de mayor a menor por promedio de calificaciones. El resumen incluye el nombre del estudiante, su número de identificación estudiantil, sus calificaciones obtenidas y su promedio de calificaciones. Se indica también si el estudiante cumple o no con los estándares de rendimiento de la escuela.
# Salir.
# Consideraciones:

# Cada estudiante registrado es un diccionario que se agrega a la lista de estudiantes.
# Codificar la función validar_promedio_calificaciones(calificaciones: list) -> bool en un módulo aparte.

from validarPromedioCalificaciones import validarPromedioCalificaciones

listaEstudiantes = []

def registrarEstudiantes():
    
    for i in range(2):
        calificaciones = []

        nombre = input("Ingrese el nombre y apellido del estudiante: ")
        numeroId = input("Ingrese el número de identificación del estudiante: ")
        while len(numeroId) != 6:
            print("Ingrese un número válido de ID")
            numeroId = input("Ingrese el número de identifiación del estudiante: ")
        for materia in range(5):
            calificacion = float(input(f"Ingrese la nota de la materia {materia + 1}: "))
            while calificacion < 0 or calificacion > 10:
                print("Nota inválida")
                calificacion = float(input(f"Ingrese la nota de la materia {materia + 1}: "))
            
            calificaciones.append(calificacion)

        estudiante = {"nombre": nombre, "numeroID": numeroId, "calificaciones": calificaciones}
       
            
        listaEstudiantes.append(estudiante)
        print(listaEstudiantes)

def agregarCalificacion():
    numeroId = input("Ingresa el número de identificación del estudiante: ")
    encontrado = False

    for estudiante in listaEstudiantes:
        if numeroId == estudiante["numeroID"]:
            nuevaNota = float(input("Ingrese la nota: "))
            estudiante["calificaciones"].append(nuevaNota)
            encontrado = True
            print("Nota agregada")
            break
    
    if encontrado == False:
        print("Número de identificación estudiantil no encontrado")
    

def mostrarResumen():
    estudiantesOrdenados = sorted(listaEstudiantes, key= lambda x: (sum(x['calificaciones'])) / len(x['calificaciones']), reverse=True)

    numeroNota = 1
    for estudiante in estudiantesOrdenados:
        print(f"{estudiante['nombre']} - Nro ID: {estudiante['numeroID']}")
        for calificacion in estudiante['calificaciones']:
            print(f"{numeroNota}. {calificacion}")
            numeroNota += 1
        numeroNota = 1
        print(f"El promedio de calificaciones es: {(sum(estudiante['calificaciones'])) / len(estudiante['calificaciones'])}")
        if validarPromedioCalificaciones(estudiante['calificaciones']):
            print("El estudiante cumple con los estándares de rendimiento de la escuela")
        else: 
            print("El estudiante no cumple con los estándares de la escuela")



while True:
    print("1. Registrar estudiantes")
    print("2. Agregar calificación")
    print("3. Mostrar resumen")
    print("4. Salir")
    opt = input("Ingrese una opción: ")

    if opt == "1":
        registrarEstudiantes()
    elif opt == "2":
        agregarCalificacion()
    elif opt == "3":
        mostrarResumen()
    elif opt == "4":
        print("Gracias por utilizar nuestro sistema!")
        break
