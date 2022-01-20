import numpy as np
import logging
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from logger import configure_logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ParticleSwarm:
    def __init__(self, n_particles: int, objective_func, w: float = 0.8, c_local: float = 0.1, c_global: float = 0.1, 
                max_iteration: int = 100, mean_iteration: int = 100, iteration_multiplier: float = 0.001, 
                global_multiplier: float = 0.1, pos: int = 5):
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
        iteration_multiplier: float
            współczynnik przez który mnożony jest numer iteracji
            podczas zmieniania wawrtości omega na podstawie
            numeru iteracji
        pos: int
            odległość od punktu (0, 0) na której mogą pojawić się
            cząsteczki na początku algorytmu
        """
        self.X = np.random.uniform(-pos, pos, (2, n_particles))
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
        self.global_multiplier = global_multiplier
        logger.debug(f"positions={self.X}")
        logger.debug(f"velocities={self.V}")
        logger.debug(f"local_best_positions={self.l_best_X}")
        logger.debug(f"local_best_values={self.l_best_vals}")
        logger.debug(f"global_best_position={self.g_best_X}")
        logger.debug(f"global_best_value={self.g_best_vals}")
        logger.debug(type(self.g_best_X))
        logger.debug(type(self.g_best_vals))

    def prepare_animation(self):
        self.x, self.y = np.array(np.meshgrid(np.linspace(-self.xlim,self.xlim,400), np.linspace(-self.ylim,self.ylim,400)))
        z = np.array(self.obj_func(self.x, self.y), dtype=np.float64)
        self.x_min = self.x.ravel()[z.argmin()]
        self.y_min = self.y.ravel()[z.argmin()]

        self.fig, self.ax = plt.subplots(figsize=(8,6))
        self.fig.set_tight_layout(True)
        img = self.ax.imshow(z, extent=[-self.xlim, self.xlim, -self.ylim, self.ylim], origin='lower', cmap='viridis', alpha=0.5)
        self.fig.colorbar(img, ax=self.ax)
        self.ax.plot([self.x_min], [self.y_min], marker='x', markersize=5, color="white")
        contours = self.ax.contour(self.x, self.y, z, 10, colors='black', alpha=0.4)
        self.ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
        self.pbest_plot = self.ax.scatter(self.l_best_X [0], self.l_best_X[1], marker='o', color='black', alpha=0.5)
        self.p_plot = self.ax.scatter(self.X[0], self.X[1], marker='o', color='blue', alpha=0.5)
        self.p_arrow = self.ax.quiver(self.X[0], self.X[1], self.V[0], self.V[1], color='blue', width=0.005, angles='xy', scale_units='xy', scale=1)
        self.gbest_plot = plt.scatter([self.g_best_X[0]], [self.g_best_X[1]], marker='*', s=100, color='black', alpha=0.4)
        self.ax.set_xlim([-self.xlim,self.xlim])
        self.ax.set_ylim([-self.ylim,self.ylim])

    def set_animation_params(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim

    def update(self):
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
        logger.debug(f"Iteration: {self.iteration}")
        logger.debug(f"global_best_position={self.g_best_X}")
        logger.debug(f"global_best_value={self.g_best_vals}")

    def animate(self, i):
        title = 'Iteration {:02d}'.format(i)
        self.update()
        self.ax.set_title(title)
        self.pbest_plot.set_offsets(self.l_best_X.T)
        self.p_plot.set_offsets(self.X.T)
        self.p_arrow.set_offsets(self.X.T)
        self.p_arrow.set_UVC(self.V[0], self.V[1])
        self.gbest_plot.set_offsets(self.g_best_X.reshape(1,-1))
        return self.ax, self.pbest_plot, self.p_plot, self.p_arrow, self.gbest_plot

    def animation(self, path, frames):
        anim = FuncAnimation(self.fig, self.animate, frames=list(range(1,frames)), interval=500, blit=False, repeat=True)
        my_writer=PillowWriter(fps=5, codec='libx264', bitrate=2)
        anim.save(filename=path, writer=my_writer)

    def update_omega(self):
        pass

    def update_omega_randomly(self):
        self.w = np.random.uniform(0, 1)
        logger.debug(f"w={self.w}")

    def update_omega_max_iteration(self):
        self.w = 1 - self.multiplier * (self.iteration / self.max_iteration * 0.5)
        logger.debug(f"w={self.w}")

    def update_omega_mean_iteration(self):
        self.w = 1 - self.iteration / self.mean_iteration * 0.5
        logger.debug(f"w={self.w}")

    def update_omega_iteration(self):
        self.w = 1 - self.iteration * self.multiplier
        logger.debug(f"w={self.w}")

    def update_omega_global_minimum(self):
        dist = np.linalg.norm(self.g_best_X - np.array([np.mean(self.X[0]), np.mean(self.X[1])]))
        self.w = min(dist / 20, 1)
        logger.debug(f"w={self.w}")

    def update_omega_global_minimum_max_iteration(self):
        dist = np.linalg.norm(self.g_best_X - np.array([np.mean(self.X[0]), np.mean(self.X[1])]))
        self.w = dist * (self.iteration / self.max_iteration) * self.global_multiplier
        logger.debug(f"w={self.w}")

    def set_update_omega_randomly(self):
        self.update_omega = self.update_omega_randomly

    def set_update_omega_max_iteration(self):
        self.update_omega = self.update_omega_max_iteration

    def set_update_omega_mean_iteration(self):
        self.update_omega = self.update_omega_mean_iteration

    def set_update_omega_iteration(self):
        self.update_omega = self.update_omega_iteration

    def set_update_omega_global_minimum(self):
        self.update_omega = self.update_omega_global_minimum

    def set_update_omega_global_minimum_max_iteration(self):
        self.update_omega = self.update_omega_global_minimum_max_iteration

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
