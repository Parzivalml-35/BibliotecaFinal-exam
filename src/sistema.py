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
        for m in self.materiales:
            if m.codigo == codigo:
                return m
        return None

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
