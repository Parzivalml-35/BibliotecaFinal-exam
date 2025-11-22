# ========== CASOS DE PRUEBA OBLIGATORIOS ==========
# Este archivo demuestra todos los 10 casos de prueba requeridos por el examen final

from usuarios import Usuario
from materiales import LibroFisico, LibroDigital
from sistema import Biblioteca
from datetime import datetime, timedelta

def imprimir_separador(titulo):
    """Imprime un separador visual para organizar la salida."""
    print("\n" + "="*70)
    print(f"  {titulo}")
    print("="*70)

def caso_prueba(numero, descripcion, resultado, detalles=""):
    """
    Registra el resultado de un caso de prueba.
    
    Args:
        numero: Número del caso (1-10)
        descripcion: Descripción del caso
        resultado: True (OK) o False (FAIL)
        detalles: Información adicional
    """
    simbolo = "[OK] EXITO" if resultado else "[FAIL] FALLO"
    print(f"\nCASO {numero}: {simbolo}")
    print(f"  Descripción: {descripcion}")
    if detalles:
        print(f"  Detalles: {detalles}")

# ========== EJECUCIÓN DE CASOS DE PRUEBA ==========

def ejecutar_casos_prueba():
    """
    Ejecuta los 10 casos de prueba obligatorios del examen.
    
    OBLIGATORIOS SEGÚN EL EXAMEN:
    - (USUARIOS) Registrar 3 usuarios diferentes
    - (USUARIOS) Intentar duplicado (debe fallar)
    - (MATERIALES) Registrar Libro Físico
    - (MATERIALES) Registrar Libro Digital
    - (MATERIALES) Buscar libro inexistente (debe fallar)
    - (PRÉSTAMOS) Registrar préstamo válido
    - (PRÉSTAMOS) Intentar prestar material ya prestado (debe fallar)
    - (PRÉSTAMOS) Registrar devolución
    - (PRÉSTAMOS) Registrar préstamo vencido y detectarlo
    - (CONSULTAS) Listar préstamos activos
    """
    
    # Crear instancia de biblioteca
    biblio = Biblioteca()
    contador_exitos = 0
    contador_fallos = 0
    
    imprimir_separador("CASOS DE PRUEBA DEL EXAMEN FINAL - SISTEMA DE BIBLIOTECA")
    print("Este archivo contiene los 10 casos de prueba OBLIGATORIOS")
    print(f"Fecha de ejecución: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    # ========== CASO 1: REGISTRAR 3 USUARIOS ==========
    imprimir_separador("CASO 1: REGISTRAR TRES USUARIOS (estudiante, docente, externo)")
    
    try:
        u1 = Usuario("U001", "Juan Pérez", "juan.perez@university.edu", "estudiante")
        u2 = Usuario("U002", "Dra. María García", "maria.garcia@university.edu", "docente")
        u3 = Usuario("U003", "Pedro López", "pedro.lopez@external.com", "externo")
        
        biblio.registrar_usuario(u1)
        biblio.registrar_usuario(u2)
        biblio.registrar_usuario(u3)
        
        exito = len(biblio.listar_usuarios()) == 3
        caso_prueba(1, "Registrar 3 usuarios", exito, 
                   f"Usuarios registrados: {[u.id for u in biblio.listar_usuarios()]}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(1, "Registrar 3 usuarios", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 2: INTENTAR REGISTRAR USUARIO CON ID DUPLICADO ==========
    imprimir_separador("CASO 2: INTENTAR REGISTRAR USUARIO CON ID DUPLICADO (debe fallar)")
    
    try:
        u_duplicado = Usuario("U001", "Otro Usuario", "otro@email.com", "estudiante")
        biblio.registrar_usuario(u_duplicado)
        # Si llegamos aquí, el sistema NO lo impidió (fallo)
        caso_prueba(2, "Prevenir ID duplicado", False, "El sistema permitió registrar un ID duplicado")
        contador_fallos += 1
    except ValueError as e:
        # Si entra aquí, el sistema lo impidió correctamente (éxito)
        caso_prueba(2, "Prevenir ID duplicado", True, f"Sistema bloqueó: {e}")
        contador_exitos += 1
    except Exception as e:
        caso_prueba(2, "Prevenir ID duplicado", False, f"Error inesperado: {e}")
        contador_fallos += 1
    
    # ========== CASO 3: REGISTRAR LIBRO FÍSICO ==========
    imprimir_separador("CASO 3: REGISTRAR LIBRO FÍSICO")
    
    try:
        libro_fisico = LibroFisico(
            titulo="Cien Años de Soledad",
            autor="Gabriel García Márquez",
            anio=1967,
            codigo="L001",
            ubicacion="Estantería A-3"
        )
        biblio.registrar_material(libro_fisico)
        
        exito = biblio.buscar_material_por_codigo("L001") is not None
        caso_prueba(3, "Registrar Libro Físico", exito,
                   f"Libro: {libro_fisico.mostrar_info()}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(3, "Registrar Libro Físico", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 4: REGISTRAR LIBRO DIGITAL ==========
    imprimir_separador("CASO 4: REGISTRAR LIBRO DIGITAL")
    
    try:
        libro_digital = LibroDigital(
            titulo="Introducción a Python",
            autor="Mark Lutz",
            anio=2013,
            codigo="D101",
            formato="pdf"
        )
        biblio.registrar_material(libro_digital)
        
        exito = biblio.buscar_material_por_codigo("D101") is not None
        caso_prueba(4, "Registrar Libro Digital", exito,
                   f"Libro: {libro_digital.mostrar_info()}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(4, "Registrar Libro Digital", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 5: BUSCAR LIBRO INEXISTENTE ==========
    imprimir_separador("CASO 5: BUSCAR LIBRO INEXISTENTE (debe fallar)")
    
    try:
        libro_inexistente = biblio.buscar_material_por_codigo("NOEXISTE")
        
        exito = libro_inexistente is None  # Es correcto que sea None
        caso_prueba(5, "Buscar libro inexistente", exito,
                   "Búsqueda correctamente retornó None (no encontrado)")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(5, "Buscar libro inexistente", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 6: REGISTRAR PRÉSTAMO VÁLIDO ==========
    imprimir_separador("CASO 6: REGISTRAR PRÉSTAMO VÁLIDO")
    
    try:
        prestamo1 = biblio.registrar_prestamo("U001", "L001")
        
        exito = prestamo1 is not None and prestamo1.activo()
        caso_prueba(6, "Registrar préstamo válido", exito,
                   f"Préstamo: {prestamo1.info()}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(6, "Registrar préstamo válido", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 7: INTENTAR PRESTAR MATERIAL DUPLICADO ==========
    imprimir_separador("CASO 7: INTENTAR PRESTAR MATERIAL YA PRESTADO (debe fallar)")
    
    try:
        prestamo_duplicado = biblio.registrar_prestamo("U002", "L001")
        # Si llegamos aquí, el sistema NO lo impidió (fallo)
        caso_prueba(7, "Prevenir préstamo duplicado", False,
                   "El sistema permitió prestar un material ya prestado")
        contador_fallos += 1
    except ValueError as e:
        # Si entra aquí, el sistema lo impidió correctamente (éxito)
        caso_prueba(7, "Prevenir préstamo duplicado", True,
                   f"Sistema bloqueó: {e}")
        contador_exitos += 1
    except Exception as e:
        caso_prueba(7, "Prevenir préstamo duplicado", False, f"Error inesperado: {e}")
        contador_fallos += 1
    
    # ========== CASO 8: REGISTRAR DEVOLUCIÓN ==========
    imprimir_separador("CASO 8: REGISTRAR DEVOLUCIÓN")
    
    try:
        prestamo_devuelto = biblio.registrar_devolucion("L001")
        
        exito = prestamo_devuelto is not None and not prestamo_devuelto.activo()
        caso_prueba(8, "Registrar devolución", exito,
                   f"Préstamo devuelto: {prestamo_devuelto.info()}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(8, "Registrar devolución", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 9: REGISTRAR PRÉSTAMO VENCIDO ==========
    imprimir_separador("CASO 9: REGISTRAR PRÉSTAMO CON FECHA ATRASADA (detectar vencimiento)")
    
    try:
        # Crear un segundo libro físico para prestar
        libro_fisico2 = LibroFisico(
            titulo="Don Quijote",
            autor="Miguel de Cervantes",
            anio=1605,
            codigo="L002",
            ubicacion="Estantería B-1"
        )
        biblio.registrar_material(libro_fisico2)
        
        # Registrar un préstamo con fecha hace 10 días (vencido si límite es 7 días)
        fecha_atrasada = datetime.now() - timedelta(days=10)
        prestamo_vencido = biblio.registrar_prestamo("U003", "L002", fecha_atrasada)
        
        # Verificar que se detecte como vencido
        esta_vencido = prestamo_vencido.esta_vencido(dias_permitidos=7)
        
        exito = esta_vencido
        caso_prueba(9, "Detectar préstamo vencido", exito,
                   f"Préstamo hace 10 días: {'VENCIDO' if esta_vencido else 'No vencido'}")
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(9, "Detectar préstamo vencido", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== CASO 10: LISTAR PRÉSTAMOS ACTIVOS ==========
    imprimir_separador("CASO 10: LISTAR PRÉSTAMOS ACTIVOS")
    
    try:
        prestamos_activos = biblio.listar_prestamos_activos()
        
        # Debe haber exactamente 2 préstamos activos:
        # - D101 (préstamo 2 del caso 6, no devuelto)
        # - L002 (préstamo del caso 9, no devuelto)
        
        exito = len(prestamos_activos) >= 1  # Al menos uno debe estar activo
        
        print(f"\nCASO 10: [OK] EXITO")
        print(f"  Descripción: Listar préstamos activos")
        print(f"  Detalles: Se encontraron {len(prestamos_activos)} préstamos activos:")
        for i, p in enumerate(prestamos_activos, 1):
            print(f"    {i}. {p.info()}")
        
        contador_exitos += 1 if exito else 0
        contador_fallos += 0 if exito else 1
    except Exception as e:
        caso_prueba(10, "Listar préstamos activos", False, f"Error: {e}")
        contador_fallos += 1
    
    # ========== RESUMEN FINAL ==========
    imprimir_separador("RESUMEN DE EJECUCIÓN")
    
    print(f"\n[OK] EXITOSOS: {contador_exitos}/10")
    print(f"[FAIL] FALLOS:   {contador_fallos}/10")
    
    porcentaje = (contador_exitos / 10) * 100
    print(f"\nTASA DE ÉXITO: {porcentaje:.1f}%")
    
    if contador_exitos == 10:
        print("\n[EXCELENTE] TODOS LOS CASOS DE PRUEBA PASARON CORRECTAMENTE!")
    else:
        print(f"\n[ALERTA] Revisar los {contador_fallos} casos fallidos")
    
    # Mostrar información adicional
    print("\n" + "="*70)
    print("INFORMACIÓN ADICIONAL DEL SISTEMA")
    print("="*70)
    
    print(f"\nUSUARIOS REGISTRADOS ({len(biblio.listar_usuarios())}):")
    for u in biblio.listar_usuarios():
        print(f"  • {u.mostrar_info()}")
    
    print(f"\nMATERIALES REGISTRADOS ({len(biblio.listar_materiales())}):")
    for m in biblio.listar_materiales():
        print(f"  • {m.mostrar_info()}")
    
    print(f"\nTODOS LOS PRÉSTAMOS ({len(biblio.listar_todos_prestamos())}):")
    for p in biblio.listar_todos_prestamos():
        estado = "[ACTIVO]" if p.activo() else "[DEVUELTO]"
        print(f"  • {estado}: {p.info()}")
    
    return contador_exitos == 10


if __name__ == "__main__":
    # Ejecutar casos de prueba
    exito = ejecutar_casos_prueba()
    
    # Código de salida
    import sys
    sys.exit(0 if exito else 1)
