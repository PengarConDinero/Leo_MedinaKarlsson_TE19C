#Uppgift 3

pokemon = {}

with open("filer/pokemonlista.txt", "r") as f:
    for rad in f:
        lst = rad.split()
        pokemon[lst[1]]=f"Typ: {lst[2]}, {lst[0]}"

print(pokemon["Gastly"])