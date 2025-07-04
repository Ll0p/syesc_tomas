def consultar_nombre() -> str:
    """ Consulta al usuario su nombre y lo retorna

    Retorna:
        str: El nombre ingresado con capitalize
    """
    usuario = input("\nIngrese su nombre: ").capitalize()
    return usuario

def preguntar_seguir() -> str:
    """ Pregunta al usuario si desea continuar y devuelve la respuesta

    Retorna:
        str: La respuesta ingresada en minusculas
    """
    seguir = input("\n¿ Desea seguir intentando [si/no]? : ").lower()
    return seguir

def consultar_opcion() -> str:
    """ Consulta al usuario para que elija una opcion y la retorna

    Retorna:
        str: La opción ingresada en minusculas
    """
    opcion = input("\nElija una opción: ").lower()
    return opcion 

###################################################################

def verificar_longitud_nombre(cadena: str) -> bool:
    """ Verifica que la longitud de la cadena sea existente

    Argumento:
        cadena (str): Cadena de texto a verificar

    Retorna:
        bool: True en caso de existir una longitud y viceversa
    """
    return len(cadena.strip()) > 0

def verificar_existencia_score(path_csv, nombre: str) -> bool:
    """ Verifica si el usuario existe en el archivo y retorna un booleano

    Argumentos:
        path (_type_): Path del archivo.csv
        nombre (str): Nombre a verificar

    Retorna:
        bool: True en caso de que el nombre exista en el archivo y viceversa
    """
    encontrado = False
    try:
        with open(path_csv, "r", encoding = "UTF-8") as archivo:
            for linea in archivo:
                if linea.split(",")[0] == nombre:
                    encontrado = True
                    break
    except FileNotFoundError:
        print("El archivo no existe")
        encontrado = False
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")
    return encontrado

def verificar_nombre(nombre: str) -> bool:
    """ Verifica que el nombre sea válido y no esté repetido.

    Argumentos:
        nombre (str): Nombre a verificar

    Retorna:
        bool: True en caso de que se cumplan ambas condiciones y viceversa
    """
    from config import path
    return verificar_longitud_nombre(nombre) and not verificar_existencia_score(path, nombre)

def verificar_seguir(decision: str) -> bool:
    """ Verifica que la decisión es igual a "si" o "no" y retorna un booleano en base a eso

    Argumentos:
        decision (str): Una cadena a analizar

    Retorna:
        bool: True en caso de ser una de las opciones y viceversa
    """
    verificado = True
    if decision.strip() != "si" and decision.strip() != "no":
        verificado = False
    return verificado

def verificar_opcion(opcion_elegida: str, opciones: tuple[str]) -> bool:
    """ Verifica si la opción elegida se encuentra en una lista de opciones

    Argumentos:
        opcion_elegida (str): La opción que se quiere verificar
        opciones (tuple[str]): La lista de opciones posibles/existentes

    Retorna:
        bool: True en caso de que la opcion exista en la lista pasada y viceversa
    """
    encontrado = False
    for opcion in opciones:
        if opcion == opcion_elegida:
            encontrado = True
            break
    return encontrado

def verificar_opcion_menu(opcion: str) -> bool:
    from Datos.datos_consola import opciones_menu
    return verificar_opcion(opcion, opciones_menu)

def verificar_opcion_respuestas(opcion: str) -> bool:
    from Datos.datos_consola import opciones_respuesta
    return verificar_opcion(opcion, opciones_respuesta)

def verificar_respuesta(pregunta: dict[str,str], respuesta: str) -> bool:
    """ Verifica si la respuesta es correcta

    Argumentos:
        pregunta (dict[str,str]): La pregunta 
        respuesta (str): La respuesta

    Retorna:
        bool: True si es correcta y viceversa
    """
    return respuesta == pregunta["respuesta_correcta"]

def verificar_ganador_perdedor(posicion: int, tablero: tuple[int]) -> bool:
    """ Verifica si ganaste o perdiste

    Argumentos:
        posicion (int): La posicion del jugador
        tablero (tuple[int]): El tablero del juego

    Retorna:
        bool: False si ganaste o perdiste
    """
    retorno = True
    if posicion <= 0:
        print("\nPerdiste... caíste en la casilla 0. :/")
        retorno = False
    elif posicion >= (len(tablero) - 1):
        print("\nFelicidades, ¡Ganaste! <3")
        retorno = False
    return retorno 

def verificar_ganador_perdedor_pygame(posicion: int, tablero: tuple[int]) -> bool:
    """ Verifica si llegaste al limite

    Argumentos:
        posicion (int): La posicion del jugador
        tablero (tuple[int]): El tablero del juego

    Retorna:
        bool: True si ganaste o perdiste
    """
    retorno = False
    if posicion <= 0 or posicion >= (len(tablero) - 1):
        retorno = True
    return retorno 

