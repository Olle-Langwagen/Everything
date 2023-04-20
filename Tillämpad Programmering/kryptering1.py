#Caesarchiffer
lower=[chr(i) for i in range(96,123)]
alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

text=("Hej")

def cesar(text,nyckel):
    nytext=""
    for i in text:
        if i in alfabet:
            nytext+=alfabet[(alfabet.index(i)+nyckel)%26]
        else:
            nytext+=i
    return nytext
