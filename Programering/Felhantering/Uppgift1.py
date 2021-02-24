import math as np #Här stod det impor, vilket jag ändrade till imoport. "numpy" fungerade inte för mig så jag tog math istället.

def distance(x, y):
    return np.sqrt((x**2)+(y**2)) #"return" var felstavat(reurn), sedan så fattades **2(upphöjt till två). Annars hade de inte fått fram avständet mellan punkterna. 

print(distance(0.5,0.5))