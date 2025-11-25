# 🔒 Encapsulamiento en el Proyecto

## Descripción General

El encapsulamiento se implementa en `src/usuarios.py` usando **@property** para validar datos antes de asignarlos.

---

## ¿Por qué?

Garantizar que **ningún usuario inválido pueda existir en el sistema**. Todos los datos se validan centralizadamente.

---

## Implementación

### 1. Atributos Privados

```python
self._id = None              # Prefijo _ = privado por convención
self._nombre = None
self._correo = None
self._tipo_usuario = None
```

### 2. @property (Getter)

```python
@property
def nombre(self):
    return self._nombre
```

Permite acceso de lectura: `print(usuario.nombre)`

### 3. @property.setter (Setter con Validación)

```python
@nombre.setter
def nombre(self, value):
    if not value or not str(value).strip():
        raise ValueError("Nombre no puede estar vacío")
    self._nombre = str(value).strip()
```

Valida antes de asignar: `usuario.nombre = "Juan"` → valida → asigna

---

## Tipos de Validación Usados

### 1. Validación de No-Vacío (id, nombre)

```python
if not value or not str(value).strip():
    raise ValueError("Campo no puede estar vacío")
```

Valida que:
- No sea `None`
- No sea string vacío
- No sea solo espacios

### 2. Validación con REGEX (correo)

```python
if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
    raise ValueError("Formato de correo inválido")
```

Regex `[^@]+@[^@]+\.[^@]+` valida estructura email:
- Parte1: 1+ caracteres sin `@`
- `@` literal
- Parte2: 1+ caracteres sin `@`
- `.` literal
- Parte3: 1+ caracteres sin `@`

### 3. Validación de Opciones (tipo_usuario)

```python
validos = {"estudiante", "docente", "externo"}
if str(value).lower() not in validos:
    raise ValueError(f"Tipo inválido. Debe ser uno de: {validos}")
```

Solo permite valores específicos.

---

## Flujo en __init__

```python
def __init__(self, usuario_id, nombre, correo, tipo_usuario):
    self._id = None              # Inicializar a None
    self._nombre = None
    self._correo = None
    self._tipo_usuario = None
    
    self.id = usuario_id         # ← Llama setter (valida)
    self.nombre = nombre         # ← Llama setter (valida)
    self.correo = correo         # ← Llama setter (valida)
    self.tipo_usuario = tipo_usuario  # ← Llama setter (valida)
```

Cada asignación pasa por validación automáticamente.

---

## Ventajas

| Ventaja | Ejemplo |
|---------|---------|
| **Validación centralizada** | Cambiar regex → cambia en 1 lugar |
| **Prevención de errores** | `usuario.id = ""` → ValueError inmediato |
| **Datos garantizados válidos** | No existen usuarios inválidos |
| **Interfaz limpia** | Se accede como atributo: `usuario.nombre` |

---

## Uso

```python
# ✅ Válido
usuario = Usuario("U001", "Juan", "juan@email.com", "estudiante")

# ❌ Inválido (levanta ValueError)
usuario = Usuario("", "Juan", "juan@email.com", "estudiante")  # ID vacío
usuario = Usuario("U001", "Juan", "juan", "estudiante")        # Email sin @
usuario = Usuario("U001", "Juan", "juan@email.com", "admin")   # Tipo no válido
```

---

## Ubicación en Código

- **Implementación:** `src/usuarios.py` (líneas 26-55)
- **Pruebas:** `src/casos_prueba.py` (Casos 1-2)

