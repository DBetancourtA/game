# 🎮 Simulador RPG - Guía rápida

## Archivos

- `main.py` → **este es el que se ejecuta.**
- `gestor_aventura.py` → la clase del juego (aquí están tus funciones).
- `colores.py` → colores para la consola (no lo edites, solo impórtalo).
- `animaciones.py` → animaciones y pantallas (no lo edites, solo impórtalo).
- `personaje.py` → dibuja a tu héroe con su equipo (no lo edites, solo impórtalo).

## Cómo jugar

1. Guarda los 5 archivos en la **misma carpeta**.
2. Abre una terminal en esa carpeta (o usa la terminal de VS Code).
   **No uses IDLE:** ahí los colores salen como códigos raros.
3. Ejecuta:

   ```
   python main.py
   ```

4. Escribe el nombre de tu héroe, elige hombre o mujer, y usa el menú (1 al 7, o 0 para salir).

## Reglas del juego

- Los **cofres** dan oro. Los **combates** dan experiencia y un poco de oro.
- **Entrenar** cuesta 10 de oro por día (máximo 5 días).
- Cada **misión** se puede completar una sola vez.
- En la **tienda**:
  - Poción de vida → cura 40 HP (úsala con la opción 7).
  - Escudo de madera → recibes 10 de daño menos por combate.
  - Casco de hierro → cambia el aspecto de tu héroe.
  - Espada de acero → +15 de fuerza.
  - Armadura élfica → recibes la mitad de daño.
- Al **subir de nivel** recuperas toda la vida y ganas 5 de fuerza.

## ¿Qué puedo modificar?

Solo `gestor_aventura.py`. Ahí puedes:
- Agregar más enemigos en `accion_combate`.
- Agregar más objetos en la tienda de `accion_comprar`.
- Agregar más misiones en `__init__` (lista `self.misiones`).
- Cambiar los valores iniciales en `__init__` (HP, oro, fuerza...).

Para que un objeto nuevo se **dibuje** en el héroe, debe llamarse igual que
los de `personaje.py` (Espada de acero, Escudo de madera, Casco de hierro,
Armadura élfica). Los demás objetos funcionan, pero no se dibujan.
