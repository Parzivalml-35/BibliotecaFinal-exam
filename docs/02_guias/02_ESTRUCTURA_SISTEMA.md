# 02 ESTRUCTURA INTERNA DEL SISTEMA

## 🔧 CÓMO ESTÁN CONECTADAS LAS PARTES

```
USUARIO EN GUI
    ↓
    ├─ Escribe datos
    ├─ Presiona botón
    └─ ¿Qué pasa internamente?
            ↓
       VISTA (GUI)
       gui_biblioteca.py
            ├─ Obtiene datos del formulario
            ├─ Valida campos básicos
            └─ Llama a CONTROLADOR
                     ↓
                CONTROLADOR
                sistema.py
                     ├─ Valida entrada más profundamente
                     ├─ Crea MODELOS
                     ├─ Almacena en diccionarios
                     ├─ Retorna éxito/error
                     └─ Devuelve a VISTA
                            ↓
                       VISTA actualiza
                       ├─ Muestra mensaje
                       ├─ Limpia formulario
                       ├─ Actualiza listas
                       └─ Usuario ve resultado
```

---

## 🏗️ ARQUITECTURA MVC

```
┌─────────────────────────────────────────────────────────┐
│  PRESENTACIÓN (Vista)                                   │
│  ┌─ gui_biblioteca.py (Tkinter GUI)                     │
│  └─ main.py (Consola)                                   │
│                                                         │
│  ¿Qué hace?: Mostrar interfaz, recopilar entrada      │
│  ¿Qué NO hace?: Lógica de negocio                      │
└────────────────────┬────────────────────────────────────┘
                     │
         (Llama a través de)
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│  LÓGICA (Controlador)                                   │
│  ┌─ sistema.py (BibliotecaController)                   │
│                                                         │
│  ¿Qué hace?: Validar, orquestar, coordinar             │
│  ¿Qué NO hace?: Mostrar en pantalla                    │
└────────────────────┬────────────────────────────────────┘
                     │
         (Usa y crea)
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│  DATOS (Modelo)                                         │
│  ┌─ usuarios.py (Clase Usuario)                         │
│  ├─ materiales.py (Clases Libro)                        │
│  └─ prestamos.py (Clase Prestamo)                       │
│                                                         │
│  ¿Qué hace?: Almacenar datos, validar negocio          │
│  ¿Qué NO hace?: Interactuar con usuario                │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 CARPETA: src/ (Código)

```
src/
├─ usuarios.py          (MODELO)
├─ materiales.py        (MODELO)
├─ prestamos.py         (MODELO)
├─ sistema.py           (CONTROLADOR)
├─ gui_biblioteca.py    (VISTA)
├─ main.py              (VISTA)
└─ __init__.py          (Exporta clases)
```

### usuarios.py (MODELO)

```python
class Usuario:
    def __init__(self, id, nombre, correo, tipo_usuario):
        self._id = id              # Privado
        self._nombre = nombre
        self._correo = correo
        self._tipo = tipo_usuario
    
    # Propiedades (getters/setters con validación)
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        # Validación: no puede estar vacío
        if len(valor) > 0:
            self._nombre = valor
    
    def validar_correo(self):
        # Validación: debe tener @
        import re
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self._correo)
    
    def info(self):
        return f"{self.id} - {self.nombre} ({self.correo})"
```

**Responsabilidades:**
- ✓ Almacenar datos de usuario
- ✓ Validar email
- ✓ Retornar información formateada

---

### materiales.py (MODELO)

```python
from abc import ABC, abstractmethod

class MaterialBibliografico(ABC):
    """Clase abstracta para todos los materiales"""
    
    def __init__(self, codigo, titulo, autor, año):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    @abstractmethod
    def mostrar_info(self):
        pass

class LibroFisico(MaterialBibliografico):
    """Libro físico en estantería"""
    
    def __init__(self, codigo, titulo, autor, año, ubicacion):
        super().__init__(codigo, titulo, autor, año)
        self.ubicacion = ubicacion
    
    def mostrar_info(self):
        return f"📕 [{self.codigo}] {self.titulo} - {self.ubicacion}"

