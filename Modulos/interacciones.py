import pygame

def salir(evento, datos_individuales: dict) -> None:
    if evento.type == pygame.QUIT:
        datos_individuales["seguir"] = False

def introducir_timer(evento, tick, sonido_click, contador_ref: dict[str, str], datos_indiv: dict, datos_base: dict, tablero: tuple[int], rects_tablero: tuple, path: str) -> None:
    """ Introduce un contador al juego

    Argumentos:
        evento (_type_): El evento actual
        tick (_type_): El evento tick
        sonido_click (_type_): El sonido click
        contador_ref (dict[str, str]): El diccionario con la referencia del contador
        datos_individuales (dict): Los datos individuales del usuario
        datos_base (dict): Los datos predeterminados del juego
        tablero (tuple[int]): El tablero del juego
        rects_tablero (tuple): Los rects del tablero en pantalla
        path (str): El path CSV
    """
    from Modulos.datos_jugador import reiniciar_contador 
    if evento.type == tick and datos_indiv["estado"] == "Jugar":
        contador_ref["valor"] = str(int(contador_ref["valor"]) - 1) # El contador menos 1

        # Si el contador llega a 0 y no hubo respuesta
        if int(contador_ref["valor"]) == 0 and datos_indiv["respuesta"] == datos_base["respuesta"]:
            datos_indiv["respuesta"] = "d" # Una respuesta incorrecta 
            sonido_click.play()
            procesar_usuario(datos_indiv, tablero, rects_tablero, path) # Se procesa la respuesta incorrecta y aplica lo suyo
            contador_ref["valor"] = reiniciar_contador(datos_base["contador"]) # Por cada respuesta hecha el contador se reinicia
            datos_indiv["respuesta"] = datos_base["respuesta"] # Osea, vuelve a ser None (una respuesta vacia)

def clickeo_en(rect: pygame.Rect, pos: tuple[int, int], sonido) -> bool:
    """ Determina si colisiona un rect en determinada posicion

    Argumentos:
        rect (pygame.Rect): El rect elegido
        pos (tuple[int, int]): La posicion del con la que se verifica si colisiona
        sonido (_type_): Un sonido para ejecutar en caso de que ocurra

    Retorna:
        bool: True en caso de colisionar y viceversa
    """
    retorno = False
    if rect.collidepoint(pos):
        sonido.play()
        retorno = True
    return retorno

def resetear_datos(datos_indiv: dict, datos_base: dict) -> None:
    """ Resetea los datos del usuario

    Argumentos:
        datos_indiv (dict): Los datos individuales del usuario
        datos_base (dict): Los datos predeterminados del juego
    """
    import copy
    for clave in datos_indiv:
        datos_indiv[clave] = copy.deepcopy(datos_base[clave])

def actualizar_preguntas(datos_indiv: dict) -> None:
    """ Actualiza el diccionario de preguntas del usuario

    Argumento:
        datos_indiv (dict): Los datos individuales del usuario
    """
    import random
    from Datos.funciones_consola import retirar_pregunta
    indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
    datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)

def procesar_usuario(datos_indiv: dict, tablero: tuple[int], rects_tablero: tuple, path: str) -> None:
    """ Procesa los datos del usuario y aplica las posiciones/estados correspondientes

    Argumentoss:
        datos_indiv (dict): Los datos individuales del usuario
        tablero (tuple[int]): El tablero del juego
        rects_tablero (tuple): Los rects del tablero en pantalla
        path (str): El path CSV
    """
    from Datos.funciones_consola import verificar_respuesta, modificar_posicion, verificar_ganador_perdedor_pygame, ingresar_datos_usuario
    datos_indiv["posicion"] = modificar_posicion(tablero, datos_indiv["posicion"], verificar_respuesta(datos_indiv["pregunta_actual"], datos_indiv["respuesta"])) # Mopdifica la posicion del usuario
    datos_indiv["rect_posicion"] = rects_tablero[datos_indiv["posicion"]] # Mueve al steve de pantalla según la posicion del usuario

    # Si todavía quedan preguntas y el jugador no ganó ni perdió
    if len(datos_indiv["copia_preguntas"]) > 0 and not verificar_ganador_perdedor_pygame(datos_indiv["posicion"], tablero):
        actualizar_preguntas(datos_indiv)
    else:
        ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"])
        datos_indiv["estado"] = "Puntaje"

################################### INTERACCIÓN_MOUSE ####################################

def interaccion_mouse_menu(rects_menu: dict, evento, sonido_click, datos_indiv: dict) -> None:
    """ Interpreta los clicks en el menú

    Argumentos:
        rects_menu (_type_): Diccionario con rects del menú
        evento (_type_): El evento actual
        sonido_click (_type_): Sonido de click
        datos_indiv (dict): Los datos individuales del usuario
    """
    if clickeo_en(rects_menu["1"], evento.pos, sonido_click):
        datos_indiv["estado"] = "Ingreso"
    elif clickeo_en(rects_menu["2"], evento.pos, sonido_click):
        datos_indiv["estado"] = "Resultados"
    elif clickeo_en(rects_menu["3"], evento.pos, sonido_click):
        datos_indiv["seguir"] = False

def interaccion_mouse_ingreso_y_resultados(rect_salida, evento, sonido_click, datos_indiv: dict) -> None:
    """ Interpreta los clicks en el ingreso de nombre y la pantalla de resultados

    Argumentos:
        rect_salida (_type_): El rect de la salida
        evento (_type_): El evento actual
        sonido_click (_type_): Sonido de click
        datos_indiv (dict): Los datos individuales del usuario
    """
    if clickeo_en(rect_salida, evento.pos, sonido_click):
        datos_indiv["usuario"] = ""
        datos_indiv["estado"] = "Menu"

