import numpy as np
import logging

from logger import configure_logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
configure_logging()



class ParticleSwarm:
    def __init__(self, n_particles: int, objective_func, w: float = 0.8, c_local: float = 0.1, c_global: float = 0.1):
        """
        Parameters
        ----------
        n_particles: int
            liczba cząstek
        objective_func: function
            funkcja celu
        w: float
            współczynnik bezwładności
        c_local: float
            współczynnik przyciągania do lokalnego rozwiązania
        c_global: float
            współczynnik przyciągania do globalengo rozwiązania
        """
        self.X = np.random.rand(2, n_particles) * 5
        self.V = np.random.randn(2, n_particles) * 0.1
        self.obj_func = objective_func
        self.l_best_X = self.X 
        self.l_best_vals = self.obj_func(self.X[0], self.X[1]) 
        self.g_best_X = self.l_best_X[:, self.l_best_vals.argmin()]
        self.g_best_vals = self.l_best_vals.min()
        self.w = w
        self.c_l = c_local
        self.c_g = c_global
        self.iteration = 0
        logger.debug(f"positions={self.X}")
        logger.debug(f"velocities={self.V}")
        logger.debug(f"local_best_positions={self.l_best_X}")
        logger.debug(f"local_best_values={self.l_best_vals}")
        logger.info(f"global_best_position={self.g_best_X}")
        logger.info(f"global_best_value={self.g_best_vals}")
        logger.debug(type(self.g_best_X))
        logger.debug(type(self.g_best_vals))

    def update(self, animate: bool = False):
        """
        Parameters
        ----------
        animate: bool
            flaga mówiąca o tym czy powinniśmy utworzyć animowany GIF prezentujący przebieg algorytmu
        """
        r1, r2 = np.random.rand(2)
        self.V = self.w * self.V \
                 + self.c_l * r1 * (self.l_best_X - self.X) \
                 + self.c_g * r2 * (self.g_best_X.reshape(-1, 1) - self.X)
        self.X = self.X + self.V
        new_obj_func_vals = self.obj_func(self.X[0], self.X[1])
        self.l_best_X[:, (self.l_best_vals >= new_obj_func_vals)] = self.X[:, (self.l_best_vals >= new_obj_func_vals)]
        self.l_best_vals = np.array([self.l_best_vals, new_obj_func_vals]).min(axis=0)
        self.g_best_X = self.l_best_X[:, self.l_best_vals.argmin()]
        self.g_best_vals = self.l_best_vals.min()

        self.iteration += 1
        logger.info(f"Iteration: {self.iteration}")
        logger.info(f"global_best_position={self.g_best_X}")
        logger.info(f"global_best_value={self.g_best_vals}")
