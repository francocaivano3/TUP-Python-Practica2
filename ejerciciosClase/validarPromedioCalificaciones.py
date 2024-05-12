
def validarPromedioCalificaciones(calificaciones: list) -> bool:
    promedio = sum(calificaciones) / len(calificaciones)
    return True if promedio >= 7 else False
    