###################################################################

def ingresar_respuesta(input: callable, verificador: callable) -> str: # No se si puedo importar "Callable", para especificar que tipo de funcion llamar.
    """ Solicita al usuario un input y la valida con una función.

    Argumentos:
        input (callable): Una función que le solicita al usuario
        verificador (callable): Una función que verifica el input

    Retorna:
        str: La respuesta ingresada por el usuario
    """
    respuesta = input()
    while not verificador(respuesta):
        print("Respuesta no valida, vuelva a intentar...")
        respuesta = input()
    return respuesta

def preguntar_salir() -> bool:
    """ Pregunta si queres seguir jugando

    Retorna:
        bool: True si queres seguir y viceversa
    """
    respuesta = ingresar_respuesta(preguntar_seguir, verificar_seguir)
    return respuesta == "si"

def ingresar_respuesta_menu() -> str:
    return ingresar_respuesta(consultar_opcion, verificar_opcion_menu)

###################################################################

def mostrar_pregunta(pregunta: dict[str, str]) -> None:
    """ Muestra la pregunta y sus opciones

    Argumentos:
        pregunta (dict[str, str]): Pregunta a mostrar
    """
    print(f"\n{pregunta['pregunta']}")
    print(f"Opcion a: {pregunta['respuesta_a']}")
    print(f"Opcion b: {pregunta['respuesta_b']}")
    print(f"Opcion c: {pregunta['respuesta_c']}")

def retirar_pregunta(preguntas: list[dict[str, str]], indice_pregunta: int) -> dict[str, str]:
    """ Retira una pregunta

    Argumentos:
        preguntas (list[dict[str, str]]): La lista de preguntas
        indice_pregunta (int): El indice de la pregunta

    Retorna:
        dict[str, str]: La pregunta eliminada (por si las dudas)
    """
    return preguntas.pop(indice_pregunta)

###################################################################

def mostrar_menu() -> None:
    """ Muestra el menú """
    print("\n----- Bienvenido a Serpientes y escaleras -----")
    print("1. Jugar")
    print("2. Ver puntajes")
    print("3. Salir")
    print("4. Jugar versión Pygame")

def imprimir_lineas() -> None:
    """ Imprime una linea """
    print(f"\n{"-" * 50}")

###################################################################

def limitar_posicion(posicion: int, tablero: tuple[int]) -> int:
    """Asegura que la posición se mantenga dentro del rango del tablero."""
    if posicion < 0:
        posicion = 0
    elif posicion >= len(tablero):
        posicion = len(tablero) - 1
    return posicion

