"""
CERTIFICADOS EN UN SEGUNDO
==========================
Lee la lista de participantes de un evento (participantes.csv) y genera
un certificado personalizado para cada persona, usando plantilla.html.
Al final abre en el navegador una página con todos los certificados.

Cómo usarlo:
    python generar_certificados.py

(Si "python" no funciona en tu computador, usa "py").

Para imprimir o guardar en PDF: abre un certificado y presiona Ctrl + P.
No hay que instalar nada: solo usa módulos que ya vienen con Python.
"""

from pathlib import Path    # Para trabajar con carpetas y archivos
import csv                  # Para leer el archivo de participantes
import webbrowser           # Para abrir el resultado en el navegador
import time                 # Para medir cuánto se demora
from datetime import date   # Para poner la fecha de hoy en el certificado

# ------------------------------------------------------------------
# CONFIGURACIÓN: de dónde leer y dónde guardar
# ------------------------------------------------------------------
ARCHIVO_PARTICIPANTES = Path("participantes.csv")
PLANTILLA = Path("plantilla.html")
CARPETA_SALIDA = Path("certificados")

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha_bonita():
    """Devuelve la fecha de hoy en español, por ejemplo: 24 de noviembre de 2026."""
    hoy = date.today()
    return f"{hoy.day} de {MESES[hoy.month - 1]} de {hoy.year}"


def nombre_de_archivo(nombre):
    """Convierte 'Laura Gómez' en 'Laura_Gómez.html' para guardar el certificado."""
    return nombre.replace(" ", "_") + ".html"


def llenar_plantilla(plantilla, persona):
    """Reemplaza cada {{campo}} de la plantilla por el dato de la persona."""
    texto = plantilla
    for campo, valor in persona.items():
        texto = texto.replace("{{" + campo + "}}", valor)
    return texto.replace("{{fecha}}", fecha_bonita())


def generar():
    """Genera un certificado por cada persona del CSV y una página índice."""
    inicio = time.time()
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    CARPETA_SALIDA.mkdir(exist_ok=True)

    # 1. Leer los participantes
    with open(ARCHIVO_PARTICIPANTES, encoding="utf-8") as f:
        participantes = list(csv.DictReader(f))   # Cada fila es un diccionario

    # 2. Crear un certificado por persona
    enlaces = []
    for persona in participantes:
        archivo = CARPETA_SALIDA / nombre_de_archivo(persona["nombre"])
        archivo.write_text(llenar_plantilla(plantilla, persona), encoding="utf-8")
        enlaces.append(f'<li><a href="{archivo.name}">{persona["nombre"]}</a> · {persona["rol"]}</li>')
        print(f"  Certificado de {persona['nombre']}")

    # 3. Crear una página índice con el enlace a cada certificado con el enlace a cada certificado
    indice = CARPETA_SALIDA / "index.html"
    indice.write_text(
        "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'><title>Certificados</title></head>"
        "<body style='font-family:Arial;margin:40px'>"
        f"<h1>{len(participantes)} certificados generados</h1><ul>{''.join(enlaces)}</ul></body></html>",
        encoding="utf-8",
    )

    segundos = time.time() - inicio
    print(f"\n¡Listo! Generé {len(participantes)} certificados en {segundos:.3f} segundos.")
    print(f"Están en la carpeta '{CARPETA_SALIDA}'. Se abrirá el índice en el navegador.")
    webbrowser.open(indice.resolve().as_uri())    # Abre el índice en el navegador


if __name__ == "__main__":
    print("Generando certificados...\n")
    generar()
