import random

resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(1000):
    # random.randint(a, b) devuelve un número entero aleatorio entre a y b (incluidos)
    dado = random.randint(1, 6)
    
    # Usamos el valor que salió en el dado para aumentar su contador
    resultados[dado] += 1

print("Resultados de 1000 lanzamientos:")

# .items() nos permite iterar sobre las claves y los valores al mismo tiempo
for cara, conteo in resultados.items():
    print(f"  Cara {cara}: {conteo} veces")