import tkinter as tk
from tkinter import ttk, messagebox
import heapq


# Crear el grafo con las ciudades y sus conexiones (aristas con peso)
graph = {
    'Ciudad A': {'Ciudad B': 4, 'Ciudad C': 2},
    'Ciudad B': {'Ciudad A': 4, 'Ciudad C': 5, 'Ciudad D': 10},
    'Ciudad C': {'Ciudad A': 2, 'Ciudad B': 5, 'Ciudad D': 3},
    'Ciudad D': {'Ciudad B': 10, 'Ciudad C': 3, 'Ciudad E': 7},
    'Ciudad E': {'Ciudad D': 7}
}


# Función para ejecutar el algoritmo de Dijkstra
def dijkstra(graph, start, end):
    """
    Ejecuta el algoritmo de Dijkstra para encontrar la ruta más corta
    desde el nodo de inicio hasta el nodo destino.
    Devuelve las distancias más cortas y la ruta completa.
    """
    queue = [(0, start)]  # Cola de prioridad para el algoritmo con tuplas (distancia, nodo)
    distances = {node: float('inf') for node in graph}  # Almacena las distancias más cortas
    distances[start] = 0  # La distancia al nodo de inicio es 0
    previous_nodes = {node: None for node in graph}  # Almacena el camino recorrido para reconstruir el camino más tarde

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Sacar el nodo con menor distancia de la cola
        if current_distance > distances[current_node]:
            continue  # Ignorar nodos ya visitados con mejor distancia

        # Revisar los vecinos para actualizar sus distancias si es posible
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Calcular la distancia al vecino
            if distance < distances[neighbor]:  # Si se encuentra una distancia más corta, actualizarla
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node  # Actualizar la ruta más corta hasta ese punto

    # Devuelve las distancias calculadas y el camino para reconstruir la ruta
    return distances, previous_nodes


# Función para reconstruir la ruta más corta desde los nodos calculados
def reconstruct_path(previous_nodes, start, end):
    """
    Reconstruye la ruta más corta desde el nodo de inicio hasta el nodo destino.
    Utiliza la información almacenada en el diccionario `previous_nodes`.
    Devuelve la ruta completa como una lista de nodos.
    """
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()  # Invertir la ruta para que vaya del inicio hasta el destino
    return path


# Clase principal para la aplicación
class MapApp:
    def __init__(self, root):
        """
        Constructor para inicializar la aplicación gráfica principal.
        Configura la ventana principal, el lienzo y los botones.
        """
        self.root = root
        self.root.title("Mapa de Ciudades - Selección de Ruta")
        
        # Crear el lienzo para visualizar el mapa
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botón para ejecutar la búsqueda
        self.search_button = ttk.Button(self.root, text="Buscar Ruta", command=self.execute_dijkstra)
        self.search_button.pack()

        # Crear una interfaz para que el usuario seleccione sus puntos de inicio y destino
        self.start_label = ttk.Label(self.root, text="Selecciona punto de inicio:")
        self.start_label.pack()
        
        # Desplegable para seleccionar el punto de inicio
        self.start_var = tk.StringVar()
        self.start_combobox = ttk.Combobox(self.root, textvariable=self.start_var, values=list(graph.keys()))
        self.start_combobox.set("Ciudad A")
        self.start_combobox.pack()

        self.end_label = ttk.Label(self.root, text="Selecciona punto de destino:")
        self.end_label.pack()
        
        # Desplegable para seleccionar el punto de destino
        self.end_var = tk.StringVar()
        self.end_combobox = ttk.Combobox(self.root, textvariable=self.end_var, values=list(graph.keys()))
        self.end_combobox.set("Ciudad E")
        self.end_combobox.pack()

        # Almacenar la ruta seleccionada
        self.path = []
        
        # Dibujar el mapa de ciudades
        self.draw_graph()

    # Función para dibujar el mapa en el lienzo
    def draw_graph(self):
        """
        Función que dibuja el mapa de ciudades en el lienzo con líneas y posiciones de ciudades.
        """
        self.city_positions = {
            'Ciudad A': (50, 50),
            'Ciudad B': (150, 50),
            'Ciudad C': (100, 150),
            'Ciudad D': (250, 150),
            'Ciudad E': (200, 300)
        }

        # Dibujar las líneas entre nodos (aristas)
        for city, neighbors in graph.items():
            for neighbor in neighbors.keys():
                x1, y1 = self.city_positions[city]
                x2, y2 = self.city_positions[neighbor]
                self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

        # Dibujar los nodos (ciudades)
        for city, position in self.city_positions.items():
            x, y = position
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
            self.canvas.create_text(x, y-15, text=city, font=('Helvetica', 10))

    # Función para ejecutar la búsqueda de la ruta más corta
    def execute_dijkstra(self):
        """
        Obtiene los puntos de inicio y destino seleccionados por el usuario
        y ejecuta el algoritmo de Dijkstra para encontrar el camino más corto.
        """
        start = self.start_var.get()
        end = self.end_var.get()
        
        # Ejecutar el algoritmo de Dijkstra
        distances, paths = dijkstra(graph, start, end)
        self.path = reconstruct_path(paths, start, end)

        # Mostrar la ruta encontrada
        if self.path:
            self.highlight_path(self.path)
            messagebox.showinfo("Ruta Encontrada", f"Camino más corto: {' -> '.join(self.path)}")
        else:
            messagebox.showerror("Error", "No se encontró ninguna ruta válida.")

    # Función para destacar la ruta en la interfaz gráfica
    def highlight_path(self, path):
        """
        Dibuja la ruta seleccionada en rojo en el lienzo para mostrar el camino encontrado.
        """
        self.canvas.delete("highlight")  # Elimina rutas previas
        for i in range(len(path) - 1):
            x1, y1 = self.city_positions[path[i]]
            x2, y2 = self.city_positions[path[i+1]]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3, tags="highlight")


# Crear la aplicación principal
root = tk.Tk()
app = MapApp(root)
root.mainloop()
