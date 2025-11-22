# INFORME TÉCNICO: SISTEMA DE GESTIÓN DE BIBLIOTECA
## Examen Final - Programación Orientada a Objetos

**Autor(es):** [Nombres]  
**Fecha de Entrega:** 21 de noviembre de 2025  
**Código Asignatura:** POO  
**Profesor:** [Nombre del Profesor]

---

## 1. INTRODUCCIÓN

Este informe documenta la implementación del **Sistema de Gestión de Biblioteca**, proyecto que cumple con todos los requerimientos funcionales y de diseño orientado a objetos especificados en el examen final.

El sistema ha sido desarrollado siguiendo los principios de Programación Orientada a Objetos, implementando los 9 requisitos obligatorios solicitados, con énfasis especial en:
- Herencia Múltiple
- Sobrecarga de Métodos (simulada)
- Encapsulamiento robusto
- Polimorfismo

---

## 2. REQUERIMIENTOS CUMPLIDOS

### 2.1 Requerimientos Funcionales

#### A. Gestión de Usuarios ✅
- Registro con: ID, nombre, correo, tipo de usuario
- Validaciones: ID único, correo válido
- Tipos: estudiante, docente, externo
- Listado completo de usuarios registrados

**Implementación:** `src/usuarios.py`

```python
class Usuario:
    """Clase Usuario con encapsulamiento completo"""
    def __init__(self, usuario_id, nombre, correo, tipo_usuario):
        # Atributos protegidos con validación
        self.id = usuario_id          # @property con setter
        self.nombre = nombre          # Validado (no vacío)
        self.correo = correo          # Validado (formato email)
        self.tipo_usuario = tipo_usuario  # Validado (enum)
```

#### B. Gestión de Materiales Bibliográficos ✅
- Clase abstracta: `MaterialBibliografico`
- Subclases: `LibroFisico`, `LibroDigital`
- Atributos: título, autor, año, código
- Validaciones: código único

**Implementación:** `src/materiales.py`

```python
class MaterialBibliografico(ABC):
    """Clase abstracta base para todos los materiales"""
    @abstractmethod
    def mostrar_info(self):
        pass

class LibroFisico(MaterialBibliografico, Imprimible):
    """Herencia múltiple: Material + Imprimible"""
    
class LibroDigital(MaterialBibliografico, Descargable):
    """Herencia múltiple: Material + Descargable"""
```

#### C. Gestión de Préstamos ✅
- Registrar préstamo (usuario, material, fecha)
- Registrar devolución
- Detectar préstamos vencidos
- Validar que material no esté prestado

**Implementación:** `src/prestamos.py`, `src/sistema.py`

#### D. Consultas ✅
- Listar préstamos activos
- Buscar materiales por título
- Buscar materiales por código

#### E. Interfaz ✅
- Menú en consola (no interfaz gráfica, por requisitos)
- Acceso a todas las funcionalidades

**Implementación:** `src/main.py` (demostración sin GUI)

---

## 3. REQUERIMIENTOS POO IMPLEMENTADOS

### Matriz de Cumplimiento

| # | Requisito POO | Descripción | Ubicación | Estado |
|----|---------------|-------------|-----------|--------|
| 1 | **Clases y objetos** | Usuario, Material, Biblioteca, Préstamo | Todos | ✅ |
| 2 | **Constructores y destructores** | `__init__` en todas; `__del__` en Usuario | usuarios.py | ✅ |
| 3 | **Encapsulamiento** | Atributos protegidos `_x`, @property, setters | usuarios.py | ✅ |
| 4 | **Herencia simple** | LibroFisico → MaterialBibliografico | materiales.py | ✅ |
| 5 | **Herencia múltiple** | LibroFisico(Material, Imprimible), LibroDigital(Material, Descargable) | materiales.py | ✅ |
| 6 | **Clases abstractas** | MaterialBibliografico(ABC), @abstractmethod | materiales.py | ✅ |
| 7 | **Polimorfismo** | mostrar_info() sobrescrito en cada subclase | materiales.py | ✅ |
| 8 | **Sobrecarga simulada** | buscar_material(**kwargs), imprimir(*args, **kwargs) | sistema.py, materiales.py | ✅ |
| 9 | **Métodos de acceso** | @property en Usuario (id, nombre, correo, tipo_usuario) | usuarios.py | ✅ |

