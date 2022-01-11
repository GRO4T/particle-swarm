import argparse
import time

from particle_swarm import ParticleSwarm
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v


stream = print


class ParticleSwarmRunner:
	obj_functions = {
		"schwefel":  schwefel_v,
		"easom": easom_v,
		"himmelblau": himmelblau_v,
		"hypersphere": hypersphere_v
	}

	omega_policies = {
		"random": lambda p: p.set_update_omega_randomly(),
		"iteration": lambda p: p.set_update_omega_iteration(),
		"max_iteration": lambda p: p.set_update_omega_max_iteration(),
	}

	stop_conditions = {
		"max_iteration": lambda p: p.stop_condition_max_iteration(),
		"best_value": lambda p: p.stop_condition_best_value(),
	}

	def __init__(self):
		self.parser = argparse.ArgumentParser(description="Runner for particle swarm algorithm")
		self.parser.add_argument("--tests", type=int, help="Number of tests", default=5)
		self.parser.add_argument("--particles", type=int, help="Number of particles", required=True)
		self.parser.add_argument("--obj_func", type=str, help="Objective function", required=True)
		self.parser.add_argument("--stop_cond", type=str, help="Stop condition", required=True)
		self.parser.add_argument("--omega_policy", type=str, help="Omega update policy", required=True)
		self.parser.add_argument("--mult", type=float, help="Multiplier", default=0.001)

		self.args = self.parser.parse_args()

	def run(self):
		iterations = list()
		global_mins = list()
		start = time.perf_counter()
		for i in range(self.args.tests):
			p = ParticleSwarm(n_particles=self.args.particles,
						  		objective_func=ParticleSwarmRunner.obj_functions[self.args.obj_func.lower()],
						  		iteration_multiplier=self.args.mult)
			ParticleSwarmRunner.omega_policies[self.args.omega_policy](p)
			while ParticleSwarmRunner.stop_conditions[self.args.stop_cond](p):
				p.update()
			iterations.append(p.iteration)
			global_mins.append(p.g_best_vals)
		stop = time.perf_counter()
		self.print_stats(self.args.obj_func.upper(), global_mins, iterations, stop, start)

	def print_stats(self, name, global_mins, iterations, stop, start):
		stream(f"{name} FUNCTION:")
		stream(f"{'Total time':35}: {stop - start:0.4f} seconds")
		stream(f"{'Found global minimum':35}: {sum(global_mins) / len(global_mins)}")
		stream(f"{'Average iterations of algorithm':35}: {sum(iterations) / len(iterations)} iterations")
		stream(f"{'Average time of algorithm':35}: {(stop - start) / self.args.tests:0.4f} seconds")


if __name__ == '__main__':
	ParticleSwarmRunner().run()