class LibroDigital(MaterialBibliografico):
    """Libro digital (PDF, EPUB, etc)"""
    
    def __init__(self, codigo, titulo, autor, año, formato):
        super().__init__(codigo, titulo, autor, año)
        self.formato = formato
    
    def mostrar_info(self):
        return f"📱 [{self.codigo}] {self.titulo} ({self.formato})"

# Mixins (comportamientos adicionales)
class Imprimible:
    def imprimir(self):
        return f"Imprimiendo {self.titulo}..."

class Descargable:
    def descargar(self):
        return f"Descargando {self.titulo}..."
```

**Responsabilidades:**
- ✓ Almacenar datos de material
- ✓ Diferenciar tipos (físico/digital)
- ✓ Retornar información

---

### prestamos.py (MODELO)

```python
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, material, usuario, fecha_inicio=None):
        self._material = material
        self._usuario = usuario
        self.fecha_inicio = fecha_inicio or datetime.now()
        self.fecha_devolucion = None
        self.activo_bool = True
    
    # Getters públicos (reemplazar acceso a _protegido)
    def get_material(self):
        return self._material
    
    def get_usuario(self):
        return self._usuario
    
    def activo(self):
        """¿Está prestado actualmente?"""
        return self.activo_bool
    
    def esta_vencido(self):
        """¿Pasaron 7 días?"""
        if not self.activo_bool:
            return False
        dias = (datetime.now() - self.fecha_inicio).days
        return dias > 7
    
    def marcar_devolucion(self):
        """Registrar devolución"""
        self.fecha_devolucion = datetime.now()
        self.activo_bool = False
    
    def info(self):
        estado = "Activo" if self.activo_bool else "Devuelto"
        return f"{self._usuario.id} → {self._material.codigo} ({estado})"
```

**Responsabilidades:**
- ✓ Almacenar datos de préstamo
- ✓ Calcular si está vencido
- ✓ Registrar devolución

---

### sistema.py (CONTROLADOR)

```python
class BibliotecaController:
    def __init__(self):
        self.usuarios = {}      # {id: Usuario}
        self.materiales = {}    # {codigo: Material}
        self.prestamos = []     # [Prestamo, ...]
    
    # USUARIOS
    def registrar_usuario(self, id_usuario, nombre, correo, tipo_usuario):
        """Registrar nuevo usuario con validación"""
        
        # 1. Validar entrada
        if id_usuario in self.usuarios:
            raise ValueError(f"ID {id_usuario} ya existe")
        
        # 2. Crear modelo
        usuario = Usuario(id_usuario, nombre, correo, tipo_usuario)
        
        # 3. Validar modelo
        if not usuario.validar_correo():
            raise ValueError(f"Email {correo} inválido")
        
        # 4. Almacenar
        self.usuarios[id_usuario] = usuario
        
        # 5. Retornar éxito
        return True
    
    def listar_usuarios(self):
        """Retornar lista de usuarios"""
        return list(self.usuarios.values())
    
    # MATERIALES
    def registrar_material(self, tipo, codigo, titulo, autor, año, campo_extra):
        """Registrar material (físico o digital)"""
        
        # 1. Validar
        if codigo in self.materiales:
            raise ValueError(f"Código {codigo} ya existe")
        
        # 2. Crear según tipo
        if tipo == "fisico":
            material = LibroFisico(codigo, titulo, autor, año, campo_extra)
        elif tipo == "digital":
            material = LibroDigital(codigo, titulo, autor, año, campo_extra)
        else:
            raise ValueError("Tipo inválido")
        
        # 3. Almacenar
        self.materiales[codigo] = material
        
        # 4. Retornar
        return True
    
    def listar_materiales(self):
        """Retornar lista de materiales"""
        return list(self.materiales.values())
    
    # PRÉSTAMOS
    def registrar_prestamo(self, id_usuario, codigo_material):
        """Registrar nuevo préstamo"""
        
        # 1. Validar usuario existe
        if id_usuario not in self.usuarios:
            raise ValueError("Usuario no existe")
        
        # 2. Validar material existe
        if codigo_material not in self.materiales:
            raise ValueError("Material no existe")
        
        # 3. Validar material NO está prestado
        for p in self.prestamos:
            if p.get_material().codigo == codigo_material and p.activo():
                raise ValueError("Material ya está prestado")
        
        # 4. Crear préstamo
        usuario = self.usuarios[id_usuario]
        material = self.materiales[codigo_material]
        prestamo = Prestamo(material, usuario)
        
        # 5. Almacenar
        self.prestamos.append(prestamo)
        
        # 6. Retornar
        return True
    
    def registrar_devolucion(self, codigo_material):
        """Registrar devolución"""
        
        # 1. Buscar préstamo activo
        for p in self.prestamos:
            if p.get_material().codigo == codigo_material and p.activo():
                p.marcar_devolucion()
                return True
        
        # 2. Si no encuentra
        raise ValueError("No hay préstamo activo")
    
    def listar_prestamos(self):
        """Retornar solo préstamos activos"""
        return [p for p in self.prestamos if p.activo()]
    
    def listar_vencidos(self):
        """Retornar solo préstamos vencidos"""
        return [p for p in self.prestamos if p.esta_vencido()]
