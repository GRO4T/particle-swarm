#!/bin/bash

TEST_NAME="animate"
echo "[TEST] $TEST_NAME"

rm ./experiments/$TEST_NAME/*.log
rm ./experiments/$TEST_NAME/*.gif
rm ./experiments/$TEST_NAME/*.png

python3 particle_swarm_runner.py --particles 50 --obj_func schwefel --limit 500 \
								 --gif 750 750 --frames 150 --omega_policy global_minimum

python3 particle_swarm_runner.py --particles 50 --obj_func hypersphere --limit 500 \
								 --gif 750 750 --frames 150 --omega_policy max_iteration

python3 particle_swarm_runner.py --particles 50 --obj_func himmelblau --limit 500 \
								 --gif 750 750 --frames 150 --omega_policy basic

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 500 \
								 --gif 750 750 --frames 150 --omega_policy iteration

mv logs/* 	./experiments/$TEST_NAME/
mv gifs/*	./experiments/$TEST_NAME/
mv graphs/* ./experiments/$TEST_NAME/