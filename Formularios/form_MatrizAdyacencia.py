import tkinter as tk
from tkinter import font
from tkinter import messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import Controlador, Guardar_MatrizAdyacencia
from PIL import Image, ImageTk
import Util.util_ventana as util_ventana
from Util.util_imagenes import resourse_path
from Formularios.form_MatrizDiagonal import Formulario_Matrizdiagonal
import copy
import networkx as nx
import matplotlib.pyplot as plt

class Formulario_MatrizAdyacencia(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_adyacencia_c, filas_indices, columnas_indices):
        super().__init__()
        self.control = Controlador()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        self.matriz_adyacencia_c = matriz_adyacencia_c
        self.filas_indices = filas_indices
        self.columnas_indices = columnas_indices
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.botones()
        self.imprimir_matriz()
        self.resizable(0, 0)
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Matriz Adyacencia')
        self.iconbitmap(resourse_path("./Imagenes/grafo.ico"))
        w, h = (860 + self.tamano_matriz * 25), (380 + self.tamano_matriz * 30)  #Ajustar el tamaño dinámicamente
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

    def imprimir_matriz(self):
        marco_matriz = tk.Frame(self, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
        marco_matriz.pack_propagate(False)
        marco_matriz.place(x = 310 - self.tamano_matriz * 6, y = 120) #Ajustar la posición del frame según sea necesario

        #Imprimir índices de columnas
        for j, index in enumerate(self.columnas_indices):
            label = tk.Label(marco_matriz, text=index, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=0, column=j + 1, padx=15, pady=5)

        #Imprimir la matriz de adyacencia
        for i, fila in enumerate(self.matriz_adyacencia_c):
            label = tk.Label(marco_matriz, text=self.filas_indices[i] + 1, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=i + 1, column=0, padx=10, pady=5)

            for j, valor in enumerate(fila):
                label = tk.Label(marco_matriz, text=valor, font=("Arial", 12), bg= COLOR_BLANCO, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
                label.grid(row=i + 1, column=j + 1, padx=15, pady=5)

    def botones(self):
        img_grah = Image.open(resourse_path("./Imagenes/Grafo.png"))
        img_grah = img_grah.resize((50,40))
        self.image_grafo = ImageTk.PhotoImage(img_grah)

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
            command=self.Form_Paso1
        )

        self.boton_Grafo = tk.Button (
            self,
            borderwidth=0,
            image=self.image_grafo,
            command=self.generar_Grafo
        )
        
        self.boton_Anterior.place(x = 50, y = 270 + self.tamano_matriz * 30)
        self.boton_Anterior.config(width = 15, height = 1)

        self.boton_Continuar.place(x = 550 + self.tamano_matriz * 28, y = 270 + self.tamano_matriz * 30)
        self.boton_Continuar.config(width = 15, height = 1)

        self.boton_Grafo.place(x = 600 + self.tamano_matriz * 30, y = 40)

    def generar_Grafo(self):
        #Crear el grafo
        G = nx.DiGraph()

        #Agregar nodos
        for i in range(self.tamano_matriz):
            G.add_node(self.filas_indices[i] + 1) 

        #Agregar aristas basadas en la matriz de adyacencia
        for i, fila in enumerate(self.matriz_adyacencia_c):
            for j, valor in enumerate(fila):
                if valor == 1:  # Si hay una arista entre i y j
                    G.add_edge(self.filas_indices[i] + 1, self.filas_indices[j] + 1)

        #Dibujar el grafo
        plt.figure(figsize=(6 + (self.tamano_matriz / 2), 6 + (self.tamano_matriz / 8)))
        pos = nx.spring_layout(G, seed=42, scale=2)
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700, font_size=10)
        plt.title("Grafo dirigido")
        plt.show()
        
    def Form_Paso1(self):
        paso1 = Formulario_Matrizdiagonal(copy.deepcopy(self.matriz_adyacencia_c), copy.deepcopy(self.filas_indices), self.columnas_indices)
        self.withdraw()
        paso1.grab_set()
        self.wait_window(paso1)
        self.deiconify()