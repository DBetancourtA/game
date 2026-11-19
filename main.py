"""
main.py
------------------------------------------------------------
Punto de entrada del Simulador RPG.

Para jugar, simplemente ejecuta este archivo:

    python main.py

Archivos necesarios en la misma carpeta:
  - colores.py        (no modificar, solo colores para la consola)
  - animaciones.py     (no modificar, animaciones y pantallas)
  - gestor_aventura.py (la clase principal del juego)
------------------------------------------------------------
"""
from gestor_aventura import GestorAventura

if __name__ == "__main__":
    juego = GestorAventura()
    juego.jugar()
