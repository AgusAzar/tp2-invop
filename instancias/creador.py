from random import sample, randint, random
import math
from itertools import product

def distancia_eucleideana(x, y):
    return int(math.sqrt((x[0] - y[0])** 2 + (x[1] - y[1])** 2))

n = 70
costo_repartidor = 5
dist_max = 80
cant_refrigerados = 5
cant_exclusivos = 1

costo_max_camion = 100

ids = [str(i) for i in range(1,n+1)]

# Primeras lineas de la entrada
file = open("instancia.txt", "w")
file.write(f"{n}\n")
file.write(f"{costo_repartidor}\n")
file.write(f"{dist_max}\n")
file.write(f"{cant_refrigerados}\n")
file.write("\n".join(sample(ids, cant_refrigerados)) + "\n")
file.write(f"{cant_exclusivos}\n")
file.write("\n".join(sample(ids, cant_exclusivos)) + "\n")

# Generar puntos aleatorios en una grilla
alto, ancho = 5*n, 5*n
grilla = [(i, j) for i, j in product(range(alto), range(ancho))]
puntos = sample(grilla, n)

# Lineas con los puntos, sus distancias y costos
for i, c_1 in enumerate(puntos):
    for j, c_2 in enumerate(puntos):
        if j <= i: continue
        dist = distancia_eucleideana(c_1, c_2)
        costo = randint(1, costo_max_camion)
        file.write(f"{i} {j} {dist} {costo}\n")

file.close()
