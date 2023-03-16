PN = input("Ange ett personnummer: ")

# Multiplicera de 9 relevanta siffrorna i personnumret (__ÅÅMMDD-NNN_), 
# växelvis med 2 resp. 1, och addera produkternas siffror till en siffersumma. 
# Förtydligande: om någon produkt blir tvåsiffrig, addera produktens båda siffror till siffersumman.

if PN.isdigit():
    PNList = PN.split()
    print(PNList)