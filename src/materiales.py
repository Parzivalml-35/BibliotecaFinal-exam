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

# ========== MIX-INS PARA HERENCIA MÚLTIPLE ==========
# Estos son clases adicionales que proporciona comportamiento adicional a través de herencia múltiple

class Descargable:
    """Mix-in que proporciona capacidad de descarga a los materiales digitales."""
    
    def __init__(self):
        self._descargas = 0  # Contador de descargas
        self._formatos_disponibles = []
    
    def descargar(self, *args, **kwargs):
        """
        Método sobrecargado para descargar materiales.
        
        Parámetros opcionales:
        - formato (por defecto: None, usa formato principal)
        - guardar_localmente (bool, por defecto False)
        
        Ejemplo:
            material.descargar()                              # Descarga en formato por defecto
            material.descargar(formato="epub")                # Descarga en formato específico
            material.descargar(formato="pdf", guardar_localmente=True)  # Descarga y guarda
        """
        titulo = getattr(self, '_titulo', 'material')
        
        # Manejo de argumentos opcionales
        formato = kwargs.get('formato', getattr(self, 'formato', 'pdf'))
        guardar_localmente = kwargs.get('guardar_localmente', False)
        
        self._descargas += 1
        
        mensaje = f"📥 Descargando '{titulo}' en formato {formato}"
        if guardar_localmente:
            mensaje += " (guardado localmente)"
        
        return mensaje
    
    def obtener_formatos(self):
        """Retorna los formatos disponibles para descarga."""
        return getattr(self, '_formatos_disponibles', [getattr(self, 'formato', 'pdf')])
    
    def get_contador_descargas(self):
        """Retorna el número total de descargas registradas."""
        return self._descargas


class Imprimible:
    """Mix-in que proporciona capacidad de impresión a los materiales físicos."""
    
    def __init__(self):
        self._impresiones = 0  # Contador de impresiones
        self._se_puede_imprimir = True
    
    def imprimir(self, *args, **kwargs):
        """
        Método sobrecargado para imprimir materiales.
        
        Parámetros opcionales:
        - copias (int, por defecto 1)
        - a_color (bool, por defecto True)
        - rango_paginas (str, ej: "1-10", por defecto None = todas)
        
        Ejemplo:
            material.imprimir()                              # Imprime 1 copia a color
            material.imprimir(copias=3)                      # Imprime 3 copias a color
            material.imprimir(copias=2, a_color=False)       # Imprime 2 copias en B/N
            material.imprimir(rango_paginas="1-5", copias=1) # Imprime páginas 1-5
        """
        if not self._se_puede_imprimir:
            return f"⚠️  No se puede imprimir '{getattr(self, '_titulo', 'material')}' (restringido)"
        
        titulo = getattr(self, '_titulo', 'material')
        
        # Manejo de argumentos con valores por defecto
        copias = kwargs.get('copias', 1)
        a_color = kwargs.get('a_color', True)
        rango_paginas = kwargs.get('rango_paginas', None)
        
        # Validar copias
        if isinstance(copias, str):
            copias = int(copias)
        copias = max(1, min(copias, 10))  # Máximo 10 copias
        
        self._impresiones += copias
        
        modo_color = "a color" if a_color else "en B/N"
        rango = f" (páginas {rango_paginas})" if rango_paginas else " (todas las páginas)"
        
        mensaje = f"🖨️  Imprimiendo '{titulo}' x{copias} {modo_color}{rango}"
        return mensaje
    
    def get_contador_impresiones(self):
        """Retorna el número total de impresiones registradas."""
        return self._impresiones
    
    def establecer_restriccion_impresion(self, permitir=True):
        """Establece si se permite imprimir el material."""
        self._se_puede_imprimir = permitir
        return f"Impresión {'permitida' if permitir else 'restringida'}"

class LibroFisico(MaterialBibliografico, Imprimible):
    """
    Representa un libro físico en la biblioteca.
    
    Herencia múltiple:
    - Hereda de MaterialBibliografico: estructura base
    - Hereda de Imprimible: capacidad de impresión
    """
    def __init__(self, titulo, autor, anio=None, codigo=None, ubicacion=None):
        MaterialBibliografico.__init__(self, titulo, autor, anio, codigo)
        Imprimible.__init__(self)
        self.ubicacion = ubicacion  # ej. estantería

    def mostrar_info(self):
        """Retorna información del libro físico."""
        return f"[F] {self._codigo} - {self._titulo} / {self._autor} ({self._anio}) - Ubicación: {self.ubicacion}"

class LibroDigital(MaterialBibliografico, Descargable):
    """
    Representa un libro digital en la biblioteca.
    
    Herencia múltiple:
    - Hereda de MaterialBibliografico: estructura base
    - Hereda de Descargable: capacidad de descarga
    """
    def __init__(self, titulo, autor, anio=None, codigo=None, formato='pdf'):
        MaterialBibliografico.__init__(self, titulo, autor, anio, codigo)
        Descargable.__init__(self)
        self.formato = formato  # ej. pdf, epub
        self._formatos_disponibles = ['pdf', 'epub', 'mobi']

    def mostrar_info(self):
        """Retorna información del libro digital."""
        return f"[D] {self._codigo} - {self._titulo} / {self._autor} ({self._anio}) [{self.formato}]"
