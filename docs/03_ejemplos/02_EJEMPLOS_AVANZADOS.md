# 02 EJEMPLOS AVANZADOS

## 📌 EJEMPLOS MÁS COMPLEJOS

---

## EJEMPLO 1: Formulario Completo con Validación

```python
import tkinter as tk
from tkinter import messagebox
import re

class FormularioUsuario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario Usuario")
        self.usuarios = {}
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Marco del formulario
        frame_form = tk.Frame(self.ventana)
        frame_form.pack(padx=10, pady=10)
        
        # ID
        tk.Label(frame_form, text="ID:").grid(row=0, column=0)
        self.entrada_id = tk.Entry(frame_form)
        self.entrada_id.grid(row=0, column=1)
        
        # Nombre
        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0)
        self.entrada_nombre = tk.Entry(frame_form)
        self.entrada_nombre.grid(row=1, column=1)
        
        # Email
        tk.Label(frame_form, text="Email:").grid(row=2, column=0)
        self.entrada_email = tk.Entry(frame_form)
        self.entrada_email.grid(row=2, column=1)
        
        # Botón
        boton_guardar = tk.Button(frame_form, text="Guardar", command=self.guardar)
        boton_guardar.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Lista de usuarios
        tk.Label(self.ventana, text="Usuarios Registrados:").pack()
        self.listbox = tk.Listbox(self.ventana, height=6)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def guardar(self):
        id_usuario = self.entrada_id.get().strip()
        nombre = self.entrada_nombre.get().strip()
        email = self.entrada_email.get().strip()
        
        # Validar
        if not id_usuario or not nombre or not email:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        if id_usuario in self.usuarios:
            messagebox.showerror("Error", "ID ya existe")
            return
        
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            messagebox.showerror("Error", "Email inválido")
            return
        
        # Guardar
        self.usuarios[id_usuario] = {"nombre": nombre, "email": email}
        self.listbox.insert(tk.END, f"{id_usuario} - {nombre} ({email})")
        
        # Limpiar
        self.entrada_id.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Usuario registrado")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = FormularioUsuario(ventana)
    ventana.mainloop()
```

---

## EJEMPLO 2: Aplicación con Pestañas y Listas

```python
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("400x500")
        
        self.tareas_pendientes = []
        self.tareas_completadas = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Notebook con pestañas
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 1: Nueva tarea
        self.tab_nueva = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_nueva, text="Nueva Tarea")
        self.crear_tab_nueva()
        
        # Pestaña 2: Pendientes
        self.tab_pendientes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_pendientes, text="Pendientes")
        self.crear_tab_pendientes()
        
        # Pestaña 3: Completadas
        self.tab_completadas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_completadas, text="Completadas")
        self.crear_tab_completadas()
    
    def crear_tab_nueva(self):
        frame = ttk.Frame(self.tab_nueva)
        frame.pack(padx=20, pady=20)
        
        ttk.Label(frame, text="Descripción:").grid(row=0, column=0, sticky="w")
        self.entrada_tarea = ttk.Entry(frame, width=40)
        self.entrada_tarea.grid(row=1, column=0, pady=10)
        
        ttk.Label(frame, text="Prioridad:").grid(row=2, column=0, sticky="w")
        self.combo_prioridad = ttk.Combobox(frame, values=["Alta", "Media", "Baja"])
        self.combo_prioridad.grid(row=3, column=0, pady=10)
        
        boton_agregar = ttk.Button(frame, text="Agregar", command=self.agregar_tarea)
        boton_agregar.grid(row=4, column=0, pady=20)
    
    def crear_tab_pendientes(self):
        self.listbox_pendientes = tk.Listbox(self.tab_pendientes, height=15)
        self.listbox_pendientes.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        frame_botones = ttk.Frame(self.tab_pendientes)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Completar", command=self.completar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)
    
    def crear_tab_completadas(self):
        self.listbox_completadas = tk.Listbox(self.tab_completadas, height=15)
        self.listbox_completadas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def agregar_tarea(self):
        tarea = self.entrada_tarea.get().strip()
        prioridad = self.combo_prioridad.get()
        
        if not tarea:
            messagebox.showerror("Error", "Ingresa una tarea")
            return
        
        if not prioridad:
            messagebox.showerror("Error", "Selecciona prioridad")
            return
        
        self.tareas_pendientes.append({"tarea": tarea, "prioridad": prioridad})
        self.actualizar_listas()
        self.entrada_tarea.delete(0, tk.END)
        self.combo_prioridad.set("")
    
    def completar_tarea(self):
        seleccion = self.listbox_pendientes.curselection()
        if seleccion:
            tarea = self.tareas_pendientes[seleccion[0]]
            self.tareas_completadas.append(tarea)
            self.tareas_pendientes.pop(seleccion[0])
            self.actualizar_listas()
    
    def eliminar_tarea(self):
        seleccion = self.listbox_pendientes.curselection()
        if seleccion:
            self.tareas_pendientes.pop(seleccion[0])
            self.actualizar_listas()
    
    def actualizar_listas(self):
        self.listbox_pendientes.delete(0, tk.END)
        for i, t in enumerate(self.tareas_pendientes):
            self.listbox_pendientes.insert(tk.END, f"[{t['prioridad']}] {t['tarea']}")
        
        self.listbox_completadas.delete(0, tk.END)
        for i, t in enumerate(self.tareas_completadas):
            self.listbox_completadas.insert(tk.END, f"✓ {t['tarea']}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = GestorTareas(ventana)
    ventana.mainloop()
```

