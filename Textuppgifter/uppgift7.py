#Programmet ska producera en lista med radnummer över filen och en referenslista som för varje ord anger på vilka rader det förekommit

#Skapar en variabel med filnamnet
filename = "input.txt"
#Öppnar filen
f = open(filename, "r")

#Skapar en lista med raderna i filen
radlista = f.readlines()

#Skapar en tom lista för referenslistan
referenslista = []

#Loopar igenom raderna i filen
for rad in radlista:
    #Skapar en lista med orden i raden
    ordlista = rad.split()
    #Loopar igenom orden i raden
    for ord in ordlista:
        #Kollar om ordet redan finns i referenslistan
        if ord in referenslista:
            #Om ordet redan finns i referenslistan så lägger vi till radnumret där ordet finns i referenslistan
            referenslista[referenslista.index(ord)].append(radlista.index(rad)+1)
        else:
            #Om ordet inte finns i referenslistan så lägger vi till ordet och radnumret där ordet finns i referenslistan
            referenslista.append([ord, radlista.index(rad)+1])

#Stänger filen
f.close()

#Skriver ut referenslistan
for ord in referenslista:
    print(ord)


