import tkinter as tk
from tkinter import font, messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
from PIL import Image, ImageTk
from Util.util_imagenes import resourse_path
import Util.util_ventana as util_ventana
from Formularios.form_Instruciones import Formulario_Instrucciones
from Formularios.form_bienvenida import Formulario_Bienvenida

class Formulario_Inicio(tk.Tk):
    #Constructor de la clase
    def __init__(self):
        super().__init__()
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
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
        self.iconbitmap(resourse_path("./Imagenes/grafo.ico"))
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

    def abrir_instrucciones(self):
        instrucciones = Formulario_Instrucciones()
        self.withdraw()
        instrucciones.grab_set()
        self.wait_window(instrucciones)
        self.deiconify()

    def btn_Instrucciones(self):

        img = Image.open(resourse_path(r"Imagenes\_informacion.png"))
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

    def abrir_inicio(self):
        bienvenida = Formulario_Bienvenida()
        bienvenida.grab_set()
        self.withdraw()
        self.wait_window(bienvenida)
        self.deiconify()

    def btn_Inicio(self):
        self.btnInicio = tk.Button(
            self, 
            text = "Iniciar", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black",
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5,
            activebackground = COLOR_CURSOR_ENCIMA,
            activeforeground = "black",
            relief = tk.FLAT,
            command = self.abrir_inicio
        )

        self.btnInicio.place(x = 30, y = 450)
        self.btnInicio.config(width = 15, height = 1)

    def btn_Salir(self):
        self.btnSalir = tk.Button(
            self, 
            text = "Salir", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black",
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5,
            activebackground = COLOR_CURSOR_ENCIMA,
            activeforeground = "black",
            relief = tk.FLAT,
            command = self.salir
        )

        self.btnSalir.place(x = 600, y = 450)
        self.btnSalir.config(width = 15, height = 1)

    def salir(self, event = None):
        self.quit()