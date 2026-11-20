import re
from collections import Counter


def contar_palabras(texto):
    """Cuenta las palabras de un texto."""
    return len(texto.strip().split())


def frecuencia_palabras(texto, top=5):
    """Devuelve las palabras más frecuentes, ignorando mayúsculas."""
    if not isinstance(top, int) or top < 1:
        raise ValueError("top debe ser un entero mayor que cero")

    palabras = re.findall(r"\w+", texto.lower())
    return dict(Counter(palabras).most_common(top))


def resumen(texto, max_chars=100):
    """Genera un resumen que no supera max_chars, salvo el indicador '...'."""
    if not isinstance(max_chars, int) or max_chars < 1:
        raise ValueError("max_chars debe ser un entero mayor que cero")

    if len(texto) <= max_chars:
        return texto

    if max_chars <= 3:
        return "." * max_chars

    fragmento = texto[:max_chars - 3]
    if " " in fragmento:
        fragmento = fragmento.rsplit(" ", 1)[0]

    return fragmento.rstrip() + "..."
