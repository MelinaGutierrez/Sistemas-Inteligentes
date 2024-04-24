class CuboRubik:
    def __init__(self):
        self.front = []
        self.back = []
        self.up = []
        self.down = []
        self.left = []
        self.right = []

    def leer_cubo(self, nombre_archivo):
        secciones={
            "Front": self.front,
            "Back": self.back,
            "Up":self.up,
            "Down":self.down,
            "Left":self.left,
            "Right":self.right
        }
                
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea.startswith('#'):
                    seccion=linea[1:].strip()
                    continue
                secciones[seccion].append(linea.split())
        
        self.objective = {
            "Front": [['R', 'O', 'W'], ['Y', 'R', 'W'], ['B', 'G', 'O']],
            "Back": [['B', 'Y', 'R'], ['G', 'O', 'O'], ['O', 'B', 'Y']],
            "Up": [['G', 'R', 'W'], ['G', 'B', 'B'], ['G', 'W', 'G']],
            "Down": [['Y', 'G', 'W'], ['Y', 'R', 'B'], ['G', 'W', 'B']],
            "Left": [['W', 'O', 'Y'], ['B', 'W', 'O'], ['O', 'B', 'R']],
            "Right": [['O', 'R', 'R'], ['G', 'Y', 'Y'], ['Y', 'R', 'W']]
        }
                   
    def mostrar_cubo(self):
        for seccion, contenido in [("Front", self.front), ("Back", self.back), ("Up", self.up),
                                   ("Down", self.down), ("Left", self.left), ("Right", self.right)]:
            print(f"#{seccion}")
            for fila in contenido:
                print(' '.join(fila))
            

    def move_up(self):
        temp_row = self.up[0][:]
        temp = self.front[0][:]
        self.front[0] = self.right[0][:]
        self.right[0] = self.back[0][:]
        self.back[0] = self.left[0][:]
        self.left[0] = temp[:]
        self.up[0] = self.up[2][:]
        self.up[1] = temp_row
        self.up[2] = self.up[0][:]
        
    def move_down(self):
        temp_row = self.down[0][:]
        temp = self.front[2][:]
        self.front[2] = self.right[2][:]
        self.right[2] = self.back[2][:]
        self.back[2] = self.left[2][:]
        self.left[2] = temp[:]
        self.down[0] = self.down[2][:]
        self.down[1] = temp_row
        self.down[2] = self.down[0][:]
    
    def move_front(self):
        temp_row = self.down[2][:]
        temp = self.up[2][:]
        self.up[2] = self.left[2][::-1]
        self.left[2] = self.down[2]
        self.down[2] = self.right[2][::-1]
        self.right[2] = temp
        for i in range(3):
            self.front[i][0], self.front[i][1], self.front[i][2], self.front[0][i], self.front[1][i], self.front[2][i] = self.front[2-i][0], self.front[2-i][1], self.front[2-i][2], self.front[0][i], self.front[1][i], self.front[2][i]
  
    def move_back(self):
        temp_row = self.down[0][:]
        temp = self.up[0][:]
        self.up[0] = self.right[0][::-1]
        self.right[0] = self.down[0]
        self.down[0] = self.left[0][::-1]
        self.left[0] = temp
        for i in range(3):
            self.back[i][0], self.back[i][1], self.back[i][2], self.back[0][i], self.back[1][i], self.back[2][i] = self.back[2-i][0], self.back[2-i][1], self.back[2-i][2], self.back[0][i], self.back[1][i], self.back[2][i]

        
    def move_left(self):
        temp_row = self.up[0][:]
        self.front[0] = self.down[0][:]
        self.down[0] = self.back[2][::-1]
        self.back[2] = self.up[0][::-1]
        self.up[0] = temp_row
        for i in range(3):
            self.left[i][0], self.left[i][1], self.left[i][2] = self.left[2-i][0], self.left[2-i][1], self.left[2-i][2]

        
    def move_right(self):
        temp_row = self.up[2][:]
        temp = self.front[2][:]
        self.front[2] = self.down[2][:]
        self.down[2] = self.back[0][::-1]
        self.back[0] = self.up[2][::-1]
        self.up[2] = temp_row
        for i in range(3):
            self.right[i][0], self.right[i][1], self.right[i][2] = self.right[2-i][0], self.right[2-i][1], self.right[2-i][2]
            
        
    def move_up_r(self):
        for _ in range(3):
            self.move_up()
    
    def move_down_r(self):
        for _ in range(3):
            self.move_down()
    
    def move_front_r(self):
        for _ in range(3):
            self.move_front()
    
    def move_back_r(self):
        for _ in range(3):
            self.move_back()
        
    def move_left_r(self):
        for _ in range(3):
            self.move_left()

        
    def move_right_r(self):
        for _ in range(3):
            self.move_right()
    
    def distancia_manhattan(self):
        distancia = 0
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    for l in range(3):
                        for m in range(3):
                            if self.front[l][m] == self.objective[k][i][j]:
                                distancia += abs(l - i) + abs(m - j)
                                break
                        else:
                            continue
                        break
        return distancia
    
    
    def resolver_cubo_a_estrella(self):
        lista_abierta = [(0, self)]
        visitados = set()
        
        while lista_abierta:
            _, estado_actual = lista_abierta.pop(0)
            
            if estado_actual==self.objective:
                return estado_actual
            
            visitados.add(estado_actual)
            
            for movimiento in [estado_actual.move_up, estado_actual.move_down, estado_actual.move_front,
                               estado_actual.move_back, estado_actual.move_left, estado_actual.move_right]:
                nuevo_estado = estado_actual.__class__()
                nuevo_estado.front = [fila[:] for fila in estado_actual.front]
                nuevo_estado.back = [fila[:] for fila in estado_actual.back]
                nuevo_estado.up = [fila[:] for fila in estado_actual.up]
                nuevo_estado.down = [fila[:] for fila in estado_actual.down]
                nuevo_estado.left = [fila[:] for fila in estado_actual.left]
                nuevo_estado.right = [fila[:] for fila in estado_actual.right]
                movimiento(nuevo_estado)
                
                costo = 1 + nuevo_estado.distancia_manhattan()
                
                if nuevo_estado not in visitados:
                    lista_abierta.append((costo, nuevo_estado))
                    lista_abierta.sort(key=lambda x: x[0])
        
        return None

