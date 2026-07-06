

def _buscar_llave_real(codigo, productos):
    
    codigo_normalizado = codigo.strip().lower()
    for llave in productos:
        if llave.strip().lower() == codigo_normalizado:
            return llave
    return None


def validar_codigo(codigo, productos):
   
    if not isinstance(codigo, str) or codigo.strip() == "":
        return False
    if _buscar_llave_real(codigo, productos) is not None:
        return False
    return True


def validar_nombre(nombre):
    if not isinstance(nombre, str) or nombre.strip() == "":
        return False
    return True


def validar_categoria(categoria):
    if not isinstance(categoria, str) or categoria.strip() == "":
        return False
    return True


def validar_precio(precio):
 
    try:
        return int(precio) > 0
    except (ValueError):
        return False


def validar_disponible(opcion):
    
    if not isinstance(opcion, str):
        return False
    return opcion.strip().lower() in ("s", "n")


def validar_stock(stock):
    try:
        return int(stock) >= 0
    except (ValueError, TypeError):
        return False


def validar_vendidos(vendidos):
    try:
        return int(vendidos) >= 0
    except (ValueError, TypeError):
        return False



def buscar_codigo(codigo, productos):
 
    return _buscar_llave_real(codigo, productos) is not None


def stock_categoria(categoria, productos, inventario):
   
    categoria_normalizada = categoria.strip().lower()
    total = 0
    encontrados = False

    for codigo, datos in productos.items():
        cat_producto = datos[1]
        if cat_producto.strip().lower() == categoria_normalizada:
            encontrados = True
            stock_producto = inventario[codigo][0]
            total += stock_producto

    if encontrados:
        print(f"Stock total para la categoría '{categoria}': {total}")
    else:
        print(f"No existen productos en la categoría '{categoria}'.")


def buscar_precio(precio_min, precio_max, productos, inventario):
   
    resultados = []

    for codigo, datos in productos.items():
        nombre = datos[0]
        precio = datos[2]
        stock_producto = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock_producto > 0:
            resultados.append((nombre, codigo))

    resultados.sort(key=lambda tupla: tupla[0].lower())

    if resultados:
        for nombre, codigo in resultados:
            print(f"{nombre}--{codigo}")
    else:
        print("No hay productos disponibles en ese rango de precio.")


def actualizar_precio(codigo, nuevo_precio, productos):
 
    llave_real = _buscar_llave_real(codigo, productos)
    if llave_real is None:
        return False
    productos[llave_real][2] = nuevo_precio
    return True


def agregar_producto(codigo, nombre, categoria, precio, disponible,
                      stock, vendidos, productos, inventario):
    
    if _buscar_llave_real(codigo, productos) is not None:
        return False

    disponible_bool = disponible.strip().lower() == "s"

    productos[codigo] = [nombre, categoria, precio, disponible_bool]
    inventario[codigo] = [stock, vendidos]
    return True


def eliminar_producto(codigo, productos, inventario):
   
    llave_real = _buscar_llave_real(codigo, productos)
    if llave_real is None:
        return False

    del productos[llave_real]
    del inventario[llave_real]
    return True


def mostrar_productos(productos, inventario):
   
    if not productos:
        print("No hay productos registrados.")
        return

    for codigo, datos in productos.items():
        nombre, categoria, precio, disponible = datos
        stock_producto, vendidos = inventario[codigo]

        print(f"CODIGO: {codigo}")
        print("--------------------------")
        print(f"Nombre: {nombre}")
        print(f"Categoría: {categoria}")
        print(f"Precio: ${precio}")
        print(f"Disponible: {disponible}")
        print(f"Stock: {stock_producto}")
        print(f"Vendidos: {vendidos}")
        print("--------------------------")