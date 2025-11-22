# 04 GUÍA COMPLETA DE TKINTER

## 📚 INDICE

1. [Conceptos Básicos](#conceptos-básicos)
2. [Estructura de una Aplicación](#estructura-de-una-aplicación)
3. [Widgets Principales](#widgets-principales)
4. [Layouts](#layouts)
5. [Eventos y Validación](#eventos-y-validación)
6. [Componentes Complejos](#componentes-complejos)
7. [Buenas Prácticas](#buenas-prácticas)

---

## CONCEPTOS BÁSICOS

### ¿Qué es Tkinter?

```python
# Tkinter es la librería GUI de Python
import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi App")
ventana.geometry("400x300")
ventana.mainloop()  # Inicia el loop de eventos
```

### Componentes Clave

```
Aplicación Tkinter
│
├─ Ventana Principal (Tk)
│  └─ Frames (contenedores)
│     ├─ Labels (etiquetas)
│     ├─ Entries (campos de texto)
│     ├─ Buttons (botones)
│     └─ Listboxes (listas)
│
└─ Event Loop (mainloop)
```

---

## ESTRUCTURA DE UNA APLICACIÓN

### Patrón MVC en Tkinter

```python
import tkinter as tk

class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi App")
        self.ventana.geometry("400x300")
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Aquí van todos los widgets
        pass
    
    def manejar_evento(self):
        # Aquí va la lógica
        pass

# Uso
if __name__ == "__main__":
    ventana = tk.Tk()
    app = MiAplicacion(ventana)
    ventana.mainloop()
```

### Ventaja del Patrón de Clase

```
✓ Código organizado
✓ Fácil de mantener
✓ Reutilizable
✓ Escalable
✓ Acceso a variables con self.variable
```

---

## WIDGETS PRINCIPALES

### 1. Label (Etiqueta)

```python
label = tk.Label(
    ventana,
    text="Hola Mundo",
    font=("Arial", 12),
    bg="lightblue",
    fg="black"
)
label.pack()
```

### 2. Entry (Campo de Texto)

```python
# Simple
entrada = tk.Entry(ventana, width=30)
entrada.pack()

# Obtener valor
valor = entrada.get()

# Limpiar
entrada.delete(0, tk.END)

# Con validación
entrada = tk.Entry(ventana)
entrada.pack()
```

### 3. Button (Botón)

```python
def mi_funcion():
    print("¡Presionado!")

boton = tk.Button(
    ventana,
    text="Click aquí",
    command=mi_funcion,
    bg="green",
    fg="white"
)
boton.pack()
```

### 4. Listbox (Lista)

```python
listbox = tk.Listbox(ventana, height=6, width=30)
listbox.pack()

# Insertar elementos
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")

# Obtener selección
seleccion = listbox.curselection()
if seleccion:
    valor = listbox.get(seleccion[0])

# Limpiar
listbox.delete(0, tk.END)
```

### 5. Frame (Contenedor)

```python
frame = tk.Frame(ventana, bg="white")
frame.pack(fill=tk.BOTH, expand=True)

# Agrupar widgets
label = tk.Label(frame, text="Dentro del frame")
label.pack()
```

### 6. Messagebox (Diálogos)

```python
from tkinter import messagebox

# Información
messagebox.showinfo("Título", "Mensaje de información")

# Error
messagebox.showerror("Error", "Algo salió mal")

# Pregunta (devuelve True/False)
if messagebox.askyesno("Confirmar", "¿Estás seguro?"):
    print("Sí presionado")
```

### 7. Text (Área de Texto)

```python
texto = tk.Text(ventana, height=10, width=40)
texto.pack()

# Insertar
texto.insert(tk.END, "Contenido")

# Obtener
contenido = texto.get("1.0", tk.END)

# Limpiar
texto.delete("1.0", tk.END)
```

---

## LAYOUTS

### Grid (Recomendado)

```python
# Organiza en filas y columnas
label = tk.Label(ventana, text="Nombre:")
label.grid(row=0, column=0)

entrada = tk.Entry(ventana)
entrada.grid(row=0, column=1)

boton = tk.Button(ventana, text="Enviar")
boton.grid(row=1, column=0, columnspan=2)

# Configurar proporciones
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(1, weight=1)
```

### Pack (Simple)

```python
# Apila widgets vertically
label.pack(side=tk.LEFT)
boton.pack(side=tk.RIGHT)
entrada.pack(fill=tk.BOTH, expand=True)
```

### Place (Posición Absoluta)

```python
# Coloca en coordenadas específicas
boton.place(x=50, y=100, width=100, height=30)
```

---

## EVENTOS Y VALIDACIÓN

### Vinculación de Eventos

```python
def al_hacer_click(evento):
    print(f"Click en ({evento.x}, {evento.y})")

boton.bind("<Button-1>", al_hacer_click)
ventana.bind("<Return>", al_hacer_click)  # Enter
ventana.bind("<Escape>", al_hacer_click)  # Escape
```

### Validación de Entrada

```python
def validar_numero(valor):
    if valor == "":
        return True
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Registrar validación
vcmd = (ventana.register(validar_numero), '%S')
entrada = tk.Entry(ventana, validate='key', validatecommand=vcmd)
entrada.pack()
```

### Variables Tkinter

```python
# StringVar
nombre = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=nombre)
print(nombre.get())  # Obtener valor
nombre.set("Nuevo valor")  # Establecer

# IntVar
edad = tk.IntVar(value=0)
edad.set(25)

# BooleanVar
activo = tk.BooleanVar(value=True)
```

---

## COMPONENTES COMPLEJOS

### Pestañas (Notebook)

```python
from tkinter import ttk

notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True)

# Crear pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Pestaña 1")
notebook.add(tab2, text="Pestaña 2")

# Agregar widgets a tab1
label = tk.Label(tab1, text="Contenido tab 1")
label.pack()
```

### Scrollbar

```python
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Listbox con scrollbar
listbox = tk.Listbox(frame, height=10)
scrollbar = tk.Scrollbar(frame, command=listbox.yview)

listbox.config(yscrollcommand=scrollbar.set)

listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Agregar elementos
for i in range(100):
    listbox.insert(tk.END, f"Item {i}")
```

### Tabla (Treeview)

```python
from tkinter import ttk

tree = ttk.Treeview(ventana, columns=("Nombre", "Edad"), height=10)
tree.column("#0", width=50)
tree.column("Nombre", width=150)
tree.column("Edad", width=100)

tree.heading("#0", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")

# Insertar fila
tree.insert("", 0, text="1", values=("Juan", 25))
tree.pack(fill=tk.BOTH, expand=True)
```

---

## BUENAS PRÁCTICAS

### 1. Estructura Organizad

```python
class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.datos = {}
        self.crear_interfaz()
        self.cargar_datos()
    
    def crear_interfaz(self):
        # Interfaces
        pass
    
    def crear_widgets(self):
        # Widgets
        pass
    
    def crear_eventos(self):
        # Eventos
        pass
    
    def cargar_datos(self):
        # Cargar datos
        pass
```

### 2. Separación de Responsabilidades

```python
# ❌ Malo: lógica en interfaz
def calcular_click():
    a = int(entrada1.get())
    b = int(entrada2.get())
    resultado = a + b
    label_resultado.config(text=str(resultado))

# ✓ Bien: separar lógica
def calcular(a, b):
    return a + b

def mostrar_resultado():
    a = int(self.entrada1.get())
    b = int(self.entrada2.get())
    resultado = self.calcular(a, b)
    self.label_resultado.config(text=str(resultado))
```

### 3. Validación Robusta

```python
def validar_entrada(self):
    """Valida campos antes de procesar"""
    nombre = self.entrada_nombre.get().strip()
    edad_str = self.entrada_edad.get().strip()
    
    if not nombre:
        messagebox.showerror("Error", "Nombre requerido")
        return False
    
    try:
        edad = int(edad_str)
        if edad < 0 or edad > 150:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Edad debe ser número 0-150")
        return False
    
    return True
```

### 4. Manejo de Errores

```python
def procesar_datos(self):
    try:
        if not self.validar_entrada():
            return
        
        resultado = self.logica_negocio()
        self.actualizar_interfaz(resultado)
        messagebox.showinfo("Éxito", "Operación completada")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
        print(f"Debug: {e}")
```

### 5. Colores y Estilos

```python
# Paleta consistente
COLORES = {
    "fondo": "#f0f0f0",
    "primario": "#007bff",
    "exito": "#28a745",
    "error": "#dc3545",
    "texto": "#333333"
}

boton = tk.Button(
    ventana,
    text="Guardar",
    bg=COLORES["exito"],
    fg="white",
    font=("Arial", 11, "bold")
)
```

---

## RESUMEN RÁPIDO

| Widget | Uso | Ejemplo |
|--------|-----|---------|
| Label | Mostrar texto | `tk.Label(ventana, text="Hola")` |
| Entry | Entrada simple | `tk.Entry(ventana)` |
| Button | Botón | `tk.Button(ventana, command=func)` |
| Listbox | Lista | `tk.Listbox(ventana)` |
| Frame | Contenedor | `tk.Frame(ventana)` |
| Text | Área texto | `tk.Text(ventana)` |
| Messagebox | Diálogos | `messagebox.showinfo()` |
| Notebook | Pestañas | `ttk.Notebook(ventana)` |

---

**Siguiente: Lee sobre la arquitectura del proyecto**
