#Encapsulamiento en python POO
# atributos, encapsulamiento, metodos, herencia
class Figura(): # <- superclase o clase padre
    def __init__(self, color, textura, nombre):
        self.color = color
        self.textura = textura
        self.nombre = nombre
        
        #encapsulamiento
        # self.__textura = 'textura'
        # self.__nombre = 'nombre'
    
    def obtener_color(self):
        return self.color
    
    # getters
    # def get_textura(self):
    #     return self.__textura
    
    # def get_nombre(self):
    #     return self.__nombre
    
    #setters
    # def set_nombre(self, name):
    #     self.__nombre = name

# # Ejemplo de metodos

# rectangulo = Figura()

# print(rectangulo.get_textura())
# print(rectangulo.get_nombre())
# rectangulo.set_nombre('Maria')
# print(rectangulo.get_nombre())

# Herencia

class Rectangulo(Figura): #clase hija
    def __init__(self, color : str, nombre : str):
        super().__init__(color, 'liso', nombre)
    
    # def obtener_color(self):
    #     return 'soy un metodo redefinido'

# rect = Rectangulo('rojo', 'Pablito')
# print(rect.color)
# print(rect.textura)
# print(rect.nombre)

# print(rect.obtener_color())