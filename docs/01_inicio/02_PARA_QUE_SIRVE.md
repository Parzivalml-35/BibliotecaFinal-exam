# 02 PARA QUÉ SIRVE ESTE PROYECTO

## 🎯 Objetivo

Aprender **Desarrollo de Software Profesional** mediante:
- ✅ **POO** (Clases, Herencia, Polimorfismo)
- ✅ **GUI** (Interfaz Gráfica con Tkinter)
- ✅ **Arquitectura** (Separación de responsabilidades)
- ✅ **Validación** (Manejo de errores)
- ✅ **Buenas Prácticas** (Código limpio)

---

## 📚 QUÉ APRENDES

### Concepto: Orientación a Objetos
```python
# Clases
class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Herencia
class LibroFisico(MaterialBibliografico):
    pass

# Polimorfismo
def mostrar_info(self):
    # Cada clase implementa diferente
    return f"Libro: {self.titulo}"
```

### Concepto: GUI (Interfaz Gráfica)
```python
# Tkinter
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hola")
label.pack()
root.mainloop()
```

### Concepto: Validación
```python
# En propiedades
@correo.setter
def correo(self, value):
    if "@" not in value:
        raise ValueError("Correo inválido")
    self._correo = value
```

---

## 🏗️ ESTRUCTURA PROFESIONAL

```
src/              ← Código Python
docs/             ← Documentación
.gitignore        ← Archivos ignorados
README.md         ← Inicio
```

**Como en empresas reales** 💼

---

## 🎓 COMPETENCIAS ADQUIRIDAS

- [ ] Crear clases con propiedades
- [ ] Usar herencia y polimorfismo
- [ ] Crear interfaces gráficas
- [ ] Validar datos
- [ ] Organizar código profesional
- [ ] Documentar proyectos
- [ ] Usar Git (.gitignore)
- [ ] Seguir mejores prácticas

---

## 📊 COMPARACIÓN

| Antes | Después |
|-------|---------|
| Código suelto | Clases organizadas |
| Sin interfaz | GUI completa |
| Sin validación | Validación robusta |
| Desorganizado | Profesional |

---

## 🎮 PRÓXIMOS PASOS

1. Ejecuta: `python src/gui_biblioteca.py`
2. Lee: `../02_guias/03_MANUAL_USUARIO.md`
3. Lee: `../02_guias/04_RESUMEN_EJECUTIVO.md`
4. Aprende más: `../02_guias/05_GUIA_TKINTER.md`

---

## 📖 CONTINUACIÓN

Tu ruta de aprendizaje:

```
00_LEEME_PRIMERO.md (este archivo) ← Estás aquí
         ↓
01_INICIO_RAPIDO.md
         ↓
02_PARA_QUE_SIRVE.md ← TÚ
         ↓
../02_guias/ (guías completas)
```

---

**¡Estás en el camino correcto! 🚀**

Siguiente: Abre la GUI o lee más guías
