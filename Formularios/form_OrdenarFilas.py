import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import Controlador
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes

class Formulario_OrdenarFilas(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_paso1, filas_indices, columnas_indices):
        super().__init__()
        self.control = Controlador()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        self.matriz_paso1 = matriz_paso1
        self.filas_indices = filas_indices
        self.columnas_indices = columnas_indices
        self.logo = util_imagenes.leer_imagen("./Imagenes/UPC_logo.png", (80, 80))
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()

        
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Matriz de Caminos - Paso 3')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = (860 + self.tamano_matriz * 25), (380 + self.tamano_matriz * 30)  # Ajustar el tamaño dinámicamente
        util_ventana.centrar_ventana(self, w, h)
        
    def colocar_Logo(self):

        self.labelLogo = tk.Label(
            self, 
            image = self.logo, 
            bg = COLOR_BACKGROUND_IMAGENES, 
            highlightbackground = COLOR_BORDE_LOGO, 
            highlightthickness = 2
        )

        self.labelLogo.place(x = 25, y = 20)    
        
    def colocar_Titulo(self):

        self.labelTitulo = tk.Label(
            self, 
            text = "Matriz de Caminos - Ordenada por filas",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)

    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)