```

**Responsabilidades:**
- ✓ Validar entrada del usuario
- ✓ Crear modelos
- ✓ Almacenar en diccionarios/listas
- ✓ Lanzar excepciones claras
- ✓ Retornar datos

---

## 🔄 FLUJO COMPLETO: Registrar Usuario

```
1. USUARIO EN GUI
   Escribe en formularios:
   - ID: "U001"
   - Nombre: "Juan"
   - Correo: "juan@email.com"
   - Tipo: "estudiante"
   
   Presiona: "Registrar Usuario"

2. GUI (gui_biblioteca.py)
   def registrar_usuario_gui(self):
       # Obtiene valores
       id_usuario = self.entrada_id.get()
       nombre = self.entrada_nombre.get()
       correo = self.entrada_correo.get()
       tipo = self.combo_tipo.get()
       
       try:
           # Llama a controlador
           self.controlador.registrar_usuario(
               id_usuario, nombre, correo, tipo
           )
           # Éxito
           messagebox.showinfo("Éxito", "Usuario registrado")
           self.actualizar_lista_usuarios()
       except ValueError as e:
           # Error
           messagebox.showerror("Error", str(e))

3. CONTROLADOR (sistema.py)
   def registrar_usuario(self, id_usuario, ...):
       # Valida ID duplicado
       if id_usuario in self.usuarios:
           raise ValueError("ID ya existe")
       
       # Crea modelo
       usuario = Usuario(id_usuario, nombre, correo, tipo)
       
       # Valida email
       if not usuario.validar_correo():
           raise ValueError("Email inválido")
       
       # Almacena
       self.usuarios[id_usuario] = usuario
       
       # Retorna OK
       return True

4. MODELO (usuarios.py)
   class Usuario:
       def __init__(self, id, nombre, correo, tipo):
           self._id = id
           self._nombre = nombre
           self._correo = correo
           self._tipo = tipo
       
       @property
       def correo(self):
           return self._correo
       
       def validar_correo(self):
           import re
           return re.match(r"^[\w\.-]+@...$", self._correo)

5. RESULTADO
   ✓ Usuario creado en memoria
   ✓ GUI muestra "Usuario registrado"
   ✓ Lista se actualiza
   ✓ Formulario se limpia
```

---

## 🎯 RESPONSABILIDADES CLARAS

| Componente | Hace | NO Hace |
|-----------|------|---------|
| **Modelo** (Usuario, Libro, Préstamo) | Almacena datos, Valida negocio | Interactúa con usuario, Muestra en pantalla |
| **Controlador** (BibliotecaController) | Valida, Orquesta, Crea modelos | Muestra en pantalla, Accede a _privado |
| **Vista** (GUI, consola) | Muestra interfaz, Recopila entrada | Lógica compleja, Directamente con datos |

---

## 🔗 DEPENDENCIAS

```
main.py / gui_biblioteca.py (VISTA)
    ↓
    imports
    ↓
