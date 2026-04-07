#Convierte notas numéricas a letras (A, B, C, D, F) usando tuplas como rangos y devuelve un reporte por estudiante

def convertir(nota):
    if nota >= 90:
        return 'A'
    elif nota >= 80:
        return 'B'
    elif nota >= 70:
        return 'C'
    elif nota >= 60:
        return 'D'
    else:
        return 'F'
    
def generar_reporte(estudiantes):
    reporte = {}
    for estudiante, nota in estudiantes.items():
        reporte[estudiante] = convertir(nota)
    return reporte

estudiantes = {
    "Pedro": 85,
    "Aleja": 92,
    "Ramon": 78,
    "Lisa": 65,
    "Luis": 55
}
reporte = generar_reporte(estudiantes)
print(reporte)