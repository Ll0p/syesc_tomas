import pygame

def salir(evento, datos_individuales):
    if evento.type == pygame.QUIT:
        datos_individuales["seguir"] = False

def introducir_timer(evento, tick, contador: str, datos_indiv: dict):
    import random
    from Datos.funciones_consola import retirar_pregunta
    if evento.type == tick and datos_indiv["estado"] == "Jugar":
        contador = int(contador) - 1 
        if int(contador) == 0:
            contador = "15"
            datos_indiv["respuesta"] = "d"
            indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
            datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)

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

def interaccion_mouse_menu(rects_menu, evento, sonido_click, datos_indiv: dict):
    if clickeo_en(rects_menu["1"], evento.pos, sonido_click):
        datos_indiv["estado"] = "Ingreso"
    elif clickeo_en(rects_menu["2"], evento.pos, sonido_click):
        datos_indiv["estado"] = "Resultados"
    elif clickeo_en(rects_menu["3"], evento.pos, sonido_click):
        datos_indiv["seguir"] = False

def interaccion_mouse_ingreso_y_resultados(rect_salida, evento, sonido_click, datos_indiv: dict):
    if clickeo_en(rect_salida, evento.pos, sonido_click):
        datos_indiv["usuario"] = ""
        datos_indiv["estado"] = "Menu"

def interaccion_mouse_puntaje(rect_salida, evento, sonido_click, datos_indiv: dict, datos_base: dict):
    if clickeo_en(rect_salida, evento.pos, sonido_click):
        resetear_datos(datos_indiv, datos_base)

def procesar_usuario(datos_indiv: dict, tablero: tuple, rects_tablero: tuple, path: str):
    from Datos.funciones_consola import verificar_respuesta, modificar_posicion, verificar_ganador_perdedor_pygame, retirar_pregunta, ingresar_datos_usuario
    import random
    es_correcta = verificar_respuesta(datos_indiv["pregunta_actual"], datos_indiv["respuesta"])
    datos_indiv["posicion"] = modificar_posicion(tablero, datos_indiv["posicion"], es_correcta)
    datos_indiv["rect_posicion"] = rects_tablero[datos_indiv["posicion"]]
    limite = verificar_ganador_perdedor_pygame(datos_indiv["posicion"], tablero)

    if len(datos_indiv["copia_preguntas"]) > 0 and not limite:
        indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
        datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)
    else:
        ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"])
        datos_indiv["estado"] = "Puntaje"

def interaccion_mouse(evento, rects_menu: dict, rects_juego: dict, rect_salida, sonido_click, tablero: tuple[int], path: str, datos_indiv: dict, datos_base: dict, rects_tablero: tuple, contador_ref: dict) -> None:
    from Datos.funciones_consola import ingresar_datos_usuario, verificar_opcion
    from Modulos.datos_jugador import reiniciar_contador

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Que evento.button == 1 significa que toqué click izquierdo
        if datos_indiv["estado"] == "Menu":
            interaccion_mouse_menu(rects_menu, evento, sonido_click, datos_indiv)

        elif datos_indiv["estado"] == "Ingreso" or datos_indiv["estado"] == "Resultados":
            interaccion_mouse_ingreso_y_resultados(rect_salida, evento, sonido_click, datos_indiv)

        elif datos_indiv["estado"] == "Puntaje":
            interaccion_mouse_puntaje(rect_salida, evento, sonido_click, datos_indiv, datos_base)

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
                datos_indiv["estado"] = "Puntaje"
                return None

            if datos_indiv["pregunta_actual"] != None and verificar_opcion(datos_indiv["respuesta"], ("a","b","c")):
                procesar_usuario(datos_indiv, tablero, rects_tablero, path)
                datos_indiv["respuesta"] = datos_base["respuesta"]
                contador_ref["valor"] = reiniciar_contador()

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