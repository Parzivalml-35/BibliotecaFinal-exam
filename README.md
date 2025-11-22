# 📚 Sistema de Biblioteca - Proyecto Educativo

**Versión:** 1.0 | **Fecha:** 21 de noviembre de 2025 | **Estado:** ✅ Completo

---

## 🎯 ¿Qué es esto?

Un **Sistema de Biblioteca completo** con interfaz gráfica, código profesional y documentación educativa para aprender:
- ✅ Programación Orientada a Objetos (POO)
- ✅ Interfaz Gráfica (Tkinter)
- ✅ Arquitectura Profesional
- ✅ Buenas Prácticas de Código

---

## 🚀 INICIO EN 2 MINUTOS

### Paso 1: Abre terminal
```bash
cd e:\PROGRAMACION\parcialFinal
```

### Paso 2: Ejecuta la app
```bash
python src/gui_biblioteca.py
```

**¡Se abre una ventana con tu aplicación! 🎉**

---

## 📁 Estructura

```
parcialFinal/
├── src/                    ← Código Python
│   ├── usuarios.py
│   ├── materiales.py
│   ├── prestamos.py
│   ├── sistema.py
│   ├── gui_biblioteca.py   ⭐ Interfaz gráfica
│   └── main.py
│
├── docs/                   ← Documentación
│   ├── 01_inicio/          📍 EMPIEZA AQUÍ
│   ├── 02_guias/           Guías completas
│   ├── 03_ejemplos/        Código ejemplo
│   ├── 04_referencia/      Consulta rápida
│   └── README_DOCS.md      Índice
│
└── README.md               Este archivo
```

---

## 📖 DOCUMENTACIÓN

### 🟢 Nivel 1: Inicio (5-30 min)
**Para todos - Empieza aquí:**

1. [`docs/01_inicio/00_LEEME_PRIMERO.md`](docs/01_inicio/00_LEEME_PRIMERO.md) - Bienvenida
2. [`docs/01_inicio/01_INICIO_RAPIDO.md`](docs/01_inicio/01_INICIO_RAPIDO.md) - Ejecutar
3. [`docs/01_inicio/02_PARA_QUE_SIRVE.md`](docs/01_inicio/02_PARA_QUE_SIRVE.md) - Qué aprenderás

### 🟡 Nivel 2: Aprendizaje (1-2 horas)
**Para estudiantes:**

3. `docs/02_guias/03_MANUAL_USUARIO.md` - Cómo usar
4. `docs/02_guias/04_RESUMEN_EJECUTIVO.md` - Overview
5. `docs/02_guias/05_GUIA_TKINTER.md` - Tkinter
6. `docs/02_guias/06_GUIA_PROYECTO.md` - Arquitectura

### 🔵 Nivel 3: Práctica (1-2 horas)
**Para practicantes:**

- `docs/03_ejemplos/08_EJEMPLOS_TKINTER.py` - Ejecutar
- Modifica `src/gui_biblioteca.py`

### 📑 Referencia Rápida
- [`docs/README_DOCS.md`](docs/README_DOCS.md) - Mapa completo

---

## 💻 Características

### Interfaz Gráfica
- 3 pestañas: Usuarios, Materiales, Préstamos
- Validación automática
- Mensajes de error/éxito
- Listas actualizables

### Gestión de Usuarios
- Registra: ID, Nombre, Correo, Tipo
- Tipos: estudiante, docente, externo
- Validaciones: ID único, correo válido

### Gestión de Materiales
- Libros Físicos: ubicación en estantería
- Libros Digitales: formato (pdf, epub)
- Herencia y polimorfismo

### Control de Préstamos
- Registra préstamos activos
- Detecta vencidos (> 7 días)
- Registro de devoluciones

---

## 🎮 Cómo Usar

### Registrar Usuario
```
Pestaña: 👤 Usuarios
ID: U001
Nombre: Juan Pérez
Correo: juan@email.com
Tipo: estudiante
→ Registrar
```

