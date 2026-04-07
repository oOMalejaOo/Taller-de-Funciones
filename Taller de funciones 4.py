#Gestiona un inventario donde cada producto tiene nombre, precio y cantidad. Calcula el valor total del inventario 

inventario = {}

def agregar(nombre, precio, cantidad):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado al inventario.")

def calcular_valor_total():
    total = sum(producto["precio"] * producto["cantidad"] for producto in inventario.values())
    return total

def mostrar_inventario():
    if inventario:
        print("Inventario:")
        for nombre, detalles in inventario.items():
            print(f"- {nombre}: ${detalles['precio']:.2f} x {detalles['cantidad']}")
        print(f"Valor total del inventario: ${calcular_valor_total():.2f}")
    else:
        print("El inventario está vacío.")


agregar("Manzanas", 800, 100)  
agregar("Naranjas", 750, 50)
agregar("Peras", 900, 30)
agregar("Bananas", 600, 80)
mostrar_inventario()
