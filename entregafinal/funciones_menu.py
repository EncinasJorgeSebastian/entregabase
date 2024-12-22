from funciones_database import *


def menu_mostrar_opciones():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")
    return opcion



def menu_registrar_producto():
    print("\nIngrese los siguientes datos del producto:")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    # Creamos un diccionario temporal
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insertar_producto(producto)
    print("\nProducto insertado exitosamente")




def menu_mostrar_productos():
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos que mostrar")



def menu_actualizar_producto():
    id = int(input("\nIngrese el id del producto a actualizar"))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        nueva_cantidad = int(input(f"Cantidad actual {get_producto[4]} - Nueva cantidad: "))
        db_actualizar_producto(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")




def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print("Registro eliminado exitosamente!")
        else:
            print("Operación cancelada.")




def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)




def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)