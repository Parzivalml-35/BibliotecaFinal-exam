# sistema.py
from prestamos import Prestamo

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.materiales = []
        self.prestamos = []

    # Usuarios
    def registrar_usuario(self, usuario):
        if any(u.id == usuario.id for u in self.usuarios):
            raise ValueError(f"ID {usuario.id} ya existe")
        self.usuarios.append(usuario)
        return usuario

    def buscar_usuario_por_id(self, id_):
        for u in self.usuarios:
            if u.id == id_:
                return u
        return None

    # Materiales
    def registrar_material(self, material):
        if any(m.codigo == material.codigo for m in self.materiales):
            raise ValueError(f"Código {material.codigo} ya existe")
        self.materiales.append(material)
        return material

    def buscar_material_por_codigo(self, codigo):
        """Busca un material por su código."""
        for m in self.materiales:
            if m.codigo == codigo:
                return m
        return None

    def buscar_material_por_titulo(self, titulo):
        """
        Busca materiales por título (búsqueda parcial, case-insensitive).
        
        Args:
            titulo (str): Título completo o parcial a buscar
            
        Returns:
            list: Lista de materiales que coinciden
        """
        titulo_busqueda = str(titulo).lower().strip()
        resultados = []
        for m in self.materiales:
            if titulo_busqueda in m.titulo.lower():
                resultados.append(m)
        return resultados
    
    def buscar_material_por_autor(self, autor):
        """
        Busca materiales por autor (búsqueda parcial, case-insensitive).
        
        Args:
            autor (str): Nombre del autor a buscar
            
        Returns:
            list: Lista de materiales que coinciden
        """
        autor_busqueda = str(autor).lower().strip()
        resultados = []
        for m in self.materiales:
            if autor_busqueda in m._autor.lower():
                resultados.append(m)
        return resultados
    
    def buscar_material(self, **kwargs):
        """
        Método de búsqueda SOBRECARGADO - búsqueda flexible con múltiples criterios.
        
        Permite búsqueda por cualquier combinación de criterios:
        - codigo: búsqueda exacta
        - titulo: búsqueda parcial
        - autor: búsqueda parcial
        - anno: búsqueda exacta
        
        Ejemplos de uso:
            biblio.buscar_material(codigo="LIB001")
            biblio.buscar_material(titulo="Python")
            biblio.buscar_material(autor="Guido")
            biblio.buscar_material(titulo="Python", anno=2023)
            biblio.buscar_material(autor="Knuth", titulo="Algoritmos")
        
        Returns:
            list: Materiales que coinciden con todos los criterios
        """
        resultados = list(self.materiales)  # Comienza con todos
        
        # Filtrar por código (búsqueda exacta)
        if 'codigo' in kwargs:
            codigo_busqueda = str(kwargs['codigo']).strip()
            resultados = [m for m in resultados if m.codigo == codigo_busqueda]
        
        # Filtrar por título (búsqueda parcial)
        if 'titulo' in kwargs:
            titulo_busqueda = str(kwargs['titulo']).lower().strip()
            resultados = [m for m in resultados if titulo_busqueda in m.titulo.lower()]
        
        # Filtrar por autor (búsqueda parcial)
        if 'autor' in kwargs:
            autor_busqueda = str(kwargs['autor']).lower().strip()
            resultados = [m for m in resultados if autor_busqueda in m._autor.lower()]
        
        # Filtrar por año (búsqueda exacta)
        if 'anno' in kwargs:
            anno_busqueda = int(kwargs['anno'])
            resultados = [m for m in resultados if m._anio == anno_busqueda]
        
        return resultados

    # Prestamos
    def registrar_prestamo(self, usuario_id, codigo_material, fecha_prestamo=None):
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")

        material = self.buscar_material_por_codigo(codigo_material)
        if not material:
            raise ValueError("Material no encontrado")

        # Verificar si material está prestado (buscar un préstamo activo del mismo código)
        for p in self.prestamos:
            if p.activo() and p.get_material().codigo == codigo_material:
                raise ValueError("Material ya está prestado")

        nuevo = Prestamo(usuario, material, fecha_prestamo)
        self.prestamos.append(nuevo)
        return nuevo

    def registrar_devolucion(self, codigo_material):
        for p in self.prestamos:
            if p.activo() and p.get_material().codigo == codigo_material:
                p.marcar_devolucion()
                return p
        raise ValueError("No hay préstamo activo para ese material")

    def listar_prestamos_activos(self):
        return [p for p in self.prestamos if p.activo()]

    def prestamos_vencidos(self, dias_permitidos=7):
        return [p for p in self.prestamos if p.esta_vencido(dias_permitidos)]

    def listar_usuarios(self):
        return self.usuarios

    def listar_materiales(self):
        return self.materiales

    def listar_todos_prestamos(self):
        return self.prestamos