### Registrar Material
```
Pestaña: 📖 Materiales
Tipo: Libro Físico
Código: LIB001
Título: Python Avanzado
Autor: Guido van Rossum
Año: 2023
Ubicación: Estantería A1
→ Registrar
```

### Hacer Préstamo
```
Pestaña: 🔄 Préstamos
ID Usuario: U001
Código Material: LIB001
→ Registrar Préstamo
→ Ver en "Préstamos Activos"
```

---

## 🐛 Solución de Problemas

### "No abre la ventana"
```bash
# Verifica Tkinter
python -m tkinter
```

### "Módulo no encontrado"
```bash
# Asegúrate de estar aquí:
cd e:\PROGRAMACION\parcialFinal
# Y que src/ exista:
ls src/
```

### "Error de validación"
```
✓ Llena TODOS los campos
✓ Correo válido: usuario@dominio.com
✓ No dejes espacios en blanco
```

---

## 📊 Contenido

| Carpeta | Archivos | Contenido |
|---------|----------|----------|
| `src/` | 7 .py | Código ejecutable |
| `docs/01_inicio/` | 3 .md | Inicio (30 min) |
| `docs/02_guias/` | 5 .md | Guías (2 horas) |
| `docs/03_ejemplos/` | 2 | Código ejemplo (2 horas) |
| `docs/04_referencia/` | 2 | Consulta rápida |

**Total:** 766 líneas de código + 5000+ de documentación

---

## 🎓 Conceptos Aprendidos

✅ Clases y Objetos
✅ Herencia y Polimorfismo
✅ Clases Abstractas (ABC)
✅ Propiedades y Validación
✅ Interfaz Gráfica (Tkinter)
✅ Eventos y Callbacks
✅ Patrón MVC
✅ Organización Profesional

---

## 🏆 Mejores Prácticas

✅ Separación: `src/` código, `docs/` documentación
✅ Nombres claros y descriptivos
✅ Comentarios y docstrings
✅ Validación robusta
✅ Manejo de errores
✅ .gitignore profesional
✅ Estructura escalable

---

## 📱 Tecnología

- **Python 3.x**
- **Tkinter** - GUI nativa
- **POO** - Orientación a Objetos
- **Git** - Control de versiones

---

## 🚀 Próximos Pasos

### Ahora (2 min)
```bash
python src/gui_biblioteca.py
```

### Luego (30 min)
Lee: `docs/01_inicio/00_LEEME_PRIMERO.md`

### Después (2-3 horas)
Estudia: `docs/02_guias/`

### Finalmente (1-2 horas)
Practica: `docs/03_ejemplos/`

---

## 📞 FAQ

**P: ¿Dónde empiezo?**
R: Ejecuta `python src/gui_biblioteca.py` luego lee `docs/01_inicio/`

**P: ¿Se guardan los datos?**
R: En memoria (se pierden al cerrar). Para persistencia: JSON/SQLite

**P: ¿Puedo modificarlo?**
R: Sí, está diseñado para aprender modificando

**P: ¿Es gratis?**
R: 100% gratuito y open-source

**P: ¿Dónde está la documentación?**
R: En `docs/` - lee [`docs/README_DOCS.md`](docs/README_DOCS.md)

---

## 🎉 Resumen

Tienes:
- ✅ Aplicación GUI funcionando
- ✅ Código profesional
- ✅ Documentación completa
- ✅ 10 ejemplos prácticos
- ✅ Todo en español

**¡Listo para aprender! 📚**

---

## 🔗 Entrada Rápida

| Necesito... | Hago... |
|-------------|---------|
| Ejecutar | `python src/gui_biblioteca.py` |
| Empezar | Lee `docs/01_inicio/00_LEEME_PRIMERO.md` |
| Entender | Lee `docs/README_DOCS.md` |
| Aprender | Estudia `docs/02_guias/` |
| Practicar | Ejecuta `docs/03_ejemplos/08_EJEMPLOS_TKINTER.py` |

---

**Creado con ❤️ para estudiantes de desarrollo**

**👉 [Comienza aquí →](docs/01_inicio/00_LEEME_PRIMERO.md)**
