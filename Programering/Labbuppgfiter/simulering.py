'''
import numpy as np
x = 0.5
y = 0.5

avstånd = np.sqrt(x**2+y**2)

print(avstånd)
'''

'''
import numpy as np
x = 1
y = 1

avstånd = np.sqrt(x**2+y**2)

print(avstånd)
'''

'''
import numpy as np
x = 0.5
y = -0.5

avstånd = np.sqrt(x**2+y**2)

print(avstånd)
'''

'''
import random as rand

for i in range(10):
    x = rand.uniform(-1,1)
    y = rand.uniform(-1,1)
    print(f"({x},{y})")
'''

'''
import random as rand

inne = 0 

for i in range (10):
    x = rand.uniform(-1,1)
    y = rand.uniform(-1,1)
    avstånd = (x**2+y**2)**0.5
    if avstånd < 1:
        inne += 1
print(inne/i+1)

andel = inne/(i+1)
print(andel*4)
'''


'''
import random
import numpy as np
import matplotlib.pyplot as plt
inne=0
for i in range(10000): 
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    
    avstånd=np.sqrt(x**2+y**2)
    if avstånd < 1: 
        plt.plot(x,y,'ro') 

    else:
        plt.plot(x,y,'bo') 

plt.show()
'''