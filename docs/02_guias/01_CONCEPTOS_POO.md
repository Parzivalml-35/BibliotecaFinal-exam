# 01 CONCEPTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS

## 📚 ¿QUÉ ES POO?

La Programación Orientada a Objetos (POO) es un paradigma que organiza código en **objetos** en lugar de funciones sueltas.

### Analogía del Mundo Real

```
MUNDO REAL                    →    POO EN CÓDIGO
─────────────────────────────────────────────

Persona (cosa)               →    class Persona
├─ Atributos                 →    Propiedades (self.nombre, self.edad)
│  ├─ nombre = "Juan"        →    def __init__(self, nombre, edad)
│  └─ edad = 25
│
└─ Métodos (acciones)        →    def saluda(self)
   ├─ Saluda                 →    def come(self)
   ├─ Come                   →    def duerme(self)
   └─ Duerme
```

---

## 🔷 PILAR 1: ENCAPSULACIÓN

**Agrupar datos y métodos en una unidad (clase)**

### Ejemplo Sin POO (Malo)

```python
# Funciones sueltas
nombre_usuario = "Juan"
edad_usuario = 25

def obtener_nombre():
    return nombre_usuario

def cumpleaños():
    global edad_usuario
    edad_usuario += 1

# Problema: Variables globales, código desorganizado
```

### Ejemplo Con POO (Bien)

```python
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def obtener_nombre(self):
        return self.nombre
    
    def cumpleaños(self):
        self.edad += 1

# Uso
usuario = Usuario("Juan", 25)
print(usuario.obtener_nombre())  # "Juan"
usuario.cumpleaños()
print(usuario.edad)  # 26
```

**Ventajas:**
- ✓ Datos y métodos juntos
- ✓ Fácil de reutilizar
- ✓ Menos variables globales
- ✓ Código organizado

---

## 🔷 PILAR 2: HERENCIA

**Una clase hereda propiedades y métodos de otra**

### Estructura

```
        Clase Padre
    (más general)
            ↑
            │
     Hereda de
            │
        Clase Hijo
    (más específica)
```

### Ejemplo del Proyecto

```python
# Clase padre (abstracta)
class MaterialBibliografico(ABC):
    def __init__(self, codigo, titulo, autor, año):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    @abstractmethod
    def mostrar_info(self):
        pass

# Clase hijo 1
class LibroFisico(MaterialBibliografico):
    def __init__(self, codigo, titulo, autor, año, ubicacion):
        super().__init__(codigo, titulo, autor, año)
        self.ubicacion = ubicacion
    
    def mostrar_info(self):
        return f"📕 Físico: {self.titulo} ({self.ubicacion})"

# Clase hijo 2
class LibroDigital(MaterialBibliografico):
    def __init__(self, codigo, titulo, autor, año, formato):
        super().__init__(codigo, titulo, autor, año)
        self.formato = formato
    
    def mostrar_info(self):
        return f"📱 Digital: {self.titulo} ({self.formato})"

# Uso
libro_fisico = LibroFisico("LIB001", "Python", "Guido", 2023, "Estantería A")
libro_digital = LibroDigital("PDF001", "Ciencia", "Wes", 2022, "pdf")

print(libro_fisico.mostrar_info())    # Usa método de LibroFisico
print(libro_digital.mostrar_info())   # Usa método de LibroDigital
```

### Jerarquía

```
MaterialBibliografico (Clase Abstracta)
├─ Propiedades comunes: codigo, titulo, autor, año
├─ Método abstracto: mostrar_info()
│
├─ LibroFisico (Clase Concreta)
│  ├─ + ubicacion
│  └─ + Implementa mostrar_info() → "📕 Físico"
│
└─ LibroDigital (Clase Concreta)
   ├─ + formato
   └─ + Implementa mostrar_info() → "📱 Digital"
```

**Ventajas:**
- ✓ Código reutilizable
- ✓ Evita duplicación
- ✓ Jerarquía clara
- ✓ Mantenimiento fácil

