# 01 EJEMPLOS TKINTER BÁSICOS

## 📌 MENÚ DE EJEMPLOS

Ejecuta: `python`

Luego copia y pega los ejemplos de abajo en la consola interactiva.

---

## EJEMPLO 1: Ventana Básica

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Primera Ventana")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="¡Hola Tkinter!")
etiqueta.pack()

ventana.mainloop()
```

**Salida:**
```
┌─ Mi Primera Ventana ─────────┐
│                              │
│   ¡Hola Tkinter!             │
│                              │
└──────────────────────────────┘
```

---

## EJEMPLO 2: Botón que Cuenta

```python
import tkinter as tk

def incrementar():
    global contador
    contador += 1
    etiqueta.config(text=f"Contador: {contador}")

ventana = tk.Tk()
ventana.title("Contador")

contador = 0

etiqueta = tk.Label(ventana, text="Contador: 0", font=("Arial", 20))
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Incrementar", command=incrementar)
boton.pack(pady=10)

ventana.mainloop()
```

---

## EJEMPLO 3: Formulario Simple

```python
import tkinter as tk
from tkinter import messagebox

def guardar():
    nombre = entrada_nombre.get()
    if nombre:
        messagebox.showinfo("Éxito", f"Hola {nombre}!")
    else:
        messagebox.showerror("Error", "Ingresa tu nombre")

ventana = tk.Tk()
ventana.title("Formulario")

label = tk.Label(ventana, text="¿Cuál es tu nombre?")
label.pack(pady=5)

entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

boton = tk.Button(ventana, text="Guardar", command=guardar)
boton.pack(pady=5)

ventana.mainloop()
```

---

## EJEMPLO 4: Lista de Tareas

```python
import tkinter as tk

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        listbox_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = listbox_tareas.curselection()
    if seleccion:
        listbox_tareas.delete(seleccion[0])

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("300x400")

label = tk.Label(ventana, text="Mis Tareas")
label.pack(pady=10)

entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
boton_agregar.pack(pady=5)

listbox_tareas = tk.Listbox(ventana, height=10)
listbox_tareas.pack(pady=10, fill=tk.BOTH, expand=True)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

ventana.mainloop()
```

---

## EJEMPLO 5: Calculadora Básica

```python
import tkinter as tk

def calcular():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        suma = a + b
        label_resultado.config(text=f"Suma: {suma}")
    except ValueError:
        label_resultado.config(text="Error: Números válidos")

ventana = tk.Tk()
ventana.title("Calculadora")

label_a = tk.Label(ventana, text="Número 1:")
label_a.pack(pady=5)
entrada_a = tk.Entry(ventana)
entrada_a.pack(pady=5)

label_b = tk.Label(ventana, text="Número 2:")
label_b.pack(pady=5)
entrada_b = tk.Entry(ventana)
entrada_b.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack(pady=10)

ventana.mainloop()
```

---

## EJEMPLO 6: Pestañas

```python
from tkinter import ttk
import tkinter as tk

ventana = tk.Tk()
ventana.title("Pestañas")

notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True)

# Pestaña 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Pestaña 1")
label1 = tk.Label(tab1, text="Contenido de la pestaña 1")
label1.pack(pady=20)

# Pestaña 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Pestaña 2")
label2 = tk.Label(tab2, text="Contenido de la pestaña 2")
label2.pack(pady=20)

ventana.mainloop()
```

---

## EJEMPLO 7: Validación de Entrada

```python
import tkinter as tk
from tkinter import messagebox

def validar_email():
    email = entrada_email.get()
    if "@" in email and "." in email:
        messagebox.showinfo("Válido", "Email válido")
    else:
        messagebox.showerror("Inválido", "Email inválido")

ventana = tk.Tk()
ventana.title("Validación")

label = tk.Label(ventana, text="Email:")
label.pack(pady=5)

entrada_email = tk.Entry(ventana, width=30)
entrada_email.pack(pady=5)

boton = tk.Button(ventana, text="Validar", command=validar_email)
boton.pack(pady=10)

ventana.mainloop()
```

---

## EJEMPLO 8: Grid Layout

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Grid Layout")

# Fila 0
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

# Fila 1
label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1, column=1, padx=5, pady=5)

# Botón que abarca 2 columnas
boton = tk.Button(ventana, text="Guardar")
boton.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()
```

---

## EJEMPLO 9: Colores y Estilos

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Estilos")
ventana.config(bg="#f0f0f0")

# Label con estilos
label = tk.Label(
    ventana,
    text="Hola Mundo",
    font=("Arial", 20, "bold"),
    bg="#007bff",
    fg="white",
    padx=20,
    pady=10
)
label.pack(pady=20)

# Botón con estilos
boton = tk.Button(
    ventana,
    text="Click",
    bg="#28a745",
    fg="white",
    font=("Arial", 14),
    padx=20,
    pady=10
)
boton.pack(pady=10)

ventana.mainloop()
```

---

## EJEMPLO 10: Clase y MVC

```python
import tkinter as tk

class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("MVC")
        self.contador = 0
        self.crear_interfaz()
    
    def crear_interfaz(self):
        self.label = tk.Label(self.ventana, text=f"Contador: {self.contador}")
        self.label.pack(pady=10)
        
        boton = tk.Button(self.ventana, text="Incrementar", command=self.incrementar)
        boton.pack(pady=10)
    
    def incrementar(self):
        self.contador += 1
        self.label.config(text=f"Contador: {self.contador}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MiAplicacion(ventana)
    ventana.mainloop()
```

---

**¡Copia y pega estos ejemplos! 🎉**

Siguiente: Lee ejemplos avanzados en `02_EJEMPLOS_AVANZADOS.md`
