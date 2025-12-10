import pygame
import sys
import random

# -------------------------
# PREGUNTAS ORIGINALES
# -------------------------
preguntas = [
    {
        "pregunta": "Un pueblo donde lo inexplicable se esconde detrás de luces parpadeantes.",
        "opciones": {
            "A": "Dark",
            "B": "Stranger Things",
            "C": "The OA",
            "D": "Glitch"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Una decisión lo cambia todo… y cada elección abre un camino distinto.",
        "opciones": {
            "A": "Black Mirror",
            "B": "Bandersnatch",
            "C": "Russian Doll",
            "D": "Maniac"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "El crimen perfecto puede nacer detrás de una máscara roja.",
        "opciones": {
            "A": "Elite",
            "B": "La Casa de Papel",
            "C": "Toy Boy",
            "D": "Lupin"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Un grupo de adolescentes y un tesoro legendario cambian para siempre un verano.",
        "opciones": {
            "A": "The Society",
            "B": "Outer Banks",
            "C": "Locke & Key",
            "D": "Everything Sucks"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Un inspector elegante que roba solo lo que considera justo.",
        "opciones": {
            "A": "You",
            "B": "Lupin",
            "C": "Narcos: México",
            "D": "Clickbait"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Un ajedrez emocional donde cada movimiento la acerca a la grandeza… o a su caída.",
        "opciones": {
            "A": "El Buen Pastor",
            "B": "La Chica del Ajedrez",
            "C": "Gambito de Dama",
            "D": "Prodigy"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una familia descubre que las paredes de su nueva casa esconden más que recuerdos.",
        "opciones": {
            "A": "Locke & Key",
            "B": "The Haunting of Bly Manor",
            "C": "Slasher",
            "D": "You"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Un agente del FBI entrevista a monstruos para atrapar a otros monstruos.",
        "opciones": {
            "A": "Hannibal",
            "B": "Mindhunter",
            "C": "Dahmer",
            "D": "Seven"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Una historia real donde el vecino amable resulta ser todo lo contrario.",
        "opciones": {
            "A": "Into the Night",
            "B": "You",
            "C": "Dahmer",
            "D": "Dirty John"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una carta misteriosa puede cambiar la vida de una adolescente invisible.",
        "opciones": {
            "A": "Love, Rosie",
            "B": "The Perfect Date",
            "C": "A todos los chicos de los que me enamoré",
            "D": "Heartstopper"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una prisión donde sobrevivir es el mayor acto de ingeniería humana.",
        "opciones": {
            "A": "Vis a Vis",
            "B": "The Platform (El Hoyo)",
            "C": "Snowpiercer",
            "D": "The Punisher"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Un chef callejero encuentra una nueva receta para su vida.",
        "opciones": {
            "A": "Chef's Table",
            "B": "Street Food",
            "C": "Chef",
            "D": "El Sabor de las Cosas"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Un viaje en tren donde cada minuto importa para sobrevivir.",
        "opciones": {
            "A": "Snowpiercer",
            "B": "Into the Night",
            "C": "Bird Box",
            "D": "Awake"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Una competencia mortal donde cientos de personas aceptan jugar por dinero, aun sabiendo que perder significa morir.",
        "opciones": {
            "A": "The 3%",
            "B": "El Juego del Calamar",
            "C": "Alice in Borderland",
            "D": "Sweet Home"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Una expedición para descubrir la verdad detrás del monstruo más famoso del mundo.",
        "opciones": {
            "A": "Godzilla",
            "B": "Colossal",
            "C": "Enola Holmes 2",
            "D": "Enola Holmes"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Una madre hará lo imposible para recuperar a su hijo desaparecido tras un extraño accidente.",
        "opciones": {
            "A": "Fractured",
            "B": "The Guilty",
            "C": "El Hoyo",
            "D": "The Mother"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Un misterioso agujero vertical decide el destino de quienes viven dentro de él.",
        "opciones": {
            "A": "Cadáver",
            "B": "Cargo",
            "C": "El Hoyo",
            "D": "Ánimas"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Un hombre despierta en una habitación sin recordar nada… excepto que debe escapar.",
        "opciones": {
            "A": "Forgotten",
            "B": "Circle",
            "C": "ELI",
            "D": "Tau"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Un grupo de adolescentes ricos se pasan el día bebiendo y drogándose.",
        "opciones": {
            "A": "Newness",
            "B": "Closer",
            "C": "Black Mirror",
            "D": "Elite"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Un ladrón rompe todas las reglas para demostrar que nadie puede atraparlo, ni siquiera el mejor agente del FBI.",
        "opciones": {
            "A": "Red Notice",
            "B": "6 Underground",
            "C": "Triple Frontera",
            "D": "El Asalto"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Una misión suicida en Las Vegas antes de que la ciudad se convierta por completo en un infierno.",
        "opciones": {
            "A": "Alive",
            "B": "Army of the Dead",
            "C": "Day of the Dead",
            "D": "Cargo"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Una madre guarda un terrible secreto mientras intenta mantener a su hija a salvo.",
        "opciones": {
            "A": "Bird Box",
            "B": "The Unforgivable",
            "C": "The Perfection",
            "D": "The Mother"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Un músico frustrado encuentra una nueva vida cuando un milagro musical ocurre en su barrio.",
        "opciones": {
            "A": "Tick, Tick… Boom!",
            "B": "Eurovision",
            "C": "Vivo",
            "D": "The Dirt"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Una simple foto desencadena una historia de amor que viaja en el tiempo.",
        "opciones": {
            "A": "Your Name",
            "B": "La Fotografía",
            "C": "Alguien Especial",
            "D": "La Última Carta de Amor"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Un grupo de ladrones expertos quiere demostrar que incluso la obra más vigilada del mundo puede desaparecer.",
        "opciones": {
            "A": "The Italian Job",
            "B": "Now You See Me",
            "C": "Army of Thieves",
            "D": "Triple Frontier"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Un músico ciego se convierte en el objetivo de una trama criminal que nunca vio venir.",
        "opciones": {
            "A": "A Perfect Fit",
            "B": "Hush",
            "C": "Andhadhun",
            "D": "Forgotten"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una niña descubre que sus poderes no son una maldición, sino su mejor arma contra la injusticia.",
        "opciones": {
            "A": "Enola Holmes",
            "B": "Nimona",
            "C": "Matilda (2022)",
            "D": "The School for Good and Evil"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una joven descubre que su vida normal esconde poderes que nunca imaginó.",
        "opciones": {
            "A": "The Innocents",
            "B": "Shadow and Bone",
            "C": "The OA",
            "D": "Fate: The Winx Saga"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Un club de forenses adolescentes resuelve crímenes más rápido que la policía.",
        "opciones": {
            "A": "Élite",
            "B": "On My Block",
            "C": "Los Misterios de Frankie Drake",
            "D": "The Irregulars"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Una familia se muda a un pueblo aparentemente tranquilo… hasta que empiezan los rituales.",
        "opciones": {
            "A": "The Society",
            "B": "Archive 81",
            "C": "Bienvenidos a Edén",
            "D": "Hemlock Grove"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Un profesor aburrido se convierte en el criminal más buscado del país.",
        "opciones": {
            "A": "Narcos",
            "B": "Better Call Saul",
            "C": "You",
            "D": "Breaking Bad"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "Tres hermanos heredan una llave que abre puertas… y secretos peligrosos.",
        "opciones": {
            "A": "Locke & Key",
            "B": "The Haunting of Hill House",
            "C": "Stranger Things",
            "D": "The Order"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "El fin del mundo empieza con un virus que transforma a los estudiantes en monstruos.",
        "opciones": {
            "A": "Sweet Home",
            "B": "Kingdom",
            "C": "All of Us Are Dead",
            "D": "Z Nation"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Un asesino inteligente deja acertijos imposibles para los agentes del FBI.",
        "opciones": {
            "A": "Luther",
            "B": "Mindhunter",
            "C": "Manhunt: Unabomber",
            "D": "You"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Una familia ve cómo su vida perfecta se derrumba cuando una hermana desaparece.",
        "opciones": {
            "A": "Safe",
            "B": "The Stranger",
            "C": "Black Earth Rising",
            "D": "Glitch"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Una joven desaparece y las visiones del más allá podrían ser la clave para resolver el caso.",
        "opciones": {
            "A": "Ghost Whisperer",
            "B": "The OA",
            "C": "El Reino de los Espíritus",
            "D": "La Chica de la Nieve"
        },
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "Un hacker anónimo pone al mundo en alerta con filtraciones que muestran la verdad que nadie quiere ver.",
        "opciones": {
            "A": "Who Killed Sara?",
            "B": "The Feed",
            "C": "Mr. Robot",
            "D": "Control Z"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Un joven aparentemente encantador esconde una obsesión peligrosa que lo lleva a vigilancias y crímenes.",
        "opciones": {
            "A": "You",
            "B": "Younger",
            "C": "You Me Her",
            "D": "Elite"
        },
        "respuesta_correcta": "A"
    }
]

# -------------------------
# CONFIGURACIÓN PYGAME
# -------------------------
pygame.init()
ANCHO = 900
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trivial Netflix - Pygame")

# Colores estilo Netflix
NEGRO = (0, 0, 0)
ROJO_NETFLIX = (229, 9, 20)
GRIS_OSCURO = (15, 15, 15)
GRIS_BOTON = (40, 40, 40)
GRIS_BOTON_HOVER = (80, 80, 80)
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)

FUENTE_TITULO = pygame.font.SysFont("arial", 40, bold=True)
FUENTE_TEXTO = pygame.font.SysFont("arial", 24)
FUENTE_PEQUE = pygame.font.SysFont("arial", 18)


def dibujar_texto_multilinea(superficie, texto, fuente, color, x, y, max_ancho, interlineado=5):
    """Dibuja texto con salto de línea automático."""
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba = linea_actual + palabra + " "
        if fuente.size(prueba)[0] <= max_ancho:
            linea_actual = prueba
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + " "
    if linea_actual:
        lineas.append(linea_actual)

    for linea in lineas:
        render = fuente.render(linea, True, color)
        superficie.blit(render, (x, y))
        y += render.get_height() + interlineado


def crear_botones_opciones():
    """Crea 4 botones para A, B, C, D."""
    botones = []
    ancho_boton = 380
    alto_boton = 60
    margen_x = 60
    margen_y_inicial = 260
    separacion_y = 80

    for fila in range(2):  # 2 filas
        for col in range(2):  # 2 columnas
            x = margen_x + col * (ancho_boton + 40)
            y = margen_y_inicial + fila * separacion_y
            rect = pygame.Rect(x, y, ancho_boton, alto_boton)
            botones.append(rect)

    return botones


def juego():
    reloj = pygame.time.Clock()
    botones = crear_botones_opciones()

    # Estados: "INICIO", "INTRO_NOMBRE", "INTRO_NUM", "PREGUNTA", "FEEDBACK", "GAME_OVER"
    estado = "INICIO"

    nombre_jugador = ""
    texto_input = ""  # reutilizable para nombre y número de preguntas
    mensaje_error = ""
    num_preguntas = 0

    mazo = []
    indice_pregunta = 0
    puntuacion = 0
    vidas = 3

    # Datos para pantalla de FEEDBACK
    ultima_correcta = False
    letra_correcta = ""
    texto_correcto = ""

    en_ejecucion = True

    def avanzar_pregunta():
        nonlocal indice_pregunta, estado, vidas
        # Si ya no quedan vidas o no hay más preguntas → fin de partida
        if vidas <= 0 or indice_pregunta >= len(mazo) - 1:
            estado = "GAME_OVER"
        else:
            indice_pregunta += 1
            estado = "PREGUNTA"

    while en_ejecucion:
        reloj.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_ejecucion = False

            # ----- TECLADO -----
            if evento.type == pygame.KEYDOWN:
                if estado == "INICIO":
                    if evento.key == pygame.K_RETURN:
                        estado = "INTRO_NOMBRE"

                elif estado in ["INTRO_NOMBRE", "INTRO_NUM"]:
                    if evento.key == pygame.K_BACKSPACE:
                        texto_input = texto_input[:-1]
                    elif evento.key == pygame.K_RETURN:
                        if estado == "INTRO_NOMBRE":
                            if texto_input.strip() == "":
                                mensaje_error = "El nombre no puede estar vacío."
                            else:
                                nombre_jugador = texto_input.strip().title()
                                texto_input = ""
                                mensaje_error = ""
                                estado = "INTRO_NUM"
                        else:  # INTRO_NUM
                            if not texto_input.isdigit():
                                mensaje_error = "Introduce un número entre 5 y 10."
                            else:
                                num = int(texto_input)
                                if num < 5 or num > 10:
                                    mensaje_error = "Elige un número entre 5 y 10."
                                elif num > len(preguntas):
                                    mensaje_error = f"Máximo {len(preguntas)} preguntas."
                                else:
                                    num_preguntas = num
                                    mazo = random.sample(preguntas, num_preguntas)
                                    indice_pregunta = 0
                                    puntuacion = 0
                                    vidas = 3
                                    texto_input = ""
                                    mensaje_error = ""
                                    estado = "PREGUNTA"
                    else:
                        if len(texto_input) < 20:
                            texto_input += evento.unicode

                elif estado == "FEEDBACK":
                    # Cualquier tecla pasa a la siguiente pregunta o al final
                    avanzar_pregunta()

                elif estado == "GAME_OVER":
                    if evento.key == pygame.K_RETURN:
                        # Volver a elegir número de preguntas manteniendo el nombre
                        texto_input = ""
                        mensaje_error = ""
                        estado = "INTRO_NUM"

            # ----- RATÓN -----
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if estado == "PREGUNTA":
                    pos = evento.pos
                    for idx, boton in enumerate(botones):
                        if boton.collidepoint(pos):
                            # Mapear índice a letra
                            letras = ["A", "B", "C", "D"]
                            letra_elegida = letras[idx]
                            pregunta_actual = mazo[indice_pregunta]
                            opciones = pregunta_actual["opciones"]
                            correcta = pregunta_actual["respuesta_correcta"]

                            letra_correcta = correcta
                            texto_correcto = opciones[correcta]

                            if letra_elegida == correcta:
                                puntuacion += 1
                                ultima_correcta = True
                            else:
                                vidas -= 1
                                ultima_correcta = False

                            estado = "FEEDBACK"

                elif estado == "FEEDBACK":
                    # Clic también pasa a la siguiente pregunta
                    avanzar_pregunta()

        # -------------------------
        # DIBUJO DE PANTALLAS
        # -------------------------
        VENTANA.fill(GRIS_OSCURO)

        # Pantalla de INICIO
        if estado == "INICIO":
            titulo = FUENTE_TITULO.render("TRIVIAL NETFLIX", True, ROJO_NETFLIX)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 150))

            subtitulo = FUENTE_TEXTO.render("Adivina la serie o película con una frase absurda.", True, BLANCO)
            VENTANA.blit(subtitulo, (ANCHO // 2 - subtitulo.get_width() // 2, 230))

            texto_inicio = FUENTE_TEXTO.render("Pulsa ENTER para empezar", True, GRIS_CLARO)
            VENTANA.blit(texto_inicio, (ANCHO // 2 - texto_inicio.get_width() // 2, 320))

        elif estado == "INTRO_NOMBRE":
            titulo = FUENTE_TITULO.render("TRIVIAL NETFLIX", True, ROJO_NETFLIX)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 60))

            subtitulo = FUENTE_TEXTO.render("Introduce tu nombre y pulsa ENTER:", True, BLANCO)
            VENTANA.blit(subtitulo, (80, 180))

            caja = pygame.Rect(80, 230, 400, 40)
            pygame.draw.rect(VENTANA, BLANCO, caja, border_radius=5)
            texto_render = FUENTE_TEXTO.render(texto_input, True, NEGRO)
            VENTANA.blit(texto_render, (caja.x + 10, caja.y + 8))

            if mensaje_error:
                error_render = FUENTE_PEQUE.render(mensaje_error, True, ROJO)
                VENTANA.blit(error_render, (80, 290))

        elif estado == "INTRO_NUM":
            titulo = FUENTE_TITULO.render(f"Hola, {nombre_jugador}", True, ROJO_NETFLIX)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 60))

            subtitulo = FUENTE_TEXTO.render("¿Cuántas preguntas quieres jugar? (5-10)", True, BLANCO)
            VENTANA.blit(subtitulo, (80, 180))

            caja = pygame.Rect(80, 230, 200, 40)
            pygame.draw.rect(VENTANA, BLANCO, caja, border_radius=5)
            texto_render = FUENTE_TEXTO.render(texto_input, True, NEGRO)
            VENTANA.blit(texto_render, (caja.x + 10, caja.y + 8))

            if mensaje_error:
                error_render = FUENTE_PEQUE.render(mensaje_error, True, ROJO)
                VENTANA.blit(error_render, (80, 290))

        elif estado == "PREGUNTA":
            pregunta_actual = mazo[indice_pregunta]
            texto_pregunta = pregunta_actual["pregunta"]
            opciones = pregunta_actual["opciones"]

            # Header
            titulo = FUENTE_TITULO.render("TRIVIAL NETFLIX", True, ROJO_NETFLIX)
            VENTANA.blit(titulo, (20, 20))

            info_jugador = FUENTE_PEQUE.render(
                f"Jugador: {nombre_jugador}  |  Puntuación: {puntuacion}  |  Vidas: {vidas}",
                True,
                BLANCO,
            )
            VENTANA.blit(info_jugador, (20, 80))

            num_preg_text = FUENTE_PEQUE.render(
                f"Pregunta {indice_pregunta + 1} de {num_preguntas}",
                True,
                BLANCO,
            )
            VENTANA.blit(num_preg_text, (ANCHO - num_preg_text.get_width() - 20, 80))

            # Pregunta
            dibujar_texto_multilinea(
                VENTANA,
                texto_pregunta,
                FUENTE_TEXTO,
                BLANCO,
                60,
                130,
                max_ancho=ANCHO - 120,
            )

            # Botones de opciones
            letras = ["A", "B", "C", "D"]
            pos_raton = pygame.mouse.get_pos()

            for idx, (letra, opcion) in enumerate(opciones.items()):
                boton = botones[idx]

                # Hover
                if boton.collidepoint(pos_raton):
                    color_boton = GRIS_BOTON_HOVER
                else:
                    color_boton = GRIS_BOTON

                pygame.draw.rect(VENTANA, color_boton, boton, border_radius=8)
                pygame.draw.rect(VENTANA, ROJO_NETFLIX, boton, 2, border_radius=8)

                texto_opcion = f"{letra}) {opcion}"
                render_opcion = FUENTE_TEXTO.render(texto_opcion, True, BLANCO)
                VENTANA.blit(
                    render_opcion,
                    (
                        boton.x + 10,
                        boton.y + (boton.height - render_opcion.get_height()) // 2,
                    ),
                )

            ayuda = FUENTE_PEQUE.render("Haz clic en una opción (A, B, C o D)", True, GRIS_CLARO)
            VENTANA.blit(ayuda, (60, ALTO - 40))

        elif estado == "FEEDBACK":
            VENTANA.fill(NEGRO)

            # Correcto / Incorrecto en grande
            if ultima_correcta:
                texto_grande = "¡CORRECTO!"
                color = VERDE
            else:
                texto_grande = "INCORRECTO"
                color = ROJO

            render_grande = FUENTE_TITULO.render(texto_grande, True, color)
            VENTANA.blit(
                render_grande,
                (ANCHO // 2 - render_grande.get_width() // 2, 150),
            )

            # Respuesta correcta
            texto_resp = f"La respuesta correcta era: {letra_correcta}) {texto_correcto}"
            render_resp = FUENTE_TEXTO.render(texto_resp, True, BLANCO)
            VENTANA.blit(
                render_resp,
                (ANCHO // 2 - render_resp.get_width() // 2, 230),
            )

            # Info de estado
            texto_info = f"Puntuación: {puntuacion}   |   Vidas restantes: {vidas}"
            render_info = FUENTE_TEXTO.render(texto_info, True, GRIS_CLARO)
            VENTANA.blit(
                render_info,
                (ANCHO // 2 - render_info.get_width() // 2, 280),
            )

            texto_cont = FUENTE_PEQUE.render(
                "Pulsa cualquier tecla o haz clic para continuar",
                True,
                GRIS_CLARO,
            )
            VENTANA.blit(
                texto_cont,
                (ANCHO // 2 - texto_cont.get_width() // 2, 340),
            )

        elif estado == "GAME_OVER":
            VENTANA.fill(NEGRO)

            titulo = FUENTE_TITULO.render("Fin de la partida", True, ROJO_NETFLIX)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 80))

            texto1 = FUENTE_TEXTO.render(f"Gracias por jugar, {nombre_jugador}.", True, BLANCO)
            VENTANA.blit(texto1, (ANCHO // 2 - texto1.get_width() // 2, 180))

            texto2 = FUENTE_TEXTO.render(
                f"Has acertado {puntuacion} de {num_preguntas} preguntas.",
                True,
                BLANCO,
            )
            VENTANA.blit(texto2, (ANCHO // 2 - texto2.get_width() // 2, 230))

            if vidas <= 0:
                texto3 = FUENTE_TEXTO.render(
                    "Te has quedado sin vidas.", True, ROJO
                )
                VENTANA.blit(texto3, (ANCHO // 2 - texto3.get_width() // 2, 280))

            texto4 = FUENTE_PEQUE.render(
                "Pulsa ENTER para volver a jugar con el mismo nombre.",
                True,
                GRIS_CLARO,
            )
            VENTANA.blit(texto4, (ANCHO // 2 - texto4.get_width() // 2, 340))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    juego()