---

## 🔷 PILAR 3: POLIMORFISMO

**Métodos con el mismo nombre hacen cosas diferentes según la clase**

### Ejemplo

```python
# Ambas clases heredan de MaterialBibliografico
# Ambas tienen mostrar_info()
# ¡Pero hacen cosas diferentes!

libro_fisico = LibroFisico(...)
libro_digital = LibroDigital(...)

# POLIMORFISMO: Mismo método, comportamiento diferente
def mostrar_todos(libros):
    for libro in libros:
        print(libro.mostrar_info())  # ¡Elige dinámicamente!

# Si es LibroFisico → Ejecuta LibroFisico.mostrar_info()
# Si es LibroDigital → Ejecuta LibroDigital.mostrar_info()

mostrar_todos([libro_fisico, libro_digital])
# Salida:
# 📕 Físico: Python (Estantería A)
# 📱 Digital: Ciencia (pdf)
```

### Ventajas

- ✓ Código flexible
- ✓ Fácil de extender
- ✓ Una función maneja varios tipos
- ✓ Menos código repetido

---

## 🔷 PILAR 4: ABSTRACCIÓN

**Mostrar solo lo necesario, ocultar detalles complejos**

### Ejemplo

```python
# Usuario ve esto (interfaz simple)
usuario = Usuario("Juan", 25)
usuario.cumpleaños()  # Simple

# Pero internamente pasa esto (detalles ocultos)
def cumpleaños(self):
    self.edad += 1
    self.actualizar_beneficios()  # Complejo
    self.notificar_sistema()       # Complejo
    self.log_cambio()              # Complejo

# Usuario solo ve: "cumpleaños()"
# Usuario NO ve: validaciones, logs, notificaciones
```

### En el Proyecto

```python
# Simple para el usuario
controlador.registrar_usuario("U001", "Juan", ...)

# Pero internamente:
def registrar_usuario(self, id, nombre, ...):
    # Valida duplicados
    if id in self.usuarios:
        raise ValueError(...)
    
    # Crea objeto
    usuario = Usuario(id, nombre, ...)
    
    # Valida email
    usuario.validar_correo()
    
    # Almacena
    self.usuarios[id] = usuario
    
    # Retorna
    return True
```

**Ventajas:**
- ✓ Interfaz simple
- ✓ Usuario no necesita entender detalles
- ✓ Fácil de cambiar internos
- ✓ Código más seguro

---

## 📊 EJEMPLO COMPLETO: USUARIOS

### Definición

```python
class Usuario:
    def __init__(self, id, nombre, correo, tipo_usuario):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._tipo = tipo_usuario
    
    # ENCAPSULACIÓN: getter con @property
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 0:
            self._nombre = valor
        else:
            raise ValueError("Nombre no puede estar vacío")
    
    def info(self):
        return f"{self.id} - {self.nombre} ({self.correo}) [{self.tipo}]"
```

### Uso

```python
# Crear usuario
usuario = Usuario("U001", "Juan", "juan@email.com", "estudiante")

# Acceder (encapsulación)
print(usuario.nombre)  # "Juan"
print(usuario.id)      # "U001"

# Modificar con validación (encapsulación)
usuario.nombre = "Juan Pérez"  # OK
usuario.nombre = ""            # Error: Nombre no puede estar vacío

# Ver información (abstracción)
print(usuario.info())  # "U001 - Juan Pérez (juan@email.com) [estudiante]"
```

---

## 🎯 LOS 4 PILARES EN EL PROYECTO

### 1. Encapsulación ✓

```python
# Datos privados con _
class Usuario:
    def __init__(self, id, nombre, ...):
        self._id = id
        self._nombre = nombre
    
    # Acceso controlado con @property
    @property
    def id(self):
        return self._id
```

### 2. Herencia ✓

