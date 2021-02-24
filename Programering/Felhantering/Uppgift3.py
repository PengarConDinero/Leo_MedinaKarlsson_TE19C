while True:
    try:
        tal = float(input("Hur många gånger i veckan vill du åka spårvagn?: "))
        assert tal>-1 and tal<60
        break
    except AssertionError:
        print("Orimligt svar!")
    except:
        print("Du måste skriva in en siffra!")

antal_månad = tal*4 
engångskostnad = antal_månad*20
månadskostnad = 100

if engångskostnad > månadskostnad:
    print("Det är bättre att köpa ett månadskort.")
else: 
    print("Det är bättre att köpa engångsbiljeter.")