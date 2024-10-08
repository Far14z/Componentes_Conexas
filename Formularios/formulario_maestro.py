import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes
from Formularios.form_Instruciones import Formulario_Instrucciones

class Formulario_Inicio(tk.Tk):
    #Constructor de la clase
    def __init__(self):
        super().__init__()
        self.logo = util_imagenes.leer_imagen("./Imagenes/UPC_logo.png", (80, 80))
        self.config_window()
        self.color_background()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.Panel()
        self.btn_Instrucciones()
        self.btn_Inicio()
        self.btn_Salir()
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = 900, 600
        util_ventana.centrar_ventana(self, w, h)
    
    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def colocar_Logo(self):

        #Logo de la aplicación
        self.labelLogo = tk.Label(
            self, 
            image = self.logo, 
            bg = COLOR_BACKGROUND_IMAGENES, 
            highlightbackground = COLOR_BORDE_LOGO, 
            highlightthickness = 2
        )

        self.labelLogo.place(x = 25, y = 20)

    def colocar_Titulo(self):
        #Titulo de la aplicación
        self.labelTitulo = tk.Label(
            self, 
            text = "Componentes Conexas de un Grafo",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 150, y = 45)

    def Panel(self):
        #Panel para mostrar el grafo
        self.panel = tk.Canvas(
            self, 
            width = 580, 
            height = 250, 
            bg = COLOR_PANEL, 
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 2
        )

        #Mostrar texto en el panel
        self.panel.create_text(
            110, 30, 
            text = "Integrantes del grupo 1:", 
            font = ("Arial", 14,),
            fill = "black"
        )

        self.panel.place(x = 150, y = 150)

    def btn_Instrucciones(self):
        #Botón de instrucciones
        self.btnInstrucciones = tk.Button(
            self, 
            text = "!", 
            font = ("Arial", 9, "bold"),
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command = self.abrir_instrucciones #Abrir Formulario Instrucciones
        )

        self.btnInstrucciones.place(x = 840, y = 40)
        self.btnInstrucciones.config(width = 3, height = 1)
    
    def abrir_instrucciones(self):
        #Método que abrirá el nuevo formulario
        instrucciones = Formulario_Instrucciones() #Crear una instancia del formulario
        self.withdraw() #Ocultar Formulario Inicio
        instrucciones.grab_set() #Bloquear el formulario principal
        self.wait_window(instrucciones) #Esperar a que se cierre el nuevo formulario
        self.deiconify() #Volver a mostrar el formulario principal

    def btn_Inicio(self):
        #Botón de inicio
        self.btnInicio = tk.Button(
            self, 
            text = "Iniciar", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
        )

        self.btnInicio.place(x = 30, y = 500)
        self.btnInicio.config(width = 15, height = 1)

    def btn_Salir(self):
        #Botón de inicio
        self.btnSalir = tk.Button(
            self, 
            text = "Salir", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command = self.salir #Función al hacer click
        )

        self.btnSalir.place(x = 700, y = 500)
        self.btnSalir.config(width = 15, height = 1)

    def salir(self, event = None):
        self.quit()