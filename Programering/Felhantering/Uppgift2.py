def ar_fyrsiffrigt(tal):
    if tal < 0:
        return False 
    elif tal //1000: 
        return True
    else:
        return False

#testprogram 
testtal = [100, 231, 10000, 100001, -1000, 102313]

for t in testtal:
    if ar_fyrsirigt(t): #fyrsiffrigt är felstavat så "ar_fyrsirigt" är odefinerat
        print(f"{t} är fyrsiffrigt")
    else:
        print(f"{t} är inte fyrsiffrigt")