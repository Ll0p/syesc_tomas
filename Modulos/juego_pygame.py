def jugar_pygame(preguntas, path, tablero) -> None:
    import pygame
    from Modulos.recursos import meter_musica_fondo, crear_font, pantalla, sonido_click, sonido_fondo, rectangulo_c, rectangulo_l, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve
    from Modulos.visuales import dibujar_visuales
    from Modulos.interacciones import salir, interaccion_mouse, interactuar_ingreso_teclado, introducir_timer
    from Modulos.datos_jugador import crear_estado_jugador, reiniciar_contador
    from Modulos.rects import rects_juego, rect_salida, rects_menu, rects_tnt, rects_tablero
    pygame.init()
    pygame.display.set_caption("Serpientes y escaleras")

    meter_musica_fondo(sonido_fondo)
    fuente_grande = crear_font("Recursos/Minecraft.ttf", 30)
    fuente_chica = crear_font("Recursos/Minecraft.ttf", 15)

    datos_individuales = crear_estado_jugador(preguntas)
    datos_base = crear_estado_jugador(preguntas)

    tick = pygame.USEREVENT
    pygame.time.set_timer(tick, 1000)
    contador = {"valor": reiniciar_contador(datos_base["contador"])}

    while datos_individuales["seguir"]:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            salir(evento, datos_individuales)

            interaccion_mouse(evento, rects_menu, rects_juego, rect_salida, sonido_click, tablero, path, datos_individuales, datos_base, rects_tablero, contador)

            interactuar_ingreso_teclado(evento, datos_individuales)

            introducir_timer(evento, tick, sonido_click, contador, datos_individuales, datos_base, tablero, rects_tablero, path)

        dibujar_visuales(pantalla, rectangulo_c, rectangulo_l, rects_menu, rects_juego, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, imagen_tnt, imagen_steve, rects_tnt, path, datos_individuales, contador["valor"])

        pygame.display.flip()

    sonido_fondo.stop()
    pygame.quit()