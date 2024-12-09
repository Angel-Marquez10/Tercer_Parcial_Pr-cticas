import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq


class PrimSimulator:
    def __init__(self, root):
        # Configurar la ventana principal
        self.root = root
        self.root.title("Simulador de Árbol Parcial Mínimo - Algoritmo de Prim")
        
        # Crear el lienzo principal con dimensiones ajustadas para visualizar mejor el proceso
        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="white")
        self.canvas.pack()

        # Listas para nodos y aristas, así como el contador de nodos
        self.nodes = []
        self.edges = {}
        self.node_counter = 0

        # Configurar los eventos: clic izquierdo para agregar nodos, clic derecho para conectar nodos
        self.canvas.bind("<Button-1>", self.add_node) 
        self.canvas.bind("<Button-3>", self.connect_nodes)

        # Etiqueta para informar al usuario sobre cómo interactuar con la interfaz
        self.info_label = tk.Label(
            self.root,
            text="Clic izquierdo para añadir nodos, clic derecho para conectar nodos.",
            bg="lightblue"
        )
        self.info_label.pack(fill=tk.X)

        # Botón para ejecutar el algoritmo de Prim
        self.run_button = tk.Button(self.root, text="Ejecutar Prim", command=self.run_prim)
        self.run_button.pack()

        # Área de texto para mostrar el log del proceso
        self.log_text = tk.Text(self.root, height=10, state=tk.DISABLED, bg="lightgray")
        self.log_text.pack(fill=tk.X)

    # Función para agregar nodos con clic izquierdo
    def add_node(self, event):
        # Obtener la posición del clic
        x, y = event.x, event.y
        node_id = self.node_counter
        self.node_counter += 1

        # Agregar el nodo a la lista de nodos y crear un espacio para sus aristas
        self.nodes.append((node_id, x, y))
        self.edges[node_id] = []

        # Dibujar el nodo con tamaño reducido para mejor visibilidad
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue", outline="black")  # Nodo más pequeño
        self.canvas.create_text(x, y, text=str(node_id), fill="white")  # Etiqueta con el ID del nodo

    # Función para conectar nodos con clic derecho
    def connect_nodes(self, event):
        # Verificar si hay suficientes nodos para crear una conexión
        if len(self.nodes) < 2:
            messagebox.showwarning("Advertencia", "Se necesitan al menos 2 nodos para conectar.")
            return

        # Pedir al usuario los IDs de los nodos a conectar
        node1 = simpledialog.askinteger("Conectar Nodos", "Ingrese el ID del primer nodo:")
        node2 = simpledialog.askinteger("Conectar Nodos", "Ingrese el ID del segundo nodo:")

        # Validar los nodos ingresados
        if node1 is None or node2 is None or node1 == node2:
            messagebox.showerror("Error", "IDs inválidos o nodos iguales.")
            return

        # Pedir el peso de la arista
        weight = simpledialog.askinteger("Peso de la Arista", "Ingrese el peso de la arista:")

        # Validar el peso
        if weight is None or weight <= 0:
            messagebox.showerror("Error", "Peso inválido.")
            return

        # Llamar a la función para agregar la arista
        self.add_edge(node1, node2, weight)

    # Función para agregar aristas
    def add_edge(self, node1, node2, weight):
        # Validar que los nodos existen en el grafo
        if node1 not in self.edges or node2 not in self.edges:
            messagebox.showerror("Error", "Nodos no encontrados.")
            return

        # Agregar la arista bidireccional con el peso correspondiente
        self.edges[node1].append((weight, node2))
        self.edges[node2].append((weight, node1))

        # Dibujar la línea entre los nodos con el peso visible en el medio
        x1, y1 = self.nodes[node1][1], self.nodes[node1][2]
        x2, y2 = self.nodes[node2][1], self.nodes[node2][2]

        self.canvas.create_line(x1, y1, x2, y2, fill="gray")
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        self.canvas.create_text(mid_x, mid_y, text=str(weight), fill="red")

    # Función para ejecutar el algoritmo de Prim
    def run_prim(self):
        # Validar si es posible ejecutar el algoritmo
        if len(self.nodes) < 2 or not any(self.edges.values()):
            messagebox.showwarning("Advertencia", "Se necesitan al menos 2 nodos y conexiones para ejecutar Prim.")
            return

        # Ejecutar el algoritmo
        mst, process_log = self.prim_algorithm()
        
        # Resaltar el resultado en la interfaz gráfica
        self.highlight_mst(mst)

        # Mostrar el proceso paso a paso en el área de texto
        self.display_process_log(process_log)

    # Implementación del algoritmo de Prim
    def prim_algorithm(self):
        # Nodo de inicio arbitrario
        start_node = 0
        visited = set()
        edges = []
        heapq.heappush(edges, (0, start_node, None))
        mst = []
        process_log = []

        process_log.append(f"Nodo inicial: {start_node}")

        # Iterar hasta que no queden más aristas por explorar
        while edges:
            weight, current, prev = heapq.heappop(edges)
            if current not in visited:
                visited.add(current)
                if prev is not None:
                    mst.append((prev, current, weight))
                    process_log.append(f"Seleccionada arista ({prev} - {current}) con peso {weight}")

                for next_weight, neighbor in self.edges[current]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (next_weight, neighbor, current))
                        process_log.append(f"Evaluando conexión ({current} - {neighbor}) con peso {next_weight}")

        process_log.append("Árbol Parcial Mínimo calculado correctamente.")
        return mst, process_log

    # Función para resaltar el MST en la interfaz
    def highlight_mst(self, mst):
        for node1, node2, weight in mst:
            x1, y1 = self.nodes[node1][1], self.nodes[node1][2]
            x2, y2 = self.nodes[node2][1], self.nodes[node2][2]
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=2)

    # Mostrar el proceso en el área de texto
    def display_process_log(self, process_log):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        for log_entry in process_log:
            self.log_text.insert(tk.END, log_entry + "\n")
        self.log_text.config(state=tk.DISABLED)


# Configuración inicial
if __name__ == "__main__":
    root = tk.Tk()
    simulator = PrimSimulator(root)
    root.mainloop()
