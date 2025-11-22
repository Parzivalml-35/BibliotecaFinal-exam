# 🎨 GUÍA COMPLETA DE TKINTER

## Tabla de Contenidos
1. [¿Qué es Tkinter?](#qué-es-tkinter)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Componentes Básicos](#componentes-básicos)
4. [Gestores de Diseño](#gestores-de-diseño)
5. [Eventos y Funciones](#eventos-y-funciones)
6. [Proyecto Completo](#proyecto-completo)

---

## ¿Qué es Tkinter?

**Tkinter** es una librería de Python que permite crear **interfaces gráficas de usuario (GUI)**.

### Características:
- ✅ Incluida por defecto en Python
- ✅ Fácil de aprender
- ✅ Multiplataforma (Windows, Mac, Linux)
- ✅ Perfecta para proyectos pequeños y medianos
- ✅ No requiere instalación adicional

### ¿Para qué sirve?

En lugar de que tu usuario escriba comandos en la terminal, puede hacer clic en botones, rellenar formularios, ver listas, etc.

---

## Conceptos Fundamentales

### 1. **Window (Ventana Principal)**
Es el contenedor principal donde van todos tus elementos.

```python
import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Mi Primera Aplicación")  # Título de la ventana
root.geometry("800x600")              # Ancho x Alto en píxeles
root.resizable(False, False)          # No permite redimensionar

root.mainloop()  # Inicia la aplicación
```

**Explicación:**
- `tk.Tk()`: Crea la ventana principal
- `mainloop()`: Mantiene la ventana activa escuchando eventos

---

### 2. **Widgets (Componentes)**
Son los elementos visuales que ves en la pantalla.

```python
import tkinter as tk

root = tk.Tk()
root.title("Widgets")

# WIDGET: Etiqueta (Label)
etiqueta = tk.Label(root, text="Hola Mundo", font=("Arial", 20))
etiqueta.pack()  # Mostrar en pantalla

# WIDGET: Botón
boton = tk.Button(root, text="Click aquí")
boton.pack()

# WIDGET: Entrada de texto
entrada = tk.Entry(root, width=30)
entrada.pack()

root.mainloop()
```

---

### 3. **Variables en Tkinter**
Para obtener datos de los widgets, usamos variables especiales de Tkinter.

```python
import tkinter as tk

root = tk.Tk()

# Variable de Tkinter
variable_texto = tk.StringVar()

entrada = tk.Entry(root, textvariable=variable_texto)
entrada.pack()

def mostrar_valor():
    valor = variable_texto.get()  # Obtener el valor
    print(f"Escribiste: {valor}")

boton = tk.Button(root, text="Mostrar", command=mostrar_valor)
boton.pack()

root.mainloop()
```

**Tipos de Variables:**
- `tk.StringVar()`: Texto
- `tk.IntVar()`: Números enteros
- `tk.DoubleVar()`: Números decimales
- `tk.BooleanVar()`: Verdadero/Falso

---

## Componentes Básicos

### Label (Etiqueta)
Muestra texto o imágenes.

```python
etiqueta = tk.Label(
    root, 
    text="Hola",
    font=("Arial", 14),        # Fuente y tamaño
    fg="blue",                 # Color del texto (foreground)
    bg="yellow",               # Color de fondo (background)
    width=20,                  # Ancho
    height=3                   # Alto
)
etiqueta.pack()
```

---

### Entry (Campo de Entrada)
Para que el usuario escriba texto.

```python
var = tk.StringVar()
entrada = tk.Entry(
    root,
    textvariable=var,
    font=("Arial", 12),
    width=30,
    show="*"  # Para contraseñas (oculta el texto)
)
entrada.pack()

# Obtener valor
valor = var.get()

# Establecer valor
var.set("Texto predeterminado")

# Limpiar
var.set("")
```

---

### Button (Botón)
Ejecuta una función cuando se presiona.

```python
def mi_funcion():
    print("¡Botón presionado!")

boton = tk.Button(
    root,
    text="Presióname",
    command=mi_funcion,        # Función sin paréntesis ()
    bg="green",
    fg="white",
    font=("Arial", 12),
    width=20,
    height=2,
    cursor="hand2"             # Cambiar cursor al pasar
)
boton.pack()
```

---

### Listbox (Lista)
Muestra una lista de elementos.

```python
lista = tk.Listbox(root, height=5, width=30)
lista.pack()

# Agregar elementos
lista.insert(0, "Elemento 1")
lista.insert(1, "Elemento 2")
lista.insert(2, "Elemento 3")

# Obtener elemento seleccionado
def mostrar_seleccion():
    seleccionado = lista.curselection()  # Retorna tupla con índice
    if seleccionado:
        valor = lista.get(seleccionado[0])
        print(f"Seleccionaste: {valor}")

boton = tk.Button(root, text="Ver selección", command=mostrar_seleccion)
boton.pack()
```

---

### Combobox (Desplegable)
Lista desplegable con opciones predefinidas.

```python
from tkinter import ttk

var_combo = tk.StringVar()
combo = ttk.Combobox(
    root,
    textvariable=var_combo,
    values=["Opción 1", "Opción 2", "Opción 3"],
    state="readonly"  # No permite escribir
)
combo.pack()

# Obtener selección
seleccion = var_combo.get()
```

---

### Checkbutton (Casilla de Verificación)
Para opciones booleanas (Sí/No, activar/desactivar).

```python
var_check = tk.BooleanVar()
checkbox = tk.Checkbutton(
    root,
    text="¿Aceptas los términos?",
    variable=var_check
)
checkbox.pack()

# Obtener valor
valor = var_check.get()  # True o False
```

---

### Radiobutton (Botones de Radio)
Seleccionar una opción entre varias (solo una).

```python
var_radio = tk.StringVar(value="opcion1")

radio1 = tk.Radiobutton(root, text="Opción 1", variable=var_radio, value="opcion1")
radio1.pack()

radio2 = tk.Radiobutton(root, text="Opción 2", variable=var_radio, value="opcion2")
radio2.pack()

radio3 = tk.Radiobutton(root, text="Opción 3", variable=var_radio, value="opcion3")
radio3.pack()

# Obtener selección
seleccion = var_radio.get()
```

---

### Text (Área de Texto)
Para párrafos largos.

```python
texto = tk.Text(root, height=10, width=50)
texto.pack()

# Agregar texto
texto.insert("1.0", "Contenido inicial")  # 1.0 = línea 1, columna 0

# Obtener todo el texto
contenido = texto.get("1.0", "end")

# Limpiar
texto.delete("1.0", "end")
```

---

### Frame (Marco)
Contenedor para agrupar otros widgets.

```python
# Marco principal
frame1 = tk.Frame(root, bg="lightblue", height=100)
frame1.pack(fill="x", padx=10, pady=10)

# Widgets dentro del marco
etiqueta = tk.Label(frame1, text="Estoy dentro del marco", bg="lightblue")
etiqueta.pack()

boton = tk.Button(frame1, text="Botón en marco")
boton.pack()
```

---

## Gestores de Diseño

Los gestores de diseño posicionan los widgets en la ventana. Hay 3 principales:

### 1. **pack()** - El más simple
Apila widgets uno encima del otro.

```python
widget.pack(
    side="top",        # top, bottom, left, right
    fill="both",       # x, y, both (rellena espacio)
    expand=True,       # Expande el widget
    padx=10,           # Espacio horizontal externo
    pady=10,           # Espacio vertical externo
)
```

---

### 2. **grid()** - El más potente
Usa una cuadrícula (filas y columnas).

```python
etiqueta = tk.Label(root, text="Nombre:")
etiqueta.grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(root)
entrada.grid(row=0, column=1, padx=5, pady=5)

boton = tk.Button(root, text="Enviar")
boton.grid(row=1, column=0, columnspan=2, pady=10)
```

**Parámetros:**
- `row`: Número de fila (0, 1, 2, ...)
- `column`: Número de columna (0, 1, 2, ...)
- `columnspan`: Ocupar múltiples columnas
- `rowspan`: Ocupar múltiples filas

---

### 3. **place()** - Posicionamiento absoluto
Define coordenadas exactas (x, y).

```python
widget.place(x=100, y=50, width=200, height=30)
```

⚠️ **NO MEZCLES los gestores** en la misma ventana.

---

## Eventos y Funciones

### Comando de Botón

```python
def accion():
    print("Evento ejecutado")

boton = tk.Button(root, text="Click", command=accion)
boton.pack()
```

---

### Vincular Teclas

```python
def tecla_presionada(event):
    print(f"Tecla presionada: {event.char}")

root.bind("<Key>", tecla_presionada)  # Cualquier tecla
root.bind("<Return>", lambda e: print("Enter presionado"))  # Enter específicamente
```

---

### Messagebox (Cuadros de Diálogo)

```python
from tkinter import messagebox

# Información
messagebox.showinfo("Título", "Mensaje informativo")

# Advertencia
messagebox.showwarning("Advertencia", "¡Cuidado!")

# Error
messagebox.showerror("Error", "Algo salió mal")

# Pregunta (retorna True/False)
respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro?")

# Entrada de texto
respuesta = messagebox.askstring("Entrada", "¿Cuál es tu nombre?")
```

---

### Temporizador

```python
def actualizar():
    print("Cada 1 segundo")
    root.after(1000, actualizar)  # Repetir cada 1000ms (1 segundo)

root.after(1000, actualizar)
```

---

## Proyecto Completo

Aquí está implementado tu Sistema de Biblioteca con Tkinter:

**Ver archivo: `gui_biblioteca.py`**

---

## Resumen Visual

```
┌─────────────────────────────────────┐
│  VENTANA TKINTER (root)             │
├─────────────────────────────────────┤
│ ┌─ FRAME 1 ──────────────────────┐  │
│ │ Label: "Nombre:"               │  │
│ │ Entry: [_________________]     │  │
│ └────────────────────────────────┘  │
│                                      │
│ ┌─ FRAME 2 ──────────────────────┐  │
│ │ Button: [Registrar]            │  │
│ │ Button: [Limpiar]              │  │
│ └────────────────────────────────┘  │
│                                      │
│ ┌─ FRAME 3 ──────────────────────┐  │
│ │ Listbox:                       │  │
│ │ ├─ Elemento 1                  │  │
│ │ ├─ Elemento 2                  │  │
│ │ └─ Elemento 3                  │  │
│ └────────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## Tips Importantes

1. **Siempre usa `root.mainloop()` al final**
2. **Las funciones en `command` NO llevan paréntesis**: `command=mi_funcion` ❌ `command=mi_funcion()`
3. **Para pasar argumentos usa `lambda`**: `command=lambda: mi_funcion(arg)`
4. **Organiza el código en clases** para proyectos grandes
5. **Usa `grid()` para formularios**, `pack()` para listas simples
6. **Separa lógica de interfaz** (GUI vs lógica de negocio)

---

**¡Ahora vamos a implementarlo con tu proyecto!**
