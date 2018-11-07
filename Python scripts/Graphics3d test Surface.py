#Graphics3d test
from Libraries.graphics3d import *
import pygame
import math

pygame.init()
clock = pygame.time.Clock()
#Verticies of cube
cube = [[1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]
#Indicies of edges of cube
edges = [[6,4], [0,4], [0,2], [2,6], [7,3], [3,1], [1,5], [5,7], [7,6], [3,2], [1,0], [5,4]]
#surface indicies with colours
surfaces = [[7,3,2,6, pygame.Color(0,255,255,150)],
            [5,1,0,4, pygame.Color(255,0,255,150)],
            [3,1,0,2, pygame.Color(255,255,0,150)],
            [7,5,4,6, pygame.Color(0,0,255,150)],
            [6,4,0,2, pygame.Color(0,255,0,150)],
            [7,3,1,5, pygame.Color(255,0,0,150)]]

#Normal startup
screen = pygame.display.set_mode([400,400])
screen.fill([255,255,255])

#Making matricies
s = Transformation("S", 3,3,3) #Scale
t = Transformation("T", 0,0,9) #Translate
rx = Transformation("Rx", 0.05)   #Rotation on x axis
ry = Transformation("Ry", 0.05)#Rotation on y axis
rz = Transformation("Rz", 0.02)   #Rotation on z axis

#initial transformation
cube_trans = [Translate(Scale(point, s), t) for point in cube]

def graph2pyg(rcube):
    #converts output of graphics to pygame scren coords
    return [[int(x*100+200), int(y*100+200)] for x,y in rcube]

def rotate_cube(rcube):
    #Rotates cube by Rx,Ry,Rz
    return [Rotate([0,0,9], point, rx,ry,rz) for point in rcube]

def draw_cube(rcube):
    #Draws cube verticies onto screen
    for point in rcube:
        pygame.draw.circle(screen, [0,0,0], point, 8)

def draw_edges(rcube):
    #Draws edges of the cube
    
    for s,e in edges:
        pygame.draw.line(screen, [0,0,0], rcube[s], rcube[e])

def argsort(seq):
    #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    #by unutbu
    return sorted(range(len(seq)), key=seq.__getitem__)

def sort(seq, indicies):
    fin = []
    for i in indicies:
        fin.append(seq[i])
    return fin

def draw_surfaces(rcube, rotated):
    surface_middle = []
    temp = []
    temp2 = []
    for pointlist in surfaces:
        temp.append(pointlist[:4])
    for indicies in temp:
        for i in indicies:
            temp2.append(rotated[i])
        surface_middle.append(temp2)
        temp2 = []
    xtemp = []
    ytemp = []
    ztemp = []
    x = []
    y = []
    z = []
    for points in surface_middle:
        for point in points:
            #print(point)
            xtemp.append(point[0])
            ytemp.append(point[1])
            ztemp.append(point[2])
        x.append(xtemp)
        y.append(ytemp)
        z.append(ztemp)
        xtemp = []
        ytemp = []
        ztemp = []
    xsum = []
    ysum = []
    zsum = []
    for points in x:
        xsum.append(sum(points)/4)
    for points in y:
        ysum.append(sum(points)/4)
    for points in z:
        zsum.append(sum(points)/4)
    #print(xsum)
    to_argsort = list(map(lambda x,y,z: abs(x)+abs(y)+abs(z), xsum, ysum, zsum))
    #print(to_argsort)
    new_surfaces = sort(surfaces, argsort(to_argsort))[::-1][3:]
    #print(new_surfaces)
    #print(argsort(to_argsort))
    for pointlist in new_surfaces:
        pygame.draw.polygon(screen, pointlist[4],
                            [rcube[pointlist[0]],
                             rcube[pointlist[1]],
                             rcube[pointlist[2]],
                             rcube[pointlist[3]]])
##    for pointlist in surfaces:
##        temp_surface = pygame.Surface((400,400), pygame.SRCALPHA, 32)
##        #temp_surface.set_alpha(100)
##        #temp_surface.fill([255,255,255, 255])
##        pygame.draw.polygon(temp_surface, pointlist[4],
##                            [rcube[pointlist[0]],
##                             rcube[pointlist[1]],
##                             rcube[pointlist[2]],
##                             rcube[pointlist[3]]])
##        screen.blit(temp_surface, (0,0))

while True:
    #Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
    #apply rotation
    rotated = rotate_cube(cube_trans)
    #Project points then convert to pygame screen coords
    gr = graph2pyg([Project(point) for point in rotated])
    #Draw
    draw_surfaces(gr, rotated)
    #draw_cube(gr)
    #draw_edges(gr)
    #advance rotation
    cube_trans = rotated
    #update screen
    pygame.display.update()
    screen.fill([255,255,255])
    #fps
    clock.tick(30)
