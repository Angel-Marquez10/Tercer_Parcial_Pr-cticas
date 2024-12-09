import tkinter as tk
from tkinter import messagebox

def selection_sort(arr):
    """
    Ordena una lista utilizando el método de selección.
    :param arr: Lista de números a ordenar.
    :return: Lista ordenada y los pasos realizados.
    """
    n = len(arr)
    steps = []  # Lista para registrar los pasos del algoritmo

    for i in range(n):
        # Encuentra el índice del menor elemento en la sublista no ordenada
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento más pequeño con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # Registra el estado actual de la lista
        steps.append(f"Paso {i + 1}: {arr}")

    return arr, steps

def ordenar_lista():
    """
    Obtiene los números ingresados por el usuario, los ordena usando Selection Sort
    y muestra el resultado junto con los pasos.
    """
    entrada = entrada_texto.get()  # Obtiene los números ingresados como texto

    try:
        # Convierte los números ingresados a una lista de flotantes
        numeros = [float(x.strip()) for x in entrada.split(",")]
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos separados por comas.")
        return

    # Ordena la lista usando Selection Sort
    lista_ordenada, pasos = selection_sort(numeros)

    # Muestra la lista original y ordenada
    resultado_original.config(text=f"Lista original: {numeros}")
    resultado_ordenado.config(text=f"Lista ordenada: {lista_ordenada}")

    # Muestra los pasos en el cuadro de texto
    pasos_texto.delete(1.0, tk.END)  # Limpia el contenido anterior
    pasos_texto.insert(tk.END, "\n".join(pasos))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ordenamiento por Selección")
ventana.geometry("500x500")

# Etiqueta de instrucciones
instrucciones = tk.Label(ventana, text="Ingrese números separados por comas:", font=("Arial", 12))
instrucciones.pack(pady=10)

# Entrada de texto para los números
entrada_texto = tk.Entry(ventana, width=50, font=("Arial", 12))
entrada_texto.pack(pady=5)

# Botón para realizar el ordenamiento
boton_ordenar = tk.Button(ventana, text="Ordenar", command=ordenar_lista, font=("Arial", 12))
boton_ordenar.pack(pady=10)

# Etiqueta para mostrar la lista original
resultado_original = tk.Label(ventana, text="", font=("Arial", 12))
resultado_original.pack(pady=5)

# Etiqueta para mostrar la lista ordenada
resultado_ordenado = tk.Label(ventana, text="", font=("Arial", 12))
resultado_ordenado.pack(pady=5)

# Cuadro de texto para mostrar los pasos del algoritmo
pasos_texto = tk.Text(ventana, width=60, height=15, font=("Arial", 10))
pasos_texto.pack(pady=10)

# Ejecución de la ventana
ventana.mainloop()
