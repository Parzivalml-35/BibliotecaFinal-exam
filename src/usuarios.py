import re

class Usuario:
    def __init__(self, usuario_id, nombre, correo, tipo_usuario):
        self._id = None
        self._nombre = None
        self._correo = None
        self._tipo_usuario = None
        
        self.id = usuario_id
        self.nombre = nombre
        self.correo = correo
        self.tipo_usuario = tipo_usuario

    def __del__(self):
        print(f"Usuario {self.id} eliminado")

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not value or not str(value).strip():
            raise ValueError("ID no puede estar vacío")
        self._id = str(value).strip()

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        if not value or not str(value).strip():
            raise ValueError("Nombre no puede estar vacío")
        self._nombre = str(value).strip()

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, value):
        if not value:
            raise ValueError("Correo no puede ser vacío")
        value = value.strip()
        # regex simple para un email (no perfecto, pero suficiente)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Formato de correo inválido")
        self._correo = value

    @property
    def tipo_usuario(self):
        return self._tipo_usuario
    
    @tipo_usuario.setter
    def tipo_usuario(self, value):
        validos = {"estudiante", "docente", "externo"}
        if str(value).lower() not in validos:
            raise ValueError(f"Tipo de usuario inválido. Debe ser uno de: {validos}")
        self._tipo_usuario = str(value).lower()

    def mostrar_info(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Email: {self._correo} | Tipo: {self._tipo_usuario}"