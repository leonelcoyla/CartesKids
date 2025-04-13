import tkinter as tk
from tkinter import Menu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from PIL import Image, ImageTk

class GraficoApp:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.puntos = []
        
        # Título
        self.size_label = tk.Label(contenedor, text="PLANO CARTESIANO", bg='#FFD700', font=("Comic Sans MS", 16, "bold"))
        self.size_label.pack(pady=10)

        # Ingreso de datos de las variables X,Y
        entrada_frame = tk.Frame(contenedor, bg='#FFD700')
        entrada_frame.pack(pady=5)
        tk.Label(entrada_frame, text="Ingrese X:", bg='#FFD700', font=("Comic Sans MS", 12)).pack(side=tk.LEFT, padx=5)
        self.entry_x = tk.Entry(entrada_frame, font=("Comic Sans MS", 12))
        self.entry_x.pack(side=tk.LEFT, padx=5)

        entrada_frame_y = tk.Frame(contenedor, bg='#FFD700')
        entrada_frame_y.pack(pady=5)
        tk.Label(entrada_frame_y, text="Ingrese Y:", bg='#FFD700', font=("Comic Sans MS", 12)).pack(side=tk.LEFT, padx=5)
        self.entry_y = tk.Entry(entrada_frame_y, font=("Comic Sans MS", 12))
        self.entry_y.pack(side=tk.LEFT, padx=5)


        # Botones en una sola fila
        botones_frame = tk.Frame(contenedor, bg='#FFD700')
        botones_frame.pack(pady=10)

        # Crear los botones con el mismo tamaño y más grandes
        self.agregar_button = tk.Button(botones_frame, text="Agregar Punto", command=self.agregarPuntos, 
                                     bg='#FF69B4', font=("Comic Sans MS", 12), width=20)  
        self.agregar_button.pack(side=tk.LEFT, padx=5, expand=True)

        self.dibujar_button = tk.Button(botones_frame, text="Graficar", command=self.dibujaPuntos, 
                                      bg='#87CEEB', font=("Comic Sans MS", 12), width=20)  
        self.dibujar_button.pack(side=tk.LEFT, padx=5, expand=True)

        self.eliminar_button = tk.Button(botones_frame, text="Eliminar Datos", command=self.eliminarDatos, 
                                      bg='#FF6347', font=("Comic Sans MS", 12), width=20)  
        self.eliminar_button.pack(side=tk.LEFT, padx=5, expand=True)

        # Crea el gráfico
        self.figure, self.ejes = plt.subplots(figsize=(5, 5))
        self.ejes.set_facecolor('#FFFACD')
        self.canvas = FigureCanvasTkAgg(self.figure, master=contenedor)
        self.canvas.get_tk_widget().pack(pady=10)

        # Configurar ejes
        self.ejes.set_xlim(0, 10)
        self.ejes.set_ylim(0, 10)
        self.ejes.xaxis.set_major_locator(MultipleLocator(1))
        self.ejes.yaxis.set_major_locator(MultipleLocator(1))
        self.ejes.grid(True, linestyle='--', linewidth=0.5)

        # Etiquetas para mostrar mensajes de error y éxito
        self.error_label = tk.Label(contenedor, text="", bg='#FFD700', fg='red', font=("Comic Sans MS", 12))
        self.error_label.pack(pady=5)  
        
        self.success_label = tk.Label(contenedor, text="", bg='#FFD700', fg='green', font=("Comic Sans MS", 12))
        self.success_label.pack(pady=5)  

    def agregarPuntos(self):
        x_texto = self.entry_x.get()
        y_texto = self.entry_y.get()

        try:
            x = float(x_texto)
            y = float(y_texto)

            # Comprobar si los valores se encuentran dentro del rango permitido (de 0 a 10).
            if not (0 <= x <= 10 and 0 <= y <= 10):
                raise ValueError("Los valores deben estar entre 0 y 10.")

            self.puntos.append((x, y))
            self.error_label.config(text="")  # Borrar el mensaje de error
            self.success_label.config(text=f"Punto ({x}, {y}) agregado.")  # Muestra mensaje de éxito
            self.entry_x.delete(0, tk.END)
            self.entry_y.delete(0, tk.END)

        except ValueError as e:
            self.error_label.config(text=f"Error: Ingrese solo valores numéricos válidos.")  # Muestra mensaje de error
            self.success_label.config(text="")  # Borrar el mensaje de éxito.

    def dibujaPuntos(self):
        if not self.puntos:
            return
        self.ejes.clear()
        self.ejes.set_facecolor('#FFFACD')
        self.ejes.set_xlim(0, 10)
        self.ejes.set_ylim(0, 10)
        self.ejes.xaxis.set_major_locator(MultipleLocator(1))
        self.ejes.yaxis.set_major_locator(MultipleLocator(1))
        x_vals, y_vals = zip(*self.puntos)
        self.ejes.scatter(x_vals, y_vals, color='red', label='Puntos ingresados')
        self.ejes.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=1)
        self.ejes.axhline(0, color='black', linewidth=0.5)
        self.ejes.axvline(0, color='black', linewidth=0.5)
        self.ejes.grid(True, linestyle='--', linewidth=0.5)
        self.ejes.set_xlabel("Eje X")
        self.ejes.set_ylabel("Eje Y")
        self.ejes.set_title("Gráfico de Puntos")
        self.canvas.draw()

    def eliminarDatos(self):
        """Eliminar los puntos y actualizar el gráfico"""
        self.puntos.clear()  # Eliminar los puntos de la lista
        self.ejes.clear()  # Limpiar el gráfico
        self.ejes.set_facecolor('#FFFACD')
        self.ejes.set_xlim(0, 10)
        self.ejes.set_ylim(0, 10)
        self.ejes.xaxis.set_major_locator(MultipleLocator(1))
        self.ejes.yaxis.set_major_locator(MultipleLocator(1))
        self.ejes.grid(True, linestyle='--', linewidth=0.5)
        self.ejes.set_xlabel("Eje X")
        self.ejes.set_ylabel("Eje Y")
        self.ejes.set_title("Gráfico de Puntos")
        self.canvas.draw()  # Redibujar el gráfico
        self.error_label.config(text="")  # Borrar el mensaje de error
        self.success_label.config(text="Datos eliminados.")  # Mensaje de éxito

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación Educativa")
        self.ventana.geometry("650x850")
        self.ventana.configure(bg="#FFD700")

        # Menú
        self.menu = Menu(ventana)
        ventana.config(menu=self.menu)

        menuPrincipal = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menú", menu=menuPrincipal)
        menuPrincipal.add_command(label="Presentación", command=self.mostrarPresentacion)
        menuPrincipal.add_command(label="Plano Cartesiano", command=self.mostrarPlanoCartesiano)
        menuPrincipal.add_command(label="Ayuda", command=self.mostrarAyuda)
        menuPrincipal.add_command(label="Acerca de", command=self.mostrarAcerca)

        # Frame para mostrar los contenidos dinámicos
        self.frameContenido = tk.Frame(ventana, bg="#FFD700")
        self.frameContenido.pack(fill=tk.BOTH, expand=True)

    def limpiarFrame(self):
        for widget in self.frameContenido.winfo_children():
            widget.destroy()

    def mostrarPresentacion(self):
        self.limpiarFrame()
        tk.Label(self.frameContenido, text=" ", bg="#FFD700", font=("Comic Sans MS", 16, "bold")).pack(pady=20)
        
        tk.Label(self.frameContenido, text="Bienvenido a la Aplicación Educativa", bg="#FFD700", font=("Comic Sans MS", 16, "bold")).pack(pady=20)
        tk.Label(self.frameContenido, text="PLANO CARTESIANO", bg="#FFD700", font=("Comic Sans MS", 16, "bold")).pack(pady=20)
    # Cargar la imagen
        try:
            # Leer la imagen mediante PIL.
            image = Image.open("Puntos.png")  
            image = image.resize((400, 400))  
            image_tk = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.frameContenido, image=image_tk, bg="#FFD700")
            image_label.image = image_tk  # Mantiene una referencia a la imagen
            image_label.pack(pady=20)# Mostrar imagen
            
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        tk.Label(self.frameContenido, text="CartesKids", bg="#FFD700", font=("Comic Sans MS", 16, "bold")).pack(pady=20)


    def mostrarPlanoCartesiano(self):
        self.limpiarFrame()
        GraficoApp(self.frameContenido)

    def mostrarAyuda(self):
        self.limpiarFrame()
        
        tk.Label(self.frameContenido, text="\n\n\nINSTRUCCIONES DE USO", bg="#FFD700", font=("Comic Sans MS", 14)).pack(pady=20)

        tk.Label(
            self.frameContenido,
            text="1. Ingresa los valores X y Y en los campos correspondientes.\n"
                 "   Estos valores deben estar dentro del rango de 0 a 10.\n\n"
                 "2. Haz clic en el botón “Agregar Punto”.\n"
                 "   Esto registrará el par ordenado (X, Y).\n\n"
                 "3. Una vez ingresados todos los puntos que desees,\n"
                 "   pulsa el botón “Graficar” para visualizar los puntos en el plano cartesiano.\n\n"
                 "4. Si necesitas comenzar de nuevo,\n"
                 "   presiona el botón “Eliminar Datos” para limpiar todos los puntos y reiniciar el gráfico.",
            bg="#FFD700",
            font=("Comic Sans MS", 10),
            justify="center",
            anchor="w"
        ).pack(pady=20, fill='x', padx=20)





    def mostrarAcerca(self):
        self.limpiarFrame()
        tk.Label(self.frameContenido, text="\n\n\n\nAplicación creada para educación primaria.\nCartesKids v1.0", bg="#FFD700", font=("Comic Sans MS", 14,"bold")).pack(pady=20)
        # Listado de contenidos para las etiquetas.
        textos = [
            "\nDesarrollado por: Leonel Coyla Idme",
            "Alfredo Mamani Canqui",
            "Juan Reynaldo Paredes Quispe",
            "José Pánfilo Tito Lipa",
            "\nContacto: lcoyla@unap.edu.pe"
        ]

        # Construir las etiquetas utilizando un bucle.
        for texto in textos:
            tk.Label(self.frameContenido, text=texto, bg="#FFD700", font=("Comic Sans MS", 14)).pack(pady=4)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
