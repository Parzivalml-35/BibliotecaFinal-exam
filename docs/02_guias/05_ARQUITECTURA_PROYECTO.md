# 05 ARQUITECTURA DEL PROYECTO

## 📐 ESTRUCTURA GENERAL

```
parcialFinal/
│
├─ src/                           # 🔧 CÓDIGO FUENTE
│  ├─ __init__.py                (Exporta clases)
│  ├─ usuarios.py                (Modelo: gestión de usuarios)
│  ├─ materiales.py              (Modelo: catálogo de libros)
│  ├─ prestamos.py               (Modelo: registro de préstamos)
│  ├─ sistema.py                 (Controlador: orquestador)
│  ├─ main.py                    (Interfaz de consola)
│  └─ gui_biblioteca.py          (Interfaz gráfica Tkinter) ⭐
│
├─ docs/                          # 📚 DOCUMENTACIÓN
│  ├─ 01_inicio/                 (Primeros pasos)
│  ├─ 02_guias/                  (Aprender paso a paso)
│  ├─ 03_ejemplos/               (Código práctico)
│  ├─ 04_referencia/             (Quick reference)
│  └─ README_DOCS.md             (Indice de documentación)
│
├─ .gitignore                    (Git ignore)
├─ README.md                     (Descripción del proyecto)
├─ ESTRUCTURA_PROYECTO.md        (Este archivo explica la estructura)
└─ __pycache__/                  (Archivos compilados Python)
```

---

## 🏗️ PATRÓN ARQUITECTÓNICO: MVC

```
┌─────────────────────────────────────────────┐
│         VISTA (GUI / Interfaz)              │
│    gui_biblioteca.py / main.py              │
│  ✓ Tkinter GUI de 3 pestañas                │
│  ✓ Consola interactiva                      │
└──────────────────┬──────────────────────────┘
                   │ (Llama a)
                   ↓
┌─────────────────────────────────────────────┐
│      CONTROLADOR (Orquestador)              │
│         sistema.py                          │
│  ✓ Valida entrada del usuario               │
│  ✓ Coordina operaciones entre modelos       │
│  ✓ Maneja errores                           │
│  ✓ Devuelve resultados a la vista           │
└──────────────────┬──────────────────────────┘
                   │ (Usa)
                   ↓
┌─────────────────────────────────────────────┐
│    MODELO (Lógica de Negocio)               │
│  usuarios.py | materiales.py | prestamos.py│
│  ✓ Clases de dominio                        │
│  ✓ Validaciones de negocio                  │
│  ✓ Métodos de procesamiento                 │
│  ✓ Ninguna referencia a GUI                 │
└─────────────────────────────────────────────┘
```

### Ventajas del MVC

```
✓ Separación de responsabilidades
✓ Fácil de testear (modelo sin GUI)
✓ Reutilizable (modelo independiente)
✓ Fácil de cambiar interfaz
✓ Código limpio y organizado
```

---

## 🔷 MODELOS (src/modelo/)

### usuarios.py - Usuario

```python
class Usuario:
    def __init__(self, id: str, nombre: str, correo: str, tipo_usuario: str)
    
    @property
    def id(self)                    # Getter
    
    @id.setter
    def id(self, valor)             # Setter con validación
    
    # Métodos de validación
    def validar_correo()            # Valida formato email
    def info()                      # Retorna representación en string
```

**Responsabilidades:**
- ✓ Almacenar datos del usuario
- ✓ Validar email con regex
- ✓ Prevenir ID duplicados via properties
- ✓ Retornar información formateada

**Tipos de Usuario:** estudiante | docente | externo

---

### materiales.py - Libros

```python
class MaterialBibliografico(ABC):
    """Clase abstracta (base para libros)"""
    @abstractmethod
    def mostrar_info()              # Debe implementarse en subclases

class LibroFisico(MaterialBibliografico):
    """Libro físico en estantería"""
    __init__(codigo, titulo, autor, año, ubicacion)
    mostrar_info()                  # Implementación concreta

class LibroDigital(MaterialBibliografico):
    """Archivo digital (PDF, EPUB)"""
    __init__(codigo, titulo, autor, año, formato)
    mostrar_info()                  # Implementación concreta

# Mixins (comportamientos adicionales)
class Imprimible:
    """Puede ser impreso"""
    def imprimir()

class Descargable:
    """Puede ser descargado"""
    def descargar()
```

