#!/bin/bash
python3 particle_swarm_runner.py --particles 50  --obj_func schwefel --stop_cond best_value --omega_policy random
python3 particle_swarm_runner.py --particles 60  --obj_func schwefel --stop_cond best_value --omega_policy random
python3 particle_swarm_runner.py --particles 70  --obj_func schwefel --stop_cond best_value --omega_policy random
python3 particle_swarm_runner.py --particles 80  --obj_func schwefel --stop_cond best_value --omega_policy random
python3 particle_swarm_runner.py --particles 90  --obj_func schwefel --stop_cond best_value --omega_policy random
python3 particle_swarm_runner.py --particles 100 --obj_func schwefel --stop_cond best_value --omega_policy random