'''
for x in range(1,101):
    print(x, end=" ")
'''

'''
for i in range(1, 101):
    if i%5 == 0:
        print("Burr")
    else:
        print(i, end=" ")
'''

'''
x = int(input("Skriv in ett valfritt heltal: "))

for i in range (1, 101):
    if i%x == 0:
        print("Burr")
    else:
        print(i, end=" ")
'''

'''
x = int(input("Skriv in ett valfritt heltal: "))
y = int(input("Skriv in yterligare ett valfritt heltal: "))

for i in range (1, 101):
    if i%x == 0:
        print("Burr")
    elif i%y == 0:
        print("birr")
    else:
        print(i, end=" ")
'''

'''
start = int(input("Välj start: "))
slut = int(input("Välj stop: "))
multipel1 = int(input("Välj ett valfritt multipel: "))
multipel2 = int(input("Välj ytterligare ett valfritt multipel: "))

for i in range(start, slut):
    if i % multipel1 and multipel2 == 0:
        print(f"{i}, Burr/Birr")
    elif i % multipel1 == 0:
        print(f"{i} Burr")
    elif i % multipel2 == 0:
        print(f"{i}, Birr")
    else:
        print(f"{i}")
        
'''

'''
print("Detta är ett burr & birr verktyg. Välj start - stop och multipel till burr & birr.")

print("  ")

start = int(input("Välj start: ")) 
stop = int(input("Välj stop: ")) 
burr = int(input("Välj en Burr multipel: ")) 
birr = int(input("Välj en Birr multipel: ")) 

for i in range(start,stop):
    if i % burr == 0:
        print(f"{i}, Burr!")
    elif i % birr == 0:
        print(f"{i}, Birr!")
    else:
        print(f"{i}")
'''