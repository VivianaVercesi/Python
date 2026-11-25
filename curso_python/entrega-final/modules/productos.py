from database.conexion import conectar
from modules.vista import mostrar_titulo, mostrar_item, mostrar_exito,mostrar_aviso, mostrar_error
from modules.validaciones import validar_texto,validar_precio, validar_entero_positivo

#Agregar un producto a la base de datos
    
def agregar_producto(nombre, categoria, precio):
    
    conexion = conectar()
    
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                           INSERT INTO productos (nombre, categoria, precio)
                           VALUES (?,?,?)
                           ''', (nombre, categoria, precio))
            
            conexion.commit()
            
            mostrar_exito("Producto agregado correctamente")
        
        except Exception as error:
            mostrar_error(f"Error al agregar el producto: {error}")
        
        finally:
            conexion.close()

#Obtener todos los productos de la base de datos

def obtener_productos():
    
    productos = []
    
    conexion = conectar()
    
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                           SELECT id, nombre, categoria, precio
                           FROM productos
                           ORDER BY id
                           ''')
            resultados = cursor.fetchall()
            
            for fila in resultados:
                productos.append(list(fila))
                
            return productos
    
        except Exception as error:
            mostrar_error(f"Error al obtener los productos: {error}")
            return[]
        
        finally:
            conexion.close()
            
    return []

#Mostrar productos

def listar_productos():
    productos = obtener_productos()
    
    if len(productos) == 0:
        mostrar_aviso("No hay productos registrados.")
    else:
        mostrar_titulo("LISTADO DE PRODUCTOS")
        for i,producto in enumerate(productos, start=1):
            mostrar_item(
                f"#: {i}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: ${producto[3]}"
                ) 
    
#Buscar un producto en la base de datos

def buscar_producto(nombre_buscar):
    productos = obtener_productos()
    if len(productos) == 0:
        mostrar_aviso("No hay productos registrados.")
    else:
        producto_encontrado = False
        for producto in productos:
            if nombre_buscar in producto[1].lower():
                print(f"#{producto[0]}- Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: ${producto[3]}")
                producto_encontrado = True        
        if not producto_encontrado:
                    mostrar_aviso("El producto buscado no existe en el inventario")    
        
    
   
    
              
#Eliminar un producto
    
def eliminar_producto(posicion):
    
    productos = obtener_productos()
    
    if posicion < 1 or posicion > len(productos):
        mostrar_aviso("Número de producto inexistente.")
        return
    producto_eliminado = productos[posicion - 1]
    id_producto = producto_eliminado[0]
        
    conexion = conectar()
        
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                            DELETE FROM productos 
                            WHERE id = ?
                        ''', (id_producto,))
                
            conexion.commit()
                
            mostrar_exito(f"Se eliminó el producto: {producto_eliminado[1]}")
            
        except Exception as error:
            conexion.rollback()
            mostrar_error(f"Error al eliminar el producto: {error}")
            
        finally:
            conexion.close()
            
#Modificar los datos de un producto

def modificar_producto(posicion):
    productos = obtener_productos()
        
    if posicion < 1 or posicion > len(productos):
        mostrar_aviso("Número de producto inexistente.")
        return
    producto_modificado = productos[posicion - 1]
    id_producto = producto_modificado[0]
    print("\nProducto seleccionado:")
    mostrar_item(f"Nombre: {producto_modificado[1]}, Categoría: {producto_modificado[2]}, Precio: ${producto_modificado[3]}")
    
    print("\nIngrese los nuevos datos:")
    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()
    precio = input("Nuevo precio: ").strip()
    
    if not validar_texto(nombre) or not validar_texto(categoria):
        mostrar_error("El nombre y la categoría no pueden estar vacíos.")
        return
    if not validar_precio(precio):
        mostrar_error("El precio debe ser un número positivo.")
        return
    precio = float(precio)       
    conexion = conectar()
            
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                                UPDATE productos 
                                SET nombre = ?, categoria = ?, precio = ? 
                                WHERE id = ?
                            ''', (nombre, categoria, precio, id_producto))
                    
            conexion.commit()
                    
            mostrar_exito(f"El producto fue modificado con éxito.")
                
        except Exception as error:
            conexion.rollback()
            mostrar_error(f"Error al modificar el producto: {error}")
                
        finally:
            conexion.close()
                
    
