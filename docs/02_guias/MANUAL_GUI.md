# 🚀 MANUAL DE USO - GUI BIBLIOTECA

## Cómo Ejecutar la Aplicación

### Opción 1: Desde Terminal
```bash
python gui_biblioteca.py
```

### Opción 2: Desde VS Code
1. Abre `gui_biblioteca.py`
2. Presiona `F5` o `Ctrl + F5`

---

## 📱 Interfaz Gráfica

La aplicación está dividida en **3 pestañas principales**:

### 🔷 Pestaña 1: USUARIOS

**Función:** Registrar y ver usuarios del sistema

#### Campos:
- **ID**: Identificador único del usuario (ej: U001, U002)
- **Nombre**: Nombre completo de la persona
- **Correo**: Correo electrónico válido (ej: juan@email.com)
- **Tipo**: Categoría del usuario
  - `estudiante`: Alumnos de la institución
  - `docente`: Profesores
  - `externo`: Personas externas

#### Botón: "✓ Registrar Usuario"
Añade el usuario a la base de datos.

**Validaciones automáticas:**
- ✓ No permite IDs duplicados
- ✓ Valida formato de correo
- ✓ Campos obligatorios
- ✓ Elimina espacios en blanco

**Ejemplo de uso:**
```
ID: U001
Nombre: Juan Pérez
Correo: juan@email.com
Tipo: estudiante
→ Click en "Registrar Usuario"
→ Mensaje: "Usuario registrado correctamente"
```

---

### 🔷 Pestaña 2: MATERIALES

**Función:** Registrar y ver materiales de la biblioteca

#### Campos:
- **Tipo**: Selecciona el tipo de material
  - `Libro Físico`: Libros en papel (requiere ubicación)
  - `Libro Digital`: Archivos PDF/Ebook (requiere formato)
- **Código**: Identificador único (ej: LIB001, PDF005)
- **Título**: Nombre del libro
- **Autor**: Autor/Escritor
- **Año**: Año de publicación
- **Ubicación/Formato**: 
  - Si es Físico → Ubicación en la estantería (ej: "Estantería A3")
  - Si es Digital → Formato del archivo (ej: "pdf", "epub")

#### Botón: "✓ Registrar Material"
Añade el material a la base de datos.

**Ejemplo de uso:**
```
Tipo: Libro Físico
Código: LIB001
Título: Python Avanzado
Autor: Guido van Rossum
Año: 2023
Ubicación: Estantería A3
→ Click en "Registrar Material"
```

---

### 🔷 Pestaña 3: PRÉSTAMOS

**Función:** Gestionar préstamos y devoluciones de materiales

#### Campos Principales:
- **ID Usuario**: ID del usuario que hace el préstamo (ej: U001)
- **Código Material**: Código del material a prestar (ej: LIB001)

#### Botones:

**1️⃣ "✓ Registrar Préstamo"**
- Crea un nuevo préstamo
- Valida que usuario y material existan
- Verifica que el material no esté prestado
- Registra la fecha/hora automáticamente

**Ejemplo:**
```
ID Usuario: U001
Código Material: LIB001
→ Click en "Registrar Préstamo"
→ Material marcado como prestado
```

**2️⃣ "↩ Registrar Devolución"**
- Marca el material como devuelto
- Solo requiere el código del material
- Actualiza la fecha de devolución

**Ejemplo:**
```
Código Material: LIB001
→ Click en "Registrar Devolución"
→ Material disponible nuevamente
```

#### Sub-Pestañas:

**Préstamos Activos:**
- Muestra todos los materiales actualmente prestados
- Información: Usuario | Material | Fecha Préstamo | Estado (Activo)

**Préstamos Vencidos:**
- Muestra préstamos que superan 7 días
- Fondo amarillo para identificarlos rápidamente
- Útil para recordar devoluciones pendientes

---

## 📋 Ejemplo Completo de Uso

### Paso 1: Crear un Usuario
```
Ir a: Pestaña "USUARIOS"
ID: U001
Nombre: María García
Correo: maria@email.com
Tipo: estudiante
→ "Registrar Usuario"
```

### Paso 2: Registrar un Material
```
Ir a: Pestaña "MATERIALES"
Tipo: Libro Físico
Código: LIB001
Título: Algoritmos
Autor: Donald Knuth
Año: 2020
Ubicación: Estantería B1
→ "Registrar Material"
```

