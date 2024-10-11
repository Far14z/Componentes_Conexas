import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes


class Formulario_MatrizDeAdyacencia(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_adyacencia):
        super().__init__()
        self.matriz_adyacencia = matriz_adyacencia #Matriz de adyacencia
        self.logo = util_imagenes.leer_imagen("./Imagenes/UPC_logo.png", (80, 80))
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.actualizar_diagonal()
        self.imprimir_matriz()
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Matriz de adyacencia - Paso 1')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = 1024, 700
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
            text = "Matriz de adyacencia",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)
    
    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def actualizar_diagonal(sefl):
        #Asegurarse de que la diagonal contenga solo 1's
        for i in range(len(sefl.matriz_adyacencia)):
            sefl.matriz_adyacencia[i][i] = 1
        return sefl.matriz_adyacencia

    def imprimir_matriz(self):
        marco_matriz = tk.Frame(self, width=400, height=200)
        marco_matriz.pack_propagate(False)
        marco_matriz.pack(pady=100)

        #Imprimir la matriz de adyacencia (con la aplicacion de 1's en la diagonal) en el marco
        for i, fila in enumerate(self.matriz_adyacencia):
            for j, valor in enumerate(fila):
                label = tk.Label(marco_matriz, text=valor, font=("Arial", 12), bg = COLOR_MATRIZ)
                label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        #Configurar el peso de las filas y columnas del marco para que crezcan proporcionalmente
        for j in range(len(self.matriz_adyacencia)):
            marco_matriz.grid_columnconfigure(j, weight=1)  #Hace que cada columna crezca por igual
        for i in range(len(self.matriz_adyacencia)):
            marco_matriz.grid_rowconfigure(i, weight=1)  #Hace que cada fila crezca por igual