**Conceptos POO Usados:**
- ✓ Herencia (`LibroFisico` hereda de `MaterialBibliografico`)
- ✓ Polimorfismo (`mostrar_info()` diferente en cada tipo)
- ✓ Clases Abstractas (`ABC` y `@abstractmethod`)
- ✓ Mixins (composición de comportamientos)

---

### prestamos.py - Registro de Préstamo

```python
class Prestamo:
    def __init__(self, material, usuario, fecha_inicio)
    
    # Getters públicos (reemplazan acceso a _ protegido)
    def get_material()              # Retorna el material
    def get_usuario()               # Retorna el usuario
    
    # Lógica de préstamo
    def activo()                    # ¿Está actualmente prestado?
    def esta_vencido()              # ¿Pasaron 7 días?
    def marcar_devolucion()         # Registra devolución
    
    def info()                      # Información formateada
```

**Reglas de Negocio:**
- Máximo 7 días de préstamo
- Un material solo puede estar prestado una vez
- Registra automáticamente fecha/hora
- Vencido = más de 7 días

---

## 🎮 CONTROLADOR (src/sistema.py)

```python
class BibliotecaController:
    """Orquestador central"""
    
    def __init__(self):
        self.usuarios = {}          # Diccionario de usuarios
        self.materiales = {}        # Diccionario de materiales
        self.prestamos = []         # Lista de préstamos
    
    # Operaciones de usuario
    def registrar_usuario(...)      # Crea nuevo usuario
    def listar_usuarios()           # Retorna todos
    
    # Operaciones de material
    def registrar_material(...)     # Crea nuevo material
    def listar_materiales()         # Retorna todos
    
    # Operaciones de préstamo
    def registrar_prestamo(...)     # Crea nuevo préstamo
    def registrar_devolucion(...)   # Marca como devuelto
    def listar_prestamos()          # Retorna todos
    def listar_vencidos()           # Retorna solo vencidos
```

**Responsabilidades:**
- ✓ Validar entrada del usuario
- ✓ Coordinar operaciones entre modelos
- ✓ Mantener diccionarios/listas
- ✓ Lanzar excepciones claras
- ✓ Retornar datos a la vista

**Ejemplo de Flujo:**
```python
# GUI llama a controlador
controlador.registrar_usuario("U001", "Juan", "juan@email.com", "estudiante")

# Controlador valida
if "U001" en self.usuarios:
    raise ValueError("ID ya existe")

# Controlador crea modelo
usuario = Usuario("U001", "Juan", "juan@email.com", "estudiante")

# Almacena
self.usuarios["U001"] = usuario

# Retorna éxito a GUI
return True
```

---

## 📱 VISTAS (GUI / Consola)

### gui_biblioteca.py - Interfaz Gráfica ⭐

```python
class BibliotecaGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.controlador = BibliotecaController()
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Pestañas
        self.notebook = ttk.Notebook()
        self.tab_usuarios = ttk.Frame()
        self.tab_materiales = ttk.Frame()
        self.tab_prestamos = ttk.Frame()
    
    # Pestaña Usuarios
    def crear_tab_usuarios(self)
    def registrar_usuario_gui(self)
    def actualizar_lista_usuarios(self)
    
    # Pestaña Materiales
    def crear_tab_materiales(self)
    def registrar_material_gui(self)
    def actualizar_lista_materiales(self)
    
    # Pestaña Préstamos
    def crear_tab_prestamos(self)
    def registrar_prestamo_gui(self)
    def registrar_devolucion_gui(self)
    def actualizar_listas_prestamos(self)
```

**Características:**
- ✓ 3 pestañas (Usuarios, Materiales, Préstamos)
- ✓ Formularios con validación
- ✓ Listas con scroll
- ✓ Mensajes de error/éxito
- ✓ Campos dinámicos (tipo material)

**Flujo Interacción:**
```
Usuario escribe datos → Valida entrada → Llama controlador → 
Actualiza lista → Muestra mensaje
```

---

### main.py - Interfaz de Consola

```python
def main():
    """Demostración en consola"""
    controlador = BibliotecaController()
    
    # Ejemplo: registrar usuario
    controlador.registrar_usuario(...)
    
    # Ejemplo: registrar material
    controlador.registrar_material(...)
    
    # Ejemplo: hacer préstamo
    controlador.registrar_prestamo(...)
    
    # Listar datos
    print(controlador.listar_usuarios())
```

**Para Ejecutar:**
```bash
python src/main.py
```

---

## 🔄 FLUJO DE DATOS

### Caso: Registrar Usuario

