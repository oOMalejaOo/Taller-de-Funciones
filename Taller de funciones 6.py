#Almacena temperaturas semanales por ciudad y encuentra la más caliente y la más fría de la semana.

temperaturas = {
    "Bogotá": [17, 7, 12, 22, 23, 10, 8],
    "Cali": [24, 30, 21, 20, 28, 24, 22],
    "Medellin": [25, 27, 23, 31, 28, 26, 29]
    }

def temperatura_mas_caliente(temperaturas):
    ciudad_mas_caliente = None
    temperatura_maxima = float('-inf')
    
    for ciudad, temp in temperaturas.items():
        max_temp_ciudad = max(temp)
        if max_temp_ciudad > temperatura_maxima:
            temperatura_maxima = max_temp_ciudad
            ciudad_mas_caliente = ciudad
            
    return ciudad_mas_caliente, temperatura_maxima

def temperatura_mas_fria(temperaturas):
    ciudad_mas_fria = None
    temperatura_minima = float('inf')
    
    for ciudad, temp in temperaturas.items():
        min_temp_ciudad = min(temp)
        if min_temp_ciudad < temperatura_minima:
            temperatura_minima = min_temp_ciudad
            ciudad_mas_fria = ciudad
            
    return ciudad_mas_fria, temperatura_minima

ciudad_caliente, temp_caliente = temperatura_mas_caliente(temperaturas)
ciudad_fria, temp_fria = temperatura_mas_fria(temperaturas)        
print(f"La ciudad más caliente es {ciudad_caliente} con una temperatura de {temp_caliente}°C.")
print(f"La ciudad más fría es {ciudad_fria} con una temperatura de {temp_fria}°C.")
