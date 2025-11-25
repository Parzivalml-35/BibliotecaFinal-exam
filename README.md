# 📚 Sistema de Biblioteca - Examen Final POO

**Estado:** ✅ Completado  
**Versión:** 1.0  
**Fecha:** 25 de noviembre de 2025

---

## 🚀 Ejecución

### Ver todos los casos de prueba

```bash
python src/casos_prueba.py
```

**Resultado esperado:**

### Ver la demostración del sistema:

```bash
cd src
python main.py
```
---

## 🎯 Requisitos Implementados

| # | Requisito | Implementación | Documentación |
|---|-----------|---|---|
| **1** | Herencia Múltiple | Mix-ins: `LibroFisico(Material, Imprimible)` | [`docs/HERENCIA_MULTIPLE.md`](docs/HERENCIA_MULTIPLE.md) |
| **2** | Búsqueda por Título | `buscar_material_por_titulo()` | [`docs/BUSQUEDA_SOBRECARGA.md`](docs/BUSQUEDA_SOBRECARGA.md) |
| **3** | Sobrecarga de Métodos | `buscar_material(**kwargs)` | [`docs/BUSQUEDA_SOBRECARGA.md`](docs/BUSQUEDA_SOBRECARGA.md) |
| **4** | Encapsulamiento | @property con validación | [`docs/ENCAPSULAMIENTO.md`](docs/ENCAPSULAMIENTO.md) |
| **5** | Destructores | `__del__()` en Usuario | [`docs/DESTRUCTORES.md`](docs/DESTRUCTORES.md) |
| **6** | Polimorfismo | @abstractmethod | [`docs/POLIMORFISMO.md`](docs/POLIMORFISMO.md) |
| **7** | Validaciones | ID único, email, préstamo | [`docs/VALIDACIONES.md`](docs/VALIDACIONES.md) |
| **8** | Ejecución Consola | terminal | `src/casos_prueba.py` |
| **9** | Casos de Prueba | 10 casos | `src/casos_prueba.py` |

---

## 📁 Estructura

```
BibliotecaFinal-exam/
├── src/
│   ├── usuarios.py              (Encapsulamiento, @property)
│   ├── materiales.py            (Herencia múltiple)
│   ├── prestamos.py             (Gestión de préstamos)
│   ├── sistema.py               (Búsqueda sobrecargada)
│   ├── main.py                  (Demostración)
│   └── casos_prueba.py          (10 CASOS DE PRUEBA)
│
└── README.md                    (Presentacion del proyecto)
```

---

## ✅ 10 Casos de Prueba

1. ✅ Registrar 3 usuarios
2. ✅ Bloquear ID duplicado
3. ✅ Registrar Libro Físico
4. ✅ Registrar Libro Digital
5. ✅ Buscar material inexistente
6. ✅ Registrar préstamo válido
7. ✅ Bloquear préstamo duplicado
8. ✅ Registrar devolución
9. ✅ Detectar préstamo vencido
10. ✅ Listar préstamos activos


---

## 🎓 Conceptos Aprendidos

- ✅ Clases y Objetos
- ✅ Herencia y Polimorfismo
- ✅ Clases Abstractas (ABC)
- ✅ Propiedades y Validación
- ✅ Organización Profesional

---

## 🏆 Mejores Prácticas

- ✅ Separación: `src/` código, `docs/` documentación
- ✅ Nombres claros y descriptivos
- ✅ Comentarios y docstrings
- ✅ Validación robusta
- ✅ Manejo de errores
- ✅ .gitignore profesional
- ✅ Estructura escalable

---

## 📱 Tecnología

- **Python 3.x**
- **POO** - Orientación a Objetos
- **Git** - Control de versiones

---
