import sqlite3

#Ruta de la base de datos
RUTA_DB = "database/inventario.db"

def conectar():
    try:
        conexion = sqlite3.connect(RUTA_DB)
        return conexion
    except sqlite3.Error as error:
        print(f"Error de conexión: {error}")
        return None

def crear_tabla():
    conexion = conectar()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS productos(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nombre TEXT NOT NULL,
                               categoria TEXT NOT NULL,
                               precio INTEGER NOT NULL)
                           ''')
            conexion.commit()
            print("Tabla productos creada correctamente")
        except sqlite3.Error as error:
            print(f"Error al crear la tabla: {error}")
        finally:
            conexion.close()        
            
if __name__ == "__main__":
    crear_tabla()