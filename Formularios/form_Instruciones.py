import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes

class Formulario_Instrucciones(tk.Toplevel):
    #Constructor de la clase
    def __init__(self):
        super().__init__()
        self.logo = util_imagenes.leer_imagen("./Imagenes/UPC_logo.png", (80, 80))
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.mostrar_parrafos()
        self.btn_aceptar()
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas - Instruciones')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = 820, 490
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
            text = "Instrucciones",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)
    
    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)
        
    def mostrar_parrafos(self):
        
        self.labelParrafoProposito1 = tk.Label(
            self,
            text="Nuestro programa calcula las componentes conexas de un grafo.",
            font=("Arial", 15, "bold"),
            bg=COLOR_BACKGROUND       
        )
        
        self.labelParrafoProposito2 = tk.Label(
            self,
            text="Para ello, sigue los siguientes pasos:",
            font=("Arial", 15, "bold"),
            bg=COLOR_BACKGROUND,
        )
        self.labelPaso1 = tk.Label(
            self,
            text="Paso 1: ",
            font=("Arial", 13, "bold"),
            fg="red",
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )

        self.labelPaso1Desc = tk.Label(
            self,
            text="Genera una matriz de adyacencia de tamaño n x n con valores aleatorios\n"
                 "o ingresados manualmente y agrega (si fuese necesario) el valor 1 en la diagonal de la matriz.",
            font=("Arial", 13),
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )
        
        self.labelPaso2 = tk.Label(
            self,
            text="Paso 2: ",
            font=("Arial", 13, "bold"),
            fg="red",
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )
        
        self.labelPaso2Desc = tk.Label(
            self,
            text="Calcula la matriz de caminos a partir de la matriz obtenida en el paso 1.",
            font=("Arial", 13),
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )
        
        self.labelPaso3 = tk.Label(
            self,
            text="Paso 3: ",
            font=("Arial", 13, "bold"),
            fg="red",
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )

        self.labelPaso3Desc = tk.Label(
            self,
            text="Ordena las filas según el número de 1s (mayor a menor). Si hay 2 filas\n"
                 "que tienen la misma cantidad de 1s, entonces se debe colocar primero aquella que tiene el 1 más\n"
                 "cercano a la primera columna.",
            font=("Arial", 13),
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )
        
        self.labelPaso4 = tk.Label(
            self,
            text="Paso 4: ",
            font=("Arial", 13, "bold"),
            fg="red",
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )

        self.labelPaso4Desc = tk.Label(
            self,
            text="Ordena las columnas de acuerdo al orden de las filas. Las componentes\n"
                 "conexas serán aquellas que se formen con los bloques cuadrados diagonales formados por 1s.",
            font=("Arial", 13),
            bg=COLOR_BACKGROUND,
            justify="left",
            anchor="w"
        )
        
        self.labelParrafoProposito1.place(x=25, y=120)
        self.labelParrafoProposito2.place(x=25, y=145)
        
        self.labelPaso1.place(x=25, y=190, anchor="nw")
        self.labelPaso1Desc.place(x=90, y=190, anchor="nw")
        
        self.labelPaso2.place(x=25, y=240, anchor="nw")
        self.labelPaso2Desc.place(x=90, y=240, anchor="nw")
        
        self.labelPaso3.place(x=25, y=275, anchor="nw")
        self.labelPaso3Desc.place(x=90, y=275, anchor="nw")
        
        self.labelPaso4.place(x=25, y=340, anchor="nw")
        self.labelPaso4Desc.place(x=90, y=340, anchor="nw")
    
    def btn_aceptar(self):
        
        #Botón de inicio
        self.btnInicio = tk.Button(
            self, 
            text = "Aceptar", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command = lambda: self.aceptar()
        )

        self.btnInicio.place(x = 600, y = 420)
        self.btnInicio.config(width = 15, height = 1)
        
    def aceptar(self, event = None):
        self.destroy()
        
        