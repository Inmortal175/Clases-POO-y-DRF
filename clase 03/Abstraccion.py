# Abstraccion en python
from abc import ABC, abstractmethod

# CLASE ABSTRACTA
class CuentaBancaria(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    #METODOS ABSTRACTOS
    @abstractmethod
    def depositar(self, monto):
        pass
    
    @abstractmethod
    def retirar(self, monto):
        pass
    
    @abstractmethod
    def consultar_saldo(self):
        pass

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if self.saldo - monto >= -self.limite_sobregiro:
            self.saldo -= monto
            print(f'Se ha retirado {monto} y queda de saldo {self.saldo}.')
        else:
            print('Fondos Insuficientes, incluyendo el sobregiro permitido.')
    
    def consultar_saldo(self):
        return self.saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if self.saldo > monto:
            self.saldo -= monto
        else: print('Fondos insuficientes...')
    
    def consultar_saldo(self):
        return self.saldo
        

cCorriente = CuentaCorriente('Freed', 1000, 500)
cCorriente.depositar(400)
cCorriente.retirar(1800)
print(cCorriente.consultar_saldo())