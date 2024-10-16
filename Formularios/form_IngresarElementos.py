import tkinter as tk
from tkinter import font
from config import COLOR_BTN, COLOR_BTN_CONFIRMACION, COLOR_CURSOR_ENCIMA, COLOR_BACKGROUND, COLOR_BACKGROUND_IMAGENES, COLOR_BORDE_LOGO, COLOR_BORDE_BTN, COLOR_PANEL, COLOR_BTN_INSTRUCIONES, COLOR_BORDE_INSTRUCIONES
import Util.util_ventana as util_ventana
from Util.util_imagenes import resourse_path
import random
import controlador as Control
from PIL import Image, ImageTk
from Formularios.form_MatrizDeAdyacencia import Formulario_MatrizDeAdyacencia

class Formulario_IngresarElementos(tk.Toplevel):
    #Constructor de la clase
    def __init__(self, tamaño_matriz):
        super().__init__()
        self.tamano_matriz = tamaño_matriz
        self.logo = Image.open(resourse_path("./Imagenes/UPC_logo.png"))
        self.logo = self.logo.resize((80,80))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.entries = []  #Entradas de la matriz
        self.filas_indices = list(range(self.tamano_matriz))
        self.columnas_indices = list(range(1, self.tamano_matriz + 1))
        self.config_window()
        self.colocar_Logo()
        self.colocar_Titulo()
        self.color_background()
        self.crear_matriz_adyacencia()
        self.botones_inferiores()
        self.botones_superiores()
        self.resizable(0, 0)
        
    def config_window(self):
        #Configuración de la ventana inicial
        self.title('Ingresar elementos')
        self.iconbitmap(resourse_path("./Imagenes/grafo.ico"))
        w, h = (770 + self.tamano_matriz * 25), (350 + self.tamano_matriz * 30)  #Ajustar el tamaño dinámicamente
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

    def crear_matriz_adyacencia(self):
        frame_matriz = tk.Frame(self)
        frame_matriz.pack_propagate(False)
        frame_matriz.place(x = 315 - self.tamano_matriz * 5, y = 120)
        
        #Crear los índices de filas y columnas
        for i in range(self.tamano_matriz + 1):
            fila_entries = []
            for j in range(self.tamano_matriz + 1):
                if i == 0 and j > 0:
                    #Índices de columnas
                    label = tk.Label(frame_matriz, text=f"{j}", font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
                    label.grid(row=i, column=j, padx=5, pady=5)
                elif j == 0 and i > 0:
                    #Índices de filas
                    label = tk.Label(frame_matriz, text=f"{i}", font=("Arial", 12, "bold"), bg=COLOR_BACKGROUND)
                    label.grid(row=i, column=j, padx=5, pady=5)
                elif i > 0 and j > 0:
                    #Entradas para la matriz
                    entry = tk.Entry(frame_matriz, width=5, justify='center')
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    self.entries.append(entry)

    def botones_inferiores(self):
        #Crear botones para obtener los valores de la matriz
        self.boton_Continuar = tk.Button(
            self,
            text = "Continuar",
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black",
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5,
            activebackground = COLOR_CURSOR_ENCIMA,
            activeforeground = "black",
            relief = tk.FLAT,
            command=self.Form_Paso1
        )

        self.boton_Random = tk.Button(
            self, 
            text = "Random", 
            font = ("Arial", 14), 
            bg = COLOR_BTN, 
            fg = "black",
            highlightbackground = COLOR_BORDE_BTN,
            highlightthickness = 5,
            activebackground = COLOR_CURSOR_ENCIMA,
            activeforeground = "black",
            relief = tk.FLAT,
            command=self.obtener_valores_Random
        )
        
        self.boton_Random.place(x = 50, y = 260 + self.tamano_matriz * 30)
        self.boton_Random.config(width = 15, height = 1)

        self.boton_Continuar.place(x = 500 + self.tamano_matriz * 28, y = 260 + self.tamano_matriz * 30)
        self.boton_Continuar.config(width = 15, height = 1)

    def botones_superiores(self):
        img1 = Image.open(resourse_path("./Imagenes/return.png"))
        img1 = img1.resize((50,40))
        self.image_return = ImageTk.PhotoImage(img1)

        img2 = Image.open(resourse_path("./Imagenes/completar.png"))
        img2 = img2.resize((50,40))
        self.image_completar = ImageTk.PhotoImage(img2)

        self.boton_Completar = tk.Button(
            self,
            borderwidth=0,
            image=self.image_completar,
            command=self.completar_con_ceros
        )

        self.boton_Volver = tk.Button(
            self,
            borderwidth=0,
            image=self.image_return,
            command=self.destroy
        )

        self.boton_Completar.place(x = 530 + self.tamano_matriz * 30, y = 40)
        self.boton_Volver.place(x = 600 + self.tamano_matriz * 30, y = 40)
    
    def completar_con_ceros(self):
        for entry in self.entries:
            if entry.get() == "":
                entry.insert(0, "0")

    def obtener_valores_Random(self):
        for entry in self.entries:
            valor_aleatorio = random.randint(0, 1)  #Generar un 0 o un 1
            entry.delete(0, tk.END)
            entry.insert(0, int(valor_aleatorio)) 

    def validar_matriz(self):
        #Recorrer cada entrada en la lista plana de self.entries
        for entry in self.entries:
            valor = entry.get()
            try:
                valor_int = int(valor)
                if valor_int not in [0, 1]:
                    return False
            except ValueError:
                return False
        return True
    
    def guardar_matriz(self):
        if self.validar_matriz():
            matriz_guardada = []
            for i in range(self.tamano_matriz):
                fila_valores = [int(self.entries[i * self.tamano_matriz + j].get()) for j in range(self.tamano_matriz)]
                matriz_guardada.append(fila_valores)
            self.matriz_guardada = matriz_guardada
            self.indices_filas_guardados = self.filas_indices
            self.indices_columnas_guardados = self.columnas_indices
        else:
            tk.messagebox.showerror("Error", "Todos los valores deben ser 0 o 1.")
    
    def Form_Paso1(self):
        if self.validar_matriz():
            self.guardar_matriz() 
            if hasattr(self, 'matriz_guardada'):  #Verificar que la matriz se ha guardado correctamente
                Control.Guardar_MatrizAdyacencia().set_matrizAdyacencia(self.matriz_guardada)
                paso1 = Formulario_MatrizDeAdyacencia(self.matriz_guardada,self.indices_filas_guardados,self.indices_columnas_guardados)
                self.withdraw()
                self.withdraw()
                paso1.grab_set()
                self.wait_window(paso1)
                self.deiconify()
            else:
                tk.messagebox.showerror("Error", "Ocurrió un problema al guardar la matriz.")
        else:
            tk.messagebox.showerror("Error", "Todos los valores deben ser 0 o 1.")