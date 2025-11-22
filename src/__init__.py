# src/__init__.py
"""
Sistema de Biblioteca - Paquete Principal

Módulos:
- usuarios: Gestión de usuarios
- materiales: Catálogo de materiales
- prestamos: Control de préstamos
- sistema: Orquestador del sistema
"""

__version__ = "1.0"
__author__ = "Estudiante de Desarrollo"

from .usuarios import Usuario
from .materiales import MaterialBibliografico, LibroFisico, LibroDigital
from .prestamos import Prestamo
from .sistema import Biblioteca

__all__ = [
    "Usuario",
    "MaterialBibliografico",
    "LibroFisico",
    "LibroDigital",
    "Prestamo",
    "Biblioteca",
]
