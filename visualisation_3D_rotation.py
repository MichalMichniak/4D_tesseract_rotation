import pygame as pg
import numpy as np

WIDTH = 1200
HEIGH = 600

def visualisation():
    pg.init()
    pg.display.set_caption("game")
    font = pg.font.SysFont(None, 24)
    win = pg.display.set_mode((WIDTH, HEIGH))
    run = True
    size = 100
    edges = np.array([
        [[0,0,0],[0,0,1]],
        [[0,0,0],[0,1,0]],
        [[0,0,0],[1,0,0]],
        [[0,0,1],[0,1,1]],
        [[0,0,1],[1,0,1]],
        [[0,1,0],[0,1,1]],
        [[0,1,0],[1,1,0]],
        [[1,0,0],[1,0,1]],
        [[1,0,0],[1,1,0]],
        [[1,1,1],[1,1,0]],
        [[1,1,1],[1,0,1]],
        [[1,1,1],[0,1,1]]
        ])*size - (size/2)
    transformation_matrix = lambda x,y,z: (np.array([[np.cos(x),-np.sin(x),0],[np.sin(x),np.cos(x),0],[0,0,1.0]])
    @np.array([[1,0,0],[0,np.cos(y),-np.sin(y)],[0,np.sin(y),np.cos(y)]])
    @np.array([[np.cos(z),0,np.sin(z)],[0,1,0],[-np.sin(z),0,np.cos(z)]])).T
    P_matrix = transformation_matrix(0.01,0.02,0.03)
    
    while run:
        win.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        #### computation ####
        for i in range(len(edges)):
            edges[i,0] = edges[i,0]@P_matrix
            edges[i,1] = edges[i,1]@P_matrix
        #### drawing #####
        for edge in edges:
            pg.draw.line(win,(255,255,255),edge[0,:2]+ np.array([WIDTH//2,HEIGH//2]) ,edge[1,:2]+ np.array([WIDTH//2,HEIGH//2]) )
        
        ### delay ###
        pg.time.delay(10)
        pg.display.update()


if __name__ == '__main__':
    visualisation()