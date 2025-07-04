def jugar_pygame(preguntas, path, tablero) -> None:
    import pygame
    from Modulos.recursos import salir, crear_sonido, crear_font, importar_imagen
    from Modulos.visuales import dibujar_visuales
    from Modulos.interacciones import interaccion_mouse, interactuar_ingreso_teclado
    from Modulos.datos_jugador import crear_estado_jugador
    from Modulos.rects import rects_juego, rect_salida, rects_menu, rects_tnt
    pygame.init()
    pantalla = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Serpientes y escaleras")

    sonido_click = crear_sonido("Recursos/Sonidos/Click.mp3", 1.0)
    sonido_fondo = crear_sonido("Recursos/Sonidos/MiceOnVenus.mp3", 0.2)
    sonido_fondo.play(-1) 

    fondo_tierra = importar_imagen("Recursos/Imagenes/fondo_tierra.jpg", (500, 500))
    fondo_madera = importar_imagen("Recursos/Imagenes/madera_osc.png", (500, 500))
    fondo_piedra = importar_imagen("Recursos/Imagenes/fondo_piedra.png", (500, 500))
    tablero_imagen = importar_imagen("Recursos/Imagenes/tablero.png", (405, 125))
    tnt = importar_imagen("Recursos/Imagenes/tnt.png", (25,25))
    steve = importar_imagen("Recursos/Imagenes/steve.png", (25,25))

    rectangulo_c = pygame.image.load("Recursos/Imagenes/rectan_mine_chico.png")
    rectangulo_l = pygame.image.load("Recursos/Imagenes/rectan_mine_largo.png")

    fuente_grande = crear_font("Recursos/Minecraft.ttf", 30)
    fuente_chica = crear_font("Recursos/Minecraft.ttf", 15)

    datos_individuales = crear_estado_jugador(preguntas)
    datos_base = crear_estado_jugador(preguntas)

    while datos_individuales["seguir"]:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            salir(evento, datos_individuales)

            interaccion_mouse(evento, rects_menu, rects_juego, rect_salida, sonido_click, tablero, path, datos_individuales, datos_base)

            interactuar_ingreso_teclado(evento, datos_individuales)

        dibujar_visuales(pantalla, rectangulo_c, rectangulo_l, rects_menu, rects_juego, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, tnt, path, datos_individuales)

        pygame.display.flip()

    sonido_fondo.stop()
    pygame.quit()