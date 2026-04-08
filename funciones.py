# ============================================================
#   Archivo de funciones del carrito de compras
# ============================================================

# ----- CATÁLOGO DE PRODUCTOS DISPONIBLES -----
catalogo = {
    1:  {"nombre": "Portatil",        "precio": 3500000},
    2:  {"nombre": "Table para apuntes digitales",   "precio":   1850000},
    3:  {"nombre": "Audifonos Bluetooth con ANC",    "precio":  220000},
    4:  {"nombre": "Power Bank",        "precio":  50000},
    5:  {"nombre": "Mouse Inalámbrico", "precio":  85000},
    6:  {"nombre": "Webcam HD",           "precio":  130000},
    7:  {"nombre": "Teclado Mecanico",    "precio": 250000},
    8:  {"nombre": "Calculadora Cientifica",       "precio":  30000},
    9:  {"nombre": "Soporte para Portatil",    "precio":  75000},
    10: {"nombre": "Audifonos de Diadema, USB",        "precio":   100000},
}


# --------------------------------------------------------
def mostrar_catalogo():
    """Muestra todos los productos disponibles con sus precios."""
    print("\n" + "="*55)
    print(f"{'ID':^5} {'PRODUCTO':<28} {'PRECIO':>15}")
    print("="*55)
    for id_prod, info in catalogo.items():
        precio_fmt = f"${info['precio']:,.0f} COP"
        print(f"{id_prod:^5} {info['nombre']:<28} {precio_fmt:>15}")
    print("="*55)


# --------------------------------------------------------
def agregar_producto(carrito, id_producto, cantidad):
    """
    Agrega un producto al carrito.
    Si ya existe, aumenta la cantidad.
    """
    if id_producto not in catalogo:
        print(f"\n   El producto con ID {id_producto} no existe en el catálogo.")
        return

    if cantidad <= 0:
        print("\n   La cantidad debe ser mayor a 0.")
        return

    nombre = catalogo[id_producto]["nombre"]

    if id_producto in carrito:
        carrito[id_producto]["cantidad"] += cantidad
        print(f"\n   Se agregaron {cantidad} unidad(es) más de '{nombre}'.")
    else:
        carrito[id_producto] = {
            "nombre":   nombre,
            "precio":   catalogo[id_producto]["precio"],
            "cantidad": cantidad,
        }
        print(f"\n   '{nombre}' agregado al carrito (x{cantidad}).")


# --------------------------------------------------------
def quitar_producto(carrito, id_producto, cantidad):
    """
    Quita una cantidad de un producto del carrito.
    Si la cantidad llega a 0, lo elimina por completo.
    """
    if id_producto not in carrito:
        print(f"\n  ✗ Ese producto no está en tu carrito.")
        return

    nombre = carrito[id_producto]["nombre"]

    if cantidad >= carrito[id_producto]["cantidad"]:
        del carrito[id_producto]
        print(f"\n  ✓ '{nombre}' eliminado del carrito.")
    else:
        carrito[id_producto]["cantidad"] -= cantidad
        print(f"\n  ✓ Se quitaron {cantidad} unidad(es) de '{nombre}'.")


# --------------------------------------------------------
def ver_carrito(carrito):
    """Muestra el contenido actual del carrito con el subtotal de cada ítem."""
    if not carrito:
        print("\n    Tu carrito está vacío.")
        return

    print("\n" + "="*65)
    print(f"{'ID':^5} {'PRODUCTO':<24} {'PRECIO':>12} {'CANT':>6} {'SUBTOTAL':>12}")
    print("="*65)

    for id_prod, item in carrito.items():
        subtotal = item["precio"] * item["cantidad"]
        precio_fmt   = f"${item['precio']:,.0f}"
        subtotal_fmt = f"${subtotal:,.0f}"
        print(f"{id_prod:^5} {item['nombre']:<24} {precio_fmt:>12} {item['cantidad']:^6} {subtotal_fmt:>12}")

    print("="*65)
    print(f"  {'TOTAL A PAGAR:':>45}  ${calcular_total(carrito):,.0f} COP")
    print("="*65)


# --------------------------------------------------------
def inspeccionar_producto(carrito, id_producto):
    """Muestra la información detallada de un producto específico dentro del carrito."""
    if id_producto not in carrito:
        print(f"\n  ✗ Ese producto no está en tu carrito.")
        return

    item = carrito[id_producto]
    subtotal = item["precio"] * item["cantidad"]

    print("\n" + "-"*40)
    print(f"   Detalle del producto")
    print("-"*40)
    print(f"  ID Producto : {id_producto}")
    print(f"  Nombre      : {item['nombre']}")
    print(f"  Precio unit.: ${item['precio']:,.0f} COP")
    print(f"  Cantidad    : {item['cantidad']}")
    print(f"  Subtotal    : ${subtotal:,.0f} COP")
    print("-"*40)


# --------------------------------------------------------
def calcular_total(carrito):
    """Retorna el total acumulado del carrito."""
    return sum(item["precio"] * item["cantidad"] for item in carrito.values())


# --------------------------------------------------------
def vaciar_carrito(carrito):
    """Elimina todos los productos del carrito."""
    if not carrito:
        print("\n    El carrito ya estaba vacío.")
        return
    carrito.clear()
    print("\n  ✓ Carrito vaciado exitosamente.")


# --------------------------------------------------------
def finalizar_compra(carrito):
    """Muestra el resumen final y 'procesa' la compra."""
    if not carrito:
        print("\n   No puedes finalizar una compra con el carrito vacío.")
        return False

    total = calcular_total(carrito)

    print("\n" + "="*55)
    print("             RESUMEN DE TU COMPRA")
    print("="*55)
    for item in carrito.values():
        subtotal = item["precio"] * item["cantidad"]
        print(f"  • {item['nombre']:<26} x{item['cantidad']}  ${subtotal:,.0f}")
    print("-"*55)
    print(f"  TOTAL:  ${total:,.0f} COP")
    print("="*55)
    print("    ¡Compra realizada con éxito! Gracias por tu compra.")
    print("="*55)
    carrito.clear()
    return True
