"""
animaciones.py
------------------------------------------------------------
Funciones de animación y presentación visual para la consola.

Este archivo NO se debe modificar. Solo se importa así:

    from animaciones import limpiar_pantalla, pausar_continuar, ...

Requiere que "colores.py" esté en la misma carpeta.
------------------------------------------------------------
"""
import os
import time
from colores import Color, texto


# --------------------------------------------------------------------
# Utilidades generales
# --------------------------------------------------------------------

def limpiar_pantalla():
    """Limpia la consola (funciona en Windows, Mac y Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def escribir_lento(mensaje, velocidad=0.02, salto_de_linea=True):
    """Imprime un texto letra por letra, como si se escribiera en vivo."""
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    if salto_de_linea:
        print()


def pausar_continuar(mensaje="Presiona ENTER para continuar..."):
    """Detiene el juego hasta que el jugador presiona ENTER."""
    input(texto(f"\n{mensaje}", Color.GRIS))


def mostrar_titulo(titulo, color=Color.CIAN, ancho=52):
    """Imprime un título centrado dentro de un marco."""
    print(texto("=" * ancho, color))
    print(texto(titulo.center(ancho), color, negrita=True))
    print(texto("=" * ancho, color))


# --------------------------------------------------------------------
# Animaciones de acciones del juego
# --------------------------------------------------------------------

def animar_cofre(oro_ganado, oro_total):
    """Animación al abrir un cofre del tesoro."""
    limpiar_pantalla()
    mostrar_titulo("💰 COFRE DEL TESORO", Color.AMARILLO)

    cofre_cerrado = [
        "     ______________     ",
        "    /              \\    ",
        "   /   🔒 CERRADO   \\   ",
        "  /____________________\\",
        "  |                    |",
        "  |____________________|",
    ]
    for linea in cofre_cerrado:
        print(texto(linea, Color.GRIS))
    time.sleep(0.6)

    print(texto("\n...el cofre comienza a brillar...", Color.GRIS))
    time.sleep(0.8)

    limpiar_pantalla()
    mostrar_titulo("💰 COFRE DEL TESORO", Color.AMARILLO)
    cofre_abierto = [
        "     ______________     ",
        "    /  ✨ ABIERTO ✨ \\   ",
        "   /______________   \\  ",
        "  |   💛  💛  💛     |  ",
        "  |____________________|",
    ]
    for linea in cofre_abierto:
        print(texto(linea, Color.AMARILLO, negrita=True))

    print()
    escribir_lento(texto(f"¡Encontraste {oro_ganado} monedas de oro!", Color.AMARILLO, negrita=True))
    print(texto(f"Oro total en tu mochila: {oro_total}", Color.BLANCO))
    pausar_continuar()


def animar_entrenamiento(dias, fuerza_ganada, fuerza_total):
    """Animación al entrenar fuerza."""
    limpiar_pantalla()
    mostrar_titulo("💪 SESIÓN DE ENTRENAMIENTO", Color.MAGENTA)

    for dia in range(1, dias + 1):
        print(texto(f"Día {dia}/{dias}: entrenando... 🏋️", Color.MAGENTA))
        time.sleep(0.3)

    print()
    escribir_lento(texto(f"¡Ganaste {fuerza_ganada} puntos de fuerza!", Color.MAGENTA, negrita=True))
    print(texto(f"Fuerza total: {fuerza_total} pts", Color.BLANCO))
    pausar_continuar()


def animar_mision(nombre_mision, encontrada, exp_ganada=0):
    """Animación al buscar una misión."""
    limpiar_pantalla()
    mostrar_titulo("📜 TABLÓN DE MISIONES", Color.CIAN)
    print(texto(f"Buscando misión: \"{nombre_mision}\"...", Color.CIAN))
    time.sleep(0.6)
    print()

    if encontrada:
        escribir_lento(texto("¡Misión encontrada! ✅", Color.VERDE, negrita=True))
        print(texto(f"Ganaste {exp_ganada} puntos de experiencia.", Color.VERDE))
    else:
        escribir_lento(texto("Esa misión no está disponible. ❌", Color.ROJO, negrita=True))
    pausar_continuar()


def animar_combate(nombre_enemigo, turnos, hp_enemigo_inicial, dano_recibido):
    """Animación de un combate por turnos."""
    limpiar_pantalla()
    mostrar_titulo(f"⚔️  COMBATE: {nombre_enemigo.upper()} ⚔️", Color.ROJO)
    print(texto(f"HP del enemigo: {hp_enemigo_inicial}", Color.ROJO))
    time.sleep(0.4)

    for turno in range(1, turnos + 1):
        print(texto(f"Turno {turno}: ¡Atacas al {nombre_enemigo}! 🗡️", Color.ROJO))
        time.sleep(0.3)

    print()
    escribir_lento(texto(f"¡Derrotaste a {nombre_enemigo} en {turnos} turnos!", Color.VERDE, negrita=True))
    if dano_recibido > 0:
        print(texto(f"Recibiste {dano_recibido} de daño durante el combate.", Color.ROJO))
    pausar_continuar()


def animar_compra(exito, nombre_objeto, precio, saldo):
    """Animación de una compra en la tienda."""
    limpiar_pantalla()
    mostrar_titulo("🛒 TIENDA DEL AVENTURERO", Color.AZUL)

    if exito:
        escribir_lento(texto(f"¡Compraste {nombre_objeto} por {precio} de oro! 🎒", Color.AZUL, negrita=True))
        print(texto(f"Oro restante: {saldo}", Color.BLANCO))
    else:
        escribir_lento(texto(f"No tienes suficiente oro para {nombre_objeto}. 😕", Color.ROJO))
        print(texto(f"Oro actual: {saldo} | Precio: {precio}", Color.BLANCO))
    pausar_continuar()


def animar_nivel(subio_nivel, dato_exp, nivel_actual):
    """Animación al verificar subida de nivel."""
    if subio_nivel:
        limpiar_pantalla()
        mostrar_titulo("⭐ ¡SUBISTE DE NIVEL! ⭐", Color.VERDE)
        escribir_lento(texto(f"Ahora eres nivel {nivel_actual}. ¡Felicidades!", Color.VERDE, negrita=True))
        print(texto(f"Experiencia sobrante: {dato_exp}", Color.BLANCO))
        pausar_continuar()


def mostrar_derrota(nombre):
    """Pantalla de fin de juego por derrota."""
    limpiar_pantalla()
    mostrar_titulo("💀 HAS SIDO DERROTADO 💀", Color.ROJO)
    print(texto(f"{nombre}, tu aventura termina aquí...", Color.ROJO))
    print(texto("¡Gracias por jugar!", Color.GRIS))
    pausar_continuar("Presiona ENTER para salir...")
