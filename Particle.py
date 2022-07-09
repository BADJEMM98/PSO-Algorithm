from random import random, uniform,randint
from typing import List
import pygame


class Particle:
    def __init__(self,bounds:List[float],dim:int):
        self.position_i=[uniform(bounds[i][0],bounds[i][1]) for i in range(dim)]          
        self.velocity_i=[uniform(-1,1) for i in range(dim)]
        self.pos_best_i=[]         
        self.err_best_i=-1          
        self.err_i=-1  
        self.color = (randint(1,254),randint(1,254),randint(1,254))             

    def evaluate(self,costFunc,target):
        self.err_i=costFunc(self.position_i,target)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i


    def update_velocity(self,pos_best_g,dim):
        w=0.5       
        c1=1       
        c2=2        

        for i in range(0,dim):
            r1=random()
            r2=random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    def update_position(self,bounds,dim):
        for i in range(0,dim):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]

            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]

    def display(self,screen,):
        pygame.draw.circle(screen, self.color, self.position_i, 7, 0)