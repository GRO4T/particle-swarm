import benchmark_functions as bf

func = bf.Schwefel(n_dimensions=2)

point = [25, -34.6]
print(func(point)) # results in -129.38197657025287

print(func.suggested_bounds())
#func.show(asHeatMap=True)

func.show(showPoints=func.minima())


