# 📋 CHEAT SHEET - REFERENCIA RÁPIDA

## 🎯 IMPORTACIONES BÁSICAS

```python
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.filedialog as filedialog
```

---

## 🪟 VENTANA PRINCIPAL

| Operación | Código |
|-----------|--------|
| Crear ventana | `ventana = tk.Tk()` |
| Título | `ventana.title("Título")` |
| Tamaño | `ventana.geometry("400x300")` |
| Ejecutar | `ventana.mainloop()` |
| Salir | `ventana.quit()` |
| Icono | `ventana.iconbitmap("icon.ico")` |
| Color fondo | `ventana.config(bg="blue")` |
| Ridimensionable | `ventana.resizable(False, False)` |

---

## 🎨 WIDGETS COMUNES

### Label (Etiqueta)

```python
label = tk.Label(
    ventana,
    text="Texto",
    font=("Arial", 12),
    fg="black",
    bg="white"
)
label.pack()
```

### Entry (Campo Simple)

```python
entrada = tk.Entry(ventana, width=30)
entrada.pack()

valor = entrada.get()              # Obtener
entrada.delete(0, tk.END)          # Limpiar
entrada.insert(0, "Texto")         # Insertar
```

### Button (Botón)

```python
def mi_funcion():
    print("¡Botón presionado!")

boton = tk.Button(
    ventana,
    text="Click",
    command=mi_funcion,
    bg="green",
    fg="white"
)
boton.pack()
```

### Listbox (Lista)

```python
listbox = tk.Listbox(ventana, height=6)
listbox.pack()

listbox.insert(tk.END, "Item 1")   # Insertar
listbox.insert(0, "Item 0")        # Al inicio

seleccion = listbox.curselection() # Obtener selección
if seleccion:
    valor = listbox.get(seleccion[0])

listbox.delete(0, tk.END)          # Limpiar
```

### Text (Área Texto)

```python
texto = tk.Text(ventana, height=10, width=40)
texto.pack()

texto.insert(tk.END, "Contenido")  # Insertar
contenido = texto.get("1.0", tk.END)  # Obtener
texto.delete("1.0", tk.END)        # Limpiar
```

### Frame (Contenedor)

```python
frame = tk.Frame(ventana, bg="white", height=100)
frame.pack(fill=tk.BOTH, expand=True)

# Agrupar widgets
label = tk.Label(frame, text="Dentro")
label.pack()
```

### Messagebox (Diálogos)

```python
messagebox.showinfo("Título", "Información")
messagebox.showerror("Error", "Mensaje de error")
messagebox.showwarning("Advertencia", "Cuidado")

resultado = messagebox.askyesno("Pregunta", "¿Estás seguro?")
respuesta = messagebox.askokcancel("OK?", "¿Continuar?")
```

---

## 📐 LAYOUTS (Posicionamiento)

### Grid (Recomendado)

```python
label = tk.Label(ventana, text="Label")
label.grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(ventana)
entrada.grid(row=0, column=1)

# Sobre varias columnas
boton = tk.Button(ventana, text="Enviar")
boton.grid(row=1, column=0, columnspan=2)

# Configurar pesos
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
```

### Pack (Simple)

```python
label.pack()                       # Apila
label.pack(side=tk.LEFT)          # Izquierda
label.pack(fill=tk.BOTH, expand=True)  # Rellena
```

### Place (Absoluto)

```python
boton.place(x=50, y=100, width=100, height=30)
```

---

## 🔗 EVENTOS

```python
# Bindings comunes
ventana.bind("<Return>", funcion)      # Enter
ventana.bind("<Escape>", funcion)      # Escape
ventana.bind("<Button-1>", funcion)    # Click izq
ventana.bind("<Button-3>", funcion)    # Click der
ventana.bind("<Motion>", funcion)      # Movimiento
ventana.bind("<Key>", funcion)         # Cualquier tecla

# En función manejadora
def manejador(evento):
    print(evento.x, evento.y)          # Posición
    print(evento.char)                 # Carácter
    print(evento.keysym)               # Nombre tecla
```

---

## ✔️ VALIDACIÓN

