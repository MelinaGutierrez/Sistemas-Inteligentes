import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = self.find_start()
        self.goal = self.find_goal()

    def find_start(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'A':
                    return (i, j)
        return None

    def find_goal(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'B':
                    return (i, j)
        return None

    def is_valid_move(self, row, col):
        return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]) and self.maze[row][col] != '#'

    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def depth_first_search(self):
        visited = set()
        stack = [(self.start, [self.start])]
        while stack:
            current_pos, path = stack.pop()
            if current_pos in visited:
                continue
            visited.add(current_pos)
            if current_pos == self.goal:
                return path
            row, col = current_pos
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid_move(new_row, new_col):
                    stack.append(((new_row, new_col), path + [(new_row, new_col)]))
        return None

    def breadth_first_search(self):
        visited = set()
        queue = [(self.start, [self.start])]
        while queue:
            current_pos, path = queue.pop(0)
            if current_pos in visited:
                continue
            visited.add(current_pos)
            if current_pos == self.goal:
                return path
            row, col = current_pos
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid_move(new_row, new_col):
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))
        return None

    def greedy_best_first_search(self):
        visited = set()
        priority_queue = [(self.manhattan_distance(self.start, self.goal), self.start, [self.start])]
        while priority_queue:
            _, current_pos, path = heapq.heappop(priority_queue)
            if current_pos in visited:
                continue
            visited.add(current_pos)
            if current_pos == self.goal:
                return path
            row, col = current_pos
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid_move(new_row, new_col):
                    heapq.heappush(priority_queue, (self.manhattan_distance((new_row, new_col), self.goal), (new_row, new_col), path + [(new_row, new_col)]))
        return None

    def solve_maze(self, search_algorithm):
        if search_algorithm == "dfs":
            return self.depth_first_search()
        elif search_algorithm == "bfs":
            return self.breadth_first_search()
        elif search_algorithm == "gbfs":
            return self.greedy_best_first_search()

def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def print_maze_with_path(maze, path):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path:
                print('*', end='')
            else:
                print(cell, end='')
        print()

def main():
    maze_file = "laberynth.txt"  # Path al archivo del laberinto
    maze = load_maze(maze_file)
    solver = MazeSolver(maze)

    print("Laberinto:")
    for row in maze:
        print("".join(row))
    print()

    print("\nBúsqueda en profundidad:")
    dfs_path = solver.solve_maze("dfs")
    if dfs_path:
        print_maze_with_path(maze, dfs_path)
    else:
        print("No se encontró un camino.")

    print("\nBúsqueda en amplitud:")
    bfs_path = solver.solve_maze("bfs")
    if bfs_path:
        print_maze_with_path(maze, bfs_path)
    else:
        print("No se encontró un camino.")

    print("\nBúsqueda 'greedy best-first':")
    gbfs_path = solver.solve_maze("gbfs")
    if gbfs_path:
        print_maze_with_path(maze, gbfs_path)
    else:
        print("No se encontró un camino.")

if __name__ == "__main__":
    main()
