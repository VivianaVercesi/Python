from colorama import Fore, Style, init
init(autoreset=True)

def mostrar_titulo(texto):
    print(Fore.MAGENTA + Style.BRIGHT + f"\n------------{texto}------------\n")

def mostrar_opcion(opcion):
    print(Fore.CYAN + opcion)
    
def mostrar_item(item):
    print(Fore.BLACK + item)

def mostrar_exito(mensaje):
    print(Fore.GREEN + Style.BRIGHT + mensaje)

def mostrar_error(mensaje):
    print(Fore.RED + Style.BRIGHT + mensaje)
    
def mostrar_aviso(mensaje):
    print(Fore.YELLOW + Style.BRIGHT + mensaje)
    

        
def mostrar_menu():
    mostrar_titulo("MENÚ DE PRODUCTOS")
    mostrar_opcion("1. Agregar producto")
    mostrar_opcion("2. Ver productos")
    mostrar_opcion("3. Buscar producto")
    mostrar_opcion("4. Eliminar producto")
    mostrar_opcion("5. Modificar producto")
    mostrar_opcion("6. Salir")


    