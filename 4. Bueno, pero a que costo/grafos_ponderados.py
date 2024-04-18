class Node:
    def __init__(self, state):
        self.state = state
        self.adjacent_nodes = {}  # Usaremos un diccionario para almacenar los nodos adyacentes y sus pesos

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent_nodes[neighbor] = weight

def depth_first_search(initial_node, goal_state):
    stack = [(initial_node, [initial_node])]
    visited = set()
    while stack:
        current_node, path = stack.pop()
        visited.add(current_node)
        if current_node.state == goal_state:
            return path
        for neighbor, _ in current_node.adjacent_nodes.items():
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

def breadth_first_search(initial_node, goal_state):
    queue = [(initial_node, [initial_node])]
    visited = set()
    while queue:
        current_node, path = queue.pop(0)
        visited.add(current_node)
        if current_node.state == goal_state:
            return path
        for neighbor, _ in current_node.adjacent_nodes.items():
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# Crear nodos
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Establecer conexiones ponderadas
node_a.add_neighbor(node_b, 5)
node_a.add_neighbor(node_c, 3)
node_b.add_neighbor(node_d, 2)
node_b.add_neighbor(node_e, 6)
node_c.add_neighbor(node_e, 7)
node_d.add_neighbor(node_f, 4)
node_e.add_neighbor(node_f, 8)

# Buscar en el grafo ponderado
print("Buscar en profundidad")
path = depth_first_search(node_a, 'F')
if path:
    print("Camino encontrado:", [node.state for node in path])

print()

print("Buscar en amplitud")
path = breadth_first_search(node_a, 'F')
if path:
    print("Camino encontrado:", [node.state for node in path])
