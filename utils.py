import numpy as np
import random

# Función para crear el tablero
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")  # Crea un tablero lleno de guiones bajos
    return tablero

# Función para colocar un barco en el tablero
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"  # Marca la posición del barco con "O"
    return tablero

# Función para crear un barco con una longitud específica (eslora)
def crear_barco(eslora, tamaño=10):
    while True:
        casilla_0 = (random.randint(0, tamaño-1), random.randint(0, tamaño-1))  # Casilla inicial aleatoria
        orientacion = random.choice(["Vertical", "Horizontal"])
        
        barco = [casilla_0]
        casilla = casilla_0
        for _ in range(1, eslora):
            if orientacion == "Vertical":
                nueva_casilla = (casilla[0] + 1, casilla[1])  # Avanzar hacia abajo
            else:
                nueva_casilla = (casilla[0], casilla[1] + 1)  # Avanzar hacia la derecha

            # Verificar que la nueva casilla no se salga del tablero
            if nueva_casilla[0] >= tamaño or nueva_casilla[1] >= tamaño:
                break  # Si se sale del tablero, descartamos este intento
            barco.append(nueva_casilla)
            casilla = nueva_casilla

        # Devolver el barco si su tamaño es correcto
        if len(barco) == eslora:
            return barco

# Función para colocar varios barcos en el tablero sin superposición
def colocar_barcos(tablero):
    barcos_esloras = [2, 2, 2, 3, 3, 4]  # Lista de tamaños de barcos
    i = 0

    while i < len(barcos_esloras):
        eslora = barcos_esloras[i]
        barco = crear_barco(eslora)  # Creamos el barco con la eslora especificada
        try:
            tablero = colocar_barco(barco, tablero)  # Intentamos colocarlo en el tablero
            i += 1  # Si se coloca correctamente, pasamos al siguiente barco
        except ValueError:
            continue  # Si no se pudo colocar, intentamos de nuevo
    return tablero

# Función para comprobar si quedan barcos en el tablero
def quedan_barcos(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "O":  # Si encontramos un barco ("O")
                return True  # Todavía quedan barcos
    return False  # No quedan barcos

# Función para gestionar el turno del jugador
def turno_jugador(tablero_maquina, tablero_disparos_jugador):
    while True:
        try:
            fila = int(input("Introduce la fila (0-9) a disparar: "))
            columna = int(input("Introduce la columna (0-9) a disparar: "))
            casilla = (fila, columna)
            if tablero_maquina[casilla] in ["A", "X"]:
                print("Ya has disparado aquí, elige otra casilla.")
            else:
                if tablero_maquina[casilla] == "O":  # Si hay un barco
                    print("¡Tocado!")
                    tablero_maquina[casilla] = "X"  # Marcamos como barco tocado
                    tablero_disparos_jugador[casilla] = "X"  # Marcamos en el tablero de disparos del jugador
                else:
                    print("¡Agua!")
                    tablero_maquina[casilla] = "A"  # Marcamos como agua en el tablero real
                    tablero_disparos_jugador[casilla] = "A"  # También lo marcamos en el tablero de disparos
                break
        except (ValueError, IndexError):
            print("Coordenadas inválidas, introduce valores entre 0 y 9.")

# Función para gestionar el turno de la máquina (aleatorio)
def turno_maquina(tablero_jugador):
    while True:
        casilla = (random.randint(0, 9), random.randint(0, 9))  # Disparo aleatorio
        if tablero_jugador[casilla] not in ["A", "X"]:
            print(f"La máquina dispara en {casilla}.")
            tablero_jugador = disparar(casilla, tablero_jugador)
            break

# Función para disparar (actualizar el tablero con agua o tocado)
def disparar(casilla, tablero):
    if tablero[casilla] == "O":  # Si hay un barco
        print("¡Tocado!")
        tablero[casilla] = "X"  # Marcamos como barco tocado
    elif tablero[casilla] == "_":  # Agua
        print("¡Agua!")
        tablero[casilla] = "A"  # Marcamos como agua
    return tablero

# Función principal que gestiona el flujo completo del juego
def hundir_la_flota():
    # Crear los tableros
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()
    
    # Crear un tablero visible para el jugador que muestre solo sus disparos sobre la máquina
    tablero_disparos_jugador = crear_tablero()  # Inicialmente vacío

    print(" ")
    print("H U N D I R    L A    F L O T A")
    print(" ")
    
    # Colocar los barcos
    print("Colocando barcos del jugador...")
    tablero_jugador = colocar_barcos(tablero_jugador)
    
    print("Colocando barcos de la máquina...")
    tablero_maquina = colocar_barcos(tablero_maquina)
    
    # Bucle de juego mientras queden barcos en ambos tableros
    while True:
        # Mostrar el tablero del jugador (con sus barcos y disparos de la máquina)
        print("\nTu tablero:")
        for fila in tablero_jugador:
            print(" ".join(fila))
        
        # Mostrar el tablero de disparos del jugador (sin los barcos de la máquina)
        print("\nTablero de disparos (sobre la máquina):")
        for fila in tablero_disparos_jugador:
            print(" ".join(fila))
        
        # Turno del jugador
        print("\nTurno del jugador:")
        turno_jugador(tablero_maquina, tablero_disparos_jugador)
        
        # Comprobar si la máquina ha perdido
        if not quedan_barcos(tablero_maquina):
            print("¡Has ganado! Todos los barcos de la máquina han sido hundidos.")
            break
        
        # Turno de la máquina
        print("\nTurno de la máquina:")
        turno_maquina(tablero_jugador)
        
        # Comprobar si el jugador ha perdido
        if not quedan_barcos(tablero_jugador):
            print("¡Has perdido! Todos tus barcos han sido hundidos.")
            break




