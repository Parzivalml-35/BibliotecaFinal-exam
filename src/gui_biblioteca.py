# gui_biblioteca.py - Interfaz Gráfica Completa del Sistema de Biblioteca

import tkinter as tk
from tkinter import ttk, messagebox
from usuarios import Usuario
from materiales import LibroFisico, LibroDigital
from sistema import Biblioteca

class BibliotecaGUI:
    """
    Clase principal para la interfaz gráfica del sistema de biblioteca.
    
    Organiza la aplicación en pestañas:
    - Usuarios: Registrar y ver usuarios
    - Materiales: Registrar y ver materiales
    - Préstamos: Gestionar préstamos y devoluciones
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación GUI.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.biblio = Biblioteca()
        
        # Configurar ventana
        self.root.title("📚 Sistema de Biblioteca")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Crear estilo
        self.estilo_titulo = ("Arial", 14, "bold")
        self.estilo_normal = ("Arial", 10)
        
        # Crear pestañas
        self.crear_pestanas()
    
    def crear_pestanas(self):
        """Crea el sistema de pestañas"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Crear cada pestaña
        self.crear_pestaña_usuarios()
        self.crear_pestaña_materiales()
        self.crear_pestaña_prestamos()
    
    # ========== PESTAÑA USUARIOS ==========
    
    def crear_pestaña_usuarios(self):
        """Crea la pestaña de gestión de usuarios"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="👤 Usuarios")
        
        # Título
        titulo = tk.Label(tab, text="Gestión de Usuarios", font=self.estilo_titulo)
        titulo.pack(pady=10)
        
        # Formulario
        frame_form = tk.Frame(tab, bg="lightgray", padx=20, pady=20)
        frame_form.pack(fill="x", padx=10, pady=10)
        
        # ID
        tk.Label(frame_form, text="ID:", font=self.estilo_normal, bg="lightgray").grid(row=0, column=0, sticky="w", pady=5)
        self.var_user_id = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_user_id, width=30).grid(row=0, column=1, pady=5)
        
        # Nombre
        tk.Label(frame_form, text="Nombre:", font=self.estilo_normal, bg="lightgray").grid(row=1, column=0, sticky="w", pady=5)
        self.var_user_nombre = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_user_nombre, width=30).grid(row=1, column=1, pady=5)
        
        # Correo
        tk.Label(frame_form, text="Correo:", font=self.estilo_normal, bg="lightgray").grid(row=2, column=0, sticky="w", pady=5)
        self.var_user_correo = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_user_correo, width=30).grid(row=2, column=1, pady=5)
        
        # Tipo de Usuario
        tk.Label(frame_form, text="Tipo:", font=self.estilo_normal, bg="lightgray").grid(row=3, column=0, sticky="w", pady=5)
        self.var_user_tipo = tk.StringVar()
        ttk.Combobox(
            frame_form, 
            textvariable=self.var_user_tipo,
            values=["estudiante", "docente", "externo"],
            state="readonly",
            width=27
        ).grid(row=3, column=1, pady=5)
        
        # Botón Registrar
        tk.Button(
            frame_form,
            text="✓ Registrar Usuario",
            command=self.registrar_usuario,
            bg="green",
            fg="white",
            font=self.estilo_normal,
            cursor="hand2",
            width=30
        ).grid(row=4, column=0, columnspan=2, pady=15)
        
        # Listado de usuarios
        tk.Label(tab, text="Usuarios Registrados:", font=self.estilo_normal).pack(anchor="w", padx=10, pady=(10, 5))
        
        # Frame para listbox + scrollbar
        frame_lista = tk.Frame(tab)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")
        
        self.lista_usuarios = tk.Listbox(
            frame_lista,
            height=12,
            yscrollcommand=scrollbar.set,
            font=("Courier", 9)
        )
        self.lista_usuarios.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lista_usuarios.yview)
        
        # Actualizar lista
        self.actualizar_lista_usuarios()
    
    def registrar_usuario(self):
        """Registra un nuevo usuario en la base de datos"""
        try:
            # Validar que no esté vacío
            if not all([self.var_user_id.get(), self.var_user_nombre.get(), 
                       self.var_user_correo.get(), self.var_user_tipo.get()]):
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
                return
            
            # Crear usuario
            usuario = Usuario(
                self.var_user_id.get(),
                self.var_user_nombre.get(),
                self.var_user_correo.get(),
                self.var_user_tipo.get()
            )
            
            # Registrar en base de datos
            self.biblio.registrar_usuario(usuario)
            
            # Limpiar campos
            self.var_user_id.set("")
            self.var_user_nombre.set("")
            self.var_user_correo.set("")
            self.var_user_tipo.set("")
            
            # Actualizar lista
            self.actualizar_lista_usuarios()
            
            messagebox.showinfo("✓ Éxito", "Usuario registrado correctamente")
        
        except ValueError as e:
            messagebox.showerror("✗ Error", f"Error al registrar: {e}")
    
    def actualizar_lista_usuarios(self):
        """Actualiza el listbox de usuarios"""
        self.lista_usuarios.delete(0, tk.END)
        for usuario in self.biblio.listar_usuarios():
            self.lista_usuarios.insert(tk.END, usuario.mostrar_info())
    
    # ========== PESTAÑA MATERIALES ==========
    
    def crear_pestaña_materiales(self):
        """Crea la pestaña de gestión de materiales"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📖 Materiales")
        
        # Título
        titulo = tk.Label(tab, text="Gestión de Materiales", font=self.estilo_titulo)
        titulo.pack(pady=10)
        
        # Formulario
        frame_form = tk.Frame(tab, bg="lightgray", padx=20, pady=20)
        frame_form.pack(fill="x", padx=10, pady=10)
        
        # Tipo de Material
        tk.Label(frame_form, text="Tipo:", font=self.estilo_normal, bg="lightgray").grid(row=0, column=0, sticky="w", pady=5)
        self.var_mat_tipo = tk.StringVar()
        ttk.Combobox(
            frame_form,
            textvariable=self.var_mat_tipo,
            values=["Libro Físico", "Libro Digital"],
            state="readonly",
            width=27
        ).grid(row=0, column=1, pady=5)
        
        # Código
        tk.Label(frame_form, text="Código:", font=self.estilo_normal, bg="lightgray").grid(row=1, column=0, sticky="w", pady=5)
        self.var_mat_codigo = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_mat_codigo, width=30).grid(row=1, column=1, pady=5)
        
        # Título
        tk.Label(frame_form, text="Título:", font=self.estilo_normal, bg="lightgray").grid(row=2, column=0, sticky="w", pady=5)
        self.var_mat_titulo = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_mat_titulo, width=30).grid(row=2, column=1, pady=5)
        
        # Autor
        tk.Label(frame_form, text="Autor:", font=self.estilo_normal, bg="lightgray").grid(row=3, column=0, sticky="w", pady=5)
        self.var_mat_autor = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_mat_autor, width=30).grid(row=3, column=1, pady=5)
        
        # Año
        tk.Label(frame_form, text="Año:", font=self.estilo_normal, bg="lightgray").grid(row=4, column=0, sticky="w", pady=5)
        self.var_mat_anio = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_mat_anio, width=30).grid(row=4, column=1, pady=5)
        
        # Campo adicional (Ubicación o Formato)
        self.var_mat_extra = tk.StringVar()
        self.label_mat_extra = tk.Label(frame_form, text="Ubicación:", font=self.estilo_normal, bg="lightgray")
        self.label_mat_extra.grid(row=5, column=0, sticky="w", pady=5)
        self.entry_mat_extra = tk.Entry(frame_form, textvariable=self.var_mat_extra, width=30)
        self.entry_mat_extra.grid(row=5, column=1, pady=5)
        
        # Vincular cambio de tipo
        self.var_mat_tipo.trace("w", self.cambiar_campo_material)
        
        # Botón Registrar
        tk.Button(
            frame_form,
            text="✓ Registrar Material",
            command=self.registrar_material,
            bg="green",
            fg="white",
            font=self.estilo_normal,
            cursor="hand2",
            width=30
        ).grid(row=6, column=0, columnspan=2, pady=15)
        
        # Listado de materiales
        tk.Label(tab, text="Materiales Registrados:", font=self.estilo_normal).pack(anchor="w", padx=10, pady=(10, 5))
        
        frame_lista = tk.Frame(tab)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")
        
        self.lista_materiales = tk.Listbox(
            frame_lista,
            height=12,
            yscrollcommand=scrollbar.set,
            font=("Courier", 9)
        )
        self.lista_materiales.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lista_materiales.yview)
        
        self.actualizar_lista_materiales()
    
    def cambiar_campo_material(self, *_):
        """Cambia el label y placeholder según el tipo de material"""
        if self.var_mat_tipo.get() == "Libro Físico":
            self.label_mat_extra.config(text="Ubicación:")
            self.entry_mat_extra.delete(0, tk.END)
        else:
            self.label_mat_extra.config(text="Formato:")
            self.entry_mat_extra.delete(0, tk.END)
    
    def registrar_material(self):
        """Registra un nuevo material"""
        try:
            if not all([self.var_mat_tipo.get(), self.var_mat_codigo.get(),
                       self.var_mat_titulo.get(), self.var_mat_autor.get(),
                       self.var_mat_anio.get(), self.var_mat_extra.get()]):
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
                return
            
            if self.var_mat_tipo.get() == "Libro Físico":
                material = LibroFisico(
                    self.var_mat_titulo.get(),
                    self.var_mat_autor.get(),
                    int(self.var_mat_anio.get()),
                    self.var_mat_codigo.get(),
                    self.var_mat_extra.get()
                )
            else:
                material = LibroDigital(
                    self.var_mat_titulo.get(),
                    self.var_mat_autor.get(),
                    int(self.var_mat_anio.get()),
                    self.var_mat_codigo.get(),
                    self.var_mat_extra.get()
                )
            
            self.biblio.registrar_material(material)
            
            # Limpiar
            self.var_mat_tipo.set("")
            self.var_mat_codigo.set("")
            self.var_mat_titulo.set("")
            self.var_mat_autor.set("")
            self.var_mat_anio.set("")
            self.var_mat_extra.set("")
            
            self.actualizar_lista_materiales()
            messagebox.showinfo("✓ Éxito", "Material registrado correctamente")
        
        except ValueError as e:
            messagebox.showerror("✗ Error", f"Error: {e}")
    
    def actualizar_lista_materiales(self):
        """Actualiza el listbox de materiales"""
        self.lista_materiales.delete(0, tk.END)
        for material in self.biblio.listar_materiales():
            self.lista_materiales.insert(tk.END, material.mostrar_info())
    
    # ========== PESTAÑA PRÉSTAMOS ==========
    
    def crear_pestaña_prestamos(self):
        """Crea la pestaña de gestión de préstamos"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔄 Préstamos")
        
        # Título
        titulo = tk.Label(tab, text="Gestión de Préstamos", font=self.estilo_titulo)
        titulo.pack(pady=10)
        
        # Formulario para nuevo préstamo
        frame_form = tk.Frame(tab, bg="lightgray", padx=20, pady=20)
        frame_form.pack(fill="x", padx=10, pady=10)
        
        tk.Label(frame_form, text="ID Usuario:", font=self.estilo_normal, bg="lightgray").grid(row=0, column=0, sticky="w", pady=5)
        self.var_prest_user = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_prest_user, width=30).grid(row=0, column=1, pady=5)
        
        tk.Label(frame_form, text="Código Material:", font=self.estilo_normal, bg="lightgray").grid(row=1, column=0, sticky="w", pady=5)
        self.var_prest_mat = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.var_prest_mat, width=30).grid(row=1, column=1, pady=5)
        
        # Botones
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=15)
        
        tk.Button(
            frame_botones,
            text="✓ Registrar Préstamo",
            command=self.registrar_prestamo,
            bg="green",
            fg="white",
            font=self.estilo_normal,
            cursor="hand2",
            width=20
        ).pack(side="left", padx=5)
        
        tk.Button(
            frame_botones,
            text="↩ Registrar Devolución",
            command=self.registrar_devolucion,
            bg="orange",
            fg="white",
            font=self.estilo_normal,
            cursor="hand2",
            width=20
        ).pack(side="left", padx=5)
        
        # Pestañas internas para préstamos activos y vencidos
        frame_tabs = ttk.Frame(tab)
        frame_tabs.pack(fill="both", expand=True, padx=10, pady=10)
        
        notebook_int = ttk.Notebook(frame_tabs)
        notebook_int.pack(fill="both", expand=True)
        
        # Préstamos activos
        tab_activos = ttk.Frame(notebook_int)
        notebook_int.add(tab_activos, text="Préstamos Activos")
        
        tk.Label(tab_activos, text="Préstamos en Curso:", font=self.estilo_normal).pack(anchor="w", padx=10, pady=5)
        
        frame_lista_activos = tk.Frame(tab_activos)
        frame_lista_activos.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar_activos = ttk.Scrollbar(frame_lista_activos)
        scrollbar_activos.pack(side="right", fill="y")
        
        self.lista_prestamos_activos = tk.Listbox(
            frame_lista_activos,
            yscrollcommand=scrollbar_activos.set,
            font=("Courier", 9)
        )
        self.lista_prestamos_activos.pack(side="left", fill="both", expand=True)
        scrollbar_activos.config(command=self.lista_prestamos_activos.yview)
        
        # Préstamos vencidos
        tab_vencidos = ttk.Frame(notebook_int)
        notebook_int.add(tab_vencidos, text="⚠ Préstamos Vencidos")
        
        tk.Label(tab_vencidos, text="Préstamos Vencidos (> 7 días):", font=self.estilo_normal).pack(anchor="w", padx=10, pady=5)
        
        frame_lista_vencidos = tk.Frame(tab_vencidos)
        frame_lista_vencidos.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar_vencidos = ttk.Scrollbar(frame_lista_vencidos)
        scrollbar_vencidos.pack(side="right", fill="y")
        
        self.lista_prestamos_vencidos = tk.Listbox(
            frame_lista_vencidos,
            yscrollcommand=scrollbar_vencidos.set,
            font=("Courier", 9),
            bg="lightyellow"
        )
        self.lista_prestamos_vencidos.pack(side="left", fill="both", expand=True)
        scrollbar_vencidos.config(command=self.lista_prestamos_vencidos.yview)
        
        self.actualizar_lista_prestamos()
    
    def registrar_prestamo(self):
        """Registra un nuevo préstamo"""
        try:
            user_id = self.var_prest_user.get()
            mat_codigo = self.var_prest_mat.get()
            
            if not user_id or not mat_codigo:
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return
            
            self.biblio.registrar_prestamo(user_id, mat_codigo)
            
            self.var_prest_user.set("")
            self.var_prest_mat.set("")
            
            self.actualizar_lista_prestamos()
            messagebox.showinfo("✓ Éxito", "Préstamo registrado correctamente")
        
        except ValueError as e:
            messagebox.showerror("✗ Error", f"Error: {e}")
    
    def registrar_devolucion(self):
        """Registra una devolución"""
        try:
            mat_codigo = self.var_prest_mat.get()
            
            if not mat_codigo:
                messagebox.showwarning("Advertencia", "Ingresa el código del material")
                return
            
            self.biblio.registrar_devolucion(mat_codigo)
            
            self.var_prest_mat.set("")
            self.actualizar_lista_prestamos()
            messagebox.showinfo("✓ Éxito", "Devolución registrada correctamente")
        
        except ValueError as e:
            messagebox.showerror("✗ Error", f"Error: {e}")
    
    def actualizar_lista_prestamos(self):
        """Actualiza los listbox de préstamos"""
        # Préstamos activos
        self.lista_prestamos_activos.delete(0, tk.END)
        for prestamo in self.biblio.listar_prestamos_activos():
            self.lista_prestamos_activos.insert(tk.END, prestamo.info())
        
        # Préstamos vencidos
        self.lista_prestamos_vencidos.delete(0, tk.END)
        for prestamo in self.biblio.prestamos_vencidos():
            self.lista_prestamos_vencidos.insert(tk.END, prestamo.info())


def main():
    """Punto de entrada de la aplicación"""
    root = tk.Tk()
    BibliotecaGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
