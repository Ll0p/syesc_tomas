import pygame

def salir(evento, datos_individuales):
    if evento.type == pygame.QUIT:
        datos_individuales["seguir"] = False

def importar_imagen(path: str, tamaño: tuple[int]):
    imagen = pygame.image.load(path)
    return pygame.transform.scale(imagen, tamaño)

def crear_font(fuente, tamaño):
    return pygame.font.Font(fuente, tamaño)

def crear_sonido(path_sonido: str, volumen: float = 0.1) -> pygame.mixer.Sound:
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(path_sonido)
    sonido.set_volume(volumen)
    return sonido