def mover_por_respuesta(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Avanza o retrocede en base a la respuesta

    Argumentos:
        posicion (int): Posición actual del jugador.
        respuesta_verificada (bool): True si respondió bien y viceversa
        largo_tablero (int): Longitud total del tablero.

    Retorna:
        int: Nueva posición
    """
    if respuesta_verificada:
        posicion += 1
    else:
        posicion -= 1
    return limitar_posicion(posicion, tablero)

def aplicar_efecto_casilla(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Aplica escalera o serpiente (solo si es necesario).

    Argumentos:
        tablero (tuple[int]): EL tablero con efectos.
        posicion (int): Posición actual del jugador.
        respuesta_verificada (bool): True si respondió bien y viceversa

    Retorna:
        int: Nueva posición con efecto (si es necesario)
    """
    casilla = tablero[posicion]

    if casilla != 0:
        if respuesta_verificada:
            posicion += casilla
        else:
            posicion -= casilla
    return limitar_posicion(posicion, tablero)

def modificar_posicion(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Modifica la posición y si hay, el efecto de la casilla

    Argumentos:
        tablero (tuple[int]): El tablero del juego
        posicion (int): Posición actual del usuario
        respuesta_verificada (bool): True en caso de responder bien y viceversa

    Retorna:
        int: La posición modificada
    """
    posicion = mover_por_respuesta(tablero, posicion, respuesta_verificada)
    posicion = aplicar_efecto_casilla(tablero, posicion, respuesta_verificada)
    return posicion

def mostrar_tablero(tablero: tuple[int], posicion: int) -> None:
    """ Muestra el tablero 

    Argumentos:
        tablero (tuple[int]): El tablero a mostrar
        posicion (int): La posición actual del jugador
    """
    print("\n----- TABLERO -----\n")
    for i in range(len(tablero)):
        casillero = ""
        if i == posicion:
            casillero += "[X]"  
        elif tablero[i] != 0:
            casillero += f"[{tablero[i]}]"
        else:
            casillero += "[ ]"

        print(f"{i} : {casillero}", end="  ")
        if (i + 1) % 5 == 0: # Para que se vea como un cuadrado en pantalla
            print(end = "\n")
    print(end = "\n") # Ya sé que sería lo mismo que no poner nada

###################################################################

def ingresar_datos_usuario(path, nombre: str, puntaje: int) -> None:
    """ Ingresa los datos del usuario al archivo

    Argumentos:
        path (_type_): Path del archivo
        nombre (str): Nombre del usuario
        puntaje (int): Puntaje del usuario
    """
    try:
        with open(path, "a", encoding = "UTF-8") as archivo:
            archivo.write(f"{nombre},{puntaje}\n")
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")

def parser_csv(path) -> list[dict]:
    """ Guarda los datos del archivo en un diccionario

    Argumentos:
        path (_type_): Ruta del archivo csv

    Retorna:
        list: Lista con diccionarios de nombre y puntajes de los jugadores
    """
    lista = []
    try:
        with open(path, "r", encoding = "UTF-8") as archivo:
            for linea in archivo:
                persona = {}
                lectura = linea.split(",")
                persona['nombre'] = lectura[0]
                persona['puntaje'] = int(lectura[1])
                lista.append(persona)
    except FileNotFoundError:
        print("No hay puntajes guardados")
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")

    return lista

def ordenar_usuarios_descendente(lista_csv: list[dict], criterio: str = 'puntaje') -> list[dict]:
    """ Ordena la lista de jugadores de mayor a menor por criterio

    Argumentos:
        lista_csv (list[dict]): Lista de jugadores

    Retorna:
        list[dict]: Copia de la lista pero ordenada.
    """
    import copy
    csv_copia = copy.deepcopy(lista_csv)
    for i in range(len(csv_copia) - 1):
        for j in range(i + 1, len(csv_copia)):
            if csv_copia[i][criterio] < csv_copia[j][criterio]:
                aux = csv_copia[i]
                csv_copia[i] = csv_copia[j]
                csv_copia[j] = aux
    return csv_copia

def mostrar_usuarios_ordenados(usuarios_ordenados: list[dict]) -> None:
    """ Muesra los usuarios ordenados

    Argumentos:
        usuarios_ordenados (list[dict]): Lista ordenada de usuarios
    """
    if len(usuarios_ordenados) > 0:
        print("\n----- JUGADORES ORDENADOS -----")
        for i in range(len(usuarios_ordenados)):
            print(f"{i+1}° | Usuario: {usuarios_ordenados[i]['nombre']} | Puntaje: {usuarios_ordenados[i]['puntaje']}")
    else:
        print("\n----- No hay jugadores -----")

def mostrar_puntajes(path) -> None:
    """ Muestra los puntajes ordenados y decorado

    Argumentos:
        path (_type_): Path del archivo
    """
    usuarios = parser_csv(path)
    usuarios_ordenados = ordenar_usuarios_descendente(usuarios)
    imprimir_lineas()
    mostrar_usuarios_ordenados(usuarios_ordenados)
    imprimir_lineas()

###################################################################

def mostrar_game_over() -> None:
    """ Muestra game over al usuario en caso de que haya agotado las preguntas"""
    print("\n¡Te quedaste sin preguntas!")
    print("----- GAME OVER -----")

def jugar_en_consola(tablero: tuple[int], preguntas: list[dict[str, str]], path: str) -> None:
    """ Ejecuta el juego

    Argumentos:
        tablero (tuple[int]): El tablero del juego
        preguntas (list[dict[str, str]]): Lista de preguntas
    """
    import random
    import copy
    posicion = 15 # O len(tablero) // 2
    copia_preguntas = copy.deepcopy(preguntas)

    nombre = ingresar_respuesta(consultar_nombre, verificar_nombre)

    seguir = True
    while seguir and len(copia_preguntas) > 0:
        indice = random.randint(0, len(copia_preguntas) - 1) # Me va a generar un numero random entre 0-len(preguntas) (menos 1 porque es una lista)
        pregunta = retirar_pregunta(copia_preguntas, indice)

        mostrar_tablero(tablero, posicion)
        mostrar_pregunta(pregunta)
        respuesta = ingresar_respuesta(consultar_opcion, verificar_opcion_respuestas)
        posicion = modificar_posicion(tablero, posicion, verificar_respuesta(pregunta, respuesta))

        seguir = verificar_ganador_perdedor(posicion, tablero)
        if seguir and len(copia_preguntas) > 0:  
            seguir = preguntar_salir()

    if len(copia_preguntas) == 0:
        mostrar_game_over()

    ingresar_datos_usuario(path, nombre, posicion)

###################################################################

def despedirse() -> bool:
    """ Se despide del usuario

    Retorna:
        bool: False
    """
    print("\n¡ Nos vemos !")
    return False
