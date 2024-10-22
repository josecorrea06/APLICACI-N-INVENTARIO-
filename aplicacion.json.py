import json
import os

# Nombre del archivo donde se almacenará el inventario
FILENAME = 'inventory.json'


# Cargar inventario desde el archivo JSON
def cargar_inventario():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}


# Guardar inventario en el archivo JSON
def guardar_inventario(inventario):
    with open(FILENAME, 'w') as file:
        json.dump(inventario, file, indent=4)


# Añadir un nuevo producto al inventario
def añadir_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio unitario: "))
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    guardar_inventario(inventario)
    print(f"Producto '{nombre}' añadido exitosamente.")


# Actualizar un producto existente
def actualizar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio unitario: "))
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' actualizado exitosamente.")
    else:
        print("Producto no encontrado.")


# Eliminar un producto del inventario
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print("Producto no encontrado.")


# Mostrar todos los productos en el inventario
def mostrar_inventario(inventario):
    if inventario:
        print("\nInventario:")
        for nombre, detalles in inventario.items():
            print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
    else:
        print("El inventario está vacío.")


# Menú principal
def menu():
    inventario = cargar_inventario()
    while True:
        print("\nSeleccione una opción:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            añadir_producto(inventario)
        elif opcion == '2':
            actualizar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario(inventario)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if  __name__ != "_main_":
    menu()