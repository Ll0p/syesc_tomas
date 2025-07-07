import pygame
from Modulos.tamaños import tamaño_fondos, tamaño_objeto, tamaño_tablero

##############################################################################

def importar_imagen(path: str, tamaño: tuple[int]):
    imagen = pygame.image.load(path)
    return pygame.transform.scale(imagen, tamaño)

def crear_font(fuente, tamaño: int):
    return pygame.font.Font(fuente, tamaño)

def crear_sonido(path_sonido: str, volumen: float = 0.1) -> pygame.mixer.Sound:
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(path_sonido)
    sonido.set_volume(volumen)
    return sonido

def meter_musica_fondo(musica_fondo) -> None:
    musica_fondo.play(-1) 

##############################################################################

pantalla = pygame.display.set_mode(tamaño_fondos)

sonido_click = crear_sonido("Recursos/Sonidos/Click.mp3", 1.0)
sonido_fondo = crear_sonido("Recursos/Sonidos/MiceOnVenus.mp3", 0.2)

fondo_tierra = importar_imagen("Recursos/Imagenes/fondo_tierra.jpg", tamaño_fondos)
fondo_madera = importar_imagen("Recursos/Imagenes/madera_osc.png", tamaño_fondos)
fondo_piedra = importar_imagen("Recursos/Imagenes/fondo_piedra.png", tamaño_fondos)
tablero_imagen = importar_imagen("Recursos/Imagenes/tablero.png", tamaño_tablero)
imagen_tnt = importar_imagen("Recursos/Imagenes/tnt.png", tamaño_objeto)
imagen_steve = importar_imagen("Recursos/Imagenes/steve.png", tamaño_objeto)

rectangulo_c = pygame.image.load("Recursos/Imagenes/rectan_mine_chico.png")
rectangulo_l = pygame.image.load("Recursos/Imagenes/rectan_mine_largo.png")