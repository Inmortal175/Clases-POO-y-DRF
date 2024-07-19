#----------Franklin, Figueroa Perez-------------------#
#----------CLASE 01----------#
#----------CLASES y OBJETOS-------------#

#creacion de la clase carro
# class Carro:
#     def __init__(self): # <- constructor de la clase
#         self.marca = 'Toyota'
#         self.color = 'Azul'
#         self.modelo = 'NX-24421'
#         self.año = 2023
#         self.propetario = 'Juan'
#         self.precio = '15000'

# creacion de objetos desde la clase Carro
# CarroJuan : Carro = Carro()
# print(f"El color del carro de juan es {CarroJuan.color}")

# Carro2 = Carro()
# print(f"La marca del carro 2 es {Carro2.marca}")

# Carro3 = Carro()

# print(f"El modelo del carro 3 es {Carro3.modelo}")

# como seria en java (abajo) instancia de un objeto
# private Carro CarroJuan;
# CarroJuan = new Carro();


# Parte 2
class Carro:
    def __init__(self, marca : str, color : str, modelo : str, 
                 año : int, prop : str, precio : float):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.año    = año
        self.propetario = prop
        self.precio = precio

carro1 = Carro('Toyota', 'Rojo', 'XS-3675-2023', 2024, 'Frank',
               11000.99)
print(f"el carro 1 marca: {carro1.marca} del año {carro1.año}, del Sr. {carro1.propetario} cuesta : $ {carro1.precio}")

carro2 = Carro('Hilux', 'Rojo', 'H-375-2022', 2023, 'Juan',
               22000.99)
print(f"el carro 2 marca: {carro2.marca} del año {carro2.año}, del Sr. {carro2.propetario} cuesta : $ {carro2.precio}")