### Paso 3: Hacer un Préstamo
```
Ir a: Pestaña "PRÉSTAMOS"
ID Usuario: U001
Código Material: LIB001
→ "Registrar Préstamo"
→ Aparece en "Préstamos Activos"
```

### Paso 4: Devolver el Material
```
En: Pestaña "PRÉSTAMOS"
Código Material: LIB001
→ "Registrar Devolución"
→ Se mueve a "Préstamos Vencidos" (si pasó 7 días)
```

---

## ⚠️ Mensajes de Error y Soluciones

### Error: "ID ya existe"
**Causa:** Intentas registrar un usuario con ID duplicado
**Solución:** Usa un ID diferente o verifica en la lista de usuarios

### Error: "Formato de correo inválido"
**Causa:** El correo no tiene formato correcto
**Solución:** Usa formato: `usuario@dominio.com`

### Error: "Material ya está prestado"
**Causa:** Intentas prestar un material que ya está prestado
**Solución:** Devuelve el material primero

### Error: "Usuario no encontrado"
**Causa:** El ID del usuario no existe en la base de datos
**Solución:** Registra el usuario primero

### Error: "Material no encontrado"
**Causa:** El código del material no existe
**Solución:** Registra el material primero

### Advertencia: "Todos los campos son obligatorios"
**Causa:** Dejaste algún campo vacío
**Solución:** Completa todos los campos del formulario

---

## 💡 Tips de Uso

1. **Velocidad**: Copia y pega IDs de la lista de usuarios en el campo de préstamos
2. **Organización**: Usa códigos consistentes (ej: LIB para libros físicos, PDF para digitales)
3. **Búsqueda**: Los listbox permiten scroll vertical si hay muchos elementos
4. **Validación**: La aplicación valida automáticamente, no podrás cometer errores comunes

---

## 🔄 Estructura de la Aplicación

```
gui_biblioteca.py
├── BibliotecaGUI (Clase Principal)
│   ├── __init__ → Inicializa ventana
│   ├── crear_pestanas() → Crea las 3 pestañas
│   │
│   ├── PESTAÑA USUARIOS
│   │   ├── crear_pestaña_usuarios()
│   │   ├── registrar_usuario()
│   │   └── actualizar_lista_usuarios()
│   │
│   ├── PESTAÑA MATERIALES
│   │   ├── crear_pestaña_materiales()
│   │   ├── registrar_material()
│   │   ├── cambiar_campo_material()
│   │   └── actualizar_lista_materiales()
│   │
│   └── PESTAÑA PRÉSTAMOS
│       ├── crear_pestaña_prestamos()
│       ├── registrar_prestamo()
│       ├── registrar_devolucion()
│       └── actualizar_lista_prestamos()
│
└── main() → Punto de entrada
```

---

## 🎨 Personalización

Si quieres modificar la aplicación:

### Cambiar Colores
```python
# En gui_biblioteca.py
bg="lightgray"    # Color de fondo
fg="white"        # Color de texto
bg="green"        # Color del botón
```

### Cambiar Tamaño de Ventana
```python
self.root.geometry("800x600")  # Ancho x Alto
```

### Cambiar Fuentes
```python
self.estilo_titulo = ("Arial", 14, "bold")
self.estilo_normal = ("Arial", 10)
```

### Días de Vencimiento
```python
self.biblio.prestamos_vencidos(7)  # Cambiar 7 a otro número
```

---

## 📝 Notas Técnicas

- **Tkinter**: Librería incluida en Python
- **Variables**: `tk.StringVar()`, `tk.IntVar()`, `tk.BooleanVar()`
- **Gestores**: `pack()`, `grid()`, `place()`
- **Validación**: Integrada en las clases del modelo
- **Base de Datos**: En memoria (se pierde al cerrar la app)

---

## 🚀 Próximas Mejoras (Opcional)

1. **Guardar en archivo** (JSON o base de datos SQL)
2. **Búsqueda de usuarios/materiales**
3. **Editar datos existentes**
4. **Gráficos de estadísticas**
5. **Exportar reportes**
6. **Autenticación de usuarios**

---

**¡Disfruta tu Sistema de Biblioteca! 📚**
