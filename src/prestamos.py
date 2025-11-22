# prestamos.py
from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, usuario, material, fecha_prestamo=None):
        self._usuario = usuario
        self._material = material
        self._fecha_prestamo = fecha_prestamo or datetime.now()
        self._fecha_devolucion = None 

    def marcar_devolucion(self, fecha=None):
        self._fecha_devolucion = fecha or datetime.now()

    def activo(self):
        return self._fecha_devolucion is None

    def get_material(self):
        return self._material

    def get_usuario(self):
        return self._usuario

    def esta_vencido(self, dias_permitidos=7):
        if not self.activo():
            return False
        vencimiento = self._fecha_prestamo + timedelta(days=dias_permitidos)
        return datetime.now() > vencimiento

    def info(self):
        estado = "Activo" if self.activo() else f"Devuelto el {self._fecha_devolucion}"
        return f"Usuario: {self.get_usuario().id} - Material: {self.get_material().codigo} - Prestado: {self._fecha_prestamo} - {estado}"
