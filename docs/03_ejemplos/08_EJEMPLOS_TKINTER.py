# ejemplos_tkinter.py - Ejemplos Progresivos de Tkinter

"""
Este archivo contiene ejemplos progresivos para aprender Tkinter.
Descomenta cada ejemplo para verlo en acción.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ===========================================================================
# EJEMPLO 1: HOLA MUNDO
# ===========================================================================

def ejemplo_1_hola_mundo():
    """Lo más básico: una ventana con un etiqueta"""
    root = tk.Tk()
    root.title("Ejemplo 1: Hola Mundo")
    root.geometry("300x100")
    
    etiqueta = tk.Label(root, text="¡Hola Mundo!", font=("Arial", 20))
    etiqueta.pack()
    
    root.mainloop()

# ejemplo_1_hola_mundo()


# ===========================================================================
# EJEMPLO 2: ENTRADA Y SALIDA
# ===========================================================================

def ejemplo_2_entrada_salida():
    """Obtener entrada del usuario y mostrar resultado"""
    root = tk.Tk()
    root.title("Ejemplo 2: Entrada y Salida")
    root.geometry("400x200")
    
    # Variable de Tkinter
    var_nombre = tk.StringVar()
    
    # Etiqueta
    etiqueta = tk.Label(root, text="¿Cuál es tu nombre?", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    # Campo de entrada
    entrada = tk.Entry(root, textvariable=var_nombre, width=30, font=("Arial", 12))
    entrada.pack(pady=10)
    
    # Función que se ejecuta al hacer click
    def saludar():
        nombre = var_nombre.get()
        messagebox.showinfo("Saludo", f"¡Hola {nombre}!")
        var_nombre.set("")  # Limpiar entrada
    
    # Botón
    boton = tk.Button(root, text="Saludar", command=saludar, bg="blue", fg="white")
    boton.pack(pady=10)
    
    root.mainloop()

# ejemplo_2_entrada_salida()


# ===========================================================================
# EJEMPLO 3: FORMULARIO CON GRID
# ===========================================================================

def ejemplo_3_formulario_grid():
    """Usar grid() para crear un formulario ordenado"""
    root = tk.Tk()
    root.title("Ejemplo 3: Formulario con Grid")
    root.geometry("400x300")
    
    # Variables
    var_usuario = tk.StringVar()
    var_correo = tk.StringVar()
    var_edad = tk.IntVar()
    
    # Título
    titulo = tk.Label(root, text="Formulario de Registro", font=("Arial", 14, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=20)
    
    # Usuario
    tk.Label(root, text="Usuario:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=var_usuario).grid(row=1, column=1, padx=10, pady=10)
    
    # Correo
    tk.Label(root, text="Correo:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=var_correo).grid(row=2, column=1, padx=10, pady=10)
    
    # Edad
    tk.Label(root, text="Edad:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=var_edad).grid(row=3, column=1, padx=10, pady=10)
    
    def enviar():
        usuario = var_usuario.get()
        correo = var_correo.get()
        edad = var_edad.get()
        messagebox.showinfo("Datos", f"Usuario: {usuario}\nCorreo: {correo}\nEdad: {edad}")
    
    # Botones
    tk.Button(root, text="Enviar", command=enviar, bg="green", fg="white", width=15).grid(row=4, column=0, pady=20)
    tk.Button(root, text="Limpiar", command=lambda: [var_usuario.set(""), var_correo.set(""), var_edad.set(0)], bg="orange", fg="white", width=15).grid(row=4, column=1, pady=20)
    
    root.mainloop()

# ejemplo_3_formulario_grid()


# ===========================================================================
# EJEMPLO 4: CHECKBUTTON Y RADIOBUTTON
# ===========================================================================

def ejemplo_4_checkbutton_radiobutton():
    """Casillas de verificación y botones de radio"""
    root = tk.Tk()
    root.title("Ejemplo 4: Checkbutton y Radiobutton")
    root.geometry("400x300")
    
    # Checkbutton
    tk.Label(root, text="Intereses:", font=("Arial", 12, "bold")).pack(pady=10)
    
    var_check1 = tk.BooleanVar()
    var_check2 = tk.BooleanVar()
    var_check3 = tk.BooleanVar()
    
    tk.Checkbutton(root, text="Programación", variable=var_check1).pack(anchor="w", padx=50)
    tk.Checkbutton(root, text="Diseño", variable=var_check2).pack(anchor="w", padx=50)
    tk.Checkbutton(root, text="Videojuegos", variable=var_check3).pack(anchor="w", padx=50)
    
    # Radiobutton
    tk.Label(root, text="Nivel de Experiencia:", font=("Arial", 12, "bold")).pack(pady=(20, 10))
    
    var_radio = tk.StringVar(value="principiante")
    
    tk.Radiobutton(root, text="Principiante", variable=var_radio, value="principiante").pack(anchor="w", padx=50)
    tk.Radiobutton(root, text="Intermedio", variable=var_radio, value="intermedio").pack(anchor="w", padx=50)
    tk.Radiobutton(root, text="Avanzado", variable=var_radio, value="avanzado").pack(anchor="w", padx=50)
    
    def ver_datos():
        intereses = []
        if var_check1.get():
            intereses.append("Programación")
        if var_check2.get():
            intereses.append("Diseño")
        if var_check3.get():
            intereses.append("Videojuegos")
        
        nivel = var_radio.get()
        
        mensaje = f"Intereses: {', '.join(intereses) if intereses else 'Ninguno'}\nNivel: {nivel}"
        messagebox.showinfo("Datos", mensaje)
    
    tk.Button(root, text="Ver Datos", command=ver_datos, bg="blue", fg="white").pack(pady=20)
    
    root.mainloop()

# ejemplo_4_checkbutton_radiobutton()


# ===========================================================================
# EJEMPLO 5: COMBOBOX (DESPLEGABLE)
# ===========================================================================

def ejemplo_5_combobox():
    """Usar Combobox (lista desplegable)"""
    root = tk.Tk()
    root.title("Ejemplo 5: Combobox")
    root.geometry("400x250")
    
    tk.Label(root, text="Selecciona tu país:", font=("Arial", 12)).pack(pady=20)
    
    var_pais = tk.StringVar()
    paises = ["México", "Argentina", "Chile", "Colombia", "España", "Perú"]
    
    combobox = ttk.Combobox(root, textvariable=var_pais, values=paises, state="readonly", width=30)
    combobox.pack(pady=10)
    
    def mostrar():
        if var_pais.get():
            messagebox.showinfo("Selección", f"Seleccionaste: {var_pais.get()}")
        else:
            messagebox.showwarning("Advertencia", "Selecciona un país primero")
    
    tk.Button(root, text="Confirmar", command=mostrar, bg="green", fg="white").pack(pady=20)
    
    root.mainloop()

# ejemplo_5_combobox()


# ===========================================================================
# EJEMPLO 6: LISTBOX
# ===========================================================================

def ejemplo_6_listbox():
    """Trabajar con Listbox (lista seleccionable)"""
    root = tk.Tk()
    root.title("Ejemplo 6: Listbox")
    root.geometry("400x400")
    
    tk.Label(root, text="Lista de Tareas:", font=("Arial", 12, "bold")).pack(pady=10)
    
    # Entrada para agregar tarea
    var_tarea = tk.StringVar()
    frame_entrada = tk.Frame(root)
    frame_entrada.pack(pady=10)
    
    tk.Entry(frame_entrada, textvariable=var_tarea, width=30).pack(side="left", padx=5)
    
    # Listbox
    listbox = tk.Listbox(root, height=10, width=40)
    listbox.pack(pady=10)
    
    def agregar_tarea():
        tarea = var_tarea.get()
        if tarea:
            listbox.insert(tk.END, tarea)
            var_tarea.set("")
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea")
    
    def eliminar_tarea():
        seleccion = listbox.curselection()
        if seleccion:
            listbox.delete(seleccion[0])
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
    
    tk.Button(frame_entrada, text="Agregar", command=agregar_tarea, bg="green", fg="white").pack(side="left")
    
    tk.Button(root, text="Eliminar Seleccionado", command=eliminar_tarea, bg="red", fg="white").pack(pady=10)
    
    root.mainloop()

# ejemplo_6_listbox()


# ===========================================================================
# EJEMPLO 7: TEXT (ÁREA DE TEXTO)
# ===========================================================================

def ejemplo_7_text():
    """Trabajar con área de texto"""
    root = tk.Tk()
    root.title("Ejemplo 7: Text (Área de Texto)")
    root.geometry("500x400")
    
    tk.Label(root, text="Editor de Texto:", font=("Arial", 12, "bold")).pack(pady=10)
    
    # Área de texto
    texto = tk.Text(root, height=15, width=50)
    texto.pack(pady=10)
    
    def guardar():
        contenido = texto.get("1.0", tk.END)
        with open("archivo.txt", "w") as f:
            f.write(contenido)
        messagebox.showinfo("Éxito", "Archivo guardado como 'archivo.txt'")
    
    def limpiar():
        texto.delete("1.0", tk.END)
    
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)
    
    tk.Button(frame_botones, text="Guardar", command=guardar, bg="blue", fg="white").pack(side="left", padx=5)
    tk.Button(frame_botones, text="Limpiar", command=limpiar, bg="orange", fg="white").pack(side="left", padx=5)
    
    root.mainloop()

# ejemplo_7_text()


# ===========================================================================
# EJEMPLO 8: FRAMES (ORGANIZACIÓN)
# ===========================================================================

def ejemplo_8_frames():
    """Usar Frames para organizar la interfaz"""
    root = tk.Tk()
    root.title("Ejemplo 8: Frames")
    root.geometry("500x400")
    
    # Frame superior (color rojo)
    frame_superior = tk.Frame(root, bg="lightblue", height=100)
    frame_superior.pack(fill="x")
    
    tk.Label(frame_superior, text="ENCABEZADO", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=20)
    
    # Frame central (color verde)
    frame_central = tk.Frame(root, bg="lightgreen")
    frame_central.pack(fill="both", expand=True)
    
    tk.Label(frame_central, text="Contenido Principal", bg="lightgreen").pack(pady=50)
    
    # Frame inferior (color rojo)
    frame_inferior = tk.Frame(root, bg="lightyellow", height=100)
    frame_inferior.pack(fill="x")
    
    tk.Label(frame_inferior, text="PIE DE PÁGINA", font=("Arial", 10), bg="lightyellow").pack(pady=20)
    
    root.mainloop()

# ejemplo_8_frames()


# ===========================================================================
# EJEMPLO 9: EVENTOS DE TECLADO
# ===========================================================================

def ejemplo_9_eventos_teclado():
    """Detectar teclas presionadas"""
    root = tk.Tk()
    root.title("Ejemplo 9: Eventos de Teclado")
    root.geometry("400x300")
    
    etiqueta = tk.Label(root, text="Presiona una tecla...", font=("Arial", 14))
    etiqueta.pack(pady=50)
    
    resultado = tk.Label(root, text="", font=("Arial", 12), fg="blue")
    resultado.pack()
    
    def tecla_presionada(event):
        if event.keysym == "Return":
            resultado.config(text="¡Presionaste ENTER!")
        elif event.keysym == "Escape":
            root.quit()
        else:
            resultado.config(text=f"Tecla presionada: {event.char} ({event.keysym})")
    
    root.bind("<Key>", tecla_presionada)
    root.mainloop()

# ejemplo_9_eventos_teclado()


# ===========================================================================
# EJEMPLO 10: TEMPORIZADOR
# ===========================================================================

def ejemplo_10_temporizador():
    """Ejecutar código cada cierto tiempo"""
    root = tk.Tk()
    root.title("Ejemplo 10: Temporizador")
    root.geometry("400x200")
    
    contador = tk.IntVar(value=0)
    
    etiqueta = tk.Label(root, textvariable=contador, font=("Arial", 40, "bold"))
    etiqueta.pack(pady=50)
    
    def incrementar():
        contador.set(contador.get() + 1)
        root.after(1000, incrementar)  # Repetir cada 1000ms (1 segundo)
    
    tk.Button(root, text="Iniciar Cuenta Atrás", command=incrementar, bg="green", fg="white").pack()
    
    root.mainloop()

# ejemplo_10_temporizador()


# ===========================================================================
# MENÚ INTERACTIVO
# ===========================================================================

def menu_ejemplos():
    """Menú para seleccionar qué ejemplo ejecutar"""
    print("\n" + "="*50)
    print("         EJEMPLOS PROGRESIVOS DE TKINTER")
    print("="*50)
    print("\n1. Hola Mundo")
    print("2. Entrada y Salida")
    print("3. Formulario con Grid")
    print("4. Checkbutton y Radiobutton")
    print("5. Combobox")
    print("6. Listbox")
    print("7. Área de Texto")
    print("8. Frames")
    print("9. Eventos de Teclado")
    print("10. Temporizador")
    print("\n0. Salir")
    
    opcion = input("\nSelecciona un ejemplo (0-10): ")
    
    ejemplos = {
        "1": ejemplo_1_hola_mundo,
        "2": ejemplo_2_entrada_salida,
        "3": ejemplo_3_formulario_grid,
        "4": ejemplo_4_checkbutton_radiobutton,
        "5": ejemplo_5_combobox,
        "6": ejemplo_6_listbox,
        "7": ejemplo_7_text,
        "8": ejemplo_8_frames,
        "9": ejemplo_9_eventos_teclado,
        "10": ejemplo_10_temporizador,
    }
    
    if opcion in ejemplos:
        print(f"\nEjecutando: {ejemplos[opcion].__doc__}\n")
        ejemplos[opcion]()
    elif opcion != "0":
        print("Opción inválida")


if __name__ == "__main__":
    menu_ejemplos()
