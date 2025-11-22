# materiales.py
from abc import ABC, abstractmethod

class MaterialBibliografico(ABC):
    def __init__(self, titulo, autor, anio=None, codigo=None):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._codigo = codigo

    @abstractmethod
    def mostrar_info(self):
        pass

    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

# mix-in para herencia múltiple
class Descargable:
    def descargar(self):
        # simulación: en un caso real devolvería un enlace/bytes
        return f"Descargando {getattr(self, '_titulo', 'material')}..."

class Imprimible:
    def imprimir(self):
        return f"Imprimiendo {getattr(self, '_titulo', 'material')}..."

class LibroFisico(MaterialBibliografico, Imprimible):
    def __init__(self, titulo, autor, anio=None, codigo=None, ubicacion=None):
        super().__init__(titulo, autor, anio, codigo)
        self.ubicacion = ubicacion  # ej. estantería

    def mostrar_info(self):
        return f"[F] {self._codigo} - {self._titulo} / {self._autor} ({self._anio}) - {self.ubicacion}"

class LibroDigital(MaterialBibliografico, Descargable):
    def __init__(self, titulo, autor, anio=None, codigo=None, formato='pdf'):
        super().__init__(titulo, autor, anio, codigo)
        self.formato = formato

    def mostrar_info(self):
        return f"[D] {self._codigo} - {self._titulo} / {self._autor} ({self._anio}) [{self.formato}]"
