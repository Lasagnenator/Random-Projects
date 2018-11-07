#Tetris 2

import pygame
import numpy as np

I = np.array([[-2,0], [-1,0], [0,0], [1,0]])
J = np.array([[-1,0], [0,0], [1,0], [1,-1]])
L = np.array([[-1,-1], [-1,0], [0,0], [1,0]])
O = np.array([[-1,-1], [-1,0], [0,0], [0,-1]])
S = np.array([[-1,-1], [0,-1], [0,0], [1,0]])
T = np.array([[-1,0], [0,0], [0,-1], [1,0]])
Z = np.array([[-1,0], [0,0], [0,-1], [1,-1]])

class Block(object):
    def __init__(self, block_name):
        pass
    def rotate(self):
        pass
    def get_pos(self):
        pass
