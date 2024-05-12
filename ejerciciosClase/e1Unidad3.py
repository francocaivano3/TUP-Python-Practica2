from datetime import date

class Usuario():
    def __init__(self, userName: str, estado: bool, email: str, password: str, nombre: str, apellido: str, fechaAlta: str, fechaBaja):
        self.__userName = userName
        self.__estado = True
        self.__email = email
        self.__password =  password
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaAlta = fechaAlta
        self.__fechaBaja = None

    def get_userName(self):
        return self.__userName
    
    def get_estado(self):
        return self.__estado
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_nombre(self):   
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_fechaAlta(self):
        return self.__fechaAlta
    
    def get_fechaBaja(self):
        return self.__fechaBaja
    
    def set_userName(self, userName: str):
        self.__userName = userName
    
    def set_estado(self, estado: bool):
        self.__estado = estado

    def set_email(self, email: str):
        self.__email = email
    
    def set_password(self, password: str):
        self.__password = password
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido
    
    def set_fechaAlta(self, fechaAlta: str):
        self.__fechaAlta = fechaAlta
    
    def set_fechaBaja(self, fechaBaja):
        self.__fechaBaja = fechaBaja
    
    



    def validarCredenciales(self, usuario: str, password: str) -> bool:
        return usuario == self.__userName and password == self.__password
    



    def bajaUsuario(self, usuario: str, password: str) -> bool:
        if self.validarCredenciales(usuario, password):
            self.__estado = False
            self.__fechaBaja = date.today()
            print("Se ha dado de baja")
            return True
        else:
            print("Usuario o contraseña no válidas")
            return False
            

