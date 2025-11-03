# 📚 Mi Biblioteca — Explicación Detallada

## 🧩 1. La lista principal — `biblioteca`

```python
biblioteca = [
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943},
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"titulo": "1984", "autor": "George Orwell", "anio": 1949}
]
```

### 💡 ¿Qué pasa aquí?

Se crea una lista llamada **`biblioteca`**, una colección **ordenada y mutable**.  
Dentro de esa lista hay **3 diccionarios** (uno por libro).  
Cada diccionario guarda información con las claves:  
- `"titulo"`  
- `"autor"`  
- `"anio"`

Esto permite que cada libro se comporte como un pequeño “objeto” dentro de la lista.

---

## 🧠 2. Mostrar los libros

```python
print("=== Mi Biblioteca ===")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")
```

### 🔍 ¿Qué ocurre?

`enumerate(biblioteca, start=1)` recorre la lista y agrega un contador (`i`) que empieza en 1.  
En cada vuelta del `for`, `libro` toma el valor de un **diccionario** dentro de la lista.

**Ejemplo del bucle:**
```
1° vuelta → libro = {"titulo": "El Principito", ...}
2° vuelta → libro = {"titulo": "Cien Años de Soledad", ...}
3° vuelta → libro = {"titulo": "1984", ...}
```

La línea:
```python
f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})"
```
muestra cada libro de forma ordenada y legible.

---

## 🧬 3. La tupla de categorías

```python
categorias = ("Ficción", "Historia", "Ciencia")
print(f"\nCategorías disponibles: {categorias}")
```

Una **tupla** es una colección **ordenada e inmutable**, es decir, no se puede modificar.  
Se usa cuando los datos son fijos, como categorías, meses o configuraciones.

📘 **Resultado:**
```
Categorías disponibles: ('Ficción', 'Historia', 'Ciencia')
```

---

## 🧮 4. Agregar un nuevo libro (input del usuario)

```python
agregar = input("\n¿Deseas agregar un nuevo libro? (s/n): ").lower()
```

- `input()` permite al usuario escribir datos en la consola.  
- `.lower()` convierte la respuesta a minúscula (por ejemplo, “S” → “s”).  

Si el usuario responde “s”:

```python
if agregar == "s":
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")
```

Aquí el programa **pide la información** necesaria para crear un nuevo libro.

---

## ⚙️ 5. Crear y agregar el nuevo libro

```python
nuevo_libro = {"titulo": titulo, "autor": autor, "anio": int(anio)}
biblioteca.append(nuevo_libro)
```

- Se crea un **diccionario** con los datos ingresados.  
- `int(anio)` convierte el texto en número.  
- `biblioteca.append(nuevo_libro)` agrega ese diccionario al final de la lista.  

---

## ✅ 6. Mostrar la lista actualizada

```python
print("\n=== Mi Biblioteca Actualizada ===")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")
```

Este bloque vuelve a mostrar todos los libros, incluyendo el nuevo.

---

## 🧠 En resumen

| Concepto Python | Aplicación en el programa |
|------------------|---------------------------|
| **list** | Guarda todos los libros (`biblioteca`). |
| **dict** | Representa cada libro con claves y valores. |
| **tuple** | Guarda géneros fijos (`categorias`). |
| **for** | Recorre y muestra los libros. |
| **input()** | Permite ingresar datos desde la consola. |
| **append()** | Agrega un libro nuevo a la lista. |

---

## 🖥️ Ejemplo de ejecución completa

```
=== Mi Biblioteca ===
1. El Principito - Antoine de Saint-Exupéry (1943)
2. Cien Años de Soledad - Gabriel García Márquez (1967)
3. 1984 - George Orwell (1949)

Categorías disponibles: ('Ficción', 'Historia', 'Ciencia')

¿Deseas agregar un nuevo libro? (s/n): s
Título: Dune
Autor: Frank Herbert
Año: 1965

✅ Libro agregado con éxito!

=== Mi Biblioteca Actualizada ===
1. El Principito - Antoine de Saint-Exupéry (1943)
2. Cien Años de Soledad - Gabriel García Márquez (1967)
3. 1984 - George Orwell (1949)
4. Dune - Frank Herbert (1965)
```

---

## 💡 Conclusión

Este programa demuestra el uso combinado de **listas, diccionarios y tuplas** en Python:

- La **lista** guarda todos los libros.  
- Cada **diccionario** representa un libro con sus datos.  
- La **tupla** contiene categorías fijas.  
- Y con un simple **bucle for** + **input()**, puedes interactuar con tu colección en tiempo real.
