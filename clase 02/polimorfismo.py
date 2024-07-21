#POLIMORFISMO
class Felino: #<- clase padre
    def __init__(self, tamaño, color, edad, nombre):
        self.tamaño = tamaño
        self.nombre = nombre
        self.color = color
        self.edad = edad
    
    def maullar(self):
        return 'Estoy maullando ...!!!!'
    
    def cazar(self):
        print('estoy cazando algo XD')

class Gato(Felino):
    def __init__(self, habitad, tamaño, color, edad, nombre):
        super().__init__(tamaño, color, edad, nombre)
        self.habitad = habitad
    
    def cazar(self):
        return 'Estoy cazando un raton'
    
class Leopardo(Felino):
    def __init__(self, habitad, tamaño, color, edad, nombre):
        super().__init__(tamaño, color, edad, nombre)
        self.habitad = habitad
    
    def cazar(self):
        return 'Estoy cazando un venado!!!!'
    
gato = Gato('domestico', 'pequeño', 'grisaseo', '1.5 años', 'Tilin')
leopardo = Leopardo('salvaje', 'grande', 'rojizo', '3 años', 'Lucho')

print(gato.cazar(), 'soy un lindo gatito')
print(leopardo.cazar(), 'soy un leopardo salvaje')
print(gato.maullar(), 'soy un lindo gatito')
print(leopardo.maullar(), 'soy un leopardo salvaje')