import pygame


def dibujar_texto_multilinea(superficie, texto, fuente, color, x, y, max_ancho, interlineado=5):
    """Dibuja texto con salto de línea automático con ancho máximo."""
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba = (linea_actual + " " + palabra).strip()
        if fuente.size(prueba)[0] <= max_ancho:
            linea_actual = prueba
        else:
            if linea_actual:
                lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    for linea in lineas:
        render = fuente.render(linea, True, color)
        superficie.blit(render, (x, y))
        y += render.get_height() + interlineado


def dibujar_texto_en_rect(superficie, texto, fuente, color, rect, margen=10, interlineado=4):
    """
    Dibuja texto multilínea dentro de un rect (para las opciones A/B/C/D),
    respetando los márgenes para que no se salga de la caja.
    """
    max_ancho = rect.width - 2 * margen
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba = (linea_actual + " " + palabra).strip()
        if fuente.size(prueba)[0] <= max_ancho:
            linea_actual = prueba
        else:
            if linea_actual:
                lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    y = rect.y + margen
    for linea in lineas:
        render = fuente.render(linea, True, color)
        superficie.blit(render, (rect.x + margen, y))
        y += render.get_height() + interlineado
