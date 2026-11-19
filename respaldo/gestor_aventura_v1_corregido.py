"""
gestor_aventura.py
------------------------------------------------------------
Clase principal del Simulador RPG.

Contiene:
  - Las 10 funciones originales (condicionales, for, while) que
    resuelven la lógica pura del juego.
  - Nuevas funciones de "acción" que conectan esa lógica con el
    jugador: piden datos por consola y muestran animaciones.
  - Un bucle principal (jugar) que arma el menú de decisiones.

Requiere los archivos "colores.py" y "animaciones.py" en la
misma carpeta (los alumnos solo los descargan, no los programan).
------------------------------------------------------------
"""
import random

from colores import Color, texto
from animaciones import (
    limpiar_pantalla, pausar_continuar, mostrar_titulo,
    animar_cofre, animar_entrenamiento, animar_mision,
    animar_combate, animar_compra, animar_nivel, mostrar_derrota,
)


class GestorAventura:

    def __init__(self):
        # Estado inicial del personaje: siempre arranca en cero
        self.nombre = "Aventurero"
        self.hp = 100
        self.oro = 0
        self.fuerza = 10
        self.exp = 0
        self.nivel = 1
        self.exp_requerida = 100
        self.historial_dano = []

    # ==================================================================
    # LAS 10 FUNCIONES ORIGINALES
    # (de la 1 a la 9 solo calculan y devuelven con return;
    #  la 10 es la única que muestra datos con print)
    # ==================================================================

    # 1. Condicionales: Evaluar salud
    def evaluar_salud(self, hp):
        if hp <= 0:
            return "Derrotado 💀"
        elif hp < 30:
            return "Crítico ⚠️"
        elif hp < 70:
            return "Herido 🩹"
        else:
            return "Saludable 💪"

    # 2. Bucle For: Acumulador de oro
    def calcular_oro_total(self, cofres):
        total = 0
        for oro in cofres:
            total += oro
        return total

    # 3. Bucle For + Condicional: Filtrar ítems valiosos
    def filtrar_equipo_valioso(self, precios, limite):
        valiosos = []
        for precio in precios:
            if precio >= limite:
                valiosos.append(precio)
        return valiosos

    # 4. Bucle While: Simulación de entrenamiento
    def simular_entrenamiento(self, dias, fuerza_inicial=10):
        fuerza = fuerza_inicial
        dia = 1
        while dia <= dias:
            fuerza += 5
            dia += 1
        return fuerza

    # 5. Condicional: Proceso de compra
    def comprar_objeto(self, oro_actual, precio):
        if oro_actual >= precio:
            saldo = oro_actual - precio
            return True, saldo
        else:
            return False, oro_actual

    # 6. Bucle For + Búsqueda: Buscar misión
    def buscar_mision(self, misiones, mision_buscada):
        for mision in misiones:
            if mision.lower() == mision_buscada.lower():
                return True
        return False

    # 7. Bucle While: Combate por turnos
    def simular_combate(self, hp_enemigo, dano_por_turno):
        turnos = 0
        while hp_enemigo > 0:
            hp_enemigo -= dano_por_turno
            turnos += 1
        return turnos

    # 8. Bucle For: Promedio de daño
    def calcular_promedio_dano(self, historial_dano):
        if not historial_dano:
            return 0
        suma_dano = 0
        for dano in historial_dano:
            suma_dano += dano
        return suma_dano / len(historial_dano)

    # 9. Condicional: Control de XP y nivel
    def verificar_subida_nivel(self, exp_actual, exp_requerida):
        if exp_actual >= exp_requerida:
            sobrante = exp_actual - exp_requerida
            return True, sobrante
        else:
            faltante = exp_requerida - exp_actual
            return False, faltante

    # 10. Función Formateadora / Integradora
    def mostrar_ficha_aventurero(self):
        estado_salud = self.evaluar_salud(self.hp)
        print(texto("=" * 40, Color.CIAN))
        print(texto(f"   📜 FICHA DEL AVENTURERO: {self.nombre.upper()}", Color.CIAN, negrita=True))
        print(texto("=" * 40, Color.CIAN))
        print(f"• Nivel              : {self.nivel}")
        print(f"• Estado de Salud    : {estado_salud} ({self.hp} HP)")
        print(f"• Oro en Mochila     : {self.oro} monedas")
        print(f"• Fuerza Alcanzada   : {self.fuerza} pts")
        print(f"• Experiencia        : {self.exp}/{self.exp_requerida} XP")
        print(texto("=" * 40, Color.CIAN))

    # ==================================================================
    # ACCIONES DEL JUEGO (piden datos por consola + animan resultados)
    # ==================================================================

    def _pedir_entero(self, mensaje, minimo=1):
        """Pide un número entero por consola, validando la entrada."""
        while True:
            entrada = input(texto(mensaje, Color.CIAN))
            try:
                valor = int(entrada)
                if valor >= minimo:
                    return valor
                print(texto(f"Ingresa un número mayor o igual a {minimo}.", Color.ROJO))
            except ValueError:
                print(texto("Eso no es un número válido.", Color.ROJO))

    def _ganar_experiencia(self, cantidad):
        """Suma experiencia y revisa si el jugador sube de nivel."""
        self.exp += cantidad
        subio, dato = self.verificar_subida_nivel(self.exp, self.exp_requerida)
        if subio:
            self.nivel += 1
            self.exp = dato
            self.exp_requerida = int(self.exp_requerida * 1.5)
            animar_nivel(True, dato, self.nivel)

    def accion_abrir_cofre(self):
        limpiar_pantalla()
        mostrar_titulo("💰 SALA DEL TESORO", Color.AMARILLO)
        print("Encontraste un cofre en el camino...")
        pausar_continuar("Presiona ENTER para abrirlo...")

        cantidad_monedas = random.randint(2, 4)
        cofres = []
        for i in range(cantidad_monedas):
            cofres.append(random.randint(10, 100))
        oro_ganado = self.calcular_oro_total(cofres)
        self.oro += oro_ganado
        animar_cofre(oro_ganado, self.oro)

    def accion_entrenar(self):
        limpiar_pantalla()
        mostrar_titulo("💪 ZONA DE ENTRENAMIENTO", Color.MAGENTA)
        dias = self._pedir_entero("¿Cuántos días quieres entrenar? ")
        fuerza_anterior = self.fuerza
        self.fuerza = self.simular_entrenamiento(dias, fuerza_inicial=self.fuerza)
        fuerza_ganada = self.fuerza - fuerza_anterior
        animar_entrenamiento(dias, fuerza_ganada, self.fuerza)

    def accion_buscar_mision(self):
        limpiar_pantalla()
        mostrar_titulo("📜 TABLÓN DE MISIONES", Color.CIAN)
        misiones_disponibles = ["Derrotar Dragón", "Rescatar Aldeano", "Limpiar Cueva"]
        print("Misiones disponibles:")
        for m in misiones_disponibles:
            print(f"  - {m}")
        mision_buscada = input(texto("\n¿Qué misión quieres buscar? ", Color.CIAN))

        encontrada = self.buscar_mision(misiones_disponibles, mision_buscada)
        if encontrada:
            exp_ganada = 30
        else:
            exp_ganada = 0
        animar_mision(mision_buscada, encontrada, exp_ganada)
        if encontrada:
            self._ganar_experiencia(exp_ganada)

    def accion_combate(self):
        limpiar_pantalla()
        mostrar_titulo("⚔️  ZONA DE COMBATE", Color.ROJO)
        enemigos = [
            {"nombre": "Goblin", "hp": 40, "dano": 5},
            {"nombre": "Orco", "hp": 70, "dano": 8},
            {"nombre": "Dragón Menor", "hp": 100, "dano": 12},
            {"nombre": "Personaje Inventado", "hp": 200, "dano": 2},
        ]
        enemigo = random.choice(enemigos)
        print(f"¡Un {enemigo['nombre']} salvaje aparece!")
        pausar_continuar("Presiona ENTER para atacar...")

        dano_por_turno = max(5, self.fuerza // 2)
        turnos = self.simular_combate(enemigo["hp"], dano_por_turno)
        dano_recibido = turnos * enemigo["dano"] // 2  # el héroe recibe la mitad del daño
        self.hp = max(0, self.hp - dano_recibido)
        self.historial_dano.append(dano_recibido)

        exp_ganada = enemigo["hp"] // 2
        animar_combate(enemigo["nombre"], turnos, enemigo["hp"], dano_recibido)
        self._ganar_experiencia(exp_ganada)

    def accion_comprar(self):
        limpiar_pantalla()
        mostrar_titulo("🛒 TIENDA DEL AVENTURERO", Color.AZUL)
        tienda = [
            ("Poción de vida", 50),
            ("Escudo de madera", 120),
            ("Espada de acero", 300),
            ("Armadura élfica", 450),
        ]
        for nombre, precio in tienda:
            print(f"  - {nombre}: {precio} de oro")

        precios = []
        for nombre, precio in tienda:
            precios.append(precio)
        objetos_de_lujo = self.filtrar_equipo_valioso(precios, 200)
        if objetos_de_lujo:
            print(texto(f"\n✨ Objetos de lujo (200+ de oro): {objetos_de_lujo}", Color.MAGENTA))

        limite = self._pedir_entero("\n¿Cuál es tu presupuesto máximo? ", minimo=0)
        hay_opciones = False
        for precio in precios:
            if precio <= limite:
                hay_opciones = True
        if not hay_opciones:
            print(texto("No hay nada disponible con ese presupuesto.", Color.ROJO))
            pausar_continuar()
            return

        print("\nPuedes comprar:")
        for nombre, precio in tienda:
            if precio <= limite:
                print(f"  - {nombre}: {precio} de oro")

        objeto_elegido = input(texto("\n¿Qué quieres comprar? (escribe el nombre) ", Color.AZUL))
        precio_elegido = None
        for nombre, precio in tienda:
            if nombre.lower() == objeto_elegido.lower():
                precio_elegido = precio

        if precio_elegido is None:
            print(texto("Ese objeto no existe en la tienda.", Color.ROJO))
            pausar_continuar()
            return

        exito, saldo = self.comprar_objeto(self.oro, precio_elegido)
        self.oro = saldo
        animar_compra(exito, objeto_elegido, precio_elegido, saldo)

    def accion_ver_ficha(self):
        limpiar_pantalla()
        self.mostrar_ficha_aventurero()
        if self.historial_dano:
            promedio = self.calcular_promedio_dano(self.historial_dano)
            print(f"• Daño Promedio Recibido : {promedio:.2f}")
        pausar_continuar()

    # ==================================================================
    # MENÚ Y BUCLE PRINCIPAL
    # ==================================================================

    def mostrar_menu(self):
        print("\n¿Qué quieres hacer?")
        print("  1. Abrir un cofre")
        print("  2. Entrenar")
        print("  3. Buscar una misión")
        print("  4. Combatir")
        print("  5. Ir a la tienda")
        print("  6. Ver mi ficha completa")
        print("  0. Salir del juego")
        return input(texto("\nElige una opción: ", Color.CIAN))

    def jugar(self):
        """Bucle principal del juego: se repite hasta que el jugador
        salga, sea derrotado, o cierre la aplicación."""
        limpiar_pantalla()
        mostrar_titulo("🎮 SIMULADOR RPG - AVENTURA POR CONSOLA")
        nombre_ingresado = input(texto("Ingresa el nombre de tu héroe: ", Color.MAGENTA)).strip()
        if nombre_ingresado != "":
            self.nombre = nombre_ingresado
        pausar_continuar("Presiona ENTER para comenzar tu aventura...")

        jugando = True
        while jugando:
            if self.hp <= 0:
                mostrar_derrota(self.nombre)
                jugando = False
                break

            limpiar_pantalla()
            self.mostrar_ficha_aventurero()
            opcion = self.mostrar_menu()

            if opcion == "1":
                self.accion_abrir_cofre()
            elif opcion == "2":
                self.accion_entrenar()
            elif opcion == "3":
                self.accion_buscar_mision()
            elif opcion == "4":
                self.accion_combate()
            elif opcion == "5":
                self.accion_comprar()
            elif opcion == "6":
                self.accion_ver_ficha()
            elif opcion == "0":
                limpiar_pantalla()
                print(texto(f"¡Gracias por jugar, {self.nombre}! 👋", Color.VERDE, negrita=True))
                jugando = False
            else:
                print(texto("Opción inválida, intenta de nuevo.", Color.ROJO))
                pausar_continuar()
