class Controlador:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Controlador, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.tamano_matriz_adjacencia = 0
            self.initialized = True

    def set_tamanoMatrizAdyacencia(self, x):
        self.tamano_matriz_adjacencia = x

    def get_tamanoMatrizAdyacencia(self):
        return self.tamano_matriz_adjacencia

class Guardar_MatrizAdyacencia:
    _instance = None

    def __new__(cls, *args, **kwargs):
        #Verifica si la instancia ya ha sido creada
        if not cls._instance:
            cls._instance = super(Guardar_MatrizAdyacencia, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        #Solo se inicializará la primera vez que se cree la instancia
        if not hasattr(self, 'initialized'):
            self.matriz_adyacencia = []
            self.initialized = True

    def set_matrizAdyacencia(self, matriz):
        self.matriz_adyacencia = matriz

    def get_matrizAdyacencia(self):
        return self.matriz_adyacencia
    
class Guardar_IndiceFila:
    _isntance = None

    def __new__(cls, *args, **kwargs):
        if not cls._isntance:
            cls._isntance = super(Guardar_IndiceFila, cls).__new__(cls)
        return cls._isntance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.indices_fila = []
            self.initialized = True

    def set_indicesFila(self, indices):
        self.indices_fila = indices

    def get_indicesFila(self):
        return self.indices_fila
