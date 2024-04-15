import matplotlib.pyplot as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Cubito:
    def __init__(self, centro, distancia, color):
        self.centro=centro
        self.distancia=distancia
        self.color= color
    
    def obtener_esquinas(self):
        x, y, z = self.centro
        semiarista = self.distancia/2
        esquinas = np.array([
            # + , + , + 
            # + , + , - 
            # + , - , + 
            # + , - , -
            # - , + , + 
            # - , + , -
            # - , - , + 
            # - , - , -
            [x+semiarista, y+semiarista, z+semiarista],
            [x+semiarista, y+semiarista, z-semiarista],
            [x+semiarista, y-semiarista, z+semiarista],
            [x+semiarista, y-semiarista, z-semiarista],
            [x-semiarista, y+semiarista, z+semiarista],
            [x-semiarista, y+semiarista, z-semiarista],
            [x-semiarista, y-semiarista, z+semiarista],
            [x-semiarista, y-semiarista, z-semiarista]
        ])
        return esquinas
    