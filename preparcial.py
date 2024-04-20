# Mostrar un menú principal con las opciones:
# 1. Registrar empleados
# Se cargarán todos los empleados de una vez. Para cada empleado, se cargan los
# siguientes datos: nombre, legajo y antigüedad en meses. Se debe validar que el legajo
# tenga 5 carácteres de longitud.
# 2. Agregar nuevo curso
# Se ingresa el legajo del empleado y se lo busca. En caso de que el legajo no sea
# encontrado mostrar un cartel aclaratorio. Si el empleado es encontrado se solicita se
# escriba el nombre del curso realizado para agregar en la lista del empleado
# cursos_realizados.
# 3. Mostrar resumen
# Se muestra un resumen cómo sigue, ordenado de mayor a menor por cantidad de
# cursos realizados.

listaEmpleados = []

def registrarEmpleados():
    for i in range(2):
        nombre = input("Cargue el nombre: ")
        while True:
            legajo = input("Cargue el legajo: ")
            if len(legajo) == 5:
                break

        antiguedad = input("Cargue la antiguedad en meses: ")
        empleado = {"nombre": nombre, "legajo": legajo, "antiguedad": antiguedad, "cursos": []}
        listaEmpleados.append(empleado)

def agregarCurso():
    legajoEmpleado = input("Ingrese el legajo del empleado: ")
    legajoEncontrado = False
    cursoRealizado = ""

    for diccionarioEmpleado in listaEmpleados:
        if diccionarioEmpleado["legajo"] == legajoEmpleado:
            cursoRealizado = input("Ingrese el nombre del curso realizado: ")
            diccionarioEmpleado["cursos"].append(cursoRealizado)
            legajoEncontrado = True
            break
        
    if not legajoEncontrado:
        print("El legajo no ha sido encontrado")
    

def validarEstandarConocimiento(cantidadCursos: int, antiguedad: int) -> bool:
    return True if antiguedad // 6 <= cantidadCursos else False 


def mostrarResumenEmpleados():
    resumen = sorted(listaEmpleados, key= lambda x: len(x["cursos"]), reverse=True)
    elemento = 1
    for empleado in resumen:
        print(elemento)
        print(f"{empleado['nombre']} - Legajo: {empleado['legajo']} - Antiguedad: {empleado['antiguedad']} meses")
        print(f"Cantidad de cursos:  {len(empleado['cursos'])}")
        if(validarEstandarConocimiento(len(empleado["cursos"]), int(empleado["antiguedad"]))):
            print("Cumple con el estándar")
        else:
            print("NO cumple con el estándar")

        elemento += 1

while True:
    print("1. Registrar empleados")
    print("2. Agregar nuevo curso")
    print("3. Mostrar resumen")
    print("4. Salir")
    opt = input("Elija una opción: ")

    if opt == "1":
        registrarEmpleados()
    elif opt == "2":
        agregarCurso()
    elif opt == "3":
        mostrarResumenEmpleados()
    elif opt == "4":
        print("Gracias por utilizar el programa")
        break