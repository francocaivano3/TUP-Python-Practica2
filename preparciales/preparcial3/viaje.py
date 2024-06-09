from datetime import date 

class Viaje():
    nroViaje = 0

    def __init__(self, nombre, fechaDesde: date, fechaHasta: date) -> None:
        self.__nombre = nombre
        self.__nroViaje = Viaje.__generarProximoNumViaje()
        self.__fechaDesde = fechaDesde
        self.__fechaHasta = fechaHasta

        