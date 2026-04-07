#1. Crea funciones que reciban una lista de notas y calculen el promedio, la nota más alta y la nota más baja.

def promedio(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def nota_mas_alta(notas):
    if not notas:
        return None
    return max(notas)

def nota_mas_baja(notas):
    if not notas:
        return None
    return min(notas)


def es_numero(s):
    partes = s.split('.')
    if len(partes) == 1:
        return partes[0].isdigit()
    elif len(partes) == 2:
        return partes[0].isdigit() and partes[1].isdigit()
    else:
        return False

entrada = input("Ingrese las notas separadas por espacios: ")
notas_str = entrada.split()
notas = []
for n in notas_str:
    if es_numero(n):
        notas.append(float(n))

if notas:
    print(f"Promedio: {promedio(notas)}")
    print(f"Nota más alta: {nota_mas_alta(notas)}")
    print(f"Nota más baja: {nota_mas_baja(notas)}")
else:
    print("No se ingresaron notas válidas.")
