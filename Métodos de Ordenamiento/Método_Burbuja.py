import tkinter as tk
from tkinter import messagebox

# Función que implementa el método de ordenamiento burbuja.
def bubble_sort(arr):
    """
    Ordena una lista de números utilizando el método Burbuja.
    :param arr: Lista de números a ordenar.
    :return: Lista ordenada.
    """
    n = len(arr)  # Obtiene el tamaño de la lista.
    for i in range(n):  # Itera a través de toda la lista.
        intercambio = False  # Bandera para verificar si se realizaron intercambios en esta pasada.
        for j in range(0, n - i - 1):  # Itera hasta el índice no ordenado.
            if arr[j] > arr[j + 1]:  # Compara elementos adyacentes.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia si están en el orden incorrecto.
                intercambio = True  # Cambia la bandera si ocurre un intercambio.
        if not intercambio:  # Si no hubo intercambios, la lista ya está ordenada.
            break
    return arr  # Devuelve la lista ordenada.

# Función para manejar el evento de ordenar la lista ingresada.
def ordenar_lista():
    """
    Toma la entrada del usuario, la convierte en una lista, la ordena y muestra los resultados.
    """
    entrada = entrada_numeros.get()  # Obtiene la entrada del usuario del campo de texto.
    try:
        # Convierte la entrada en una lista de números flotantes separados por comas.
        lista = list(map(float, entrada.split(',')))
        lista_original.set(f"Lista original: {lista}")  # Actualiza el texto para mostrar la lista original.
        
        # Ordena la lista usando el método Burbuja.
        lista_ordenada = bubble_sort(lista[:])  # Copia la lista original antes de ordenarla.
        lista_resultado.set(f"Lista ordenada: {lista_ordenada}")  # Muestra la lista ordenada.
    except ValueError:
        # Muestra un mensaje de error si la entrada no es válida.
        messagebox.showerror("Error", "Por favor, ingrese una lista de números válidos separados por comas.\nEjemplo: -2.5, 3, -1, 4.7")

# Configuración de la ventana principal de la interfaz gráfica.
ventana = tk.Tk()  # Crea la ventana principal.
ventana.title("Ordenamiento Burbuja")  # Establece el título de la ventana.
ventana.geometry("450x350")  # Establece el tamaño de la ventana.

# Variables para almacenar y mostrar los resultados en la interfaz.
lista_original = tk.StringVar()  # Variable para la lista original.
lista_resultado = tk.StringVar()  # Variable para la lista ordenada.

# Etiqueta de bienvenida.
etiqueta_bienvenida = tk.Label(
    ventana, text="Método de Ordenamiento Burbuja", font=("Arial", 14)
)  # Crea una etiqueta con un mensaje de bienvenida.
etiqueta_bienvenida.pack(pady=10)  # Coloca la etiqueta con un margen vertical.

# Etiqueta que solicita ingresar una lista de números.
etiqueta_ingreso = tk.Label(
    ventana, text="Ingrese números separados por comas (ej. -2.5, 3, -1, 4.7):"
)  # Crea una etiqueta con instrucciones para el usuario.
etiqueta_ingreso.pack()  # Coloca la etiqueta en la ventana.

# Campo de texto para que el usuario ingrese los números.
entrada_numeros = tk.Entry(ventana, width=50)  # Crea un campo de entrada de texto.
entrada_numeros.pack(pady=5)  # Coloca el campo con un margen vertical.

# Botón para iniciar el proceso de ordenamiento.
boton_ordenar = tk.Button(
    ventana, text="Ordenar", command=ordenar_lista
)  # Crea un botón que ejecuta la función `ordenar_lista`.
boton_ordenar.pack(pady=10)  # Coloca el botón con un margen vertical.

# Etiqueta para mostrar la lista original ingresada por el usuario.
etiqueta_lista_original = tk.Label(
    ventana, textvariable=lista_original, fg="blue"
)  # Crea una etiqueta que muestra la lista original.
etiqueta_lista_original.pack(pady=5)  # Coloca la etiqueta en la ventana.

# Etiqueta para mostrar la lista ordenada.
etiqueta_lista_resultado = tk.Label(
    ventana, textvariable=lista_resultado, fg="green"
)  # Crea una etiqueta que muestra la lista ordenada.
etiqueta_lista_resultado.pack(pady=5)  # Coloca la etiqueta en la ventana.

# Ejecutar el bucle principal de la aplicación.
ventana.mainloop()  # Inicia el bucle de eventos de `tkinter`.
