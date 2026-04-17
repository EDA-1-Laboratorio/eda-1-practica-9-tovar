import random
import string

def generar_contrasena(longitud=12):
    # string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.digits = '0123456789'
    # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
        
    return contrasena

# Generar 5 contraseñas de diferentes longitudes
print("Contraseñas generadas:")
for longitud in [8, 12, 16, 20, 24]:
    print(f"  Longitud {longitud}: {generar_contrasena(longitud)}")