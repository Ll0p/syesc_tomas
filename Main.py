from Modulos.juego_pygame import jugar_pygame
from Datos.preguntas import preguntas
from Datos.tablero import tablero
from config import path

jugar_pygame(preguntas, path, tablero)

# Tengo que meter timer por cada pregunta, si se termina, la respuesta es incorrecta y se pasa a la siguiente pregunta.

# Cuando el juego termina por cualquier motivo se debe
# guardar el puntaje en el archivo y mostrar al jugador su
# posición y puntaje (pantalla puntaje).

# Terminar el tablero