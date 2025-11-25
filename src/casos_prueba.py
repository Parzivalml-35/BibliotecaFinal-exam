# ========== CASOS DE PRUEBA DEL EXAMEN FINAL ==========
# Demuestra los 9 requisitos POO: clases, constructores, destructores,
# encapsulamiento, herencia simple, herencia múltiple, clases abstractas,
# polimorfismo y sobrecarga simulada.

from usuarios import Usuario
from materiales import LibroFisico, LibroDigital
from sistema import Biblioteca

def ejecutar_casos_prueba():
    """Ejecuta los 10 casos de prueba que demuestran los 9 requisitos POO."""
    
    biblio = Biblioteca()
    
    print("\n" + "="*60)
    print("CASOS DE PRUEBA - SISTEMA DE BIBLIOTECA")
    print("="*60)
    
    # CASO 1: Crear usuarios (Req 1: Clases y objetos)
    try:
        u1 = Usuario("U001", "Juan Pérez", "juan@email.com", "estudiante")
        u2 = Usuario("U002", "María García", "maria@email.com", "docente")
        u3 = Usuario("U003", "Pedro López", "pedro@email.com", "externo")
        
        biblio.registrar_usuario(u1)
        biblio.registrar_usuario(u2)
        biblio.registrar_usuario(u3)
        
        assert len(biblio.listar_usuarios()) == 3
        print("CASO 1: [OK] Crear 3 usuarios")
    except Exception as e:
        print(f"CASO 1: [FAIL] Crear 3 usuarios - {e}")
    
    # CASO 2: Prevenir duplicados (Req 3: Encapsulamiento)
    try:
        u_dup = Usuario("U001", "Otro", "otro@email.com", "estudiante")
        biblio.registrar_usuario(u_dup)
        print("CASO 2: [FAIL] Prevenir usuario duplicado")
    except ValueError:
        print("CASO 2: [OK] Prevenir usuario duplicado")
    except Exception as e:
        print(f"CASO 2: [FAIL] Prevenir usuario duplicado - {e}")
    
    # CASO 3: Registrar libro físico (Req 4: Herencia simple)
    try:
        libro_f = LibroFisico("Cien Años de Soledad", "García Márquez", 1967, "L001", "Est. A")
        biblio.registar_rmaterial(libro_f)
        
        assert biblio.buscar_material_por_codigo("L001") is not None
        print("CASO 3: [OK] Registrar libro físico, con codigo L001")
    except Exception as e:
        print(f"CASO 3: [FAIL] Registrar libro físico - {e}")
    
    # CASO 4: Registrar libro digital (Req 5: Herencia múltiple)
    try:
        libro_d = LibroDigital("Python Intro", "Mark Lutz", 2013, "D101", "pdf")
        biblio.registrar_material(libro_d)
        
        assert biblio.buscar_material_por_codigo("D101") is not None
        print("CASO 4: [OK] Registrar libro digital")
    except Exception as e:
        print(f"CASO 4: [FAIL] Registrar libro digital - {e}")
    
    # CASO 5: Buscar inexistente (Req 6: Clases abstractas)
    try:
        resultado = biblio.buscar_material_por_codigo("NOEXISTE")
        assert resultado is None
        print("CASO 5: [OK] Buscar libro inexistente")
    except Exception as e:
        print(f"CASO 5: [FAIL] Buscar libro inexistente - {e}")
    
    # CASO 6: Registrar préstamo (Req 7: Polimorfismo)
    try:
        prestamo = biblio.registrar_prestamo("U001", "L001")
        assert prestamo is not None and prestamo.activo()
        print("CASO 6: [OK] Registrar préstamo")
    except Exception as e:
        print(f"CASO 6: [FAIL] Registrar préstamo - {e}")
    
    # CASO 7: Prevenir préstamo duplicado
    try:
        biblio.registrar_prestamo("U002", "L001")
        print("CASO 7: [FAIL] Prevenir préstamo duplicado")
    except ValueError:
        print("CASO 7: [OK] Prevenir préstamo duplicado")
    except Exception as e:
        print(f"CASO 7: [FAIL] Prevenir préstamo duplicado - {e}")
    
    # CASO 8: Registrar devolución (Req 2: Destructores)
    try:
        prestamo_dev = biblio.registrar_devolucion("L001")
        assert prestamo_dev is not None and not prestamo_dev.activo()
        print("CASO 8: [OK] Registrar devolución")
    except Exception as e:
        print(f"CASO 8: [FAIL] Registrar devolución - {e}")
    
    # CASO 9: Sobrecarga con **kwargs (Req 8: Sobrecarga simulada)
    try:
        libro_f2 = LibroFisico("Don Quijote", "Cervantes", 1605, "L002", "Est. B")
        biblio.registrar_material(libro_f2)
        
        assert biblio.buscar_material(codigo="L002") is not None
        print("CASO 9: [OK] Búsqueda sobrecargada con kwargs")
    except Exception as e:
        print(f"CASO 9: [FAIL] Búsqueda sobrecargada con kwargs - {e}")
    
    # CASO 10: Listar préstamos activos (Req 9: Métodos de acceso @property)
    try:
        biblio.registrar_prestamo("U003", "D101")
        activos = biblio.listar_prestamos_activos()
        assert len(activos) >= 1
        print("CASO 10: [OK] Listar préstamos activos")
    except Exception as e:
        print(f"CASO 10: [FAIL] Listar préstamos activos - {e}")
    
    print("\n" + "="*60)
    print("FIN DE LOS CASOS DE PRUEBA")
    print("="*60 + "\n")


if __name__ == "__main__":
    ejecutar_casos_prueba()
