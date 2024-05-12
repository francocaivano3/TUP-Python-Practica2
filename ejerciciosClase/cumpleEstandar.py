def cumpleEstandar(cliente: dict) -> bool:
    return True if len(cliente["historialCompras"]) >= 5 else False