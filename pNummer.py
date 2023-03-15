def kontrollera_personnummer(personnummer):
    personnummer = "".join(c for c in personnummer if c.isdigit())

    personnummer = personnummer[-10:]
    print(f"Personnummer utan bindestreck och i format ÅÅMMDD-0000: {personnummer}")
    # Kontrollera att personnumret är 10 siffror långt
    if len(personnummer) != 10:
        return False
    kontrollsiffra = int(personnummer[-1])
    siffersumma = 0
    for i in range(9):
        siffra = int(personnummer[i])
        if i % 2 == 0:
            produkt = siffra * 2
            if produkt >= 10:
                siffersumma += produkt // 10 + produkt % 10
            else:
                siffersumma += produkt
        else:
            siffersumma += siffra
    tiotal = siffersumma // 10
    kontrollberakning = tiotal * 10 + 10 - siffersumma
    if kontrollberakning == kontrollsiffra:
        return True
    else:
        return False

personnummer = input("Ange personnummer: ")
if kontrollera_personnummer(personnummer):
    print("Personnumret är giltigt.")
    print("Kontrollsiffran är: " + personnummer[-1])
else:
    print("Personnumret är ogiltigt.")