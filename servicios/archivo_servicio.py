import json
from pathlib import Path

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta):
        ruta = Path(ruta)
        with ruta.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