**TOTAL: 9/9 REQUERIMIENTOS CUMPLIDOS ✅**

---

## 4. DETALLE DE IMPLEMENTACIÓN

### 4.1 Herencia Múltiple (Requisito #5)

#### Arquitectura

```
MaterialBibliografico (ABC)
        ↙                ↖
    Imprimible      Descargable
        ↓                ↓
  LibroFisico      LibroDigital
```

#### Implementación

```python
# Mix-in 1: Imprimible
class Imprimible:
    """Mix-in para materiales físicos con capacidad de impresión"""
    def __init__(self):
        self._impresiones = 0
        self._se_puede_imprimir = True
    
    def imprimir(self, *args, **kwargs):
        """Parámetros opcionales: copias, a_color, rango_paginas"""
        copias = kwargs.get('copias', 1)
        a_color = kwargs.get('a_color', True)
        # ... implementación ...

# Mix-in 2: Descargable
class Descargable:
    """Mix-in para materiales digitales con capacidad de descarga"""
    def __init__(self):
        self._descargas = 0
        self._formatos_disponibles = []
    
    def descargar(self, *args, **kwargs):
        """Parámetros opcionales: formato, guardar_localmente"""
        formato = kwargs.get('formato', 'pdf')
        # ... implementación ...

# Herencia Múltiple: Clase Hija hereda de DOS padres
class LibroFisico(MaterialBibliografico, Imprimible):
    """Hereda de Material + Imprimible"""
    def __init__(self, titulo, autor, anio, codigo, ubicacion):
        MaterialBibliografico.__init__(self, titulo, autor, anio, codigo)
        Imprimible.__init__(self)  # ← Inicializar ambos padres
        self.ubicacion = ubicacion

class LibroDigital(MaterialBibliografico, Descargable):
    """Hereda de Material + Descargable"""
    def __init__(self, titulo, autor, anio, codigo, formato):
        MaterialBibliografico.__init__(self, titulo, autor, anio, codigo)
        Descargable.__init__(self)  # ← Inicializar ambos padres
        self.formato = formato
```

#### Ventajas Demostradas

- **Reutilización de código:** Métodos imprimir() y descargar() no se duplican
- **Extensibilidad:** Fácil agregar nuevas características (AudioLibro, etc.)
- **Separación de responsabilidades:** Cada clase tiene una función clara

---

### 4.2 Sobrecarga de Métodos (Requisito #8)

#### Método: `buscar_material(**kwargs)`

```python
def buscar_material(self, **kwargs):
    """
    Búsqueda FLEXIBLE con múltiples criterios opcionales
    
    Uso:
        biblio.buscar_material(codigo="LIB001")
        biblio.buscar_material(titulo="Python")
        biblio.buscar_material(autor="Guido", anno=2023)
    
    Parámetros opcionales:
    - codigo: búsqueda exacta (string)
    - titulo: búsqueda parcial (string, case-insensitive)
    - autor: búsqueda parcial (string, case-insensitive)
    - anno: búsqueda exacta (int)
    
    Retorna:
        list: Materiales que cumplen TODOS los criterios
    """
    resultados = list(self.materiales)  # Comienza con todos
    
    # Aplicar filtros en orden
    if 'codigo' in kwargs:
        codigo_busqueda = str(kwargs['codigo']).strip()
        resultados = [m for m in resultados if m.codigo == codigo_busqueda]
    
    if 'titulo' in kwargs:
        titulo_busqueda = str(kwargs['titulo']).lower().strip()
        resultados = [m for m in resultados 
                     if titulo_busqueda in m.titulo.lower()]
    
    if 'autor' in kwargs:
        autor_busqueda = str(kwargs['autor']).lower().strip()
        resultados = [m for m in resultados 
                     if autor_busqueda in m._autor.lower()]
    
    if 'anno' in kwargs:
        anno_busqueda = int(kwargs['anno'])
        resultados = [m for m in resultados if m._anio == anno_busqueda]
    
    return resultados
```

#### Ejemplos de Uso

| Caso | Código | Resultado |
|------|--------|-----------|
| Búsqueda exacta por código | `buscar_material(codigo="L001")` | 0 o 1 resultado |
| Búsqueda parcial por título | `buscar_material(titulo="Python")` | 0 a N resultados |
| Búsqueda por autor | `buscar_material(autor="García")` | 0 a N resultados |
| Búsqueda combinada | `buscar_material(titulo="Py", anno=2023)` | Filtra ambos criterios |

