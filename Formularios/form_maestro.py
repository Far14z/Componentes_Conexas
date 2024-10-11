import tkinter as tk
from tkinter import font, messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
from PIL import Image, ImageTk
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes
from Formularios.form_Instruciones import Formulario_Instrucciones
from Formularios.form_bienvenida import Formulario_Bienvenida

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
        w, h = 800, 550
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
            width = 520,
            height = 220,
            bg = COLOR_PANEL, 
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 2
        )

        #Mostrar texto en el panel
        self.panel.create_text(
            115, 30, 
            text = "Integrantes del grupo 1:", 
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.create_text(
            200, 60,
            text = "1. Cheel Animaca, Nicolas - U20231D456", 
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.create_text(
            244, 90,
            text = "2. Coronel Espinoza, Farid Sebastian - U202312508",
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.create_text(
            214, 120,
            text = "3. Orejuela Lluncor, Gianpiere - U20191B010",
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.create_text(
            236, 150,
            text = "4. Rodríguez Rodríguez, Luis Piero - U202311334",
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.create_text(
            247, 180,
            text = "5. Valderrama Bautista, Oscar Enrique - U202312314",
            font = ("Arial", 14,),
            fill = "black",
        )

        self.panel.place(x = 150, y = 150)

    def btn_Instrucciones(self):

        img = Image.open("Imagenes\informacion.png")  # Asegúrate de que la imagen esté en la misma carpeta o especifica la ruta
        img = img.resize((50, 50))
        self.circulo_img = ImageTk.PhotoImage(img)

        # Crear el botón con la imagen circular
        self.btnInstrucciones = tk.Button(
            self, 
            image=self.circulo_img,
            command=self.abrir_instrucciones,
            borderwidth=0  
        )
        
        self.btnInstrucciones.place(x=700, y=40)
        #self.btnInstrucciones.config(width = 3, height = 1)
    
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
            command = self.abrir_inicio
        )

        self.btnInicio.place(x = 30, y = 450)
        self.btnInicio.config(width = 15, height = 1)

    def abrir_inicio(self): 
        #Método que abrirá el nuevo formulario
        bienvenida = Formulario_Bienvenida()
        self.withdraw()
        bienvenida.grab_set()
        self.wait_window(bienvenida)
        self.deiconify()

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

        self.btnSalir.place(x = 600, y = 450)
        self.btnSalir.config(width = 15, height = 1)

    def salir(self, event = None):
        self.quit()