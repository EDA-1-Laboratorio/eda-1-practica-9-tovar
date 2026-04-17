import os

# Directorio actual
print("Directorio actual:", os.getcwd())

# Listar archivos en el directorio actual
print("\nArchivos en el directorio:")
for archivo in os.listdir("."):
    tipo = "DIR" if os.path.isdir(archivo) else "FILE"
    print(f"  [{tipo}] {archivo}")

# Verificar si un archivo existe
archivo = "bibliotecas.py"
if os.path.exists(archivo):
    tamano = os.path.getsize(archivo)
    print(f"\n'{archivo}' existe y pesa {tamano} bytes")
else:
    print(f"\n'{archivo}' no existe")

# Variables de entorno
usuario = os.environ.get("USER", "desconocido")
print(f"\nUsuario del sistema: {usuario}")