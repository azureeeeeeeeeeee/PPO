import numpy as np
import random
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(2*x + y) + (x - y)**2 - 3.5*x + 5.5*y + 1

all_xy = {f'xy{i}': {'x': random.randint(1,10), 'y': random.randint(1, 10)} for i in range(1, 11)}
all_v = {f'v{i}': {'vx': 0, 'vy': 0} for i in range(1, 11)}
pbest = {f'xy{i}': None for i in range(1, 11)}
temp = {f'xy{i}': None for i in range(1, 11)}

# Variabel
c1 = 1
c2 = 0.5
w = 1
gbest = None
isConvergen = False

# Mencari PBest untuk setiap x
def updatePBest(all_xy=all_xy, temp=temp, pbest=pbest):
    # Mencari nilai f(x, y) untuk setiap (x, y)
    for key, value in all_xy.items():
        temp[key] = f(value['x'], value['y'])
    
    # Update nilai PBest
    for key, value in temp.items():
        if pbest[key] is None or temp[key] < pbest[key]:
            pbest[key] = temp[key]

def updateGBest(all_xy=all_xy):
    global gbest
    global isConvergen
    temp_gbest = all_xy[min(pbest, key=lambda k: pbest[k])]
    if gbest == temp_gbest:
        isConvergen = True
    else:
        gbest = temp_gbest

def updateV(all_v=all_v, all_xy=all_xy, w=w, c1=c1, c2=c2):
    for key in all_v:
        r1 = random.random()
        r2 = random.random()
        
        index = int(key[1:])
        xi = all_xy[f'xy{index}']
        pbest_i = all_xy[f'xy{index}']

        # update v
        all_v[key]['vx'] = w * all_v[key]['vx'] + c1 * r1 * (pbest_i['x'] - xi['x']) + c2 * r2 * (gbest['x'] - xi['x'])
        all_v[key]['vy'] = w * all_v[key]['vy'] + c1 * r1 * (pbest_i['y'] - xi['y']) + c2 * r2 * (gbest['y'] - xi['y'])

def updateX(all_xy=all_xy, all_v=all_v):
    for key in all_xy:
        index = int(key[2:])
    
        all_xy[key]['x'] += all_v[f'v{index}'][f'vx']
        all_xy[key]['y'] += all_v[f'v{index}'][f'vy']


iterasi = int(input('Masukkan Jumlah Iterasi : '))

    
for i in range(1, iterasi+1):
    print(f'iterasi {i}')

    print('\n Nilai (x, y)')
    for key, value in all_xy.items():
        print(f"{key} : ({value['x']}, {value['y']})")

    print('\nNilai f(x, y)')
    for key, value in all_xy.items():
        print(f"{key} : {f(value['x'], value['y'])}")

    print('\nNilai PBest')
    updatePBest()
    for key, value in pbest.items():
        print(f'{key} : {value}')

    updateGBest()
    print(f"\nGbest : ({gbest['x']}, {gbest['y']})")
    if isConvergen:
        print('\nFungsi sudah convergen')
        break

    print('\nNilai V')
    updateV()
    for key, value in all_v.items():
        print(f"{key} : ({value['vx']}, {value['vy']})")

    print('\nUpdate X dengan\nxi = xi + vi')

    print('\n\n')
    updateX()