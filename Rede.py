import Camada
class Rede:
    def __init__(self, arquitetura):
        #gerar camadas
        self.camadas = []
        for i in range(1,len(arquitetura)):
            self.camadas.append(Camada.Camada(arquitetura[i],arquitetura[i-1]))
            
        
    def feed_forward(self, entradas):
        
        self.camadas[0].feed_neuronios(entradas)
        
        for i in range(1,len(self.camadas)):
            self.camadas[i].feed_neuronios(self.camadas[i-1].get_saidas())
            
        return self.camadas[len(self.camadas)-1].get_saidas()
     
        
    
    
    def treinar(self, interacoes = 1000):
        for i in range(interacoes):
            pass
                


if __name__ == "__main__":
    r = Rede([2,3,1])
    print(r.feed_forward([1,1]))
    
