import Neuronio


class Camada():
    def __init__(self, nNeuronios):
        ''' Construtor da classe camadas '''
        neuronios = []
        for i in range(nNeuronios):
            neuronios.append(Neuronio())
        self.neuronios = neuronios

    def feed_neuronio(self, entradas):
        ''' Recebe uma lista de entradas da camada e calcula
        a saida para cada um dos neuronios presentes nessa camada '''
        for i in range(len(self.neuronios)):
            self.neuronios[i].calcular_saida(entradas)
        return

    def get_saidas(self):
        saidas = []
        for i in range(len(self.neuronios)):
            saidas.append(neuronios.saida)
        return saidas
