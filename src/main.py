# main.py - Punto de entrada y demostración del sistema

from usuarios import Usuario
from materiales import LibroFisico, LibroDigital
from sistema import Biblioteca

def main():
    # Crear instancia de biblioteca
    biblio = Biblioteca()
    
    # ========== CREAR USUARIOS ==========
    print("=== REGISTRANDO USUARIOS ===")
    u1 = Usuario("U001", "Juan Pérez", "juan@email.com", "estudiante")
    u2 = Usuario("U002", "María García", "maria@email.com", "docente")
    u3 = Usuario("U003", "Pedro López", "pedro@email.com", "externo")
    
    biblio.registrar_usuario(u1)
    biblio.registrar_usuario(u2)
    biblio.registrar_usuario(u3)
    print(f"Usuarios registrados: {len(biblio.listar_usuarios())}")
    
    # ========== CREAR MATERIALES ==========
    print("\n=== REGISTRANDO MATERIALES ===")
    libro1 = LibroFisico("Python Avanzado", "Guido van Rossum", 2023, "LIB001", "Estantería A3")
    libro2 = LibroDigital("Ciencia de Datos", "Wes McKinney", 2022, "LIB002", "pdf")
    libro3 = LibroFisico("Algoritmos", "Donald Knuth", 2020, "LIB003", "Estantería B1")
    
    biblio.registrar_material(libro1)
    biblio.registrar_material(libro2)
    biblio.registrar_material(libro3)
    print(f"Materiales registrados: {len(biblio.listar_materiales())}")
    
    # ========== DEMOSTRACIÓN DE HERENCIA MÚLTIPLE ==========
    print("\n=== DEMOSTRACIÓN DE HERENCIA MÚLTIPLE ===")
    print("\n[LIBRO FÍSICO - Herencia: MaterialBibliografico + Imprimible]")
    print(f"  Info: {libro1.mostrar_info()}")
    print(f"  Acción: {libro1.imprimir(copias=2, a_color=True)}")
    print(f"  Total impresiones: {libro1.get_contador_impresiones()}")
    
    print("\n[LIBRO DIGITAL - Herencia: MaterialBibliografico + Descargable]")
    print(f"  Info: {libro2.mostrar_info()}")
    print(f"  Acción: {libro2.descargar(formato='epub', guardar_localmente=True)}")
    print(f"  Total descargas: {libro2.get_contador_descargas()}")
    print(f"  Formatos disponibles: {libro2.obtener_formatos()}")
    
    # ========== BÚSQUEDA SOBRECARGADA ==========
    print("\n=== BÚSQUEDA SOBRECARGADA (por múltiples criterios) ===")
    resultados = biblio.buscar_material(titulo="Python")
    print(f"Búsqueda por título 'Python': {len(resultados)} resultado(s)")
    for m in resultados:
        print(f"  • {m.mostrar_info()}")
    
    resultados = biblio.buscar_material(autor="Knuth")
    print(f"\nBúsqueda por autor 'Knuth': {len(resultados)} resultado(s)")
    for m in resultados:
        print(f"  • {m.mostrar_info()}")
    
    # ========== REALIZAR PRÉSTAMOS ==========
    print("\n=== REALIZANDO PRÉSTAMOS ===")
    try:
        prestamo1 = biblio.registrar_prestamo("U001", "LIB001")
        print(f"✓ Préstamo 1: {prestamo1.info()}")
        
        prestamo2 = biblio.registrar_prestamo("U002", "LIB002")
        print(f"✓ Préstamo 2: {prestamo2.info()}")
        
        prestamo3 = biblio.registrar_prestamo("U003", "LIB003")
        print(f"✓ Préstamo 3: {prestamo3.info()}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    # ========== INTENTAR DUPLICADO ==========
    print("\n=== INTENTAR PRESTAR MATERIAL YA PRESTADO ===")
    try:
        biblio.registrar_prestamo("U001", "LIB001")  # Ya está prestado
    except ValueError as e:
        print(f"✗ Error (esperado): {e}")
    
    # ========== LISTAR PRÉSTAMOS ACTIVOS ==========
    print("\n=== PRÉSTAMOS ACTIVOS ===")
    for p in biblio.listar_prestamos_activos():
        print(f"  {p.info()}")
    
    # ========== DEVOLVER MATERIAL ==========
    print("\n=== DEVOLVIENDO MATERIAL ===")
    try:
        devuelto = biblio.registrar_devolucion("LIB001")
        print(f"✓ Devolución: {devuelto.info()}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    # ========== LISTAR TODOS LOS PRÉSTAMOS ==========
    print("\n=== TODOS LOS PRÉSTAMOS (incluyendo devueltos) ===")
    for p in biblio.listar_todos_prestamos():
        print(f"  {p.info()}")
    
    # ========== MOSTRAR INFO DE USUARIOS Y MATERIALES ==========
    print("\n=== INFORMACIÓN DE USUARIOS ===")
    for u in biblio.listar_usuarios():
        print(f"  {u.mostrar_info()}")
    
    print("\n=== INFORMACIÓN DE MATERIALES ===")
    for m in biblio.listar_materiales():
        print(f"  {m.mostrar_info()}")

if __name__ == "__main__":
    main()