```python
# MaterialBibliografico es padre
# LibroFisico y LibroDigital son hijos
class LibroFisico(MaterialBibliografico):
    pass

class LibroDigital(MaterialBibliografico):
    pass
```

### 3. Polimorfismo ✓

```python
# Mismo método mostrar_info()
# Diferentes implementaciones

# En LibroFisico
def mostrar_info(self):
    return f"Físico: {self.titulo}"

# En LibroDigital
def mostrar_info(self):
    return f"Digital: {self.titulo}"
```

### 4. Abstracción ✓

```python
# MaterialBibliografico es abstracto
class MaterialBibliografico(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# No se puede instanciar directamente
# material = MaterialBibliografico()  # ERROR

# Solo se instancia a través de subclases
libro = LibroFisico(...)  # OK
```

---

## 🧬 DIAGRAMA DE CLASES

```
┌─────────────────────────────┐
│   MaterialBibliografico     │  ← Abstracta
│          (ABC)              │
├─────────────────────────────┤
│ - codigo                    │
│ - titulo                    │
│ - autor                     │
│ - año                       │
├─────────────────────────────┤
│ + mostrar_info() (abstract) │
└──────────────┬──────────────┘
               │
        ┌──────┴────────┐
        │               │
        ↓               ↓
    ┌─────────────┐  ┌─────────────┐
    │ LibroFisico │  │ LibroDigital │
    ├─────────────┤  ├─────────────┤
    │ - ubicacion │  │ - formato   │
    ├─────────────┤  ├─────────────┤
    │+ mostrar_info  │+ mostrar_info
    │ (Implementa)   │ (Implementa)
    └─────────────┘  └─────────────┘
         │                 │
         └─────────────────┘
          (Se pueden usar
           intercambiablemente)
```

---

## 💡 COMPARACIÓN: CON Y SIN POO

### ❌ Sin POO (Procedural)

```python
# Funciones y variables sueltas
usuarios_ids = ["U001", "U002"]
usuarios_nombres = ["Juan", "María"]
usuarios_emails = ["juan@e.com", "maria@e.com"]

def crear_usuario(id, nombre, email):
    usuarios_ids.append(id)
    usuarios_nombres.append(nombre)
    usuarios_emails.append(email)

def obtener_email(id):
    idx = usuarios_ids.index(id)
    return usuarios_emails[idx]

# Problemas:
# - Datos dispersos
# - Fácil de confundir
# - No se escalan
# - Sin validación
```

### ✅ Con POO (Orientado a Objetos)

```python
class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

usuarios = {
    "U001": Usuario("U001", "Juan", "juan@e.com"),
    "U002": Usuario("U002", "María", "maria@e.com"),
}

def obtener_email(id):
    if id in usuarios:
        return usuarios[id].email
    raise ValueError("Usuario no existe")

# Ventajas:
# - Datos organizados
# - Claro y fácil
# - Se escala bien
# - Con validación
```

---

## 🎓 EJERCICIO: CREAR UNA CLASE

Crea una clase `Libro` con:
- Atributos: titulo, autor, páginas
- Método: `info()` que retorne descripción
- Propiedad: `disponible` (True/False)

**Solución:**

```python
class Libro:
    def __init__(self, titulo, autor, paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible
    
    def info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.paginas} pág) - {estado}"

# Uso
libro = Libro("Python", "Guido", 450)
print(libro.info())  # Python por Guido (450 pág) - Disponible
```

---

## 📝 RESUMEN

| Concepto | Qué es | Ventaja |
|----------|--------|---------|
| **Encapsulación** | Agrupar datos y métodos | Organización |
| **Herencia** | Clases que heredan de otras | Reutilización |
| **Polimorfismo** | Mismo método, diferentes implementaciones | Flexibilidad |
| **Abstracción** | Ocultar detalles complejos | Simplicidad |

---

**Siguiente: Lee `02_ESTRUCTURA_SISTEMA.md` para entender cómo todo está conectado**
