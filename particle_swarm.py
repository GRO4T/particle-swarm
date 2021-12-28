import numpy as np
import logging

from logger import configure_logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
configure_logging()

logging.debug("Start")

class ParticleSwarm:
    def __init__(self, n_particles: int, objective_func, w: float = 0.8, c_local: float = 0.1, c_global: float = 0.1, 
                max_iteration: int = 100, mean_iteration: int = 100, iteration_multiplier: float = 0.001):
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
        max_iteration: int
            maksymalna liczba iteracji algorytmu
        """
        self.X = np.random.rand(2, n_particles) * 5
        self.V = np.random.randn(2, n_particles) * 0.1
        self.obj_func = objective_func
        self.l_best_X = self.X 
        self.l_best_vals = self.obj_func(self.X[0], self.X[1]) 
        self.g_best_X = self.l_best_X[:, self.l_best_vals.argmin()]
        self.g_best_vals = self.l_best_vals.min()
        self.last_g_best_vals = list()
        self.w = w
        self.c_l = c_local
        self.c_g = c_global
        self.iteration = 0
        self.max_iteration = max_iteration
        self.mean_iteration = mean_iteration
        self.multiplier = iteration_multiplier
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
        self.update_omega()
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
        self.add_g_best_val()
        self.iteration += 1
        logger.info(f"Iteration: {self.iteration}")
        logger.info(f"global_best_position={self.g_best_X}")
        logger.info(f"global_best_value={self.g_best_vals}")

    def update_omega(self):
        pass

    def update_omega_randomly(self):
        self.w = np.random.random()

    def update_omega_max_iteration(self):
        self.w = 1 - self.iteration / self.max_iteration * 0.5

    def update_omega_mean_iteration(self):
        self.w = 1 - self.iteration / self.mean_iteration * 0.5

    def update_omega_iteration(self):
        self.w = 1 - self.iteration * self.multiplier

    def set_update_omega_randomly(self):
        self.update_omega = self.update_omega_randomly

    def set_update_omega_max_iteration(self):
        self.update_omega = self.update_omega_max_iteration

    def set_update_omega_mean_iteration(self):
        self.update_omega = self.update_omega_mean_iteration

    def set_update_omega_iteration(self):
        self.update_omega = self.update_omega_iteration

    def add_g_best_val(self):
        if len(self.last_g_best_vals) == 10:
            del self.last_g_best_vals[0]
        self.last_g_best_vals.append(self.g_best_vals)

    def stop_condition_max_iteration(self):
        return self.iteration < self.max_iteration

    def stop_condition_best_value(self):
        if len(self.last_g_best_vals) < 10:
            return True
        return abs(sum(self.last_g_best_vals) / 10 - self.g_best_vals) >= 0.000000001


