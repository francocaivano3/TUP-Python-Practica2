from ejerciciosPropios.ejerciciosClase.e1Unidad3 import Usuario
from datetime import date 

userName = input("Ingrese el nombre de usuario: ")
estado = True
email = input("Ingrese el email: ")
password = input("Ingrese el password: ")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
fechaAlta = date.today()
fechaBaja = None

usuario1 = Usuario(userName, estado, email, password, nombre, apellido, fechaAlta, fechaBaja)

userNameLogin = input("Ingrese el nombre de usuario: ")
userPassLogin = input("Ingrese la contraseña: ")

usuario1.validarCredenciales(userNameLogin, userPassLogin)
