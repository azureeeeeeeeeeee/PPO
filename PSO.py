import numpy as np
import random
import matplotlib.pyplot as plt

# Fungsi Minimum
def f(x):
    return 3 * np.exp(x**3) - 2*x

# Inisiasi partikel, kecepatan, dan pbest
all_x = {f'x{i}': random.randint(0, 3) for i in range(3)}
all_v = {f'v{i}': 0 for i in range(3)}
pbest = {f'x{i}': None for i in range(3)}
temp = {f'x{i}': None for i in range(3)}


# Variabel
c1 = 0.5
c2 = 1
w = 1
gbest = None
gbest_value = []
ite = []

# Fungsi update PBest
def updatePBest(temp=temp, pbest=pbest):
    for key, value in all_x.items():
        temp[key] = f(value)

    for key in pbest:
        if pbest[key] is None or temp[key] <= pbest[key]:
            pbest[key] = all_x[key]

# Update GBest
def updateGBest():
    global gbest
    gbest = all_x[min(pbest, key=lambda k: pbest[k])]

# Update V
def updateV(v=all_v):
    for key in all_x:
        r1, r2 = random.random(), random.random()
        if pbest[key] is not None:
            all_v[f'v{key[1:]}'] = w * all_v[f'v{key[1:]}'] + c1 * r1 * (pbest[key] - all_x[key]) + c2 * r2 * (gbest - all_x[key])
        else:
            pass

# Update X
def updateX(all_x=all_x):
    for key in all_x:
        all_x[key] = all_x[key] + all_v[f'v{key[1:]}']

# Memulai Perhitungan
iters = int(input('Masukkan Jumlah Iterasi : '))
for i in range(1, iters+1):
    print(f'\niterasi {i}')

    print('Nilai X')
    for key, value in all_x.items():
        print(f'{key} : {value}')

    print('\nNilai f(xi)')
    for key, value in all_x.items():
        print(f'f({key}) : {f(value)}')

    print('\nNilai PBest')
    updatePBest()
    for key, value in pbest.items():
        print(f'{key} : {value}')

    updateGBest()
    print(f'\nGbest : {gbest}')
    print(f'\nNilai f(x) menggunakan GBest : \n{f(gbest)}')
    gbest_value.append(f(gbest))
    updateV()

    print('\nNilai V')
    for key, value in all_v.items():
        print(f'{key} : {value}')

    print('\n')
    updateX()
    ite.append(i)

plt.plot(ite, gbest_value)
plt.xlabel('Iterasi')
plt.ylabel('f(x) dengan GBest')
plt.show()