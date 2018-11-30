"""
    Manejo de Excepciones
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "El error esta mal  %s" %(self.valor)
