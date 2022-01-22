#!/bin/bash

TEST_NAME="animate"
echo "[TEST] $TEST_NAME"

if [ $# -gt 0 ] && [ $1 = "quick" ]; then
	echo "skipping"
	exit 0
fi

rm ./experiments/$TEST_NAME/*.log
rm ./experiments/$TEST_NAME/*.gif
rm ./experiments/$TEST_NAME/*.png

# python3 particle_swarm_runner.py --particles 20 --obj_func schwefel --limit 500 \
# 								 --gif 500 500 --frames 150 --omega_policy global_minimum

# python3 particle_swarm_runner.py --particles 20 --obj_func hypersphere --limit 10 \
# 								 --gif 10 10 --frames 150 --omega_policy max_iteration

# python3 particle_swarm_runner.py --particles 20 --obj_func himmelblau --limit 4 \
# 								 --gif 4 4 --frames 150 --omega_policy basic

# python3 particle_swarm_runner.py --particles 20 --obj_func easom --limit 100 \
# 								 --gif 100 100 --frames 150 --omega_policy iteration



python3 particle_swarm_runner.py --particles 20 --obj_func schwefel --limit 500 \
								 --gif 500 500 --frames 150 --omega_policy global_minimum

python3 particle_swarm_runner.py --particles 20 --obj_func schwefel --limit 500 \
								 --gif 500 500 --frames 150 --omega_policy iteration

python3 particle_swarm_runner.py --particles 20 --obj_func himmelblau --limit 4 \
								 --gif 4 4 --frames 150 --omega_policy global_minimum

python3 particle_swarm_runner.py --particles 20 --obj_func himmelblau --limit 4 \
								 --gif 4 4 --frames 150 --omega_policy iteration

mv logs/* 	./experiments/$TEST_NAME/
mv gifs/*	./experiments/$TEST_NAME/
mv graphs/* ./experiments/$TEST_NAME/