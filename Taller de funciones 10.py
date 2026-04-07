#Registra votos de una lista de candidatos, detecta votos inválidos y determina el ganador con su porcentaje.

def registrar_votos(votos):
    conteo = {}
    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
        else:
            conteo[voto] = 1
    return conteo

def votos_invalidos(votos, candidatos_validos):
    return [voto for voto in votos if voto not in candidatos_validos]

def determinar_ganador(votos):
    if not votos:
        return None, 0
    conteo = registrar_votos(votos)
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / len(votos)) * 100
    return ganador, porcentaje

# Ejemplo de uso
votos = ["Lopez", "Gomez", "Cepedea", "Valencia", "Lopez", "Gomez", "Cepedea", "Valencia", "Gomez"]
candidatos_validos = ["Cepedea", "Valencia", "Lopez", "Gomez"]

conteo_votos = registrar_votos(votos)
print("Conteo de votos:")
for candidato, cantidad in conteo_votos.items():
    if candidato in candidatos_validos:
        print(f"{candidato}: {cantidad}")

invalidos = votos_invalidos(votos, candidatos_validos)
if invalidos:
    print(f"\nVotos inválidos: {', '.join(invalidos)}")
else:
    print("\nNo hay votos inválidos.")

ganador, porcentaje = determinar_ganador(votos)
if ganador:
    print(f"\nGanador: {ganador} con {porcentaje:.2f}% de los votos")
else:
    print("\nNo hay votos.")

