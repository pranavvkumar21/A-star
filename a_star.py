#!/usr/bin/env python3
import sys, pygame, math
import numpy as np
import time
import random

X=30
Y=30
start = (3,27)
goal = (27,3)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
width,height = SCREEN_WIDTH//X,SCREEN_HEIGHT//Y
#class for each node in the grid_map
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class node:
    def __init__(self,x,y,width,height):
        self.id = int(str(x)+str(y))
        self.surf = pygame.Surface((width,height))
        self.surf.fill((255, 255, 255))
        pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)
        self.obstructed = 0
        self.x = x
        self.y = y
        self.parent = -1
        self.g = -1
        self.h = -1
        self.status = 'u'
        self.f = -1

    def __repr__(self):
        return str(self.id)
    def __call__(self):
        return (self.x,self.y)
    def change_color(self,color):
        if color=="g":
            self.surf.fill((0, 255, 0))
            pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)
        elif color=="b":
            self.surf.fill((0, 0, 255))
            pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)
        elif color=="r":
            self.surf.fill((255, 0, 0))
            pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)
        elif color=="y":
            self.surf.fill((255, 255, 0))
            pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)
        elif color=="b0":
            self.surf.fill((0, 0, 0))
            pygame.draw.rect(self.surf, (0,0,0), [0, 0, width, height], 1)


#function to get distance between points
def distance(initial,final):
    return math.sqrt((final.x-initial.x)**2+(final.y-initial.y)**2)
#function to get neighbors
def get_neighbors(current,X,Y):
    neigh = []
    neigh.append(int(str(current.x)+"00"+str(current.y-1))) if current.y>0 else 0
    neigh.append(int(str(current.x)+"00"+str(current.y+1))) if current.y<Y-1 else 0
    neigh.append(int(str(current.x-1)+"00"+str(current.y-1))) if current.y>0 and current.x>0 else 0
    neigh.append(int(str(current.x-1)+"00"+str(current.y+1))) if current.y<Y-1 and current.x>0 else 0
    neigh.append(int(str(current.x+1)+"00"+str(current.y-1))) if current.y>0 and current.x<X-1 else 0
    neigh.append(int(str(current.x+1)+"00"+str(current.y+1))) if current.y<Y-1 and current.x<X-1 else 0
    neigh.append(int(str(current.x-1)+"00"+str(current.y))) if current.x>0 else 0
    neigh.append(int(str(current.x+1)+"00"+str(current.y))) if current.x<X-1 else 0
    for i in neigh:
        if grid_map[i].status == "o":
            neigh.remove(i)
    return neigh
#function to get node with lowest f score
def get_lowestf(open_set):
    lowest_id = open_set[0]
    lowest_score = grid_map[open_set[0]].f
    for i,elem in enumerate(open_set):
        if grid_map[elem].f<=lowest_score and grid_map[elem].f!=-1:
            lowest_score = grid_map[elem].f
            lowest_id = open_set[i]
    return lowest_id



# create grid_map as a dictionary
def create_obstruction():
    for elem in grid_map.keys():
        if random.random()<0.3:
            grid_map[elem].status = "o"
            grid_map[elem].change_color("b0")
    update()

def reconstruct_path(current,start,goal):
    #start = int(str(start[0])+str(start[1]))
    #goal = int(str(goal[0])+str(goal[1]))
    path  = [current]
    while current!=start:
        current = grid_map[current].parent
        path.insert(0,current)
        #print(path)
    return path

grid_map = {}
for i in range(X):
    for j in range(Y):
        grid_map[int(str(i)+"00"+str(j))]=node(i,j,width,height)
        screen.blit(grid_map[int(str(i)+"00"+str(j))].surf,(i*width,j*height))
#print(grid_map)
#update screen
def update():
    for i in range(X):
        for j in range(Y):
            screen.blit(grid_map[int(str(i)+"00"+str(j))].surf,(i*width,j*height))
            pygame.display.flip()
pygame.display.flip()
def A_star(grid_map,start,goal):
    create_obstruction()
    start = int(str(start[0])+"00"+str(start[1]))
    goal = int(str(goal[0])+"00"+str(goal[1]))

    open_set = [start]
    closed_set = []
    grid_map[start].g = 0
    grid_map[start].status = "u"
    grid_map[goal].status = "u"
    grid_map[start].f = distance(grid_map[start],grid_map[goal])
    grid_map[start].change_color("b")
    grid_map[goal].change_color("g")
    #screen.blit(grid_map[start].surf,(grid_map[start].x*width,grid_map[start].y*height))
    update()
    time.sleep(2)
    while len(open_set)!=0:
        for element in open_set:
            #print(open_set)
            if element!=start or element!=goal:
                grid_map[element].change_color("y")
        for element in closed_set:
            if element!=start or element!=goal:
                grid_map[element].change_color("r")
        #update()
        current = get_lowestf(open_set)
        if current == goal:
            print("goal achieved")
            return reconstruct_path(current,start,goal)
        open_set.remove(current)
        closed_set.append(current)
        for neighbor in get_neighbors(grid_map[current],X,Y):
            if grid_map[neighbor].status == "o":
                continue
            if neighbor in closed_set:
                continue
            tentative_g_score = grid_map[current].g + distance(grid_map[current],grid_map[neighbor])
            if neighbor not in open_set:
                open_set.append(neighbor)
            elif tentative_g_score >= grid_map[neighbor].g:
                continue
            grid_map[neighbor].parent = current
            grid_map[neighbor].g = tentative_g_score
            grid_map[neighbor].f = tentative_g_score + distance(grid_map[neighbor],grid_map[goal])
    #return -1    #print(1)
path = A_star(grid_map,start,goal)
for p in path:
    grid_map[p].change_color("g")
update()
time.sleep(7)
