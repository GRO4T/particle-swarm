#!/bin/bash

TEST_NAME="convergence"
echo "[TEST] $TEST_NAME"

rm ./experiments/$TEST_NAME/*.log
rm ./experiments/$TEST_NAME/*.gif
rm ./experiments/$TEST_NAME/*.png

python3 particle_swarm_runner.py --particles 50 --obj_func schwefel --limit 500 \
								 --stop_cond max_iteration --max_iteration 10000 \
								 --graph --omega_policy basic

python3 particle_swarm_runner.py --particles 50 --obj_func himmelblau --limit 500 \
								 --stop_cond max_iteration --max_iteration 10000 \
								 --graph --omega_policy basic

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 500 \
								 --stop_cond max_iteration --max_iteration 10000 \
								 --graph --omega_policy basic

python3 particle_swarm_runner.py --particles 50 --obj_func hypersphere --limit 500 \
								 --stop_cond max_iteration --max_iteration 10000 \
								 --graph --omega_policy basic

mv logs/* 	./experiments/$TEST_NAME/
mv gifs/*	./experiments/$TEST_NAME/
mv graphs/* ./experiments/$TEST_NAME/