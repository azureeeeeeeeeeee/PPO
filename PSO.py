import numpy as np
import random

# Fungsi Minimum

def f(x):
    return 3 * np.exp(x**3) - 2*x

all_x = {f'x{i}': random.random() for i in range(1, 11)}
all_v = {f'v{i}': 0 for i in range(1, 11)}
pbest = {f'x{i}': None for i in range(1, 11)}
temp = {f'x{i}': None for i in range(1, 11)}


# Variabel
v = 0
c1 = 0.5
c2 = 1
w = 1
gbest = None

# Fungsi Bantuan
def updatePBest(temp=temp, pbest=pbest):
    for key, value in all_x.items():
        temp[key] = f(value)

    for key in pbest:
        if pbest[key] is None or temp[key] <= pbest[key]:
            pbest[key] = temp[key]

def updateGBest():
    global gbest
    gbest = all_x[min(pbest, key=lambda k: pbest[k])]

def updateV(v=all_v):
    for key in all_x:
        r1, r2 = random.random(), random.random()
        if pbest[key] is not None:
            all_v[f'v{key[1:]}'] = w * all_v[f'v{key[1:]}'] + c1 * r1 * (pbest[key] - all_x[key]) + c2 * r2 * (gbest - all_x[key])
        else:
            pass

def updateX(all_x=all_x):
    for key in all_x:
        all_x[key] = all_x[key] + all_v[f'v{key[1:]}']


for i in range(1, 4):
    print(f'iterasi {i}')

    print('\nNilai X')
    for key, value in all_x.items():
        print(f'{key} : {value}')

    print('\nPBest i')
    updatePBest()
    for key, value in pbest.items():
        print(f'{key} : {value}')

    updateGBest()
    print(f'\nGbest : {gbest}')
    updateV()

    for key, value in all_v.items():
        print(f'{key} : {value}')

    print('\n\n')
    updateX()