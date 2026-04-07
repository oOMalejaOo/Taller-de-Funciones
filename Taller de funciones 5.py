#Dada una lista de palabras, construye un diccionario con la frecuencia de aparición de cada una.

def contar_frecuencia(palabras):
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia


palabras = ["Perro", "Gato", "Hamster"]
frecuencia_palabras = contar_frecuencia(palabras)     
