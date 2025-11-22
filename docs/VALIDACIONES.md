# ✅ Validaciones en el Proyecto

## Tipos de Validaciones Implementadas

### 1. Validación de ID Único

**Ubicación:** `src/usuarios.py`

**Implementación:**
```python
class Usuario:
    _usuarios_registrados = set()  # Conjunto de clase
    
    @id.setter
    def id(self, value):
        if id in Usuario._usuarios_registrados:
            raise ValueError("ID ya existe")
        Usuario._usuarios_registrados.add(id)
        self._id = value
```

**Resultado:** No puedes crear dos usuarios con el mismo ID.

**Prueba:** `casos_prueba.py` Caso 2 - "Prevenir ID duplicado"

---

### 2. Validación de Email (REGEX)

**Ubicación:** `src/usuarios.py` (correo.setter)

**Implementación:**
```python
import re

@correo.setter
def correo(self, value):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValueError("Formato de correo inválido")
    self._correo = value
```

**REGEX explicado:**
- `[^@]+` = 1+ caracteres sin @
- `@` = el símbolo @ literal
- `[^@]+` = 1+ caracteres sin @
- `\.` = un punto literal
- `[^@]+` = 1+ caracteres sin @

**Resultado:** Email debe tener formato: usuario@dominio.extensión

---

### 3. Validación de Préstamo Único

**Ubicación:** `src/sistema.py` (registrar_prestamo)

**Implementación:**
```python
def registrar_prestamo(self, usuario_id, material_id):
    # Verificar que material no esté prestado
    for prestamo in self.prestamos:
        if prestamo.material_id == material_id and prestamo.devuelto_en is None:
            raise ValueError("Material ya está prestado")
    
    # Si llega aquí, es válido
    prestamo = Prestamo(usuario_id, material_id)
    self.prestamos.append(prestamo)
    return prestamo
```

**Resultado:** No puedes prestar el mismo material dos veces.

**Prueba:** `casos_prueba.py` Caso 7 - "Prevenir préstamo duplicado"

---

### 4. Validación de Vencimiento

**Ubicación:** `src/prestamos.py`

**Implementación:**
```python
def esta_vencido(self, dias_limite=7):
    if self.devuelto_en:
        return False
    
    dias_pasados = (datetime.now() - self.prestado_en).days
    return dias_pasados > dias_limite
```

**Resultado:** Detecta si un préstamo activo ha superado el plazo.

**Prueba:** `casos_prueba.py` Caso 9 - "Detectar préstamo vencido"

---

## Tabla de Validaciones

| Validación | Ubicación | Tipo | Caso |
|-----------|-----------|------|------|
| ID único | Usuario | Conjunto (set) | 2 |
| Email válido | Usuario | REGEX | 1 |
| No-vacío | Usuario | Condicional | 1 |
| Préstamo único | Biblioteca | Búsqueda en lista | 7 |
| Vencimiento | Préstamo | Cálculo de días | 9 |

---

## Ubicación en Código

- **ID único:** `src/usuarios.py`
- **Email:** `src/usuarios.py` (REGEX)
- **Préstamo:** `src/sistema.py`
- **Vencimiento:** `src/prestamos.py`
- **Pruebas:** `src/casos_prueba.py` (5 casos validados)

