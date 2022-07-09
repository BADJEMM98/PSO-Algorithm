from random import random
from turtle import update
from typing import List
from Particle import Particle
import pygame

WIDTH,HEIGHT=500,500
pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Interactive PSO Algorithm")
clock = pygame.time.Clock()
BGCOLOR = (255,255,255)

def display_target(target_pos:List[float]):
    pygame.draw.circle(WIN,(0,0,0,250), tuple(target_pos), 15, 0)

def draw_window(swarm:List[Particle],target_pos:List[float]):
    WIN.fill(BGCOLOR)
    clock.tick(20)
    for particle in swarm:
        particle.display(WIN)
    display_target(target_pos=target_pos)
    pygame.display.update()


class PSO():
    def __init__(self,costFunc,target,num_particles,maxiter,bounds=[(-WIDTH,WIDTH),(-HEIGHT,HEIGHT)]):
        global dim

        dim=len(target)
        err_best_g=-1                   
        pos_best_g=[]
        self.gamma = 0.0001                   

        swarm=[Particle(bounds=bounds,dim=dim) for i in range(num_particles)]

        run = True
        while run:
            i=0
            while i < maxiter:
                restart=False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        target = [event.pos[0],event.pos[1]]
                        restart = True
                        draw_window(swarm,target)

                    for j in range(0,num_particles):
                        swarm[j].evaluate(costFunc,target)

                        # determine if current particle is the best (globally)
                        if swarm[j].err_i < err_best_g or err_best_g == -1:
                            pos_best_g=list(swarm[j].position_i)
                            err_best_g=float(swarm[j].err_i)

                        if restart:
                            err_best_g=-1
                            pos_best_g = [swarm[j].position_i[idx]+self.gamma*(swarm[j].err_i)*random() for idx in range(0,dim)]
                        


                            
                    print("evaluation :",i)

                    # cycle through swarm and update velocities and position
                    for j in range(0,num_particles):
                        swarm[j].update_velocity(pos_best_g,dim)
                        swarm[j].update_position(bounds,dim)

                    print("update :",i)
                    for part in swarm:
                        print(part.position_i)
                    draw_window(swarm,target)

                i+=1
                if run==False:
                    break
