#!/bin/bash

# test
echo "Test different omega policies and stop conditions"
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy basic 			--stop_cond best_value
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy basic 			--stop_cond max_iteration	--max_iteration 1000
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy iteration		--stop_cond best_value
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy iteration 		--stop_cond max_iteration	--max_iteration 1000
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy random 			--stop_cond best_value
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy max_iteration 	--stop_cond best_value		--max_iteration 1000 --mult 1
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy max_iteration 	--stop_cond max_iteration 	--max_iteration 1000 --mult 1 

echo "Test different particle counts"
python3 particle_swarm_runner.py --test --tests 5 --particles 50  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	
python3 particle_swarm_runner.py --test --tests 5 --particles 60  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	
python3 particle_swarm_runner.py --test --tests 5 --particles 70  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	
python3 particle_swarm_runner.py --test --tests 5 --particles 80  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	
python3 particle_swarm_runner.py --test --tests 5 --particles 90  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	

echo "Graph"
python3 particle_swarm_runner.py --graph --particles 50  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	

echo "Animate"
python3 particle_swarm_runner.py --gif 10 10 --frames 100 --particles 50  --obj_func hypersphere --omega_policy random			--stop_cond max_iteration	--max_iteration 1000	