import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import	Controlador, Guardar_MatrizAdyacencia
from PIL import Image, ImageTk
import Util.util_ventana as util_ventana
from Util.util_imagenes import resourse_path
import numpy as np

class Formulario_Componentes_Conexas(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_caminos_filas, filas_indices_ordenada, columnas_indices_ordenda):
        super().__init__()
        self.control = Controlador()
        self.matriz_load = Guardar_MatrizAdyacencia()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        self.matriz_caminos_filas = matriz_caminos_filas
        self.filas_indices_ordenada = filas_indices_ordenada
        self.columnas_indices_ordenada = [indice + 1 for indice in filas_indices_ordenada]
        self.matriz_adyacencia = self.matriz_load.get_matrizAdyacencia()
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.componentes_conexas = []
        self.Algoritmo_Tarjan()
        self.botones()
        self.ordenar_columnas()
        self.imprimir_matriz()
        self.resizable(0, 0)
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Componentes Conexas - Paso 4')
        self.iconbitmap(resourse_path("./Imagenes/grafo.ico"))
        w, h = (660 + self.tamano_matriz * 50), (380 + self.tamano_matriz * 30)  # Ajustar el tamaño dinámicamente
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
            text = "Componentes Conexas",
            font = ("Arial", 20, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.labelTitulo.pack(side = tk.TOP, pady = 10)
        self.labelTitulo.place(x = 130, y = 45)

    def color_background(self):
        #Color de fondo de la ventana
        self.configure(bg= COLOR_BACKGROUND)

    def Algoritmo_Tarjan(self):
        self.indice = 0
        self.pila = []
        self.lowlink = [0] * self.tamano_matriz
        self.indices = [-1] * self.tamano_matriz
        self.en_pila = [False] * self.tamano_matriz

        for v in range(self.tamano_matriz):
            if self.indices[v] == -1:
                self.fuerte_conectar(v)
        
        #Invertir el orden de los componentes conexos
        self.componentes_conexas.reverse()

        #Posición inicial para los Labels de componentes
        y_offset = -150 + self.tamano_matriz * 28
        
        self.componentes_conexas_Text = tk.Label(
            self, 
            text = "Las Componentes Conexas son: ",
            font = ("Arial", 12, "bold"), 
            bg = COLOR_BACKGROUND
        )

        self.componentes_conexas_Text.place(x = 380 + self.tamano_matriz * 35, y = -180 + self.tamano_matriz * 28)

        for idx, componente in enumerate(self.componentes_conexas):
            label_componente = tk.Label(
                self,
                text=f"V{idx + 1}: {componente}",
                font=("Arial", 12),
                bg=COLOR_BACKGROUND
            )

            label_componente.place(x = 400 + self.tamano_matriz * 35, y=y_offset + (idx * 25))

        #Mostrar los componentes conexas después de ejecutar el algoritmo
        for idx, componente in enumerate(self.componentes_conexas):
            print(f"Componente fuertemente conectado {idx + 1}: {componente}")

    def fuerte_conectar(self, v):
        self.indices[v] = self.indice
        self.lowlink[v] = self.indice
        self.indice += 1
        self.pila.append(v)
        self.en_pila[v] = True

        for w in range(self.tamano_matriz):
            if self.matriz_adyacencia[v][w]:  #Si hay una arista de v a w
                if self.indices[w] == -1:  #w no ha sido visitado
                    self.fuerte_conectar(w)
                    self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
                elif self.en_pila[w]:  #w está en la pila
                    self.lowlink[v] = min(self.lowlink[v], self.indices[w])

        #Si v es un nodo raíz, genera un componente fuertemente conectado
        if self.lowlink[v] == self.indices[v]:
            componente = []
            while True:
                w = self.pila.pop()
                self.en_pila[w] = False
                componente.append(w + 1)
                if w == v:
                    break
            self.componentes_conexas.append(componente)

    def ordenar_columnas(self):
        self.matriz_caminos_ordenada = np.array(self.matriz_caminos_filas)

        #Ordenar las columnas de acuerdo al orden de las filas
        self.matriz_caminos_columnas = self.matriz_caminos_ordenada[:, self.filas_indices_ordenada]

    def imprimir_matriz(self):

        marco_matriz = tk.Frame(self, highlightbackground = COLOR_BORDE_BTN, highlightthickness = 1)
        marco_matriz.pack_propagate(False)
        marco_matriz.place(x = 150 - self.tamano_matriz * 6, y = 120)

        # Imprimir índices de columnas
        for j, index in enumerate(self.columnas_indices_ordenada):
            label = tk.Label(marco_matriz, text=index, font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
            label.grid(row=0, column=j + 1, padx=15, pady=5)

        # Imprimir la matriz de caminos ordenada por filas
        for i, fila in enumerate(self.matriz_caminos_columnas):
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

        self.boton_Anterior.place(x = 250 + self.tamano_matriz * 50, y = 270 + self.tamano_matriz * 30)
        self.boton_Anterior.config(width = 15, height = 1)
        
