#Uppgift 1

poäng = 0

kurs = {
    "matte": 100,
    "fysik": 150,
    "engelska": 100,
    "webbutveckling": 100,
    "svenska": 100,
    "programering": 100,
    "daodac": 100,
    "idrott": 100
}
for key in kurs:
    print(f"{key}   \t  \t  {kurs[key]}")
    poäng += kurs[key]
print("\n")
print(f"Totala suman av poängen {poäng}")