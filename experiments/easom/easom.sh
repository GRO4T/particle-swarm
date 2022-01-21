#!/bin/bash

TEST_NAME="easom"
echo "[TEST] $TEST_NAME"

rm ./experiments/$TEST_NAME/*.log
rm ./experiments/$TEST_NAME/*.gif
rm ./experiments/$TEST_NAME/*.png

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy basic

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy random 

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy iteration

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy max_iteration --mult 1

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy global_minimum

python3 particle_swarm_runner.py --particles 50 --obj_func easom --limit 100 \
								 --stop_cond max_iteration --max_iteration 100 \
								 --graph --graph_omega --omega_policy global_minimum_iteration

mv logs/* 	./experiments/$TEST_NAME/
mv gifs/*	./experiments/$TEST_NAME/
mv graphs/* ./experiments/$TEST_NAME/