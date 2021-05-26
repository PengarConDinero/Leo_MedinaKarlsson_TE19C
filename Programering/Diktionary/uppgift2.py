#Uppgift 2

import random as rnd

kast = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}

for i in range(100000):
    x = rnd.randint(1,6)
    for j in range(1,7):
        if x == j:
            kast[f"{j}"] += 1

for key in kast:
    print(f"{key}: {kast[key]}")