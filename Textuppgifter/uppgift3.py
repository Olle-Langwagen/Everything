text = "äööädäl"
transtab = {'å': 'aa', 'ä': 'ae', 'ö': 'oe'}
print(text)
for word, initial in transtab.items():
    text = text.replace(word, initial)
print(text)
