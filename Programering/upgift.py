
s = 5

for i in range(1,11):
    i*=s
    print(i, end=" ")



for i in range(1,11):
    for j in range(1,11):
        j *= i 
        print(j, end=" ")
    print(" ")



s = float(input("Vilken gångertabell vill du räkna ut?: "))

for i in range(1,11):
    i*=s
    print(i, end=" ")



