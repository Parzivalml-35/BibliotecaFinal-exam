# 🗑️ Destructores en el Proyecto

## Descripción General

Ubicación: `src/usuarios.py` (línea 20)

```python
def __del__(self):
    """
    Destructor - se ejecuta cuando el objeto es eliminado.
    Registra la eliminación (auditoría del sistema).
    """
    print(f"[DESTRUCTOR] Usuario '{self._id}' ({self._nombre}) eliminado del sistema")
```

---

## ¿Cuándo se ejecuta?

El destructor se ejecuta automáticamente cuando:

1. El objeto sale de scope
2. Se elimina con `del usuario`
3. El programa termina
4. Se asigna otro valor a la variable

---

## Uso

```python
usuario = Usuario("U001", "Juan", "juan@email.com", "estudiante")
# Usuario creado

# Usuario sale de scope al terminar la función
# → __del__() se ejecuta automáticamente
# → Se imprime: [DESTRUCTOR] Usuario 'U001' (Juan) eliminado del sistema
```

---

## En el Proyecto

**Propósito:** Demostrar el ciclo de vida de objetos y auditoria del sistema.

**Prueba:** `src/casos_prueba.py` (línea 292, al final)

Verás la salida:
```
[DESTRUCTOR] Usuario 'U001' (Juan Pérez) eliminado del sistema
[DESTRUCTOR] Usuario 'U002' (María García) eliminado del sistema
[DESTRUCTOR] Usuario 'U003' (Pedro López) eliminado del sistema
```

---

## Ubicación en Código

- **Implementación:** `src/usuarios.py` (líneas 20-23)
- **Pruebas:** `src/casos_prueba.py` (línea 292)

