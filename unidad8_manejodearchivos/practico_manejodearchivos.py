ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    productos_iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno,450.0,15",
        "Regla,90.0,25"
    ]
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for linea in productos_iniciales:
            f.write(linea + "\n")
    print("Archivo inicial creado con 3 productos.\n")

def leer_productos():
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
                print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        crear_archivo_inicial()
        productos = leer_productos()
    return productos

def agregar_producto():
    print("\nAgregar nuevo producto")
    nombre = input("Nombre: ").strip()
    precio = input("Precio: ").strip()
    cantidad = input("Cantidad: ").strip()

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.\n")

def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip()
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("\nProductos guardados correctamente en el archivo.")

def main():
    print("GESTIÓN DE PRODUCTOS")
    productos = leer_productos()

    while True:
        print("\nOpciones:")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar y salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            productos = leer_productos()
        elif opcion == "2":
            agregar_producto()
            productos = leer_productos()
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            guardar_productos(productos)
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
