def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    # Crear el diccionario del producto y agregarlo a la lista
    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(nuevo_producto)
    print(f"✅ Producto '{nombre}' agregado con éxito.")

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    
    # Recorrer el inventario e imprimir cada producto con el mismo formato
    for p in inventario:
        # Se usa :<20 para alinear a la izquierda y :>10 para la derecha
        print(f"{p['nombre']:<20} ${p['precio']:>9.2f} {p['cantidad']:>10}")

def buscar_producto(inventario, nombre):
    # Buscar y retornar el producto cuyo nombre coincida
    for producto in inventario:
        # Usamos .lower() para que la búsqueda no distinga mayúsculas y minúsculas
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        # Actualizar la cantidad del producto accediendo a su clave
        producto["cantidad"] = nueva_cantidad
        print("✅ Cantidad actualizada con éxito.")
    else:
        print("❌ Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    # Buscar el producto utilizando la función que ya creamos
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        # Usamos .remove() para sacarlo de la lista
        inventario.remove(producto)
        print(f"✅ Producto '{nombre}' eliminado con éxito.")
    else:
        print("❌ Producto no encontrado.")

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    
    # Total de productos distintos (longitud de la lista)
    total_productos = len(inventario)
    
    # Valor total: Sumamos la multiplicación del precio por la cantidad de cada producto
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    
    # Producto más caro y más barato usando las funciones max() y min()
    # Le pasamos una función lambda para decirle que compare usando la clave "precio"
    producto_caro = max(inventario, key=lambda x: x["precio"])
    producto_barato = min(inventario, key=lambda x: x["precio"])
    
    print("\n📊 --- RESUMEN DEL INVENTARIO ---")
    print(f"Total de productos distintos: {total_productos}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(f"Producto más caro: {producto_caro['nombre']} (${producto_caro['precio']:.2f})")
    print(f"Producto más barato: {producto_barato['nombre']} (${producto_barato['precio']:.2f})")

def menu():
    inventario = []
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Resumen")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                # Mostrar el producto con formato en lugar del diccionario crudo
                print(f"Encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            else:
                print("❌ No encontrado.")
        elif opcion == "4":
            actualizar_cantidad(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            resumen(inventario)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Iniciar el programa
if __name__ == "__main__":
    menu()