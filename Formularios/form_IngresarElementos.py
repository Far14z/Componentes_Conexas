import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
import Util.util_ventana as util_ventana
import Util.util_imagenes as util_imagenes
from controlador import Controlador
import random
from Formularios.form_MatrizDeAdyacencia import Formulario_MatrizDeAdyacencia

class Formulario_IngresarElementos(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, tamaño_matriz):
        super().__init__()
        self.tamano_matriz = tamaño_matriz #Tamaño de la matriz de adyacencia
        self.logo = util_imagenes.leer_imagen("./Imagenes/UPC_logo.png", (80, 80))
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.crear_Matriz()
        self.botones()
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Ingresar elementos')
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
            text = "Ingresar elementos",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)
    
    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def crear_Matriz(self):
        #Crear un marco para la matriz con un tamaño fijo
        marco_matriz = tk.Frame(self, width = 400, height = 200)  #Ajusta el tamaño según lo necesites
        marco_matriz.pack_propagate(False)  #Evita que el marco cambie de tamaño según su contenido
        marco_matriz.pack(pady = 100)  #Ajusta la posición del marco

        #Crear la matriz de adyacencia a partir del tamaño ingresado
        self.entries = []  #Asegúrate de inicializar self.entries aquí
        for i in range(self.tamano_matriz):
            fila = []
            for j in range(self.tamano_matriz):
                #Crear widget de entrada
                entry = tk.Entry(marco_matriz, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  #Ajustar la posición de la matriz
                fila.append(entry)
            self.entries.append(fila)

        #Ajustar el peso de las filas y columnas
        for j in range(self.tamano_matriz):
            marco_matriz.grid_columnconfigure(j, weight=1) #Ajusta el peso de las columnas

    def botones(self):
        #Crear botones para obtener los valores de la matriz
        self.boton_Continuar = tk.Button(
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
            command=self.continuar_Paso1
        )

        self.boton_Random = tk.Button(
            self, 
            text = "Valores Aleatorios", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command=self.obtener_valores_Random
        )

        #Crear botón para guardar los valores de la matriz
        self.boton_guardar = tk.Button(
            self, 
            text = "Guardar", 
            font = ("Arial", 14), 
            fg = "black",
            command=self.guardar_matriz
        )
        
        self.boton_guardar.place(x = 440, y = 580)
        self.boton_guardar.config(width = 15, height = 1)

        self.boton_Random.place(x = 50, y = 600)
        self.boton_Random.config(width = 15, height = 1)

        self.boton_Continuar.place(x = 800, y = 600)
        self.boton_Continuar.config(width = 15, height = 1)
    
    def validar_matriz(self):
        for fila in self.entries:
            for entry in fila:
                valor = entry.get()
                if valor not in ["0", "1"]:  #Verifica si el valor no es '0' o '1'
                    return False  #Retorna False si encuentra un valor no válido
        return True  #Retorna True si todos los valores son válidos
    
    def guardar_matriz(self):

        if self.validar_matriz():
            matriz_guardada = []

            for fila in self.entries:
                fila_valores = [entry.get() for entry in fila]  # Obtener los valores de la fila
                matriz_guardada.append(fila_valores)  # Agregar la fila a la matriz

            self.matriz_guardada = matriz_guardada

        else:
            tk.messagebox.showerror("Error", "Todos los valores deben ser 0 o 1.")

    def continuar_Paso1(self):
        if self.validar_matriz():
            paso1 = Formulario_MatrizDeAdyacencia(matriz_adyacencia=self.matriz_guardada)
            self.withdraw()
            paso1.grab_set()
            self.wait_window(paso1)
            self.deiconify()
        else:
            tk.messagebox.showerror("Error", "Todos los valores deben ser 0 o 1.")
    
    def obtener_valores_Random(self):
        #Obtener valores aleatorios (0 o 1) para la matriz
        for fila in self.entries:
            for entry in fila:
                #Generar un valor aleatorio (0 o 1)
                valor_aleatorio = random.randint(0, 1)  #Genera un 0 o un 1
                entry.delete(0, tk.END)  #Borrar el contenido actual
                entry.insert(0, str(valor_aleatorio))  #Insertar el valor aleatorio como string