def validar_texto(texto):
    return texto != ""

def validar_precio(precio):
    try:
        return float(precio) > 0
    except ValueError:
        return False

def validar_entero_positivo(numero):
    return numero.isdigit() and int(numero)>0