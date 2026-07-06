
import modulo 


def leer_opcion():
  
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("===================================")


def pedir_entero(mensaje):
   
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero válido.")


def opcion_stock_categoria(productos, inventario):
    categoria = input("Ingrese la categoría a consultar: ")
    modulo.stock_categoria(categoria, productos, inventario)


def opcion_buscar_precio(productos, inventario):
    precio_min = pedir_entero("Ingrese el precio mínimo: ")
    precio_max = pedir_entero("Ingrese el precio máximo: ")
    modulo.buscar_precio(precio_min, precio_max, productos, inventario)


def opcion_actualizar_precio(productos):
    continuar = "s"
    while continuar.lower() == "s":
        codigo = input("Ingrese el código del producto: ")

        if modulo.buscar_codigo(codigo, productos):
            nuevo_precio = pedir_entero("Ingrese el nuevo precio: ")
            modulo.actualizar_precio(codigo, nuevo_precio, productos)
            print("Precio actualizado correctamente.")
        else:
            print("Código inexistente")

        continuar = input("¿Desea actualizar otro producto? (s/n): ")


def opcion_agregar_producto(productos, inventario):
    codigo = input("Ingrese el código del producto: ")
    if not modulo.validar_codigo(codigo, productos):
        print("Código inválido o ya existente.")
        return

    nombre = input("Ingrese el nombre del producto: ")
    if not modulo.validar_nombre(nombre):
        print("Nombre inválido.")
        return

    categoria = input("Ingrese la categoría del producto: ")
    if not modulo.validar_categoria(categoria):
        print("Categoría inválida.")
        return

    precio = pedir_entero("Ingrese el precio del producto: ")
    if not modulo.validar_precio(precio):
        print("Precio inválido, debe ser mayor que cero.")
        return

    disponible = input("¿Producto disponible? (s/n): ")
    if not modulo.validar_disponible(disponible):
        print("Opción inválida, debe ingresar 's' o 'n'.")
        return

    stock = pedir_entero("Ingrese el stock: ")
    if not modulo.validar_stock(stock):
        print("Stock inválido, debe ser mayor o igual a cero.")
        return

    vendidos = pedir_entero("Ingrese la cantidad vendida: ")
    if not modulo.validar_vendidos(vendidos):
        print("Cantidad vendida inválida, debe ser mayor o igual a cero.")
        return

    agregado = modulo.agregar_producto(
        codigo, nombre, categoria, precio, disponible,
        stock, vendidos, productos, inventario
    )

    if agregado:
        print("Producto agregado correctamente.")
    else:
        print("El código ya existe, no se pudo agregar el producto.")


def opcion_eliminar_producto(productos, inventario):
    codigo = input("Ingrese el código del producto a eliminar: ")
    if modulo.eliminar_producto(codigo, productos, inventario):
        print("Producto eliminado correctamente.")
    else:
        print("Código inexistente")


def main():
    
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            opcion_stock_categoria(productos, inventario)
        elif opcion == 2:
            opcion_buscar_precio(productos, inventario)
        elif opcion == 3:
            opcion_actualizar_precio(productos)
        elif opcion == 4:
            opcion_agregar_producto(productos, inventario)
        elif opcion == 5:
            opcion_eliminar_producto(productos, inventario)
        elif opcion == 6:
            modulo.mostrar_productos(productos, inventario)
        elif opcion == 7:
            print("Saliendo del sistema... ¡Hasta luego!")


