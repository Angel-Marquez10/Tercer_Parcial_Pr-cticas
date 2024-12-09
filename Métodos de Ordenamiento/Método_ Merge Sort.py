# Importar la librería para la interfaz gráfica
import tkinter as tk
from tkinter import messagebox


# Función para fusionar dos subarreglos ordenados
def merge(left, right, steps_text):
    """
    Función para fusionar dos subarreglos en orden ascendente.
    También actualiza los pasos en la interfaz.
    """
    result = []
    i = j = 0

    steps_text.insert(tk.END, f"Fusionando: {left} y {right}\n")  # Mostrar paso en la interfaz

    # Comparar elementos de ambas mitades
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar los elementos restantes de la mitad izquierda
    while i < len(left):
        result.append(left[i])
        i += 1

    # Agregar los elementos restantes de la mitad derecha
    while j < len(right):
        result.append(right[j])
        j += 1

    steps_text.insert(tk.END, f"Resultado de la fusión: {result}\n")  # Mostrar el resultado de la fusión
    return result


# Función principal de Merge Sort
def merge_sort(arr, steps_text):
    """
    Función que implementa el algoritmo Merge Sort.
    También actualiza los pasos en la interfaz.
    """
    if len(arr) <= 1:
        steps_text.insert(tk.END, f"Base del caso: {arr}\n")  # Mostrar el caso base
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    steps_text.insert(tk.END, f"Dividiendo la lista: {arr} en {arr[:mid]} y {arr[mid:]}\n")  # Mostrar división
    left_half = merge_sort(arr[:mid], steps_text)
    right_half = merge_sort(arr[mid:], steps_text)

    # Fusionar las dos mitades ordenadas
    merged = merge(left_half, right_half, steps_text)
    return merged


# Función para ejecutar la ordenación y mostrar el resultado
def execute_merge_sort():
    """
    Esta función se ejecuta al presionar el botón en la interfaz gráfica.
    Toma la entrada del usuario, aplica Merge Sort y muestra el resultado.
    """
    try:
        # Limpiar el área de texto de pasos anteriores
        steps_text.delete(1.0, tk.END)

        # Obtener la cadena de números ingresados por el usuario
        user_input = entry.get()
        # Convertir la cadena de texto en una lista de números (separados por comas)
        user_list = [float(x) for x in user_input.split(",")]

        # Aplicar Merge Sort a la lista
        sorted_list = merge_sort(user_list, steps_text)

        # Mostrar la lista ordenada en el área de salida
        result_label.config(text="Lista Ordenada: " + str(sorted_list))
    except ValueError:
        # Mensaje de error si la entrada no es válida
        messagebox.showerror("Error", "Por favor, ingrese una lista válida de números separados por comas.")


# Crear la ventana principal de la interfaz gráfica
window = tk.Tk()
window.title("Merge Sort - Interfaz Gráfica con Pasos")
window.geometry("600x500")  # Definir el tamaño de la ventana

# Crear un título para la interfaz
title_label = tk.Label(window, text="Ordenamiento con Merge Sort", font=("Helvetica", 16))
title_label.pack(pady=10)  # Mostrar el título en la parte superior

# Crear un campo de texto donde el usuario puede ingresar los números
entry_label = tk.Label(window, text="Ingrese una lista de números separados por comas:")
entry_label.pack()
entry = tk.Entry(window, width=40)  # Campo de entrada
entry.pack(pady=5)

# Crear un botón para ejecutar Merge Sort
sort_button = tk.Button(window, text="Ordenar con Merge Sort", command=execute_merge_sort)
sort_button.pack(pady=10)

# Crear una etiqueta para mostrar el resultado de la ordenación
result_label = tk.Label(window, text="Lista Ordenada: ", font=("Helvetica", 12))
result_label.pack(pady=10)

# Crear un área de texto para mostrar los pasos intermedios del algoritmo
steps_text = tk.Text(window, height=15, width=70)  # Crear el área de texto para visualizar los pasos
steps_text.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()
