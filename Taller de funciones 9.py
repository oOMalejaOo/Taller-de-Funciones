#Dado un listado de tuplas (producto, categoría), agrupa los productos por categoría usando un diccionario de listas

def agrupar_por_categoria(productos):
    categorias = {}
    for producto, categoria in productos:
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(producto)
    return categorias

productos = [
    ("Laptop", "Tecnología"),
    ("Silla", "Muebles"),           
    ("Smartphone", "Tecnología"),
    ("Mesa", "Muebles"),
    ("Auriculares", "Tecnología"), 
    ("Sofá", "Muebles"),
    ("Televisor", "Tecnología"),
    ("Lámpara", "Muebles")
]

resultado = agrupar_por_categoria(productos)
for categoria, lista_productos in resultado.items():
    print(f"{categoria}: {', '.join(lista_productos)}")
