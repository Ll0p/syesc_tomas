def crear_estado_jugador(preguntas: list[dict]) -> dict:
    import copy
    import pygame
    return {
        "estado" : "Menu",
        "usuario" : "",
        "posicion" : 15,
        "contador" : 5,
        "rect_posicion": pygame.Rect(254,105,25,25),
        "respuesta" : None,
        "mensaje_error" : "",
        "error_nombre" : "",
        "copia_preguntas" : copy.deepcopy(preguntas),
        "pregunta_actual" : None,
        "seguir" : True
    }

def reiniciar_contador():
    return "3"