cubo_resolver = CuboRubik()
cubo_resolver.leer_cubo('cube_scramble2.txt')
print("cubo 1")
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO UP*************")
print("cubo 2")
cubo_resolver.move_up()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_up_r()
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO DOWN*************")
print("cubo 2")
cubo_resolver.move_down()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_down_r()
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO FRONT*************")
print("cubo 2")
cubo_resolver.move_front()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_front_r()
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO BACK*************")
print("cubo 2")
cubo_resolver.move_back()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_back_r()
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO LEFT*************")
print("cubo 2")
cubo_resolver.move_left()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_left_r()
cubo_resolver.mostrar_cubo()

print("*************MOVER CUBO RIGHT*************")
print("cubo 2")
cubo_resolver.move_right()
cubo_resolver.mostrar_cubo()
print("cubo 1")
cubo_resolver.move_right_r()
cubo_resolver.mostrar_cubo()

# Ejemplo de uso
cubo_resolver = CuboRubik()
cubo_resolver.leer_cubo('cube_scramble2.txt')
print("Cubo antes de resolver:")
cubo_resolver.mostrar_cubo()

# Resolver el cubo usando A*
cubo_resuelto = cubo_resolver.resolver_cubo_a_estrella()
if cubo_resuelto:
    print("Cubo después de resolver:")
    cubo_resuelto.mostrar_cubo()
else:
    print("No se pudo resolver el cubo.")