sistema.py (CONTROLADOR)
    ↓
    imports
    ↓
usuarios.py + materiales.py + prestamos.py (MODELOS)
```

**Flujo de importación:**
```python
# En gui_biblioteca.py
from src.sistema import BibliotecaController

# En sistema.py
from src.usuarios import Usuario
from src.materiales import LibroFisico, LibroDigital
from src.prestamos import Prestamo
```

---

## 💾 ALMACENAMIENTO EN MEMORIA

```
BibliotecaController
│
├─ usuarios (diccionario)
│  └─ "U001" → Usuario(id="U001", nombre="Juan", ...)
│  └─ "U002" → Usuario(id="U002", nombre="María", ...)
│
├─ materiales (diccionario)
│  └─ "LIB001" → LibroFisico(codigo="LIB001", ...)
│  └─ "PDF001" → LibroDigital(codigo="PDF001", ...)
│
└─ prestamos (lista)
   └─ Prestamo(usuario=U001, material=LIB001, activo=True)
   └─ Prestamo(usuario=U002, material=PDF001, activo=False)
```

---

## ⚠️ FLUJO DE ERRORES

```
Usuario presiona botón
    ↓
GUI intenta registrar
    ↓
Controlador valida
    ↓
¿Error de validación?
    ├─ SÍ → raise ValueError("Mensaje claro")
    │       ↓
    │       GUI captura con try/except
    │       ↓
    │       Muestra messagebox.showerror()
    │       ↓
    │       Usuario ve: "Error: Mensaje claro"
    │
    └─ NO → Crea modelo
           ↓
           Almacena
           ↓
           return True
           ↓
           GUI muestra éxito
           ↓
           Usuario ve confirmación
```

---

## 📊 DIAGRAMA DE FLUJO: Registrar Préstamo

```
Usuario selecciona:
- ID Usuario: U001
- Código Material: LIB001
- Presiona: "Registrar Préstamo"
    ↓
GUI: registrar_prestamo_gui()
    ├─ Obtiene entrada
    └─ Llama: controlador.registrar_prestamo("U001", "LIB001")
         ↓
CONTROLADOR: registrar_prestamo()
    ├─ ¿Usuario existe? ("U001" in usuarios)
    │  └─ NO → raise ValueError("Usuario no existe")
    │
    ├─ ¿Material existe? ("LIB001" in materiales)
    │  └─ NO → raise ValueError("Material no existe")
    │
    ├─ ¿Material YA está prestado?
    │  for p in prestamos:
    │      if codigo == "LIB001" and p.activo()
    │          └─ SÍ → raise ValueError("Ya está prestado")
    │
    └─ ✓ TODO OK
       ├─ usuario = usuarios["U001"]
       ├─ material = materiales["LIB001"]
       ├─ prestamo = Prestamo(material, usuario)
       ├─ prestamos.append(prestamo)
       └─ return True
           ↓
GUI: 
    ├─ messagebox.showinfo("Éxito", "Préstamo registrado")
    ├─ actualizar_listas_prestamos()
    └─ Usuario ve en "Préstamos Activos": U001 → LIB001
```

---

## 🎓 RESUMEN

**Separación de capas:**

1. **VISTA** (GUI)
   - Muestra botones, campos, listas
   - Recopila entrada del usuario
   - Llama al controlador
   - Muestra resultado

2. **CONTROLADOR** (Orquestador)
   - Valida entrada
   - Crea modelos
   - Almacena datos
   - Retorna OK/ERROR

3. **MODELO** (Datos)
   - Almacena información
   - Valida reglas de negocio
   - No conoce a GUI

**Ventaja:** Cambiar GUI sin cambiar lógica ✓

---

**Siguiente: Lee `03_MANUAL_USUARIO.md` para aprender a usar la GUI**
