from benchmark_functions.benchmark_functions import Hypersphere
import numpy as np
from particle_swarm import ParticleSwarm
import benchmark_functions as bf
from experiments import experiments_basic, experiments_basic_max_iteration, experiments_iteration, experiments_iteration_max_iteration, experiments_max_iteration, experiments_randomly, experiments_mean_iteration, experiments_randomly_max_iteration
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v

HYPERSPHERE = "HYPERSPHERE"
EASOM = "EASOM"
HIMMELBLAU = "HIMMELBLAU"
SCHWEFEL = "SCHWEFEL"

def main():
    np.random.seed(100)
    
    print("Basic experiments:")
    experiments_basic(HYPERSPHERE, hypersphere_v)
    experiments_basic(EASOM, easom_v)
    experiments_basic(HIMMELBLAU, himmelblau_v)
    experiments_basic(SCHWEFEL, schwefel_v)
    
    print("\nExperiments with updating omega randomly:")
    experiments_randomly(HYPERSPHERE, hypersphere_v)
    experiments_randomly(EASOM, easom_v)
    experiments_randomly(HIMMELBLAU, himmelblau_v)
    experiments_randomly(SCHWEFEL, schwefel_v)

    print("\nExperiments with updating omega randomly with max iteration:")
    experiments_randomly_max_iteration(HYPERSPHERE, hypersphere_v)
    experiments_randomly_max_iteration(EASOM, easom_v)
    experiments_randomly_max_iteration(HIMMELBLAU, himmelblau_v)
    experiments_randomly_max_iteration(SCHWEFEL, schwefel_v)

    print("\nBasic experiments with max iteration:")
    experiments_basic_max_iteration(HYPERSPHERE, hypersphere_v)
    experiments_basic_max_iteration(EASOM, easom_v)
    experiments_basic_max_iteration(HIMMELBLAU, himmelblau_v)
    experiments_basic_max_iteration(SCHWEFEL, schwefel_v)
    
    print("\nExperiments with updating omega based on iteration:")
    for multiplier in (0.0001, 0.0005, 0.001, 0.005, 0.01):
        print("Multiplier:", multiplier)
        experiments_iteration(HYPERSPHERE, hypersphere_v, multiplier)
        experiments_iteration(EASOM, easom_v, multiplier)
        experiments_iteration(HIMMELBLAU, himmelblau_v, multiplier)
        experiments_iteration(SCHWEFEL, schwefel_v, multiplier)
    
    print("\nExperiments with updating omega based on iteration with max iteration:")
    for multiplier in (0.0001, 0.0005, 0.001):
        print("Multiplier:", multiplier)
        experiments_iteration_max_iteration(HYPERSPHERE, hypersphere_v, multiplier)
        experiments_iteration_max_iteration(EASOM, easom_v, multiplier)
        experiments_iteration_max_iteration(HIMMELBLAU, himmelblau_v, multiplier)
        experiments_iteration_max_iteration(SCHWEFEL, schwefel_v, multiplier)
    
    print("\nExperiments with updating omega basen on mean iterations")
    experiments_mean_iteration(HYPERSPHERE, hypersphere_v, 40)
    experiments_mean_iteration(EASOM, easom_v, 40)
    experiments_mean_iteration(HIMMELBLAU, himmelblau_v, 40)
    experiments_mean_iteration(SCHWEFEL, schwefel_v, 40)

    print("\nExperiments with updating omega based on max iteration:")
    experiments_max_iteration(HYPERSPHERE, hypersphere_v, 1000)
    experiments_max_iteration(EASOM, easom_v, 1000)
    experiments_max_iteration(HIMMELBLAU, himmelblau_v, 1000)
    experiments_max_iteration(SCHWEFEL, schwefel_v, 1000)
    
if __name__ == '__main__':
    main()
    
