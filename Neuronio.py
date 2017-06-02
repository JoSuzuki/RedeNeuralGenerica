import random
import numpy as np
class Neuronio:
    
    def __init__(self, numero_pesos):
        self.pesos = []
        self.saida = 0
        self.soma = 0
        self.entradas = []
        for i in range(0, numero_pesos):
            self.pesos.append(random.random())
        
    def calcular_saida(self, entradas):
        self.entradas = entradas
        self.soma = self.somatoria(entradas)
        self.saida = self.ativacao(self.soma)
        
    def somatoria(self, entradas):
        valor = 0
        for i in range(0, len(entradas)):
            valor = valor + entradas[i] * self.pesos[i]

        return valor

    def ativacao(self, x):
        return 1/(1+ np.exp(-x))

    def derivada_ativacao(self, valor):
        return (valor*(1-valor))
    
