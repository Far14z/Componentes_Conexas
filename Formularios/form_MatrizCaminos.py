import tkinter as tk
from tkinter import font
from tkinter import messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import Controlador, Guardar_MatrizAdyacencia
from Formularios.form_OrdenarFilas import Formulario_OrdenarFilas
import Util.util_ventana as util_ventana
from PIL import Image, ImageTk
from Util.util_imagenes import resourse_path
import copy

class Formulario_MatrizDeCaminos(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_paso1, filas_indices, columnas_indices):
        super().__init__()
        self.control = Controlador()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        self.matriz_load = Guardar_MatrizAdyacencia()
        self.matriz = self.matriz_load.get_matrizAdyacencia()
        self.matriz_paso1 = matriz_paso1
        self.filas_indices = filas_indices
        self.columnas_indices = columnas_indices
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)

        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.algoritmo_warshall()
        self.imprimir_matriz()
        self.botones()
        self.resizable(0, 0)
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas - Paso 2')
        self.iconbitmap(resourse_path("./Imagenes/grafo.ico"))
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
            text = "Matriz de Caminos",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)

    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def algoritmo_warshall(self):
    
        V = len(self.matriz_paso1)
        self.matriz_caminos = self.matriz_paso1.copy()
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    self.matriz_caminos[i][j] = self.matriz_caminos[i][j] or (self.matriz_caminos[i][k] and self.matriz_caminos[k][j])
        return self.matriz_caminos

    def imprimir_matriz(self):

        marco_matriz = tk.Frame(self, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
        marco_matriz.pack_propagate(False)
        marco_matriz.place(x = 310 - self.tamano_matriz * 6, y = 120) #Ajustar la posición del frame según sea necesario

        # Imprimir índices de columnas
        for j, index in enumerate(self.columnas_indices):
            label = tk.Label(marco_matriz, text=index, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=0, column=j + 1, padx=15, pady=5)

        # Imprimir la matriz de caminos
        for i, fila in enumerate(self.matriz_caminos):
            label = tk.Label(marco_matriz, text=self.filas_indices[i] + 1, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=i + 1, column=0, padx=10, pady=5)

            for j, valor in enumerate(fila):
                label = tk.Label(marco_matriz, text=valor, font=("Arial", 12), bg= COLOR_BLANCO, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
                label.grid(row=i + 1, column=j + 1, padx=15, pady=5)

    def botones(self):
        #Crear botones para obtener los valores de la matriz
        self.boton_Anterior = tk.Button(
            self,
            text = "Anterior",
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black", #Color de la letra
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5, #Tamaño del borde
            activebackground = COLOR_CURSOR_ENCIMA, #Color de fondo al pasar el cursor
            activeforeground = "black", #Color de la letra al pasar el cursor
            relief = tk.FLAT, #Tipo de borde
            command=self.destroy
        )

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
            command=self.Form_Paso3
        )
        
        self.boton_Anterior.place(x = 50, y = 270 + self.tamano_matriz * 30)
        self.boton_Anterior.config(width = 15, height = 1)

        self.boton_Continuar.place(x = 550 + self.tamano_matriz * 28, y = 270 + self.tamano_matriz * 30)
        self.boton_Continuar.config(width = 15, height = 1)

    def Form_Paso3(self):
        paso3 = Formulario_OrdenarFilas(copy.deepcopy(self.matriz_caminos), copy.deepcopy(self.filas_indices), self.columnas_indices)
        self.withdraw()
        paso3.grab_set()
        self.wait_window(paso3)
        self.deiconify()