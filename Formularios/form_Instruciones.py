import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes

class Formulario_Instrucciones(tk.Toplevel):
    #Constructor de la clase
    def __init__(self):
        super().__init__()
        self.config_window()
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas - Instruciones')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = 900, 600
        util_ventana.centrar_ventana(self, w, h)
