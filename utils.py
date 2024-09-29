import numpy as np
import random

# Función para crear el tablero
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")
    return tablero

# Función para colocar barcos en el tablero
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

# Función para disparar
def disparar(casilla, tablero):
    if tablero[casilla] == "O":  # Si hay un barco
        print("Tocado!")
        tablero[casilla] = "X"
    elif tablero[casilla] == "_":  # Agua
        print("Agua!")
        tablero[casilla] = "A"
    return tablero

# Función para crear un barco
def crear_barco(eslora):
    casilla_0 = (random.randint(0, 9), random.randint(0, 9))  # Casilla inicial
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0] + 1, casilla[1])  # Avanza en vertical
        else:
            casilla = (casilla[0], casilla[1] + 1)  # Avanza en horizontal
        barco.append(casilla)  # Añadir la casilla al barco

    return barco

# Función para colocar barcos en el tablero
def colocar_barcos(tablero):
    barcos_esloras = [2, 2, 2, 3, 3, 4]  # Lista de tamaños de barcos
    i = 0  # Inicializamos el contador para los barcos

    while i < len(barcos_esloras):
        eslora = barcos_esloras[i]  # i es 0 al iniciar
        barco = crear_barco(eslora)  # Creamos el barco
        try:
            tablero = colocar_barco(barco, tablero)  # Intentamos colocarlo
            i += 1  # Avanzamos solo si el barco se coloca bien
        except ValueError:
            pass  # Intentamos de nuevo si hay error
    return tablero

# Función para mostrar el tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    for fila in tablero:
        fila_mostrar = []
        for casilla in fila:
            if ocultar_barcos and casilla == "O":
                fila_mostrar.append("_")  # Ocultamos los barcos de la máquina
            else:
                fila_mostrar.append(casilla)
        print(" ".join(fila_mostrar))

# Función para generar disparos aleatorios
def generar_disparo_aleatorio(tamaño):
    fila = random.randint(0, tamaño - 1)
    columna = random.randint(0, tamaño - 1)
    return (fila, columna)

# Función para comprobar si todos los barcos han sido hundidos
def comprobar_ganador(tablero):
    for fila in tablero:
        if "O" in fila:
            return False  # Si hay "O", aún quedan barcos
    return True  # No hay más barcos, se ha ganado

# Función principal para jugar Batalla Naval
def jugar_batalla_naval():
    tamaño = 10
    # Crear y colocar barcos en ambos tableros
    tablero_jugador = crear_tablero(tamaño)
    tablero_maquina = crear_tablero(tamaño)

    tablero_jugador = colocar_barcos(tablero_jugador)
    tablero_maquina = colocar_barcos(tablero_maquina)

    turno = "jugador"
    
    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)  # Mostrar el tablero del jugador
        
        print("\nTablero de la máquina (sin barcos):")
        mostrar_tablero(tablero_maquina, ocultar_barcos=True)  # Mostrar solo los disparos en el tablero de la máquina

        if turno == "jugador":
            print("Es tu turno. Introduce la casilla donde quieres disparar (formato: fila columna):")
            disparo = tuple(map(int, input().split()))
            tablero_maquina = disparar(disparo, tablero_maquina)

            # Comprobar si el jugador ha ganado
            if comprobar_ganador(tablero_maquina):
                print("¡¡¡Felicidades, has ganado!!! Todos los barcos de la máquina han sido hundidos. 🎉🎉🎉")
                print("¡Eres el campeón del océano!")
                break

            turno = "maquina"  # Cambiar turno a la máquina

        elif turno == "maquina":
            print("Turno de la máquina...")
            disparo_maquina = generar_disparo_aleatorio(tamaño)
            print(f"La máquina ha disparado en la casilla: {disparo_maquina}")
            tablero_jugador = disparar(disparo_maquina, tablero_jugador)

            # Comprobar si la máquina ha ganado
            if comprobar_ganador(tablero_jugador):
                print("¡¡¡La máquina ha ganado!!! Todos tus barcos han sido hundidos. 😢")
                print("¡Mejor suerte la próxima vez, capitán!")
                break

            turno = "jugador"  # Cambiar turno al jugador

# Ejecutar el juego
jugar_batalla_naval()
