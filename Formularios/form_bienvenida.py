import tkinter as tk
from tkinter import font, messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes
from controlador import Controlador
from PIL import Image, ImageTk
from Util.util_imagenes import resourse_path
from Formularios.form_IngresarElementos import Formulario_IngresarElementos

class Formulario_Bienvenida(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.config_window()
        self.color_background()
        self.colocar_Titulo()
        self.colocar_logo()
        self.mostrar_label()
        self.mostrar_spinbox()
        self.mostrar_botones()
        self.resizable(0, 0)
        
    def colocar_Titulo(self):

        self.labelTitulo = tk.Label(
            self, 
            text = "Bienvenido!",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)
    
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas')
        self.iconbitmap("./Imagenes/grafo.ico")
        w, h = 715, 270
        util_ventana.centrar_ventana(self, w, h)
        self.configure(bg= COLOR_BACKGROUND)

    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)
    
    def colocar_logo(self):
        
        self.labelLogo = tk.Label(
            self, 
            image = self.logo, 
            bg = COLOR_BACKGROUND_IMAGENES, 
            highlightbackground = COLOR_BORDE_LOGO, 
            highlightthickness = 2
        )

        self.labelLogo.place(x = 25, y = 20)    
    
    def mostrar_label(self):
        
        self.label = tk.Label(
            self,
            text="Ingrese el tamaño de la matriz de adyacencia:",
            font=("Arial", 15),
            bg=COLOR_BACKGROUND       
        )

        self.label.place(x=25, y=120)
        
    def mostrar_spinbox(self):
        
        def validate_input(value_if_allowed):
            if value_if_allowed.isdigit() or value_if_allowed == "":
                return True
            if value_if_allowed == "" or (int(value_if_allowed) >= 8 and int(value_if_allowed) <= 16):
                return True
            return False
            
        vcmd = (self.register(validate_input), '%P')
        
        self.entrada = tk.Spinbox (
            self,
            from_= 8,  #Valor mínimo
            to = 16,    #Valor máximo
            increment = 1,  #Incremento de 1 en 1
            bg = "lightblue",
            font=("Arial", 15),
            validate="key",
            validatecommand=vcmd
        )
        
        self.entrada.place(x=445, y=122)
        
    def mostrar_botones(self):
        
        self.boton_continuar = tk.Button(
            self, 
            text = "Continuar", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command = lambda: self.continuar()
        )

        self.boton_cancelar = tk.Button(
            self,
            text = "Cancelar",
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command = lambda: self.destroy()
        )

        self.boton_continuar.place(x = 30, y = 170)
        self.boton_continuar.config(width = 15, height = 1)
        
        self.boton_cancelar.place(x = 497, y = 170)
        self.boton_cancelar.config(width = 15, height = 1)
        
    def continuar(self):
            
        if self.entrada.get() == "":
            messagebox.showwarning("Error", "Ingrese un tamaño para la matriz de adyacencia")
        else:
            #Convierte el valor del Spinbox a un entero
            tamano_matriz = int(self.entrada.get())

            #Verifica si el tamaño de la matriz está en el rango deseado (8 a 16)
            if tamano_matriz < 8 or tamano_matriz > 16:
                messagebox.showwarning("Error", "El tamaño de la matriz debe estar entre 8 y 16")

            else:
                #Si la validación es exitosa, procede con la lógica del controlador
                control = Controlador()
                control.set_tamanoMatrizAdyacencia(tamano_matriz)
            
                opcion = messagebox.askquestion("Confirmacion", "¿Desea ingresar los elementos?")
            
                if opcion == "yes":
                    ingresarElementos = Formulario_IngresarElementos(control.get_tamanoMatrizAdyacencia())
                    self.withdraw()
                    ingresarElementos.grab_set()
                    self.wait_window(ingresarElementos)
                    self.deiconify()
                
            






