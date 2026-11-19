"""
personaje.py
------------------------------------------------------------
Dibuja al héroe en la consola, como hombre o mujer, con el
equipo que haya comprado o conseguido.

Este archivo NO se debe modificar. Solo se importa así:

    from personaje import dibujar_personaje, animar_equipar

Y se usa así:

    dibujar_personaje("hombre", ["Espada de acero"])
    dibujar_personaje("mujer", ["Escudo de madera", "Armadura élfica"])

Objetos que se dibujan (deben escribirse igual que en la tienda):
  - "Espada de acero"   -> aparece en la mano derecha
  - "Escudo de madera"  -> aparece en la mano izquierda
  - "Armadura élfica"   -> cambia el cuerpo
  - "Casco de hierro"   -> cambia la cabeza
Cualquier otro objeto se ignora en el dibujo.

Requiere que "colores.py" y "animaciones.py" estén en la misma carpeta.
------------------------------------------------------------
"""
from colores import Color, texto
from animaciones import limpiar_pantalla, mostrar_titulo, pausar_continuar, escribir_lento


# --------------------------------------------------------------------
# Piezas del dibujo (cada pieza tiene 11 caracteres de ancho)
# --------------------------------------------------------------------

_CABEZA = {
    "hombre": [
        "    ___    ",
        "   /___\\   ",
        "   (o o)   ",
        "    \\-/    ",
    ],
    "mujer": [
        "   .~~~.   ",
        "  ((o o))  ",
        "  ( \\-/ )  ",
        "   ~   ~   ",
    ],
}

_CABEZA_CASCO = {
    "hombre": [
        "    _^_    ",
        "   [===]   ",
        "   [o o]   ",
        "    \\-/    ",
    ],
    "mujer": [
        "    _^_    ",
        "   [===]   ",
        "  ~[o o]~  ",
        "  ~ \\-/ ~  ",
    ],
}

_CUERPO = [
    "   /| |\\   ",
    "  / | | \\  ",
    "    |_|    ",
]

_CUERPO_ARMADURA = [
    "   /[#]\\   ",
    "  / [#] \\  ",
    "    [_]    ",
]

_PIERNAS = {
    "hombre": [
        "    / \\    ",
        "   /   \\   ",
    ],
    "mujer": [
        "    /_\\    ",
        "   /___\\   ",
    ],
}

# Columna derecha (espada) y columna izquierda (escudo): una línea por fila.
_ESPADA = ["      ", "      ", "  /\\  ", "  ||  ", "  ||  ", " =##= ", "  ||  ", "      ", "      "]
_ESCUDO = ["      ", "      ", "      ", "      ", " .--. ", " |++| ", " '--' ", "      ", "      "]
_VACIO = ["      "] * 9


def _normalizar_genero(genero):
    """Acepta 'hombre', 'mujer', 'h' o 'm' (mayúsculas o minúsculas)."""
    genero = str(genero).strip().lower()
    if genero in ("m", "mujer", "f", "femenino"):
        return "mujer"
    return "hombre"


def _tiene(equipo, objeto):
    """Revisa si un objeto está en la lista de equipo (sin importar mayúsculas)."""
    for cosa in equipo:
        if str(cosa).lower() == objeto.lower():
            return True
    return False


def armar_dibujo(genero, equipo):
    """
    Devuelve una lista de líneas (texto) con el dibujo del héroe.
    No imprime nada: sirve si quieres usar el dibujo en otro lado.
    """
    genero = _normalizar_genero(genero)

    if _tiene(equipo, "Casco de hierro"):
        cabeza = _CABEZA_CASCO[genero]
    else:
        cabeza = _CABEZA[genero]

    if _tiene(equipo, "Armadura élfica"):
        cuerpo = _CUERPO_ARMADURA
    else:
        cuerpo = _CUERPO

    centro = cabeza + cuerpo + _PIERNAS[genero]
    izquierda = _ESCUDO if _tiene(equipo, "Escudo de madera") else _VACIO
    derecha = _ESPADA if _tiene(equipo, "Espada de acero") else _VACIO

    lineas = []
    for i in range(len(centro)):
        lineas.append(izquierda[i] + centro[i] + derecha[i])
    return lineas


def dibujar_personaje(genero, equipo, color=Color.AMARILLO):
    """
    Imprime al héroe en la consola.

    genero : "hombre" o "mujer" (también acepta "h" o "m")
    equipo : lista con los nombres de los objetos que tiene el héroe
    """
    for linea in armar_dibujo(genero, equipo):
        print(texto(linea, color, negrita=True))

    if len(equipo) == 0:
        print(texto("  Equipo: (nada todavía)", Color.GRIS))
    else:
        print(texto("  Equipo: " + ", ".join(str(cosa) for cosa in equipo), Color.GRIS))


def animar_equipar(genero, equipo, nombre_objeto):
    """Pantalla que muestra cómo se ve el héroe con su nuevo objeto."""
    limpiar_pantalla()
    mostrar_titulo("🛡️  ¡NUEVO EQUIPO!", Color.AMARILLO)
    dibujar_personaje(genero, equipo)
    print()
    escribir_lento(texto(f"Ahora llevas: {nombre_objeto}", Color.AMARILLO, negrita=True))
    pausar_continuar()


def mostrar_eleccion_genero():
    """Muestra los dos héroes posibles para que el jugador elija."""
    hombre = armar_dibujo("hombre", [])
    mujer = armar_dibujo("mujer", [])
    print(texto("      1. Hombre                   2. Mujer", Color.CIAN, negrita=True))
    for i in range(len(hombre)):
        print(texto(hombre[i] + "      " + mujer[i], Color.AMARILLO, negrita=True))
