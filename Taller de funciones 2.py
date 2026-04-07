#Usa una lista de tuplas (nombre, nota) y una función que devuelva solo los estudiantes aprobados (nota ≥ 3.0).

def estudiantes_aprobados(estudiantes):
    aprobados = []
    for nombre, nota in estudiantes:
        if nota >= 3.0:
            aprobados.append(nombre)
    return aprobados

def es_numero(s):
    partes = s.split('.')
    if len(partes) == 1:
        return partes[0].isdigit()
    elif len(partes) == 2:
        return partes[0].isdigit() and partes[1].isdigit()
    else:
        return False

estudiantes = []
while True:
    estudiante = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if estudiante.lower() == 'fin':
        break
    nota_str = input(f"Ingrese la nota de {estudiante}: ")
    if es_numero(nota_str):
        nota = float(nota_str)
        estudiantes.append((estudiante, nota))
    else:
        print("Nota inválida. Por favor ingrese un número.")


aprobados = estudiantes_aprobados(estudiantes)
if aprobados:
    print("Estudiantes aprobados:")
    for nombre in aprobados:
        print(nombre)
else:
    print("No hay estudiantes aprobados.")