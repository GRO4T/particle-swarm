# Repozytorium projektu z przedmiotu Przeszukiwanie i optymalizacja [POP]
W ramach projektu będziemy badać zachowanie algorytmu roju cząstek (eng. particle swarm) przy różnym zachowaniu wartości współczynnika bezwładności.

## Uruchom testy
```
./clean.sh | true && time ./experiments/run_all.sh | tee experiments.log
```
Bez animacji
```
./clean.sh | true && time ./experiments/run_all.sh quick | tee experiments.log
```

## Wyniki stress testu
```
grep -r SUMMARY ./experiments/stress_test/*.log
```

## Przykładowe wywołania algorytmu
Graph
```
python3 particle_swarm_runner.py --particles 50 --obj_func schwefel --limit 500 \
								 --stop_cond max_iteration --max_iteration 1000 \
								 --graph --graph_omega --omega_policy global_minimum
```
Test
```
python3 particle_swarm_runner.py --particles 50 --obj_func schwefel --limit 500 \
								 --stop_cond max_iteration --max_iteration 1000 \
								 --test --tests 5 --omega_policy global_minimum
```
Animate
```
python3 particle_swarm_runner.py --particles 50 --obj_func schwefel --limit 500 \
								 --gif 750 750 --frames 150 --omega_policy global_minimum
```

## Wyczyść katalogi
```
rm gifs/* logs/* graphs/*
```