```
┌─ GUI ─────────────────────────┐
│ Usuario escribe en Entry      │
│ ID: "U001"                    │
│ Nombre: "Juan"                │
│ Correo: "juan@email.com"      │
│ Tipo: "estudiante"            │
│ → Click "Registrar"           │
└───────────────┬───────────────┘
                ↓
┌─ Controlador ──────────────────────┐
│ registrar_usuario(U001, Juan, ...) │
│                                    │
│ 1. Validar entrada                │
│    - ID no duplicado?             │
│    - Email válido?                │
│    - Campos completos?            │
│                                    │
│ 2. Si todo ok:                    │
│    usuario = Usuario(...)         │
│    self.usuarios[U001] = usuario  │
│    return True                    │
│                                    │
│ 3. Si error:                      │
│    raise ValueError("mensaje")    │
└───────────────┬───────────────────┘
                ↓
┌─ Modelo ──────────────────────────┐
│ class Usuario:                    │
│   @property                       │
│   def id(self):                   │
│       return self._id             │
│                                   │
│   Datos guardados en memoria      │
└───────────────┬───────────────────┘
                ↓
┌─ GUI ─────────────────────────┐
│ Actualiza lista               │
│ Muestra: "✓ Usuario registrado"│
└───────────────────────────────┘
```

---

## 📋 FLUJO DE PRÉSTAMO (Caso Completo)

```
┌─────────────────────────────────────────────┐
│ 1. REGISTRAR USUARIO                        │
│    entrada: ID="U001", nombre="Juan", ...  │
│    resultado: Usuario guardado             │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ 2. REGISTRAR MATERIAL                       │
│    entrada: código="LIB001", título="...",  │
│    resultado: Material guardado             │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ 3. REGISTRAR PRÉSTAMO                       │
│    entrada: U001 → LIB001                  │
│    validar: Usuario existe? ✓              │
│    validar: Material existe? ✓             │
│    validar: Material NO prestado? ✓        │
│    crear: Prestamo(material, usuario)      │
│    resultado: Préstamo activo              │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ 4. VER PRÉSTAMOS ACTIVOS                    │
│    lista: [Usuario→Material, ...]           │
│    muestra: Usuarios | Materiales | Fechas │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ 5. ESPERAR 7+ DÍAS                          │
│    préstamo.esta_vencido() → True          │
│    Se muestra en fondo AMARILLO             │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ 6. REGISTRAR DEVOLUCIÓN                     │
│    entrada: código="LIB001"                 │
│    validar: Hay préstamo activo? ✓        │
│    acción: prestamo.marcar_devolucion()    │
│    resultado: Material disponible nuevamente│
└─────────────────────────────────────────────┘
```

---

## 🎯 RESPONSABILIDADES POR ARCHIVO

| Archivo | Responsabilidad | Tipo | Líneas |
|---------|-----------------|------|--------|
| `usuarios.py` | Modelo usuario | Dato + Lógica | 65 |
| `materiales.py` | Modelo material | Dato + Lógica | 55 |
| `prestamos.py` | Modelo préstamo | Dato + Lógica | 35 |
| `sistema.py` | Controlador | Orquestador | 65 |
| `gui_biblioteca.py` | Vista GUI | Interfaz | 466 |
| `main.py` | Vista Consola | Interfaz | 80 |

---

## 🔐 PRINCIPIOS DE DISEÑO APLICADOS

### 1. Separación de Responsabilidades
```
✓ Modelos: Solo datos y validación
✓ Controlador: Solo orquestación
✓ Vista: Solo presentación
```

### 2. DRY (Don't Repeat Yourself)
```
✓ Métodos reutilizables
✓ Validación centralizada
✓ Mensajes de error consistentes
```

### 3. SOLID
```
✓ S: Cada clase una responsabilidad
✓ O: Abierto a extensión (ABC)
✓ L: Liskov substitution (herencia correcta)
✓ I: Interfaces segregadas
✓ D: Dependencia en abstracciones
```

---

## 🚀 EJECUCIÓN

### Opción 1: GUI (Recomendado)
```bash
cd e:\PROGRAMACION\parcialFinal
python src/gui_biblioteca.py
```

### Opción 2: Consola
```bash
cd e:\PROGRAMACION\parcialFinal
python src/main.py
```

---

## 📦 IMPORTACIONES

### Desde otra carpeta:
```python
from src.usuarios import Usuario
from src.materiales import LibroFisico
from src.sistema import BibliotecaController
```

### Desde src/__init__.py:
```python
from src import Usuario, LibroFisico, BibliotecaController
```

---

**Siguiente: Lee ejemplos prácticos**
