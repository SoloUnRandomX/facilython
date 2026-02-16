import tokenize
import io

def bootstrap(archivo):
    # Diccionario de traducción
    MAPEO = {
        "si": "if",
        "sino": "else",
        "imprimir": "print",
        "mientras": "while",
        "para": "for",
        "en": "in",
        "definir": "def",
        "retornar": "return"
    }

    with open(archivo, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        resultado = []

        for type, val, _, _, _ in tokens:
            # Solo reemplazamos si es un nombre y está en nuestro mapa
            if type == tokenize.NAME and val in MAPEO:
                resultado.append((type, MAPEO[val]))
            else:
                resultado.append((type, val))

    # Convertimos los tokens de vuelta a código string
    codigo_final = tokenize.untokenize(resultado)
    
    # Ejecutamos el código en el contexto global
    exec(codigo_final, {"__name__": "__main__"})

if __name__ == "__main__":
    bootstrap("main.py")
