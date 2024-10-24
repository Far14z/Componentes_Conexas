import tkinter as tk
from tkinter import font
from tkinter import messagebox
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES, COLOR_MATRIZ, COLOR_BLANCO
from controlador import	Controlador, Guardar_MatrizAdyacencia, Guardar_IndiceFila
from PIL import Image, ImageTk
import Util.util_ventana as util_ventana
from Util.util_imagenes import resourse_path
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Formulario_Componentes_Conexas(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, matriz_caminos_filas, filas_indices_ordenada, columnas_indices_ordenda):
        super().__init__()
        #Obtener el tamaño n x n de la matriz de adyacencia
        self.control = Controlador()
        self.tamano_matriz = self.control.get_tamanoMatrizAdyacencia()
        #obtener la matriz de adyacencia
        self.matriz_load = Guardar_MatrizAdyacencia()
        self.matriz_adyacencia = self.matriz_load.get_matrizAdyacencia()
        #obtener los indices de la fila de la matriz de adyacencia
        self.fila_load = Guardar_IndiceFila()
        self.indices_fila_original = self.fila_load.get_indicesFila()
        ##
        self.matriz_caminos_filas = matriz_caminos_filas
        self.filas_indices_ordenada = filas_indices_ordenada
        self.columnas_indices_ordenada = [indice + 1 for indice in filas_indices_ordenada]
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

        print(self.filas_indices_ordenada)
        print(self.columnas_indices_ordenada)

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

    def generar_Grafo(self):
        #Crear el grafo dirigido
        G = nx.DiGraph()

        #Agregar nodos
        for i in range(self.tamano_matriz):
            G.add_node(self.indices_fila_original[i] + 1)

        #Agregar aristas basadas en la matriz de adyacencia
        for i, fila in enumerate(self.matriz_adyacencia):
            for j, valor in enumerate(fila):
                if valor == 1: 
                    G.add_edge(self.indices_fila_original[i] + 1, self.indices_fila_original[j] + 1)

        #Asignar colores a cada componente conexa
        color_map = []
        componentes_colores = {}
        for idx, componente in enumerate(self.componentes_conexas):
            color = plt.cm.get_cmap('tab10')(idx)  #Colores únicos para cada componente conexa
            for nodo in componente:
                componentes_colores[nodo] = color  #Asignar color a cada nodo

        #Crear el color map para los nodos del grafo
        for node in G.nodes():
            color_map.append(componentes_colores.get(node, "lightblue"))  # Si no está en una componente, color default

        plt.figure(figsize=(6 + (self.tamano_matriz / 2), 6 + (self.tamano_matriz / 8)))
        pos = nx.spring_layout(G, seed=42, scale=2)
        nx.draw(G, pos, with_labels=True, node_color=color_map, font_weight="bold", node_size=700, font_size=10)
        plt.title("Grafo con Componentes Conexas")
        plt.show()

    def botones(self):
        img_grah = Image.open(resourse_path("./Imagenes/Grafo.png"))
        img_grah = img_grah.resize((50,40))
        self.image_grafo = ImageTk.PhotoImage(img_grah)
    
        self.boton_Anterior = tk.Button(
            self,
            text = "Anterior",
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black",
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5,
            activebackground = COLOR_CURSOR_ENCIMA,
            activeforeground = "black",
            relief = tk.FLAT,
            command=self.destroy
        )

        self.boton_Grafo = tk.Button (
            self,
            borderwidth=0,
            image=self.image_grafo,
            command=self.generar_Grafo
        )

        self.boton_Anterior.place(x = 250 + self.tamano_matriz * 50, y = 270 + self.tamano_matriz * 30)
        self.boton_Anterior.config(width = 15, height = 1)

        self.boton_Grafo.place(x = 50, y = 270 + self.tamano_matriz * 30)
