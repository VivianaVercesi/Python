"""Requerimientos:

Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada producto sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).OK

Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.OK

Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.OK

Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

Requisitos

Usar listas para almacenar y gestionar los datos. 

Incorporar bucles while y for según corresponda. 

Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.

Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.

Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.

El programa debe continuar funcionando hasta que se elija una opción para salir."""

productos = []

while True:
        #Menú
        
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("\nIngrese una opción (1-5): ").strip()

        #Agregar productos
        if opcion == "1":
                print("Seleccionó agregar producto.")
                while True:
                        print("\nIngrese los datos del producto (salir para finalizar).")
                        nombre = input("Nombre del producto: ").strip()
                        if nombre.lower() == "salir":
                                break  
                        while nombre == "" or not nombre.isalpha():
                                if nombre == "":
                                        print("El nombre del producto no puede estar vacío.")
                                else: 
                                        print("El nombre ingresado no es válido. Sólo se permiten letras.") 
                                nombre = input("Nombre del producto: ").strip()
                                
                                continue
                        categoria = input("Categoría: ").strip()
                        while categoria == "" or not categoria.isalpha():
                                if categoria == "":
                                        print("La categoría del producto no puede estar vacía.")
                                else: 
                                        print("La categoría ingresada no es válida. Sólo se permite letras") 
                                categoria = input("Categoría: ").strip()
                                
                        precio = input("Precio (sin centavos): ").strip()
                        while precio == "" or not precio.isdigit():
                                if precio == "":
                                       print("Debe ingresar un valor para el precio")
                                else:
                                       print("El precio debe ser un número entero válido") 
                                precio = input("Precio (sin centavos): ").strip()
                        
                        producto = [nombre, categoria, int(precio)]
                        productos.append(producto)
                        print(f"\n¡Producto '{nombre}' agregado correctamente!")
                        
                print("\n---   Listado de Productos   ---")
                for i,producto in enumerate(productos, start = 1):
                        print(f"#{i}- Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")

        #Ver listado de productos
        elif opcion == "2":
                print("\nSeleccionó ver productos.")
                if not productos: 
                        print("Aún no hay productos cargados en el sistema.")
                else:
                        print("\n---   Listado de Productos   ---")
                        for i,producto in enumerate(productos, start=1):
                                print(f"#{i}- Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
        #Buscar un producto
        elif opcion == "3":
                print("\nSeleccionó buscar producto.")
                while True:
                        if not productos: 
                                print("\nAún no hay productos cargados en el sistema")
                        else:
                                buscar = input("\nIngrese el nombre del producto a buscar (salir para finalizar): ").strip().lower()
                                if buscar.lower() == "salir":
                                        break  
                                for i,producto in enumerate(productos, start=1):
                                        if buscar in producto[0].lower():
                                                print(f"#{i}- Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
                                                break
                                else:
                                        print("El producto buscado no existe en el inventario")
                                

        #Eliminar un producto
        elif opcion == "4":
                print("\nSeleccionó eliminar producto:")
                print("\n---   Listado de Productos   ---")
                for i,producto in enumerate(productos, start=1):
                        print(f"#{i}- Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
                while True:
                        eliminar = input("\nIngrese el número del producto a eliminar (o salir para terminar): ").strip()
                        
                        if eliminar.lower() == "salir":
                                                        break
                        
                        if not eliminar.isdigit():
                                print("Debe ingresar un número válido.")
                                continue
                        
                        eliminar = int(eliminar)
                        
                        if eliminar < 1 or eliminar > len(productos):
                                "No existe un producto con ese número."        
                                continue
                        
                        producto_eliminado = productos.pop(eliminar-1) 
                        print(f"\nEl producto '{eliminar}' fue eliminado correctamente.")
                
                print("\n---   Listado de Productos   ---")
                for i,producto in enumerate(productos, start=1):
                        print(f"#{i}- Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
                        
        #Salir                
        elif opcion == "5":
                print("\nSeleccionó salir. \nGracias por utilizar el sistema de gestión de inventarios.")
                break
        else:
            print("\nError. Opción incorrecta") 
        