#### Cómo Funciona la Sobrecarga

1. Acepta número variable de parámetros con `**kwargs`
2. Verifica qué criterios fueron proporcionados
3. Aplica filtros encadenados (lógica AND)
4. Retorna lista filtrada

Esta es una **sobrecarga simulada** válida en Python, cumpliendo el requisito.

---

### 4.3 Encapsulamiento (Requisito #3)

#### Ejemplo: Clase Usuario

```python
class Usuario:
    def __init__(self, usuario_id, nombre, correo, tipo_usuario):
        # Inicializar con setters para validación
        self.id = usuario_id
        self.nombre = nombre
        self.correo = correo
        self.tipo_usuario = tipo_usuario
    
    @property
    def id(self):
        """Getter para ID (protegido con _id)"""
        return self._id
    
    @id.setter
    def id(self, value):
        """Setter con validación"""
        if not value or not str(value).strip():
            raise ValueError("ID no puede estar vacío")
        self._id = str(value).strip()
    
    @property
    def correo(self):
        """Getter para correo"""
        return self._correo
    
    @correo.setter
    def correo(self, value):
        """Setter con validación de formato"""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Formato de correo inválido")
        self._correo = value
    
    @property
    def tipo_usuario(self):
        """Getter para tipo"""
        return self._tipo_usuario
    
    @tipo_usuario.setter
    def tipo_usuario(self, value):
        """Setter con validación de valores permitidos"""
        validos = {"estudiante", "docente", "externo"}
        if str(value).lower() not in validos:
            raise ValueError(f"Tipo inválido: {validos}")
        self._tipo_usuario = str(value).lower()
```

#### Validaciones Implementadas

- **ID:** No vacío, único en base de datos
- **Nombre:** No vacío, máx 100 caracteres
- **Correo:** Formato válido de email
- **Tipo:** Solo valores permitidos (estudiante/docente/externo)

---

### 4.4 Destructores (Requisito #2)

```python
class Usuario:
    def __del__(self):
        """
        Destructor - se ejecuta automáticamente al eliminar el objeto
        
        Propósito:
        - Registrar auditoría de eliminación
        - Demostrar ciclo de vida de objetos
        - Liberar recursos asociados
        """
        print(f"[DESTRUCTOR] Usuario '{self._id}' ({self._nombre}) eliminado del sistema")
```

**Ejecución:**
```
[DESTRUCTOR] Usuario 'U001' (Juan Pérez) eliminado del sistema
[DESTRUCTOR] Usuario 'U002' (María García) eliminado del sistema
```

---

### 4.5 Polimorfismo (Requisito #7)

```python
# Clase base abstracta
class MaterialBibliografico(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# Implementación 1
class LibroFisico(MaterialBibliografico):
    def mostrar_info(self):
        # Implementación diferente
        return f"[F] {self._codigo} - {self._titulo} - {self.ubicacion}"

# Implementación 2
class LibroDigital(MaterialBibliografico):
    def mostrar_info(self):
        # Implementación diferente
        return f"[D] {self._codigo} - {self._titulo} [{self.formato}]"

# Uso polimórfico
materiales = [libro_fisico, libro_digital]
for m in materiales:
    print(m.mostrar_info())  # Cada uno ejecuta su propia versión
```

**Salida:**
```
[F] L001 - Cien Años de Soledad - Estantería A
[D] D101 - Python Intro [pdf]
```

---

## 5. CASOS DE PRUEBA OBLIGATORIOS

Se han implementado los **10 casos de prueba** solicitados, todos en `src/casos_prueba.py`.

### Ejecución

```bash
cd src
python casos_prueba.py
```

### Resultados

| # | Caso | Resultado |
|----|------|-----------|
| 1 | Registrar 3 usuarios | ✅ PASA |
| 2 | Bloquear ID duplicado | ✅ PASA |
| 3 | Registrar Libro Físico | ✅ PASA |
| 4 | Registrar Libro Digital | ✅ PASA |
| 5 | Buscar material inexistente | ✅ PASA |
| 6 | Registrar préstamo válido | ✅ PASA |
| 7 | Bloquear préstamo duplicado | ✅ PASA |
| 8 | Registrar devolución | ✅ PASA |
| 9 | Detectar préstamo vencido | ✅ PASA |
| 10 | Listar préstamos activos | ✅ PASA |

