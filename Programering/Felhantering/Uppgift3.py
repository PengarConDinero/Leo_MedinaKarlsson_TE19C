while True:
    try:
        tal = float(input("Hur många gånger i veckan vill du åka spårvagn"))
        assert tal>0 and tal<50
        break
    except AssertionError:
        print("Talet du skrev är orimligt!")
    except:
        print("Du måste skriva in en siffra!")

antal_månad = tal4 
engångskostnad = antal_månad50
månadskostnad = 500

if engångskostnad > månadskostnad:
    print("Det är bättre att köpa ett månadskort.")
else: 
    print("Det är bättre att köpa engångsbiljeter.")