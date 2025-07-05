import pygame

################################### INTERACCIÓN_MOUSE ####################################

def clickeo_en(rect: pygame.Rect, pos: tuple[int, int], sonido) -> bool:
    retorno = False
    if rect.collidepoint(pos):
        sonido.play()
        retorno = True
    return retorno

def resetear_datos(datos_indiv: dict, datos_base: dict) -> None:
    import copy
    for clave in datos_indiv:
        datos_indiv[clave] = copy.deepcopy(datos_base[clave])

def interaccion_mouse(evento, rects_menu: dict, rects_juego: dict, rect_salida, sonido_click, tablero: tuple[int], path: str, datos_indiv: dict, datos_base: dict, rects_tablero: tuple) -> None:
    import random
    from Datos.funciones_consola import ingresar_datos_usuario, verificar_opcion, modificar_posicion, verificar_ganador_perdedor_pygame, verificar_respuesta, retirar_pregunta
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Que evento.button == 1 significa que toqué click izquierdo
        if datos_indiv["estado"] == "Menu":
            if clickeo_en(rects_menu["1"], evento.pos, sonido_click):
                datos_indiv["estado"] = "Ingreso"
            elif clickeo_en(rects_menu["2"], evento.pos, sonido_click):
                datos_indiv["estado"] = "Resultados"
            elif clickeo_en(rects_menu["3"], evento.pos, sonido_click):
                datos_indiv["seguir"] = False

        elif datos_indiv["estado"] == "Ingreso" or datos_indiv["estado"] == "Resultados":
            if clickeo_en(rect_salida, evento.pos, sonido_click):
                datos_indiv["usuario"] = ""
                datos_indiv["estado"] = "Menu"

        elif datos_indiv["estado"] == "Jugar":
            datos_indiv["respuesta"] = datos_base["respuesta"]
            if clickeo_en(rects_juego["a"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "a"
            elif clickeo_en(rects_juego["b"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "b"
            elif clickeo_en(rects_juego["c"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "c"
            elif clickeo_en(rects_juego["salir"], evento.pos, sonido_click):
                ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"])
                resetear_datos(datos_indiv, datos_base)
                return None

            if datos_indiv["pregunta_actual"] != None and verificar_opcion(datos_indiv["respuesta"], ("a","b","c")):
                es_correcta = verificar_respuesta(datos_indiv["pregunta_actual"], datos_indiv["respuesta"])
                datos_indiv["posicion"] = modificar_posicion(tablero, datos_indiv["posicion"], es_correcta)
                datos_indiv["rect_posicion"] = rects_tablero[datos_indiv["posicion"]]
                limite = verificar_ganador_perdedor_pygame(datos_indiv["posicion"], tablero)
                if len(datos_indiv["copia_preguntas"]) > 0 and not limite:
                    indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
                    datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)
                else:
                    ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"]) 
                    resetear_datos(datos_indiv, datos_base)

####################################################################################################################################################################################

############################## INTERACCIÓN_INGRESO_TECLADO ###############################

def borrar_letra(usuario: str) -> str:
    return usuario[:-1]

def verificar_alnum(caracter: str) -> bool:
    return caracter.isalnum()

def mensaje_caracter(caracter: str) -> str:
    mensaje = ""
    if not verificar_alnum(caracter):
        mensaje = "Caracter no valido"
    return mensaje

def interactuar_ingreso_teclado(evento, datos_indiv: dict) -> None:
    import random
    from Datos.funciones_consola import verificar_nombre, retirar_pregunta
    if evento.type == pygame.KEYDOWN and datos_indiv["estado"] == "Ingreso":
        if evento.key == pygame.K_BACKSPACE:
            datos_indiv["usuario"] = borrar_letra(datos_indiv["usuario"])
            datos_indiv["mensaje_error"] = ""
        elif evento.key == pygame.K_RETURN:
            if verificar_nombre(datos_indiv["usuario"]):
                datos_indiv["estado"] = "Jugar"
                indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
                datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)
                datos_indiv["mensaje_error"] = ""
            else:
                datos_indiv["mensaje_error"] = "No puede usar este nombre"
        else:
            datos_indiv["mensaje_error"] = mensaje_caracter(evento.unicode)
            if datos_indiv["mensaje_error"] == "":
                datos_indiv["usuario"] += evento.unicode

####################################################################################################################################################################################