import pygame
from Datos.funciones_consola import parser_csv, ordenar_usuarios_descendente

def meter_fondo(pantalla, fondo) -> None:
    pantalla.blit(fondo, (0, 0))

####################################### MENU_VISUAL ######################################

def meter_rectangulos_menu(pantalla, rectangulo_c, rectangulo_l) -> None:
    pantalla.blit(rectangulo_l, (50, 75))
    lista_pos_y = [150, 210, 270]
    for y in lista_pos_y:
        pantalla.blit(rectangulo_c, (125, y))

def mostrar_textos_menu(pantalla, fuente, color) -> None:
    textos = ["Serpientes y Escaleras", "Jugar", "Ver resultados", "Salir"]
    lista_pos_x = [80, 210, 145, 210]
    lista_pos_y = [87, 162, 222, 282]
    for i in range(len(textos)):
        pantalla.blit(fuente.render(textos[i], True, color), (lista_pos_x[i],lista_pos_y[i]))

def dibujar_menu(pantalla, rectangulo_c, rectangulo_l, fuente_grande) -> None:
    from Colores import GRIS_MC
    meter_rectangulos_menu(pantalla, rectangulo_c, rectangulo_l)
    mostrar_textos_menu(pantalla, fuente_grande, GRIS_MC)

##########################################################################################

###################################### JUEGO_VISUAL ######################################

def mostrar_imagenes_juego(pantalla, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve, rects_tnt: dict[str, list], rect_posicion) -> None:
    pantalla.blit(fondo_piedra, (0, 230))
    pantalla.blit(fondo_madera, (0, 310))
    pantalla.blit(tablero_imagen, (45, 55))
    for key in rects_tnt:
        for tnt in rects_tnt[key]:
            pantalla.blit(imagen_tnt, (tnt.x, tnt.y))
    pantalla.blit(imagen_steve, (rect_posicion.x, rect_posicion.y))

def dibujar_lineas_juego(pantalla, color: tuple) -> None:
    pygame.draw.line(pantalla, color, (0, 230), (500, 230), 10)
    pygame.draw.line(pantalla, color, (0, 310), (500, 310), 10)
    lista_x = [10, 135, 260, 385] 
    for x in lista_x:
        pygame.draw.rect(pantalla, color, (x, 245, 110, 55))

def meter_rectangulos_juego(pantalla, rectangulo_c) -> None:
    lista_pos_x = [15, 140, 265, 390]
    for x in lista_pos_x:
        pantalla.blit(rectangulo_c, (x,250))

def mostrar_textos_rects_juego(pantalla, fuente_grande, color: tuple) -> None:
    textos = ["A", "B", "C", "Salir"]
    lista_pos_x = [55, 180, 305, 410]
    for i in range(len(textos)):
        pantalla.blit(fuente_grande.render(textos[i], True, color), (lista_pos_x[i],260))

def mostrar_preguntas(pantalla, fuente_chica, color: tuple, pregunta_actual: dict[str, str]) -> None:
    lista_pos_y = [340, 375, 400, 425]
    textos = [pregunta_actual["pregunta"], f"A: {pregunta_actual["respuesta_a"]}", f"B: {pregunta_actual["respuesta_b"]}", f"C: {pregunta_actual["respuesta_c"]}"]
    for i in range(len(lista_pos_y)):
        pantalla.blit(fuente_chica.render(textos[i], True, color), (20, lista_pos_y[i]))

def mostrar_tiempo(pantalla, fuente_chica, color, contador_valor: str) -> None:
    pantalla.blit(fuente_chica.render(contador_valor, True, color),(450,450))

def dibujar_juego(pantalla, rectangulo_c, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve, rects_tnt: dict[str, list], pregunta_actual: dict[str, str], rect_posicion, contador_valor: str) -> None:
    from Colores import NEGRO, GRIS_MC
    mostrar_imagenes_juego(pantalla, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve ,rects_tnt, rect_posicion)
    dibujar_lineas_juego(pantalla, NEGRO)
    meter_rectangulos_juego(pantalla, rectangulo_c)
    mostrar_textos_rects_juego(pantalla, fuente_grande, GRIS_MC)
    mostrar_tiempo(pantalla,fuente_chica,GRIS_MC,contador_valor)
    if pregunta_actual != None:
        mostrar_preguntas(pantalla, fuente_chica, GRIS_MC, pregunta_actual)

##########################################################################################

##################################### INGRESO_VISUAL #####################################

def meter_rects_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida) -> None:
    pantalla.blit(rectangulo_c, (rect_salida.x, rect_salida.y))
    pantalla.blit(rectangulo_l, (40, 210))

