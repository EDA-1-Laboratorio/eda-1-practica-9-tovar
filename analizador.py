def contar_palabras(texto):
    # split() divide el texto en una lista usando los espacios en blanco
    return len(texto.split())

def contar_oraciones(texto):
    # Contamos la cantidad de veces que aparecen los signos de puntuación finales
    return texto.count('.') + texto.count('!') + texto.count('?')

def palabra_mas_frecuente(texto):
    # Limpiamos signos de puntuación y pasamos a minúsculas para un conteo real
    texto_limpio = texto.lower().replace('.', '').replace(',', '').replace('!', '').replace('¡', '').replace('?', '').replace('¿', '')
    palabras = texto_limpio.split()
    
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
        
    # max() puede recibir una función 'key' para saber por qué criterio buscar el máximo
    # En este caso, busca la clave cuyo valor (la frecuencia) sea el más alto
    return max(frecuencias, key=frecuencias.get)

def palabras_unicas(texto):
    texto_limpio = texto.lower().replace('.', '').replace(',', '').replace('!', '').replace('¡', '').replace('?', '').replace('¿', '')
    # La estructura 'set' elimina automáticamente todos los duplicados
    return set(texto_limpio.split())

def longitud_promedio_palabras(texto):
    # Limpiamos para no contar las comas o puntos como si fueran letras de la palabra
    texto_limpio = texto.replace('.', '').replace(',', '').replace('!', '').replace('¡', '').replace('?', '').replace('¿', '')
    palabras = texto_limpio.split()
    
    if not palabras:
        return 0
        
    total_letras = sum(len(p) for p in palabras)
    return total_letras / len(palabras)

def buscar_palabra(texto, palabra):
    # Limpiamos el texto para que "Python," o "Python." cuenten como "Python"
    texto_limpio = texto.replace('.', '').replace(',', '').replace('!', '').replace('¡', '').replace('?', '').replace('¿', '')
    lista_palabras = texto_limpio.split()
    # El método count() de las listas busca coincidencias exactas
    return lista_palabras.count(palabra)

def reemplazar_palabra(texto, vieja, nueva):
    # El método replace() de las cadenas busca un fragmento y lo sustituye por otro
    return texto.replace(vieja, nueva)

# Texto de ejemplo para analizar
texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
"""

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: '{palabra_mas_frecuente(texto_ejemplo)}'")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")