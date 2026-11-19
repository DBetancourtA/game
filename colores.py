"""
colores.py
------------------------------------------------------------
Módulo de colores y estilos de texto para la consola.

Este archivo NO se debe modificar. Solo se importa así:

    from colores import Color, texto

Y se usa así:

    print(texto("¡Ganaste oro!", Color.AMARILLO, negrita=True))
------------------------------------------------------------
"""


class Color:
    """Códigos ANSI de color para texto en consola."""
    RESET = "\033[0m"
    NEGRITA = "\033[1m"

    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIAN = "\033[96m"
    BLANCO = "\033[97m"
    GRIS = "\033[90m"


def texto(mensaje, color=Color.BLANCO, negrita=False):
    """
    Devuelve el mensaje envuelto en códigos de color ANSI, listo para
    imprimirse con print().

    Ejemplo:
        print(texto("Nivel subido!", Color.VERDE, negrita=True))
    """
    estilo = Color.NEGRITA if negrita else ""
    return f"{estilo}{color}{mensaje}{Color.RESET}"
