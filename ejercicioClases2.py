# Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
# Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
# En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.

class Cuenta:
    class CajaAhorra:
        
        def __init__(self, nombreTitular, monto):
            self.nombreTitular = nombreTitular
            self.monto = monto
        
        def mostrar(self):
            print(f"Titular: {self.nombreTitular}")
            print(f"Monto: {self.monto}")

class CajaAhorro(Cuenta):

    def __init__(self):
        super().__init__(self.titular, self.monto)

    def mostrar(self):
        print(f"Cuenta de ahorro")
        super().mostrar()
    
class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__(self, nombreTitular, monto, plazo, interes)
        self.plazo = plazo 
        self.interes = interes 
    
    def mostrar(self):
        print(f"Plazo fijo")
        super().mostrar()



# solucion profe 
# class PlazoFijo(Cuenta):

#     def __init__(self,titular,monto,plazo,interes):
#         super().__init__(titular,monto)
#         self.plazo=plazo
#         self.interes=interes

#     def imprimir(self):
#         print("Cuenta de plazo fijo")
#         super().imprimir()
#         print("Plazo en dias:",self.plazo)
#         print("Interes:",self.interes)
#         self.ganancia_interes()

#     def ganancia_interes(self):
#         ganancia=self.monto*self.interes/100
#         print("Importe del interes:",ganancia)

# # bloque principal

# cajaahorro=CajaAhorro("Juan", 2000)
# cajaahorro.imprimir()

# plazofijo=PlazoFijo("Diego", 10000, 30, 0.75)
# plazofijo.imprimir()