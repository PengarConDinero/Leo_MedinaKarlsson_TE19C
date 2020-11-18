 
'''
n = 1
while n < 10:
    print(n, end= " ")
    n = n + 1
'''

'''
n = 1
while n <10:
    n+=2
    print(n)
'''

'''
n = 1
summa = 0

while n <50:
    summa = summa + n
    n+=2    
print(f"1+3+5+7+9 = {summa}")
'''


'''
1L mjölk 1500000 bakterier
I rumstemp ökar antalet bakterier med 50% varje timme
Mjölk blir sur när bakterierna överstiger 10000000 st
Hur många timmar tills mjölken blir sur?
'''

'''
mjölk = 1500000

while mjölk < 10000000:
    mjölk*= 1.5 
    print(mjölk, end=" ")
'''

'''
n = 1
summa = 0

while n <50:
    summa = summa + n
    n+=1    
print(f"1+2+3+4...+99+100 = {summa}")
'''

'''
import random

någotnummer = random.randint(0,101)


gissa = ""
while gissa!= någotnummer:
    gissa = int(input("Gissa ett tal emellan 0 och 100: "))
    if gissa == någotnummer:
        print(f"Gött! Du gissade talet {någotnummer}!")
        exit
    elif gissa > någotnummer:
        print("Gissa lägre")
    elif gissa < någotnummer:
        print("Gissa högre")
'''