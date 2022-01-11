import logging
from benchmark_functions.benchmark_functions import Hypersphere
import numpy as np
from particle_swarm import ParticleSwarm
import benchmark_functions as bf
from experiments import experiments_basic, experiments_basic_max_iteration, experiments_iteration, experiments_iteration_max_iteration, experiments_max_iteration, experiments_randomly, experiments_mean_iteration, experiments_randomly_max_iteration
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


HYPERSPHERE = "HYPERSPHERE"
EASOM = "EASOM"
HIMMELBLAU = "HIMMELBLAU"
SCHWEFEL = "SCHWEFEL"


def main():
    np.random.seed(100)

    # print(f"Animation {SCHWEFEL}")
    # p = ParticleSwarm(100, schwefel_v)
    # p.set_animation_params(750, 750)
    # p.prepare_animation()
    # p.set_update_omega_randomly()
    # p.animation(SCHWEFEL + "_rand.gif", 100)

    # print(f"Animation {SCHWEFEL}")
    # p = ParticleSwarm(100, schwefel_v)
    # p.set_animation_params(750, 750)
    # p.prepare_animation()
    # p.animation(SCHWEFEL + ".gif", 100)

    print(f"Animation {SCHWEFEL} it")
    logger.debug(f"Animation {SCHWEFEL} it")
    p = ParticleSwarm(100, schwefel_v, iteration_multiplier=1)
    p.set_animation_params(750, 750)
    p.prepare_animation()
    p.set_update_omega_iteration()
    p.animation(SCHWEFEL + "_it.gif", 100)

    print(f"Animation {SCHWEFEL} max it")
    logger.debug(f"Animation {SCHWEFEL} max it")
    p = ParticleSwarm(100, schwefel_v, iteration_multiplier=5)
    p.set_animation_params(750, 750)
    p.prepare_animation()
    p.set_update_omega_max_iteration()
    p.animation(SCHWEFEL + "_max_it.gif", 100)
    
if __name__ == '__main__':
    main()
    
