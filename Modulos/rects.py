import pygame

##################################################################

rects_menu = {
    "1": pygame.Rect(125, 150, 250, 50),
    "2": pygame.Rect(125, 210, 250, 50),
    "3": pygame.Rect(125, 270, 250, 50)
}

rects_juego = {
    "a": pygame.Rect(15, 250, 100, 45),
    "b": pygame.Rect(140, 250, 100, 45),
    "c": pygame.Rect(265, 250, 100, 45),
    "salir": pygame.Rect(390, 250, 100, 45)
}

rect_salida = pygame.Rect(400, 0, 100, 50)

##################################################################

rect_steve = pygame.Rect(254,105,25,25)
rects_tnt = {
"1" : [pygame.Rect(94,65,25,25),pygame.Rect(94,105,25,25),pygame.Rect(254,105,25,25),pygame.Rect(294,105,25,25),pygame.Rect(54,145,25,25),pygame.Rect(334,145,25,25)],
"2" : [pygame.Rect(214,105,25,25),pygame.Rect(174,145,25,25)],
"3" : [pygame.Rect(254,65,25,25)]
}

def mover_por_respuesta_pygame(rect_steve, respuesta: bool) -> None:
    if respuesta:
        rect_steve.x += 40
    else:
        rect_steve.x -= 40

def aplicar_borde(rect_steve, limite_izq, limite_der) -> None:
    if rect_steve.x > limite_der:
        rect_steve.x = limite_izq
        rect_steve.y -= 40
    elif rect_steve.x < limite_izq:
        rect_steve.x = limite_der - rect_steve.size
        rect_steve.y += 40

def aplicar_efecto_casilla_pygame(rects_tnt, rect_steve):
    pass

def modificar_posicion_steve(rect_steve, respuesta: bool):
    mover_por_respuesta_pygame(rect_steve, respuesta)
    aplicar_borde(rect_steve)