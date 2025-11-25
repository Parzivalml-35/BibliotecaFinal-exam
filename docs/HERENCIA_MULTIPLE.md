# 🧬 Herencia Múltiple en el Proyecto

## Descripción General

Implementada en `src/materiales.py` mediante **Mix-ins**. Permite que una clase herede funcionalidad de múltiples padres.

---

## Implementación

### Base Abstracta

```python
from abc import ABC, abstractmethod

class MaterialBibliografico(ABC):
    @abstractmethod
    def info(self):
        pass
```

### Mix-ins (Funcionalidad adicional)

```python
class Imprimible:
    def imprimir(self):
        return f"Imprimiendo: {self.titulo}"

class Descargable:
    def descargar(self):
        return f"Descargando: {self.titulo}"
```

### Herencia Múltiple

```python
class LibroFisico(MaterialBibliografico, Imprimible):
    """Hereda de Material Y de Imprimible"""
    
    def info(self):
        return f"[F] {self.titulo} - Ubicación: {self.ubicacion}"

class LibroDigital(MaterialBibliografico, Descargable):
    """Hereda de Material Y de Descargable"""
    
    def info(self):
        return f"[D] {self.titulo} - Formato: {self.formato}"
```

---

## Ventajas

| Aspecto | Beneficio |
|--------|-----------|
| **Reutilización** | `LibroFisico` reutiliza `Imprimible` sin duplicar |
| **Modularidad** | Mix-ins pueden usarse en otras clases |
| **Flexibilidad** | Combina funcionalidades según necesidad |
| **Claridad** | Expresa relaciones correctamente |

---

## Uso

```python
libro_fisico = LibroFisico("L001", "Título", "Autor", 2020, "Estantería A")
libro_fisico.info()       # De MaterialBibliografico
libro_fisico.imprimir()   # De Imprimible

libro_digital = LibroDigital("D001", "Título", "Autor", 2020, "pdf")
libro_digital.info()      # De MaterialBibliografico
libro_digital.descargar() # De Descargable
```

---

## Ubicación en Código

- **Clases base:** `src/materiales.py` (líneas 1-70)
- **Pruebas:** `src/casos_prueba.py` (Casos 3-4)
- **Demostración:** `src/main.py` (líneas 45-75)

