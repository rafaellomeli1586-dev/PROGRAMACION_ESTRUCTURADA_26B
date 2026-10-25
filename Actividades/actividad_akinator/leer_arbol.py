import json
import sys

ARCHIVO = sys.argv[1] if len(sys.argv) > 1 else "akinator.json"


def imprimir(nodo, prefijo="", etiqueta=""):
    print(etiqueta + (nodo.get("pregunta") or nodo["respuesta"]))
    if "pregunta" in nodo:
        print(prefijo + "├── sí: ", end="")
        imprimir(nodo["si"], prefijo + "│   ")
        print(prefijo + "└── no: ", end="")
        imprimir(nodo["no"], prefijo + "    ")


with open(ARCHIVO, encoding="utf-8") as f:
    imprimir(json.load(f))