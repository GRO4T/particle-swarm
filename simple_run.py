import numpy as np

from particle_swarm import ParticleSwarm


def f(x,y):
    "Objective function"
    return (x-3.14)**2 + (y-2.72)**2 + np.sin(3*x+1.41) + np.sin(4*y-1.73)


p = ParticleSwarm(20, f)
for i in range(20):
    p.update()
