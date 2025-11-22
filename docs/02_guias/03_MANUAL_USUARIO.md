# 03 MANUAL DE USUARIO - Cómo Usar la Aplicación

## 📱 INTERFAZ GRÁFICA

La aplicación tiene **3 pestañas principales**:

```
┌────────────────────────────────────┐
│ 📚 Sistema de Biblioteca           │
├────────────────────────────────────┤
│ [👤 Usuarios] [📖 Materiales] [🔄 Préstamos]
│
│ CONTENIDO DE LA PESTAÑA...
└────────────────────────────────────┘
```

---

## 🔷 PESTAÑA 1: USUARIOS

### Campos
- **ID:** Identificador único (ej: U001)
- **Nombre:** Nombre completo
- **Correo:** Email válido (usuario@dominio.com)
- **Tipo:** Estudiante | Docente | Externo

### Validaciones
- ✓ ID no puede ser duplicado
- ✓ Correo debe tener formato válido
- ✓ Todos los campos obligatorios

### Ejemplo
```
ID: U001
Nombre: María García
Correo: maria@email.com
Tipo: estudiante
→ Registrar Usuario
→ ✓ Aparece en lista
```

---

## 🔷 PESTAÑA 2: MATERIALES

### Campos
**Comunes:**
- **Tipo:** Libro Físico | Libro Digital
- **Código:** LIB001, PDF002, etc
- **Título:** Nombre del libro
- **Autor:** Escritor
- **Año:** Año de publicación

**Específicos:**
- **Si es Físico:** Ubicación (Estantería A1)
- **Si es Digital:** Formato (pdf, epub)

### Validaciones
- ✓ Código no puede ser duplicado
- ✓ Todos los campos obligatorios

### Ejemplo Libro Físico
```
Tipo: Libro Físico
Código: LIB001
Título: Python Avanzado
Autor: Guido van Rossum
Año: 2023
Ubicación: Estantería A1
→ Registrar Material
```

### Ejemplo Libro Digital
```
Tipo: Libro Digital
Código: PDF001
Título: Ciencia de Datos
Autor: Wes McKinney
Año: 2022
Formato: pdf
→ Registrar Material
```

---

## 🔷 PESTAÑA 3: PRÉSTAMOS

### Registrar Préstamo
**Campos:**
- ID Usuario: (ej: U001)
- Código Material: (ej: LIB001)

**Validaciones:**
- ✓ Usuario debe existir
- ✓ Material debe existir
- ✓ Material NO puede estar prestado ya
- ✓ Automático: registra fecha/hora

**Ejemplo:**
```
ID Usuario: U001
Código Material: LIB001
→ Registrar Préstamo
→ ¡Aparece en "Préstamos Activos"!
```

### Registrar Devolución
**Campos:**
- Código Material: (ej: LIB001)

**Validaciones:**
- ✓ Material debe estar prestado
- ✓ Automático: registra fecha/hora de devolución

**Ejemplo:**
```
Código Material: LIB001
→ Registrar Devolución
→ ¡Se marca como devuelto!
```

### Sub-pestañas

**Préstamos Activos:**
- Lista materiales actualmente prestados
- Info: Usuario | Material | Fecha | Estado

**Préstamos Vencidos:**
- Préstamos más de 7 días
- Fondo amarillo para identificar
- Útil para recordatorios

---

## 🔄 FLUJO COMPLETO

### Paso 1: Registra Usuario
```
Pestaña: 👤 Usuarios
ID: U001
Nombre: Juan Pérez
Correo: juan@email.com
Tipo: estudiante
→ Click "Registrar Usuario"
→ ✓ Mensaje éxito
→ ✓ Aparece en lista
```

### Paso 2: Registra Material
```
Pestaña: 📖 Materiales
Tipo: Libro Físico
Código: LIB001
Título: Python Básico
Autor: Guido van Rossum
Año: 2023
Ubicación: Estantería A1
→ Click "Registrar Material"
→ ✓ Aparece en lista
```

### Paso 3: Hace Préstamo
```
Pestaña: 🔄 Préstamos
ID Usuario: U001
Código Material: LIB001
→ Click "Registrar Préstamo"
→ ✓ Aparece en "Préstamos Activos"
→ ✓ Muestra: Usuario|Material|Fecha|Activo
```

### Paso 4: Devuelve Material
```
Pestaña: 🔄 Préstamos
Código Material: LIB001
→ Click "Registrar Devolución"
→ ✓ Se marca como devuelto
→ Puede prestar nuevamente
```

---

## ⚠️ MENSAJES Y ERRORES

### Éxito ✓
```
✓ Éxito: Usuario registrado correctamente
✓ Éxito: Material registrado correctamente
✓ Éxito: Préstamo registrado correctamente
✓ Éxito: Devolución registrada correctamente
```

### Error ✗
```
✗ Error: ID ya existe
✗ Error: Código ya existe
✗ Error: Formato de correo inválido
✗ Error: Tipo de usuario inválido
✗ Error: Usuario no encontrado
✗ Error: Material no encontrado
✗ Error: Material ya está prestado
✗ Error: No hay préstamo activo para ese material
```

### Advertencia ⚠️
```
⚠️ Advertencia: Todos los campos son obligatorios
⚠️ Advertencia: Selecciona una opción
```

---

## 💡 TIPS DE USO

1. **Copia y Pega:** Copia IDs de la lista para no escribir
2. **Nómina:** Usa U001, U002 para usuarios; LIB001, LIB002 para materiales
3. **Scroll:** Si hay muchos, usa scroll en las listas
4. **Limpia después:** Usa "Limpiar" para preparar siguiente entrada
5. **Múltiples:** Puedes registrar muchos usuario y hacer varios préstamos

---

## 🔒 VALIDACIONES AUTOMÁTICAS

La aplicación **NO te deja**:
- ❌ Duplicar ID de usuario
- ❌ Duplicar código de material
- ❌ Usar correo inválido
- ❌ Prestar material que ya está prestado
- ❌ Dejar campos vacíos
- ❌ Registrar usuario/material que no existe

**Verás mensajes claros si algo no es válido** ✓

---

## 📊 CASOS DE USO

### Caso 1: Primer Uso
1. Registra 3 usuarios
2. Registra 5 materiales
3. Haz 3 préstamos
4. Devuelve 1 material

### Caso 2: Biblioteca Real
1. Importa usuarios de listado
2. Importa catálogo de libros
3. Gestiona préstamos diarios
4. Revisa vencidos

### Caso 3: Pruebas
1. Intenta ID duplicado → Error
2. Intenta correo inválido → Error
3. Intenta prestar material prestado → Error

---

## ❌ SOLUCIÓN DE PROBLEMAS

### "No puedo registrar usuario"
**Causa:** Probablemente ID duplicado o campo vacío
**Solución:** 
- Usa ID diferente
- Llena TODOS los campos
- Revisa correo (debe tener @)

### "El material no aparece en la lista"
**Causa:** Código duplicado o error de validación
**Solución:**
- Usa código diferente
- Completa todos los campos
- Intenta de nuevo

### "No puedo hacer préstamo"
**Causa:** Usuario o material no existe, o material ya está prestado
**Solución:**
- Registra usuario primero
- Registra material primero
- Devuelve material si ya está prestado

### "Devolución no funciona"
**Causa:** No hay préstamo activo para ese material
**Solución:**
- Verifica que el material esté en "Préstamos Activos"
- Usa código correcto
- Revisa la pestaña

---

**¡Ahora sabes cómo usar la aplicación! 🎉**

Siguiente: Lee sobre la arquitectura del proyecto