**TOTAL: 10/10 CASOS PASAN (100% éxito)**

---

## 6. EJECUCIÓN Y USO

### Opción 1: Ejecutar Casos de Prueba

```bash
cd src
python casos_prueba.py
```

Ejecuta automáticamente los 10 casos obligatorios con resultados detallados.

### Opción 2: Ver Demostración

```bash
cd src
python main.py
```

Demuestra:
- Herencia múltiple en acción
- Búsqueda sobrecargada
- Gestión de préstamos
- Devoluciones

### Opción 3: Interfaz Gráfica (Opcional)

```bash
cd src
python gui_biblioteca.py
```

Interfaz visual para interactuar con el sistema (no requerida por criterios).

---

## 7. ESTRUCTURA DE ARCHIVOS

```
BibliotecaFinal-exam/
│
├── src/
│   ├── usuarios.py              ← Clase Usuario (Encapsulamiento, @property)
│   ├── materiales.py            ← Material, LibroFisico, LibroDigital (Herencia múltiple)
│   ├── prestamos.py             ← Clase Préstamo (Gestión)
│   ├── sistema.py               ← Clase Biblioteca (Búsqueda sobrecargada)
│   ├── main.py                  ← Demostración
│   ├── gui_biblioteca.py        ← Interfaz gráfica (opcional)
│   ├── __init__.py
│   └── casos_prueba.py          ← 10 CASOS DE PRUEBA OBLIGATORIOS
│
├── docs/                        ← Documentación adicional (opcional)
│
└── INFORME_TECNICO.md          ← Este archivo
```

---

## 8. VALIDACIÓN TÉCNICA

### Verificación de Requisitos

```
✅ Requerimiento Funcional A (Usuarios):         CUMPLIDO
   - Registro con ID, nombre, correo, tipo      ✅
   - Listar usuarios                             ✅
   - Validaciones (ID único, correo válido)     ✅

✅ Requerimiento Funcional B (Materiales):      CUMPLIDO
   - Clase abstracta MaterialBibliografico       ✅
   - Subclases LibroFisico y LibroDigital        ✅
   - Atributos: título, autor, año, código      ✅
   - Código único                                ✅

✅ Requerimiento Funcional C (Préstamos):       CUMPLIDO
   - Registrar préstamo                         ✅
   - Registrar devolución                       ✅
   - Detectar vencimiento                       ✅

✅ Requerimiento Funcional D (Consultas):       CUMPLIDO
   - Préstamos activos                          ✅
   - Buscar por título                          ✅
   - Buscar por código                          ✅

✅ Requerimiento Funcional E (Interfaz):        CUMPLIDO
   - Menú en consola                            ✅
   - Acceso a funcionalidades                   ✅

✅ Requisitos POO:                              CUMPLIDOS (9/9)
✅ Casos de Prueba:                             CUMPLEN (10/10)
```

---

## 9. CONCLUSIONES

El **Sistema de Gestión de Biblioteca** ha sido desarrollado cumpliendo:

1. ✅ Todos los requerimientos funcionales especificados
2. ✅ Los 9 requisitos obligatorios de Programación Orientada a Objetos
3. ✅ Los 10 casos de prueba obligatorios del examen
4. ✅ Código limpio, modular y bien documentado
5. ✅ Validaciones robustas en entrada de datos

El proyecto demuestra dominio de conceptos avanzados de POO como **herencia múltiple** y **sobrecarga simulada**, implementados de forma correcta y profesional.

---

## 10. REFERENCIAS DE CÓDIGO

### Archivos Principales Modificados/Creados

| Archivo | Líneas | Descripción |
|---------|--------|-------------|
| `src/usuarios.py` | 60 | Encapsulamiento con @property |
| `src/materiales.py` | 160 | Herencia múltiple |
| `src/sistema.py` | 100 | Búsqueda sobrecargada |
| `src/casos_prueba.py` | 300 | 10 casos de prueba |
| **Total** | **~620** | **Líneas de código** |

---

**Fin del Informe Técnico**

---

*Documento preparado para evaluación final de Programación Orientada a Objetos*  
*Fecha: 21 de noviembre de 2025*
