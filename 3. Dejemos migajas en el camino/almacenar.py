class Node:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.adjacent_nodes = []

def add_bidirectional_edge(node1, node2):
    node1.children.append(node2)
    node2.children.append(node1)
    node1.adjacent_nodes.append(node2)
    node2.adjacent_nodes.append(node1)

def depth_first_search(initial_node, goal_state):
    stack = [(initial_node, [initial_node])]
    visited = set()
    while stack:
        current_node, path = stack.pop()
        visited.add(current_node)
        if current_node.state == goal_state:
            return path, current_node  # Devolver el camino y el nodo objetivo
        for child in current_node.children:
            if child not in visited:
                stack.append((child, path + [child]))
    return None, None  # Si no se encuentra el objetivo, devolver None

def breadth_first_search(initial_node, goal_state):
    queue = [(initial_node, [initial_node])]
    visited = set()
    while queue:
        current_node, path = queue.pop(0)
        visited.add(current_node)
        if current_node.state == goal_state:
            return path, current_node  # Devolver el camino y el nodo objetivo
        for child in current_node.children:
            if child not in visited:
                queue.append((child, path + [child]))
    return None, None  # Si no se encuentra el objetivo, devolver None

# Crear nodos
node_0 = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)


# Establecer conexiones bidireccionales
add_bidirectional_edge(node_0, node_1)
add_bidirectional_edge(node_0, node_3)
add_bidirectional_edge(node_1, node_5)
add_bidirectional_edge(node_1, node_6)
add_bidirectional_edge(node_1, node_3)
add_bidirectional_edge(node_3, node_4)
add_bidirectional_edge(node_3, node_2)
add_bidirectional_edge(node_4, node_2)
add_bidirectional_edge(node_4, node_6)
add_bidirectional_edge(node_2, node_5)


# Buscar en el grafo bidireccional y guardar el camino
print("Buscar en profundidad")
path, goal_node = depth_first_search(node_0, 4)
if path:
    print("Camino encontrado:", [node.state for node in path])
    # Almacenar el camino y el nodo objetivo
    stored_path = path
    stored_goal_node = goal_node

print()

print("Buscar en amplitud")
path, goal_node = breadth_first_search(node_0, 4)
if path:
    print("Camino encontrado:", [node.state for node in path])
    # Almacenar el camino y el nodo objetivo
    stored_path = path
    stored_goal_node = goal_node
