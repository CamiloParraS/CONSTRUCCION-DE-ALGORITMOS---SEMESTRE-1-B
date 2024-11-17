# -----------------------------------------------------------------
# Enumeraciones
# -----------------------------------------------------------------
from enum import Enum

""" 
class Departamento(Enum):
    Enumeradores para el departamento del curso.
    MATEMATICAS = 'Matemáticas'
    FISICA = 'Física'
    SISTEMAS = 'Ingeniería de sistemas'
    BIOLOGIA = 'Biología'
    """
class Departamento:
    def __init__(self, nombre: str):
        self.nombre = nombre