def interaccion_mouse_puntaje(rect_salida, evento, sonido_click, datos_indiv: dict, datos_base: dict) -> None:
    """ Interpreta los clicks en la pantalla de puntaje

    Argumentos:
        rect_salida (_type_): _description_
        evento (_type_): _description_
        sonido_click (_type_): _description_
        datos_indiv (dict): _description_
        datos_base (dict): _description_
    """
    if clickeo_en(rect_salida, evento.pos, sonido_click):
        resetear_datos(datos_indiv, datos_base)

def interaccion_mouse(evento, rects_menu: dict, rects_juego: dict, rect_salida, sonido_click, tablero: tuple[int], path: str, datos_indiv: dict, datos_base: dict, rects_tablero: tuple, contador_ref: dict[str, str]) -> None:
    """ Interpreta todas las interacciones con el mouse en los diferentes estados y aplica cambios en base a esto

    Argumentos:
        evento (_type_): El evento actual
        rects_menu (dict): Los rects del menu
        rects_juego (dict): Los rects del juego
        rect_salida (_type_): El rect de salida
        sonido_click (_type_): El sonido click
        tablero (tuple[int]): El tablero del juego
        path (str): El path CSV
        datos_indiv (dict): Los datos individuales del usuario
        datos_base (dict): Los datos predeterminados del juego
        rects_tablero (tuple): Los rects del tablero en pantalla
        contador_ref (dict[str, str]): El diccionario con la referencia del contador 
    """
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
            if clickeo_en(rects_juego["a"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "a"
            elif clickeo_en(rects_juego["b"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "b"
            elif clickeo_en(rects_juego["c"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "c"
            elif clickeo_en(rects_juego["salir"], evento.pos, sonido_click):
                ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"])
                datos_indiv["estado"] = "Puntaje"
                return None # Para que no siga el programa
            
            # Si todavia existen preguntas y la respuesta es valida (porque sinó interpreta todos los clicks)
            if datos_indiv["pregunta_actual"] != datos_base["pregunta_actual"] and verificar_opcion(datos_indiv["respuesta"], ("a","b","c")):
                procesar_usuario(datos_indiv, tablero, rects_tablero, path) 
                datos_indiv["respuesta"] = datos_base["respuesta"] # Osea, vuelve a ser None (una respuesta vacia)
                contador_ref["valor"] = reiniciar_contador(datos_base["contador"]) # Por cada respuesta hecha el contador se reinicia

####################################################################################################################################################################################

############################## INTERACCIÓN_INGRESO_TECLADO ###############################

def borrar_letra(usuario: str) -> str:
    """ Borra la ultima letra de una cadena (nombre del usuario)

    Argumentos:
        usuario (str): La cadena que se va a utilizar

    Retorna:
        str: La cadena sin la ultima letra
    """
    return usuario[:-1]

def validar_usuario(datos_indiv: dict) -> None:
    """ Valida el usuario

    Argumentos:
        datos_indiv (dict): Los datos individuales del usuario
    """
    import random
    from Datos.funciones_consola import retirar_pregunta
    datos_indiv["estado"] = "Jugar"
    actualizar_preguntas(datos_indiv)
    datos_indiv["mensaje_error"] = ""

def analizar_usuario(datos_indiv: dict) -> None:
    """ Analiza al usuario ingresado

    Argumentos:
        datos_indiv (dict): Los datos individuales del usuario
    """
    from Datos.funciones_consola import verificar_nombre
    if verificar_nombre(datos_indiv["usuario"]):
        validar_usuario(datos_indiv)
    else:
        datos_indiv["mensaje_error"] = "No puede usar este nombre"

def verificar_alnum(caracter: str) -> bool:
    """ Verifica si un caracter (letra) es alfanumerico

    Argumentos:
        caracter (str): El caracter a analizar

    Retorna:
        bool: True en caso de serlo y viceversa
    """
    return caracter.isalnum()

def modificar_mensaje(caracter: str, verificacion: callable) -> str:
    """ Retorna un mensaje en base a el caracter (letra) analizado

    Argumentos:
        caracter (str): El caracter a analizar

    Retorna:
        str: Un mensaje en caso de no cumplir con la verificacion 
    """
    mensaje = ""
    if not verificacion(caracter):
        mensaje = "Caracter no valido"
    return mensaje

def agregar_caracter(cadena: str, caracter: str) -> str:
    """ Agrega un caracter a una cadena

    Argumentos:
        cadena (str): Cadena a modificar
        caracter (str): El caracter a agregar

    Retorna:
        str: La cadena modificada
    """
    cadena_modificada = cadena + caracter
    return cadena_modificada

def interactuar_ingreso_teclado(evento, datos_indiv: dict) -> None:
    """ Interactua con el teclado cuando el estado es "Ingreso" y determina estados

    Argumentos:
        evento (_type_): El evento actual
        datos_indiv (dict): Los datos individuales del usuario"""
    if evento.type == pygame.KEYDOWN and datos_indiv["estado"] == "Ingreso":
        if evento.key == pygame.K_BACKSPACE:
            datos_indiv["usuario"] = borrar_letra(datos_indiv["usuario"])
            datos_indiv["mensaje_error"] = "" # Borra el error para que no se muestre en pantalla
        elif evento.key == pygame.K_RETURN:
            analizar_usuario(datos_indiv)
        else: 
            datos_indiv["mensaje_error"] = modificar_mensaje(evento.unicode, verificar_alnum) # Actualiza el mensaje según un criterio
            if datos_indiv["mensaje_error"] == "":
                datos_indiv["usuario"] = agregar_caracter(datos_indiv["usuario"], evento.unicode)

####################################################################################################################################################################################