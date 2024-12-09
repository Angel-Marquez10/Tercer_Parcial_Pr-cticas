import tkinter as tk
from tkinter import messagebox


# Función de QuickSort
def quicksort(arr):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elegir el último elemento como pivote
    pivote = arr[-1]

    # Crear listas para los elementos menores y mayores
    menores = [x for x in arr[:-1] if x <= pivote]
    mayores = [x for x in arr[:-1] if x > pivote]

    # Aplicar QuickSort de manera recursiva y devolver la combinación
    return quicksort(menores) + [pivote] + quicksort(mayores)


# Función para procesar la entrada del usuario y realizar el ordenamiento
def ejecutar_quicksort():
    try:
        # Capturar la entrada del usuario
        entrada = entry_numeros.get()
        
        # Convertir la cadena en una lista de números
        lista_numeros = [float(x.strip()) for x in entrada.split(",")]

        # Ordenar la lista usando el método QuickSort
        resultado = quicksort(lista_numeros)

        # Mostrar el resultado en la interfaz
        etiqueta_resultado.config(text=f"Lista ordenada: {resultado}")
    except ValueError:
        # Mostrar un mensaje de error en caso de datos inválidos
        messagebox.showerror("Error", "Por favor ingresa números válidos separados por comas")


# Crear la interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("QuickSort con Interfaz Gráfica")
ventana.geometry("500x350")

# Crear una etiqueta de instrucciones
etiqueta_instrucciones = tk.Label(
    ventana, text="Ingresa una lista de números separados por comas:"
)
etiqueta_instrucciones.pack(pady=10)

# Crear un campo de entrada para que el usuario ingrese los números
entry_numeros = tk.Entry(ventana, width=50)
entry_numeros.pack(pady=5)

# Crear un botón para ejecutar el ordenamiento
boton_ordenar = tk.Button(
    ventana, text="Ordenar con QuickSort", command=ejecutar_quicksort
)
boton_ordenar.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Lista ordenada: ", font=("Arial", 12))
etiqueta_resultado.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()
