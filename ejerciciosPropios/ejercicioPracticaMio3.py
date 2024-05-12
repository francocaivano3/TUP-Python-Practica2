
# ¡Por supuesto! Aquí tienes otro ejercicio para practicar:

# Ejercicio: Crear una clase de Libro
# Crea una clase llamada Libro que tenga los siguientes atributos y métodos:

# Atributos:

# titulo - Título del libro
# autor - Autor del libro
# genero - Género del libro
# paginas - Número de páginas del libro
# estado - Estado del libro (por ejemplo, "prestado", "disponible", etc.)
# Métodos:

# informacion() - Método que imprime un resumen de la información del libro, incluyendo título, autor, género, número de páginas y estado.
# prestar_libro() - Método que cambia el estado del libro a "prestado".
# devolver_libro() - Método que cambia el estado del libro a "disponible".
# Luego, instancia un objeto de la clase Libro, configura sus atributos y llama a los métodos para probar su funcionamiento. ¡Buena suerte!

class Libro():
    def __init__(self, titulo, autor, genero, paginas, estado):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.estado = estado
    
    def informacion(self):
        print(f"Título: {self.titulo} \n Autor: {self.autor} \n Género: {self.genero} \n Páginas: {self.paginas} \n Estado: {self.estado}")
    
    def prestarLibro(self):
        self.estado = "Prestado"
    
    def devolverLibro(self):
        self.estado = "Disponible"
    
libro1 = Libro("El extranjero", "Albert Camus", "Absurdo / Existencialismo", 84, "Disponible")

libro1.informacion()
libro1.prestarLibro()
libro1.informacion()
libro1.devolverLibro()
libro1.informacion()