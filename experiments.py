from particle_swarm import ParticleSwarm
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v

NUM_OF_TESTS = 1000
NUM_OF_PARTICLES = 20

def experiments_basic(name, func_v):
    iterations = list()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations")
