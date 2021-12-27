from particle_swarm import ParticleSwarm
from test_functions import hypersphere_v, easom_v, himmelblau_v, schwefel_v


p = ParticleSwarm(20, hypersphere_v)
for i in range(20):
    p.update()


p = ParticleSwarm(20, easom_v)
for i in range(20):
    p.update()


p = ParticleSwarm(20, himmelblau_v)
for i in range(20):
    p.update()


p = ParticleSwarm(20, schwefel_v)
for i in range(20):
    p.update()
