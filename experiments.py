from particle_swarm import ParticleSwarm
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v

NUM_OF_TESTS = 1000
NUM_OF_PARTICLES = 20

def experiments_hypersphere_basic():
    iterations = list()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, hypersphere_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
    print(sum(iterations) / len(iterations))

def experiments_easom_basic():
    iterations = list()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, easom_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
    print(sum(iterations) / len(iterations))

def experiments_himmelblau_basic():
    iterations = list()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, himmelblau_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
    print(sum(iterations) / len(iterations))

def experiments_schwefel_basic():
    iterations = list()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, schwefel_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
    print(sum(iterations) / len(iterations))
