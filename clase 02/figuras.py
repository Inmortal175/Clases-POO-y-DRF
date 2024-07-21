from turtle import Turtle

class Figura(): # <- superclase o clase padre
    def __init__(self, color : str, pen : Turtle):
        self.color = color
        self.lapiz : Turtle = pen

    def dibujar(self):
        pass
    
    # def colorear(self):

class Circulo(Figura):
    def __init__(self, color:str, pen : Turtle, radio:float):
        super().__init__(color, pen)
        self.radio = radio
    
    def dibujar(self):
        self.lapiz.up()
        self.lapiz.goto(-self.radio, 0)
        self.lapiz.down()
        self.lapiz.color(self.color)
        self.lapiz.begin_fill()
        self.lapiz.circle(self.radio)
        self.lapiz.end_fill()
        # colocamos el lapiz al inicio
        self.lapiz.up()
        self.lapiz.goto(0,0)
        

class Rectangulo(Figura):
    def __init__(self, color:str, pen: Turtle, base : float, altura : float):
        super().__init__(color, pen)
        self.base = base
        self.altura = altura
    
    def dibujar(self):
        self.lapiz.goto(20, 0)
        self.lapiz.down()
        
        self.lapiz.color(self.color)
        self.lapiz.begin_fill()
        for vuelta in range(2):
            self.lapiz.forward(self.base)
            self.lapiz.left(90)
            self.lapiz.forward(self.altura)
            self.lapiz.left(90)
        self.lapiz.end_fill()
        
        # ir adelante de la figura 20 px
        self.lapiz.up()
        self.lapiz.goto(self.base + 40, 0)            

class Cuadrado(Figura):
    def __init__(self, color: str, pen: Turtle, lado : float):
        super().__init__(color, pen)
        self.lado = lado
    
    def dibujar(self):
        self.lapiz.down()
        self.lapiz.color(self.color)
        self.lapiz.begin_fill()
        for i in range(4):
            self.lapiz.forward(self.lado)
            self.lapiz.left(90)
        self.lapiz.end_fill()