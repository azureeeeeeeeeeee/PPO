import numpy as np
import random

# Fungsi Minimum
def f(x):
    return 3 * np.exp(x**3) - 2*x

# Inisiasi partikel, kecepatan, dan pbest
all_x = {f'x{i}': random.randint(1, 10) for i in range(1, 11)}
all_v = {f'v{i}': 0 for i in range(1, 11)}
pbest = {f'x{i}': None for i in range(1, 11)}
temp = {f'x{i}': None for i in range(1, 11)}


# Variabel
c1 = 0.5
c2 = 1
w = 1
gbest = None
isConvergen = False


# Fungsi update PBest
def updatePBest(temp=temp, pbest=pbest):
    global all_gbest_value
    for key, value in all_x.items():
        temp[key] = f(value)

    for key in pbest:
        if pbest[key] is None or temp[key] <= pbest[key]:
            pbest[key] = all_x[key]

# Update GBest
def updateGBest():
    global gbest
    global isConvergen
    temp_gbest = all_x[min(pbest, key=lambda k: pbest[k])]
    if temp_gbest == gbest:
        isConvergen = True
    else:
        gbest = temp_gbest

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
    print(f'iterasi {i}')

    print('Nilai X')
    for key, value in all_x.items():
        print(f'{key} : {value}')

    print('\nNilai f(x)')
    for key, value in all_x.items():
        print(f'{key} : {f(value)}')

    print('\nNilai PBest')
    updatePBest()
    for key, value in pbest.items():
        print(f'{key} : {value}')

    updateGBest()
    print(f'\nGbest : {gbest}')
    if isConvergen:
        print('\nFungsi telah konvergen')
        break
    updateV()

    print('\nNilai V')
    for key, value in all_v.items():
        print(f'{key} : {value}')

    print('\nUpdate X dengan\nxi = xi + vi')

    print('\n\n')
    updateX()