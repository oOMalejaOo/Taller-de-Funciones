# ============================================================
#   Programa principal — Carrito de Compras 
# ============================================================

from funciones import (
    mostrar_catalogo,
    agregar_producto,
    quitar_producto,
    ver_carrito,
    inspeccionar_producto,
    vaciar_carrito,
    finalizar_compra,
    calcular_total,
)


# -------  UTILIDADES DE MENÚ  ----------------------------

def pedir_entero(mensaje):
    """Solicita un número entero al usuario, reintentando si el input es inválido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("    Por favor ingresa un número válido.")


def mostrar_menu():
    print("\n" + "="*45)
    print("          CARRITO DE COMPRAS")
    print("="*45)
    print("  [1]  Ver catálogo de productos")
    print("  [2]  Agregar producto al carrito")
    print("  [3]  Quitar producto del carrito")
    print("  [4]  Ver mi carrito")
    print("  [5]  Inspeccionar un producto del carrito")
    print("  [6]  Ver total acumulado")1
    print("  [7]  Vaciar carrito")
    print("  [8]  Finalizar compra")
    print("  [0]  Salir")
    print("="*45)


# -------  PROGRAMA PRINCIPAL  ----------------------------

def main():
    carrito = {}   # Diccionario que actúa como carrito de compras

    print("\n  Bienvenido a la Tienda Virtual ")

    while True:
        mostrar_menu()
        opcion = pedir_entero("  Elige una opción: ")

        # --- Ver catálogo ---
        if opcion == 1:
            mostrar_catalogo()

        # --- Agregar producto ---
        elif opcion == 2:
            mostrar_catalogo()
            id_prod  = pedir_entero("  ID del producto a agregar : ")
            cantidad = pedir_entero("  Cantidad                  : ")
            agregar_producto(carrito, id_prod, cantidad)

        # --- Quitar producto ---
        elif opcion == 3:
            if not carrito:
                print("\n    Tu carrito está vacío, no hay nada que quitar.")
            else:
                ver_carrito(carrito)
                id_prod  = pedir_entero("  ID del producto a quitar : ")
                cantidad = pedir_entero("  Cantidad a quitar        : ")
                quitar_producto(carrito, id_prod, cantidad)

        # --- Ver carrito ---
        elif opcion == 4:
            ver_carrito(carrito)

        # --- Inspeccionar producto ---
        elif opcion == 5:
            if not carrito:
                print("\n    Tu carrito está vacío.")
            else:
                ver_carrito(carrito)
                id_prod = pedir_entero("  ID del producto a inspeccionar: ")
                inspeccionar_producto(carrito, id_prod)

        # --- Total acumulado ---
        elif opcion == 6:
            total = calcular_total(carrito)
            if total == 0:
                print("\n    Tu carrito está vacío.")
            else:
                print(f"\n   Total acumulado: ${total:,.0f} COP")

        # --- Vaciar carrito ---
        elif opcion == 7:
            confirmacion = input("\n  ¿Estás seguro de vaciar el carrito? (s/n): ").strip().lower()
            if confirmacion == "s":
                vaciar_carrito(carrito)
            else:
                print("  Operación cancelada.")

        # --- Finalizar compra ---
        elif opcion == 8:
            exito = finalizar_compra(carrito)
            if exito:
                break   # Sale del programa tras comprar

        # --- Salir ---
        elif opcion == 0:
            print("\n    ¡Hasta pronto!")
            break

        else:
            print("\n   Opción inválida. Elige entre 0 y 8.")


# -------  PUNTO DE ENTRADA  ------------------------------

if __name__ == "__main__":
    main()