---

## EJEMPLO 3: Tabla con Treeview

```python
from tkinter import ttk
import tkinter as tk

class TablaDatos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Tabla de Datos")
        self.ventana.geometry("600x400")
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Crear treeview
        columns = ("ID", "Nombre", "Edad", "Correo")
        self.tree = ttk.Treeview(self.ventana, columns=columns, height=12)
        
        # Definir columnas
        self.tree.column("#0", width=50, minwidth=50)
        self.tree.column("ID", width=50, minwidth=50)
        self.tree.column("Nombre", width=150, minwidth=150)
        self.tree.column("Edad", width=80, minwidth=80)
        self.tree.column("Correo", width=200, minwidth=200)
        
        # Definir encabezados
        self.tree.heading("#0", text="#")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Correo", text="Correo")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.ventana, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Agregar datos de ejemplo
        datos = [
            ("U001", "Juan García", 25, "juan@email.com"),
            ("U002", "María López", 30, "maria@email.com"),
            ("U003", "Pedro Rodríguez", 28, "pedro@email.com"),
            ("U004", "Ana Martínez", 26, "ana@email.com"),
        ]
        
        for i, datos_fila in enumerate(datos):
            self.tree.insert("", i, text=str(i+1), values=datos_fila)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = TablaDatos(ventana)
    ventana.mainloop()
```

---

## EJEMPLO 4: Validación en Tiempo Real

```python
import tkinter as tk

class ValidadorTiempoReal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Validador")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Edad
        tk.Label(self.ventana, text="Edad (0-150):").pack(pady=5)
        self.entrada_edad = tk.Entry(self.ventana)
        self.entrada_edad.pack(pady=5)
        self.entrada_edad.bind("<KeyRelease>", self.validar_edad)
        
        self.label_edad = tk.Label(self.ventana, text="", fg="red")
        self.label_edad.pack()
        
        # Email
        tk.Label(self.ventana, text="Email:").pack(pady=5)
        self.entrada_email = tk.Entry(self.ventana)
        self.entrada_email.pack(pady=5)
        self.entrada_email.bind("<KeyRelease>", self.validar_email)
        
        self.label_email = tk.Label(self.ventana, text="", fg="red")
        self.label_email.pack()
    
    def validar_edad(self, evento):
        edad_str = self.entrada_edad.get()
        if edad_str == "":
            self.label_edad.config(text="")
            return
        
        try:
            edad = int(edad_str)
            if 0 <= edad <= 150:
                self.label_edad.config(text="✓ Válido", fg="green")
            else:
                self.label_edad.config(text="✗ Debe estar entre 0-150", fg="red")
        except ValueError:
            self.label_edad.config(text="✗ Debe ser un número", fg="red")
    
    def validar_email(self, evento):
        email = self.entrada_email.get()
        if email == "":
            self.label_email.config(text="")
            return
        
        if "@" in email and "." in email:
            self.label_email.config(text="✓ Válido", fg="green")
        else:
            self.label_email.config(text="✗ Email inválido", fg="red")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ValidadorTiempoReal(ventana)
    ventana.mainloop()
```

---

## EJEMPLO 5: Eventos de Teclado y Ratón

```python
import tkinter as tk

class EventosDemo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Eventos")
        self.ventana.geometry("400x300")
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        self.label_eventos = tk.Label(
            self.ventana,
            text="Evento: ",
            font=("Arial", 14),
            bg="lightblue",
            height=10
        )
        self.label_eventos.pack(fill=tk.BOTH, expand=True)
        
        # Vincular eventos
        self.label_eventos.bind("<Button-1>", self.al_click)
        self.label_eventos.bind("<Motion>", self.al_mover)
        self.label_eventos.bind("<Double-Button-1>", self.al_doble_click)
        self.ventana.bind("<Key>", self.al_tecla)
    
    def al_click(self, evento):
        self.label_eventos.config(text=f"Click en ({evento.x}, {evento.y})")
    
    def al_mover(self, evento):
        self.label_eventos.config(text=f"Movimiento: ({evento.x}, {evento.y})")
    
    def al_doble_click(self, evento):
        self.label_eventos.config(text="¡Doble click!")
    
    def al_tecla(self, evento):
        self.label_eventos.config(text=f"Tecla presionada: {evento.char}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = EventosDemo(ventana)
    ventana.mainloop()
```

---

**¡Estos ejemplos son más desafiantes! 💪**

Siguiente: Lee la referencia rápida
