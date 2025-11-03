# ==========================================
# 📚 Mi Biblioteca - Ejercicio de Colecciones
# ==========================================

# 1️⃣ Lista que almacena libros (cada libro es un diccionario)
biblioteca = [
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943},
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"titulo": "1984", "autor": "George Orwell", "anio": 1949}
]

# 2️⃣ Mostrar los libros con formato numerado
print("=== Mi Biblioteca ===")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")

# 3️⃣ Tupla con categorías literarias
categorias = ("Ficción", "Historia", "Ciencia")
print(f"\nCategorías disponibles: {categorias}")

# 4️⃣ Opción para agregar un nuevo libro
agregar = input("\n¿Deseas agregar un nuevo libro? (s/n): ").lower()

if agregar == "s":
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")

    nuevo_libro = {"titulo": titulo, "autor": autor, "anio": int(anio)}
    biblioteca.append(nuevo_libro)

    print("\n✅ Libro agregado con éxito!")

    # Mostrar lista actualizada
    print("\n=== Mi Biblioteca Actualizada ===")
    for i, libro in enumerate(biblioteca, start=1):
        print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")