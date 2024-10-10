class Controlador():
    
    def __init__(self):
        super().__init__()
        self.__tamanoMatrizAdyacencia = 0
        
    def set_tamanoMatrizAdyacencia(self, x):
        self.__tamanoMatrizAdyacencia = x
        
    def get_tamanoMatrizAdyacencia(self):
        return self.__tamanoMatrizAdyacencia
        
            
                                    