```python
def validar_numero(valor):
    if valor == "":
        return True
    try:
        int(valor)
        return True
    except:
        return False

vcmd = (ventana.register(validar_numero), '%S')
entrada = tk.Entry(ventana, validate='key', validatecommand=vcmd)
```

---

## 🔤 VARIABLES TKINTER

```python
# StringVar
nombre = tk.StringVar(value="Inicial")
entrada = tk.Entry(ventana, textvariable=nombre)
valor = nombre.get()
nombre.set("Nuevo")

# IntVar
edad = tk.IntVar(value=0)
edad.set(25)

# BooleanVar
activo = tk.BooleanVar(value=True)
activo.set(False)
```

---

## 🎨 ESTILOS Y COLORES

```python
# Fuentes
font_normal = ("Arial", 12)
font_bold = ("Arial", 12, "bold")
font_italic = ("Arial", 12, "italic")

label = tk.Label(ventana, text="Texto", font=font_bold)

# Colores
AZUL = "#007bff"
VERDE = "#28a745"
ROJO = "#dc3545"
GRIS = "#6c757d"

boton = tk.Button(ventana, bg=VERDE, fg="white")
```

---

## 🎯 COMPONENTES AVANZADOS

### Notebook (Pestañas)

```python
from tkinter import ttk

notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Pestaña 1")
notebook.add(tab2, text="Pestaña 2")
```

### Scrollbar

```python
listbox = tk.Listbox(ventana)
scrollbar = tk.Scrollbar(ventana, command=listbox.yview)

listbox.config(yscrollcommand=scrollbar.set)

listbox.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
```

### Treeview (Tabla)

```python
from tkinter import ttk

tree = ttk.Treeview(ventana, columns=("Nombre", "Edad"))
tree.column("#0", width=50)
tree.column("Nombre", width=150)
tree.heading("#0", text="ID")
tree.heading("Nombre", text="Nombre")

tree.insert("", 0, text="1", values=("Juan", 25))
tree.pack()
```

---

## 📝 CLASES - ESTRUCTURA RECOMENDADA

```python
class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi App")
        self.ventana.geometry("400x300")
        
        # Variables
        self.datos = {}
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crear todos los widgets"""
        self.label = tk.Label(self.ventana, text="Hola")
        self.label.pack()
        
        self.boton = tk.Button(self.ventana, command=self.manejar_evento)
        self.boton.pack()
    
    def manejar_evento(self):
        """Manejar eventos"""
        print("Evento disparado")
    
    def procesar_datos(self):
        """Lógica de negocio"""
        pass

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MiAplicacion(ventana)
    ventana.mainloop()
```

---

## 🚀 EJERCICIO RÁPIDO

Crea una calculadora simple:

```python
import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        
        # Display
        self.display = tk.Entry(ventana, font=("Arial", 20), justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=5, sticky="nsew")
        
        # Botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in botones:
            btn = tk.Button(ventana, text=text, font=("Arial", 18),
                          command=lambda x=text: self.al_click(x))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
    def al_click(self, char):
        if char == '=':
            try:
                resultado = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()
```

---

## 📚 MÉTODOS ÚTILES

| Método | Descripción |
|--------|------------|
| `after(ms, func)` | Ejecutar después de ms milisegundos |
| `bind(evento, func)` | Vincular evento |
| `pack()` | Posicionar con pack |
| `grid(row, col)` | Posicionar con grid |
| `place(x, y)` | Posicionamiento absoluto |
| `destroy()` | Destruir widget |
| `update()` | Actualizar interfaz |
| `config()` | Cambiar propiedades |
| `get()` | Obtener valor |
| `set()` | Establecer valor |

---

## 🔥 TIPS FINALES

1. **Siempre usa clases** para aplicaciones complejas
2. **Valida entrada antes** de procesarla
3. **Usa mensajes claros** de error y éxito
4. **Separa lógica de interfaz** (MVC)
5. **Comenta tu código** para facilitar mantenimiento
6. **Prueba eventos** antes de desplegar
7. **Usa grid** en lugar de pack para layouts complejos
8. **Guarda datos** antes de permitir cambios grandes

---

**¡Ahora tienes todo lo que necesitas! 🎉**
