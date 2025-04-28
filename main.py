"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def imprimir_mayusculas_desde_archivo(nombre_archivo):  
  try:
    with open(nombre_archivo, 'r') as archivo:
      for linea in archivo:
        palabra = linea.strip()  # Elimina espacios en blanco al principio y al final
        print(palabra.upper())
  except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
  except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=not ascending)

def remove_duplicates(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("You must provide the filename as the first argument")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates(word_list)

    imprimir_mayusculas_desde_archivo("words.txt")

    print(sort_list(word_list))

