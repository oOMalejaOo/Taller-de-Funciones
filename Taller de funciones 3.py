#Implementa una agenda simple con funciones para agregar, buscar y eliminar contactos usando un diccionario.

agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con teléfono '{telefono}'.")  

def buscar_contacto(nombre):
    telefono = agenda.get(nombre)
    if telefono:
        print(f"El teléfono de '{nombre}' es '{telefono}'.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")
        
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")


def mostrar_menu():
    print("\nAGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        nombre = input("Nombre a buscar: ")
        buscar_contacto(nombre)
    elif opcion == '3':
        nombre = input("Nombre a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == '4':
        if agenda:
            print("Contactos:")
            for nombre, telefono in agenda.items():
                print(f"- {nombre}: {telefono}")
        else:
            print("La agenda está vacía.")
    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Elija una opción del 1 al 5.")

