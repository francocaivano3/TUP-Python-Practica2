class Estadia():

    def __init__(self, fecha, nroPatente, horaEntrada, horaSalida, cantHoras, estado, pagado):
        self.fecha = fecha
        self.nroPatente = nroPatente
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida
        self.cantHoras = cantHoras
        self.estado = estado
        self.pagado = pagado


    def __str__(self) -> str:
        
    

class Precio():
    def __init__(self, precioHora, calcularImporte):
        self.precioHora = precioHora
        self.calcularImporte = calcularImporte
             