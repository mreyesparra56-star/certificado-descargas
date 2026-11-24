# Certificados para un Evento

Lee la lista de participantes de un evento (`participantes.csv`) y genera **un certificado personalizado para cada persona** en segundos. Al final abre en el navegador una página con todos los certificados.

> Este README es el punto de partida. Mejorarlo es uno de los issues del equipo.

## Cómo usarlo

Solo necesitas Python. No hay que instalar nada, ni crear un entorno virtual.

```
python generar_certificados.py
```

Si `python` no funciona en tu computador, usa `py`.

Los certificados quedan en la carpeta `certificados`. Para imprimir uno o guardarlo en PDF, ábrelo y presiona **Ctrl + P**.

## Los tres archivos del proyecto

| Archivo | Qué es | Quién lo cambia |
|---|---|---|
| `participantes.csv` | Miguelangel Reyes, Miguel Arenas, Samuelombis Lopombis, Jetbe | Los organizadores del evento |
| `plantilla.html` | El diseño del certificado. Las palabras entre `{{ }}` se reemplazan por los datos de cada persona | El diseñador |
| `generar_certificados.py` | [Ejemplo de certificado generado ](assets/certificado-ejemplo.png) | El programador |

Así trabajan las automatizaciones reales: **los datos, el diseño y el código van separados**. Se puede cambiar la lista o el diseño sin tocar el código.

## Lo que vas a aprender con este script

| Concepto | Dónde está en el código | Qué hace |
|---|---|---|
| **Variable** | `PLANTILLA = Path("plantilla.html")` | Guarda un dato para usarlo después |
| **Lista** | `MESES = ["enero", "febrero", ...]` | Guarda varios valores en orden |
| **Diccionario** | `persona["nombre"]` | Cada fila del CSV es un diccionario: columna → valor |
| **Función** | `def llenar_plantilla(plantilla, persona):` | Un bloque de código con nombre, que se puede usar muchas veces |
| **Ciclo `for`** | `for persona in participantes:` | Repite lo mismo con cada persona de la lista |
| **Reemplazar texto** | `texto.replace("{{nombre}}", valor)` | Cambia una parte de un texto por otra |
| **Módulos** | `import csv`, `import webbrowser` | Herramientas que ya trae Python: leer el CSV y abrir el navegador |
| **f-string** | `f"Generé {len(participantes)} certificados"` | Arma un texto con valores adentro |

## Cómo está organizado el código

1. **Configuración** (arriba): de dónde se leen los datos y la plantilla, y dónde se guardan los certificados.
2. **`fecha_bonita()`**: escribe la fecha de hoy en español.
3. **`nombre_de_archivo()`**: convierte el nombre de la persona en un nombre de archivo.
4. **`llenar_plantilla()`**: reemplaza cada `{{campo}}` por el dato de la persona.
5. **`generar()`**: lee el CSV, crea un certificado por persona y la página índice, y mide cuánto se demoró.
6. **`if __name__ == "__main__":`**: lo que se ejecuta cuando corres `python generar_certificados.py`.
