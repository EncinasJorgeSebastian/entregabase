import sqlite3


ruta_db = r"C:\Users\Seba\Desktop\entregafinal\inventario.db"


def db_crear_tabla_productos():
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )"""
        )
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()


def db_insertar_producto(producto):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?,?,?,?,?)"
    placeholders = (
        producto["nombre"],
        producto["descripcion"],
        producto["categoria"],
        producto["cantidad"],
        producto["precio"],
    )
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()

def db_get_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()  
    conexion.close()
    return lista_productos

def db_get_producto_by_id(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()
    conexion.close()
    return producto


def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


def db_eliminar_producto(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos