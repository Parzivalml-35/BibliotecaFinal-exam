# 📚 Búsqueda y Sobrecarga de Métodos

## Búsqueda por Título

Ubicación: `src/sistema.py` (línea 85)

```python
def buscar_material_por_titulo(self, titulo):
    """Busca un material por título (insensible a mayúsculas)"""
    for material in self.materiales:
        if material.titulo.lower() == titulo.lower():
            return material
    return None
```

**Uso:**
```python
biblio = Biblioteca()
material = biblio.buscar_material_por_titulo("Python")
```

---

## Sobrecarga de Métodos

Ubicación: `src/sistema.py` (línea 120)

```python
def buscar_material(self, codigo=None, titulo=None, autor=None, anno=None):
    """
    Busca flexible: acepta cualquier combinación de parámetros.
    Simula sobrecarga de métodos en Python.
    """
    if codigo:
        return self.buscar_material_por_codigo(codigo)
    elif titulo:
        return self.buscar_material_por_titulo(titulo)
    elif autor:
        return self.buscar_material_por_autor(autor)
    elif anno:
        return self.buscar_material_por_anno(anno)
    return None
```

**Uso:**
```python
biblio.buscar_material(codigo="L001")
biblio.buscar_material(titulo="Python")
biblio.buscar_material(autor="Guido")
biblio.buscar_material(titulo="Python", autor="Guido")
```

---

## Técnica: **kwargs

Python no soporta sobrecarga tradicional (mismo nombre, diferentes tipos). La solución es usar **parámetros opcionales**:

```python
# Un método que se adapta a lo que le pases
def buscar_material(self, codigo=None, titulo=None, autor=None, anno=None):
    # Ejecuta lógica diferente según qué parámetro tenga valor
```

---

## Ubicación en Código

- **Búsqueda:** `src/sistema.py` (líneas 85-120)
- **Pruebas:** `src/casos_prueba.py` (Caso 5-6)

