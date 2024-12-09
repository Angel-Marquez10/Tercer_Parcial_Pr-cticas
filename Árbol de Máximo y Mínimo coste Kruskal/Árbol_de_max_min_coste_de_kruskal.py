import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class KruskalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("\u00c1rbol de M\u00e1ximo y M\u00ednimo Costo - Kruskal")

        self.edges = []  # Lista para almacenar las aristas con sus pesos
        self.nodes = set()  # Conjunto para almacenar los nodos

        self.create_widgets()  # Inicializa los elementos de la interfaz

    def create_widgets(self):
        # Marco para la entrada de datos de nodos y aristas
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Nodo 1:").grid(row=0, column=0, padx=5, pady=5)
        self.node1_entry = tk.Entry(input_frame, width=10)
        self.node1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Nodo 2:").grid(row=0, column=2, padx=5, pady=5)
        self.node2_entry = tk.Entry(input_frame, width=10)
        self.node2_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Peso:").grid(row=0, column=4, padx=5, pady=5)
        self.weight_entry = tk.Entry(input_frame, width=10)
        self.weight_entry.grid(row=0, column=5, padx=5, pady=5)

        tk.Button(input_frame, text="Agregar Arista", command=self.add_edge).grid(row=0, column=6, padx=5, pady=5)

        # Selección del tipo de árbol
        tk.Label(self.root, text="Selecciona tipo de \u00c1rbol:").pack(pady=5)
        self.tree_type = ttk.Combobox(self.root, values=["M\u00ednimo Costo", "M\u00e1ximo Costo"])
        self.tree_type.pack(pady=5)
        self.tree_type.current(0)  # Selecciona "M\u00ednimo Costo" por defecto

        # Marco para mostrar los resultados
        output_frame = tk.Frame(self.root, padx=10, pady=10)
        output_frame.pack()

        tk.Button(output_frame, text="Calcular \u00c1rbol", command=self.calculate_tree).pack(pady=5)

        self.output_text = tk.Text(output_frame, width=60, height=20, state="disabled")
        self.output_text.pack()

        # Canvas para visualizar los nodos y aristas
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)

    def add_edge(self):
        # Obtiene los valores ingresados por el usuario
        node1 = self.node1_entry.get().strip()
        node2 = self.node2_entry.get().strip()
        try:
            weight = int(self.weight_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "El peso debe ser un n\u00famero entero.")
            return

        if not node1 or not node2:
            messagebox.showerror("Error", "Ambos nodos deben estar especificados.")
            return

        # Agrega la arista y actualiza los nodos
        self.edges.append((weight, node1, node2))
        self.nodes.update([node1, node2])
        self.node1_entry.delete(0, tk.END)
        self.node2_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.log(f"Arista agregada: {node1} - {node2} con peso {weight}")

        # Dibuja los nodos y la arista en el canvas
        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")  # Limpia el canvas
        positions = {}  # Diccionario para almacenar posiciones de los nodos
        radius = 20  # Radio de los nodos
        x_offset, y_offset = 50, 50  # Espaciado inicial

        # Calcula posiciones para los nodos
        for i, node in enumerate(self.nodes):
            x = (i % 5) * 120 + x_offset
            y = (i // 5) * 120 + y_offset
            positions[node] = (x, y)
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
            self.canvas.create_text(x, y, text=node, font=("Arial", 10, "bold"))

        # Dibuja las aristas
        for weight, node1, node2 in self.edges:
            x1, y1 = positions[node1]
            x2, y2 = positions[node2]
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            self.canvas.create_text(mid_x, mid_y, text=str(weight), font=("Arial", 10, "bold"))

    def calculate_tree(self):
        if not self.edges:
            messagebox.showerror("Error", "No hay aristas para calcular el \u00e1rbol.")
            return

        tree_type = self.tree_type.get()
        if tree_type == "M\u00ednimo Costo":
            edges = sorted(self.edges)
        else:
            edges = sorted(self.edges, reverse=True)

        parent = {node: node for node in self.nodes}  # Inicializa el padre de cada nodo

        # Función para encontrar el representante del conjunto
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        # Función para unir dos conjuntos
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root2] = root1

        mst = []  # Lista para almacenar las aristas del Árbol Generador Mínimo/Máximo
        self.log("Iniciando el c\u00e1lculo del \u00c1rbol...")
        for weight, node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
                mst.append((node1, node2, weight))
                self.log(f"Arista a\u00f1adida al \u00e1rbol: {node1} - {node2} con peso {weight}")

        # Muestra el resultado final
        self.log("\n\u00c1rbol generado:")
        total_cost = 0
        for node1, node2, weight in mst:
            self.log(f"{node1} - {node2} con peso {weight}")
            total_cost += weight
        self.log(f"\nCosto total del \u00c1rbol: {total_cost}")

        # Dibuja el árbol final en el canvas
        self.edges = [(weight, node1, node2) for node1, node2, weight in mst]
        self.draw_graph()

    def log(self, message):
        # Muestra mensajes en el área de texto
        self.output_text.config(state="normal")
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state="disabled")
        self.output_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = KruskalGUI(root)
    root.mainloop()