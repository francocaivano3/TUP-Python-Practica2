def validarNumeroDocumento(medicos: list, nroDocumento:str) -> bool:
    existente = False

    for i in medicos:
        if i["nroDocumento"] == nroDocumento:
            existente = True
            break

    return existente
            