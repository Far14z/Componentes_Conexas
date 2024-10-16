import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import Controlador
from Formularios.form_componentes_conexas import Formulario_Componentes_Conexas
import Util.util_ventana as util_ventana
from PIL import Image, ImageTk
from Util.util_imagenes import resourse_path

class Formulario_OrdenarFilas(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_caminos, filas_indices, columnas_indices):
        super().__init__()
        self.control = Controlador()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        self.matriz_caminos = matriz_caminos
        self.filas_indices = filas_indices
        self.columnas_indices = columnas_indices
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.ordenar_filas()
        self.imprimir_matriz()
        self.botones()
        self.resizable(0, 0)
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas - Paso 3')
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
            text = "Matriz de Caminos - Ordenada por filas",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)

    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def ordenar_filas(self):
        #Calcular la cantidad de 1's en cada fila y mantener los índices originales
        cantidad_unos_y_filas = [(sum(fila), index) for index, fila in enumerate(self.matriz_caminos)]
        
        #Ordenar las filas en orden descendente de acuerdo a la cantidad de 1's
        cantidad_unos_y_filas.sort(reverse=True, key=lambda x: x[0])
        
        #Reordenar la matriz y los índices de filas en función del nuevo orden
        self.matriz_caminos_filas = [self.matriz_caminos[indice] for _, indice in cantidad_unos_y_filas]
        self.filas_indices_ordenada = [self.filas_indices[indice] for _, indice in cantidad_unos_y_filas]

    def imprimir_matriz(self):

        marco_matriz = tk.Frame(self, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
        marco_matriz.pack_propagate(False)
        marco_matriz.place(x = 310 - self.tamano_matriz * 6, y = 120)

        # Imprimir índices de columnas
        for j, index in enumerate(self.columnas_indices):
            label = tk.Label(marco_matriz, text=index, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=0, column=j + 1, padx=15, pady=5)

        # Imprimir la matriz de caminos ordenada por filas
        for i, fila in enumerate(self.matriz_caminos_filas):
            label = tk.Label(marco_matriz, text=self.filas_indices_ordenada[i] + 1, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
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
            command=self.Form_Paso4
        )
        
        self.boton_Anterior.place(x = 50, y = 270 + self.tamano_matriz * 30)
        self.boton_Anterior.config(width = 15, height = 1)

        self.boton_Continuar.place(x = 550 + self.tamano_matriz * 28, y = 270 + self.tamano_matriz * 30)
        self.boton_Continuar.config(width = 15, height = 1)

    def Form_Paso4(self):
        paso4 = Formulario_Componentes_Conexas(self.matriz_caminos_filas, self.filas_indices_ordenada, self.columnas_indices)
        self.withdraw()
        self.withdraw()
        paso4.grab_set()
        self.wait_window(paso4)
        self.deiconify()
