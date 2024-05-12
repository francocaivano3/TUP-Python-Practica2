from ejerciciosClase.validarNumeroDocumento import validarNumeroDocumento

listaMedicos = []

def registrarMedico():
    nombre = input("Ingrese el nombre y apellido del médico: ")
    nroDocumento = input("Ingrese el número de documento: ")

    if validarNumeroDocumento(listaMedicos, nroDocumento) == False:
        medico = {"nombre": nombre, "nroDocumento": nroDocumento, "titulosRealizados": []}
        listaMedicos.append(medico)
    else:
        print("El número de documento ingresado ya está registrado.")


def agregarTitulo():
    documentoMedico = input("Ingrese el número de documento del médico: ")
    documentoEncontrado = False

    for i in listaMedicos:
        if i["nroDocumento"] == documentoMedico:
            tituloRealizado = input("Ingrese el nombre del título: ")
            i["titulosRealizados"].append(tituloRealizado)
            documentoEncontrado = True    
            break
    
    if documentoEncontrado == False:
        print("El número de documento no ha sido encontrado")


def mostrarResumen():
    resumen = sorted(listaMedicos, key= lambda x: len(x["titulosRealizados"]), reverse=True)
    elemento = 1
    contadorTitulos = 1
    for medico in resumen:
        print(elemento)
        print(f"{medico['nombre']} - Nro Doc: {medico['nroDocumento']}")
        print(f"Cantidad de titulos: {len(medico['titulosRealizados'])}")
        print("Titulos realizados:")
        if len(medico["titulosRealizados"]) > 0:
            for titulos in medico["titulosRealizados"]:
                print(f"{contadorTitulos}. {titulos}")
                contadorTitulos += 1
        print("")
        elemento += 1
        contadorTitulos = 1


while True:
    print("1. Registrar médico")
    print("2. Agregar título reconocido")
    print("3. Mostrar resumen")
    print("4. Salir")
    opt = input("Elija una opción: ")

    if opt == "1":
        registrarMedico()
    elif opt == "2":
        agregarTitulo()
    elif opt == "3":
        mostrarResumen()
    elif opt == "4":
        print("Gracias por utilizar nuestro sistema!")
        break
    else:
        print("Ha seleccionado una opción no válida.")

