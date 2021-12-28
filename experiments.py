import time
from particle_swarm import ParticleSwarm
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v

NUM_OF_TESTS = 2000
NUM_OF_PARTICLES = 20

def experiments_basic(name, func_v):
    iterations = list()
    global_mins = list()
    start = time.perf_counter()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v)
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
        global_mins.append(p.g_best_vals)
    stop = time.perf_counter()
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations in {stop - start:0.4f} seconds")
    print(f"Found global minimum: {sum(global_mins) / len(global_mins)}")
    print(f"Average time of algorithm: {(stop - start) / NUM_OF_TESTS:0.4f} seconds")

def experiments_randomly(name, func_v):
    iterations = list()
    global_mins = list()
    start = time.perf_counter()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v)
        p.set_update_omega_randomly()
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
        global_mins.append(p.g_best_vals)
    stop = time.perf_counter()
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations in {stop - start:0.4f} seconds")
    print(f"Found global minimum: {sum(global_mins) / len(global_mins)}")
    print(f"Average time of algorithm: {(stop - start) / NUM_OF_TESTS:0.4f} seconds")

def experiments_iteration(name, func_v, iteration_multiplier):
    iterations = list()
    global_mins = list()
    start = time.perf_counter()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v, iteration_multiplier=iteration_multiplier)
        p.set_update_omega_iteration()
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
        global_mins.append(p.g_best_vals)
    stop = time.perf_counter()
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations in {stop - start:0.4f} seconds")
    print(f"Found global minimum: {sum(global_mins) / len(global_mins)}")
    print(f"Average time of algorithm: {(stop - start) / NUM_OF_TESTS:0.4f} seconds")

def experiments_max_iteration(name, func_v, max_iteration):
    iterations = list()
    global_mins = list()
    start = time.perf_counter()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v, max_iteration=max_iteration)
        p.set_update_omega_max_iteration()
        while p.stop_condition_max_iteration():
            p.update()
        iterations.append(p.iteration)
        global_mins.append(p.g_best_vals)
    stop = time.perf_counter()
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations in {stop - start:0.4f} seconds")
    print(f"Found global minimum: {sum(global_mins) / len(global_mins)}")
    print(f"Average time of algorithm: {(stop - start) / NUM_OF_TESTS:0.4f} seconds")

def experiments_mean_iteration(name, func_v, mean_iteration):
    iterations = list()
    global_mins = list()
    start = time.perf_counter()
    for i in range(NUM_OF_TESTS):
        p = ParticleSwarm(NUM_OF_PARTICLES, func_v, mean_iteration=mean_iteration)
        p.set_update_omega_mean_iteration()
        while p.stop_condition_best_value():
            p.update()
        iterations.append(p.iteration)
        global_mins.append(p.g_best_vals)
    stop = time.perf_counter()
    print(f"{name} function : {sum(iterations) / len(iterations)} iterations in {stop - start:0.4f} seconds")
    print(f"Found global minimum: {sum(global_mins) / len(global_mins)}")
    print(f"Average time of algorithm: {(stop - start) / NUM_OF_TESTS:0.4f} seconds")

