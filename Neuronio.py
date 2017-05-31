#Importa Rede e Camada porque vai que precisa.
#Importa math só por causa da função exp.
#Importa random so para atribuir pesos aleatórios para as entradas.

import Rede as R
import Camada as C
import math as M
import random

class Neuronio():
    def _init_(self, numero_pesos):
        self.pesos = []
        for i in range(0, numero_pesos):
            self.pesos.append(random.random())
        
    def somatoria(self, entradas, bias):
        valor = 0
        for i in range(0, len(self.entradas)):
            valor = valor + entradas[i] * pesos[i]

        return valor + bias

    def ativacao(self, valor):
        return 1.0/(1 + M.exp(-valor))

    def derivada_ativacao(self, valor):
        return M.exp(valor)/(M.exp(valor) + 1)^2
