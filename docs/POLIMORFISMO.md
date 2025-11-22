# 🔍 Polimorfismo en el Proyecto

## Descripción General

Implementado mediante **clases abstractas** en `src/materiales.py`. Diferentes subclases implementan el mismo método de forma distinta.

---

## Implementación

### Clase Base Abstracta

```python
from abc import ABC, abstractmethod

class MaterialBibliografico(ABC):
    
    @abstractmethod
    def info(self):
        """Cada subclase DEBE implementar esto"""
        pass
```

### Implementaciones Diferentes

```python
class LibroFisico(MaterialBibliografico):
    def info(self):
        # Implementación para físico
        return f"[F] {self.titulo} - Ubicación: {self.ubicacion}"

class LibroDigital(MaterialBibliografico):
    def info(self):
        # Implementación para digital
        return f"[D] {self.titulo} - Formato: {self.formato}"
```

---

## Ventaja

```python
# Código cliente no sabe qué tipo es
def listar_materiales(materiales):
    for material in materiales:
        print(material.info())  # Ejecuta la versión correcta automáticamente

# Mismo llamado, comportamiento diferente
listar_materiales([libro_fisico, libro_digital])
# Salida:
# [F] Título1 - Ubicación: Estantería A
# [D] Título2 - Formato: pdf
```

---

## Ubicación en Código

- **Implementación:** `src/materiales.py` (líneas 1-70)
- **Pruebas:** `src/casos_prueba.py` (Casos 3-4)

