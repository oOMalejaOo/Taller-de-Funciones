#Simula un carrito de compras con funciones para agregar productos, aplicar descuentos y generar el total a pagar

def agregar(carrito, producto, precio):
    carrito.append((producto, precio))
    return carrito     

def aplicar_descuento(carrito, descuento):
    total = sum(precio for _, precio in carrito)
    total_con_descuento = total * (1 - descuento / 100)
    return total_con_descuento

def generar_reporte(carrito):
    reporte = "Carrito de Compras:\n"
    for producto, precio in carrito:
        reporte += f"- {producto}: ${precio:.2f}\n"
    return reporte

carrito = []
carrito = agregar(carrito, "Portátil", 2500000)
carrito = agregar(carrito, "Mouse", 25000)
carrito = agregar(carrito, "Teclado", 150000)
reporte = generar_reporte(carrito)
print(reporte)
total_con_descuento = aplicar_descuento(carrito, 10)
print(f"Total a pagar con descuento: ${total_con_descuento:.2f}")
