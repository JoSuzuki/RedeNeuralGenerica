import Neuronio

class Camada:
    def __init__(self, nNeuronios, nNeuroniosAnterior, bias = 1):
        ''' Construtor da classe camadas '''
        self.neuronios = []
        for i in range(nNeuronios):
            self.neuronios.append(Neuronio.Neuronio(nNeuroniosAnterior + 1))
        
        self.bias = bias

    def feed_neuronios(self, entradas):        
        ''' Recebe uma lista de entradas da camada e calcula
        a saida para cada um dos neuronios presentes nessa camada '''
        
        entradas.append(self.bias)
        
        for i in range(len(self.neuronios)):
            self.neuronios[i].calcular_saida(entradas)
        return

    def get_saidas(self):
        saidas = []
        for i in range(len(self.neuronios)):
            saidas.append(self.neuronios[i].saida)
        return saidas
        
