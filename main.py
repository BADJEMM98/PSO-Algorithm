from random import random
from PSO import PSO

def cost_function(pos,target):
    total=0 
    for i in range(len(pos)):
        total+=(target[i]-pos[i])**2
    return total

if __name__ == "__main__":
    initial=[50+150*random(),50+150*random()]               # initial starting location [x1,x2...]
    # bounds=  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
    init_target = [60,100]
    PSO(costFunc=cost_function,target=init_target,num_particles=50,maxiter=30)