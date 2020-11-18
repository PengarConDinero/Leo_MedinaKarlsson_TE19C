import matplotlib.pyplot as plt

sträcka = [10, 20 ,30, 40, 50, 60, 70, 80, 90, 100]
tid = [1.83, 2.87, 3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69]

plt.plot(tid,sträcka)
plt.show()

'''
import matplotlib.pyplot as plt
import numpy

a_vals = []

for x in range(1,10000):
    a = round(5*(2+4/x),2)
    a_vals.append(a)

print(a_vals)

plt.plot(a_vals)
plt.show()

#Gå till kod stugan
'''