def mostrar_textos_ingreso(pantalla, fuente, color: tuple, usuario: str) -> None:
    pantalla.blit(fuente.render("Salir",True,color), (420, 15))
    pantalla.blit(fuente.render(f"Nombre: {usuario}",True,color), (50, 220))

def mostrar_error_ingreso(pantalla, fuente, color: tuple, mensaje_error: str) -> None:
    pantalla.blit(fuente.render(mensaje_error, True, color), (50, 270))

def dibujar_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida, fuente_chica, fuente_grande, mensaje_error_vacio: str, mensaje_error_nombre: str, usuario: str) -> None:
    from Colores import GRIS, GRIS_MC
    meter_rects_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida)
    mostrar_textos_ingreso(pantalla, fuente_grande, GRIS_MC, usuario)
    if mensaje_error_vacio != "":
        mostrar_error_ingreso(pantalla, fuente_chica, GRIS, mensaje_error_vacio)
    elif mensaje_error_nombre != "":
        mostrar_error_ingreso(pantalla, fuente_chica, GRIS, mensaje_error_nombre)

##########################################################################################

############################## RESULTADO_VISUAL_INDIVIDUAL ###############################

def mostrar_fin(pantalla, fuente_grande, fuente_chica, nombre: str, puntaje: int, color) -> None:
    pantalla.blit(fuente_grande.render("FIN DEL JUEGO",True,color), (125,150))
    pantalla.blit(fuente_chica.render(f"Usuario: {nombre}", True, color), (150,200))
    pantalla.blit(fuente_chica.render(f"Puntaje: {puntaje}", True, color), (150,220))

def dibujar_puntaje(pantalla, fuente_grande, fuente_chica, rectangulo_c, rect_salida, nombre: str, puntaje: int):
    from Colores import GRIS_MC
    mostrar_salida(pantalla, rectangulo_c, rect_salida, fuente_grande, GRIS_MC)
    mostrar_fin(pantalla, fuente_grande, fuente_chica, nombre, puntaje, GRIS_MC)

##########################################################################################

#################################### RESULTADO_VISUAL ####################################

def mostrar_salida(pantalla, rectangulo_c, rect_salida, fuente_grande, color) -> None:
    pantalla.blit(rectangulo_c, (rect_salida.x, rect_salida.y))
    pantalla.blit(fuente_grande.render("Salir",True,color), (420, 15))

def mostrar_puntajes_pygame(pantalla, fuente, color, usuarios_ordenados: list[dict]) -> None:
    distancia = 20
    for i in range(len(usuarios_ordenados)):
        pantalla.blit(fuente.render(f"{i+1}° | Usuario: {usuarios_ordenados[i]["nombre"]} | Puntaje: {usuarios_ordenados[i]["puntaje"]}", True, color), (50,distancia))
        distancia += 20

def dibujar_resultados(pantalla, rectangulo_c, rect_salida, fuente_chica, fuente_grande, path) -> None:
    from Colores import GRIS_MC
    mostrar_salida(pantalla, rectangulo_c, rect_salida, fuente_grande, GRIS_MC)
    usuarios = parser_csv(path)
    usuarios_ordenados = ordenar_usuarios_descendente(usuarios)
    mostrar_puntajes_pygame(pantalla, fuente_chica, GRIS_MC, usuarios_ordenados)

######################################### VISUAL #########################################

def dibujar_visuales(pantalla, rectangulo_c, rectangulo_l, rects_menu: dict, rects_juego: dict, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve, rects_tnt: dict[str, list], path: str, datos_indiv: dict, contador_valor: str) -> None:
    meter_fondo(pantalla, fondo_tierra)
    if datos_indiv["estado"] == "Menu":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_menu["1"].size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_menu(pantalla, rectangulo_c, rectangulo_l, fuente_grande)

    elif datos_indiv["estado"] == "Ingreso":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida, fuente_chica, fuente_grande, datos_indiv["mensaje_error"], datos_indiv["error_nombre"], datos_indiv["usuario"])

    elif datos_indiv["estado"] == "Jugar":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_juego["a"].size)
        dibujar_juego(pantalla, rectangulo_c, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve, rects_tnt, datos_indiv["pregunta_actual"], datos_indiv["rect_posicion"], contador_valor)

    elif datos_indiv["estado"] == "Puntaje":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        dibujar_puntaje(pantalla, fuente_grande, fuente_chica, rectangulo_c, rect_salida, datos_indiv["usuario"], datos_indiv["posicion"])

    elif datos_indiv["estado"] == "Resultados":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        dibujar_resultados(pantalla, rectangulo_c, rect_salida, fuente_chica, fuente_grande, path)

##########################################################################################