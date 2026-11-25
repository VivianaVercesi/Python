from database.conexion import crear_tabla

from modules.productos import obtener_productos, agregar_producto, listar_productos, buscar_producto, eliminar_producto, modificar_producto 

from modules.validaciones import validar_texto, validar_precio, validar_entero_positivo

from modules.vista import mostrar_titulo, mostrar_menu, mostrar_opcion, mostrar_item, mostrar_exito, mostrar_aviso, mostrar_error



productos = []

while True:
        #Menú
        
        mostrar_menu()
        
        opcion = input("\nIngrese una opción (1-6): ").strip()

        #Agregar productos
        if opcion == "1":
                print("Seleccionó agregar producto.")
                while True:
                        print("\nIngrese los datos del producto (salir para finalizar).")
                        nombre = input("Nombre del producto: ").strip().lower()
                        if nombre.lower() == "salir":
                                break  
                        while not validar_texto(nombre):
                                mostrar_error("El nombre del producto no puede estar vacío.") 
                                nombre = input("Nombre del producto: ").strip().lower()
                                
                        categoria = input("Categoría: ").strip().lower()
                        while not validar_texto(categoria):
                                mostrar_error("La categoría del producto no puede estar vacía.")
                                categoria = input("Categoría: ").strip().lower()
                                
                        precio = input("Precio: ").strip()
                        while not validar_precio(precio):
                                mostrar_error("El precio debe ser un número mayor a cero.") 
                                precio = input("Precio: ").strip()
                        
                        agregar_producto(nombre, categoria, float(precio))
                        
                listar_productos()

        #Ver listado de productos
        elif opcion == "2":
                print("\nSeleccionó ver productos.")
                listar_productos()
                
        #Buscar un producto
        elif opcion == "3":
                print("\nSeleccionó buscar producto.")
                productos = obtener_productos()
                while True:
                        if not productos: 
                                mostrar_aviso("\nAún no hay productos cargados en el sistema")
                        else:
                                producto_buscado = input("\nIngrese el nombre del producto a buscar (salir para finalizar): ").strip().lower()
                                if producto_buscado.lower() == "salir":
                                        break  
                                else:
                                        buscar_producto(producto_buscado)
                                

        #Eliminar un producto
        elif opcion == "4":
                print("\nSeleccionó eliminar producto:")
                listar_productos()
                while True:
                        eliminar = input("\nIngrese el número del producto a eliminar (o salir para terminar): ").strip()
                        
                        if eliminar.lower() == "salir":
                                                        break
                        
                        while not validar_entero_positivo(eliminar):
                                mostrar_error("Debe ingresar un número válido.")
                                continue
                        
                        eliminar = int(eliminar)
                        eliminar_producto(eliminar)
                
                        listar_productos()
        
        #Modificar un producto
        elif opcion == "5":
                print("\nSeleccionó modificar producto:")
                listar_productos()
                while True:
                        modificar = input("\nIngrese el número del producto a modificar (o salir para terminar): ").strip()
                                
                        if modificar.lower() == "salir":
                                                                break
                                
                        while not validar_entero_positivo(modificar):
                                mostrar_error("Debe ingresar un número válido.")
                                continue
                                
                        modificar = int(modificar)
                        modificar_producto(modificar)
                        
                        listar_productos()
                        
        #Salir                
        elif opcion == "6":
                print("\nSeleccionó salir. \nGracias por utilizar el sistema de gestión de inventarios.")
                break
        else:
            print("\nError. Opción incorrecta") 
        
