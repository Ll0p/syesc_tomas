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

rects_tablero = (pygame.Rect(54,65,25,25),pygame.Rect(94,65,25,25),pygame.Rect(134,65,25,25),pygame.Rect(174,65,25,25),pygame.Rect(214,65,25,25),pygame.Rect(254,65,25,25),pygame.Rect(294,65,25,25),pygame.Rect(334,65,25,25),pygame.Rect(374,65,25,25),pygame.Rect(414,65,25,25),
                pygame.Rect(54,105,25,25),pygame.Rect(94,105,25,25),pygame.Rect(134,105,25,25),pygame.Rect(174,105,25,25),pygame.Rect(214,105,25,25),pygame.Rect(254,105,25,25),pygame.Rect(294,105,25,25),pygame.Rect(334,105,25,25),pygame.Rect(374,105,25,25),pygame.Rect(414,105,25,25),
                pygame.Rect(54,145,25,25),pygame.Rect(94,145,25,25),pygame.Rect(134,145,25,25),pygame.Rect(174,145,25,25),pygame.Rect(214,145,25,25),pygame.Rect(254,145,25,25),pygame.Rect(294,145,25,25),pygame.Rect(334,145,25,25),pygame.Rect(374,145,25,25),pygame.Rect(414,145,25,25),pygame.Rect(454,145,25,25))

rect_steve = pygame.Rect(254,105,25,25)
rects_tnt = {
"1" : [pygame.Rect(94,65,25,25),pygame.Rect(94,105,25,25),pygame.Rect(254,105,25,25),pygame.Rect(294,105,25,25),pygame.Rect(54,145,25,25),pygame.Rect(334,145,25,25)],
"2" : [pygame.Rect(214,105,25,25),pygame.Rect(174,145,25,25)],
"3" : [pygame.Rect(254,65,25,25)]
}