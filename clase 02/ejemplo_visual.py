#Ejemplo visual de POO
# importamos los modulos necesarios
import turtle
from figuras import Circulo, Rectangulo, Cuadrado

#definimos la pantalla de la tortuga
screen = turtle.Screen()
screen.title('Pactica visual de  POO')

#creamos un lapi de tortuga
pen = turtle.Turtle()
pen.shape('turtle')

#creamos los objetos de las figuras
circ = Circulo('blue', pen, 100)
rect = Rectangulo('yellow', pen, 170, 130)
cuad = Cuadrado('red', pen, 170)

#dibujamos el circulo
circ.dibujar()
rect.dibujar()
cuad.dibujar()

pen.hideturtle()

#mantenemos abierta la pantalla
screen.mainloop()