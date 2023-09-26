import random
from colorama import Fore

print("Wordle, gissa ett 5 bokstavs ord. (x) = rätt plats, /x/ = rätt bokstav, fel plats, *x* = fel bokstav")

# välj ord slumpmässigt från en lista
words = ['sabel', 'huvud', 'sagas', 'rumpa', 'snopp', 'samba', 'samma', 'agent', 'zebra', 'laget']
word = random.choice(words)

# lista för redan gissade bokstäver (fylls senare med gissade bokstäver)
guessed_letters = []
yellow_letters = []
correct_positions = [' '] * len(word)

# antal gissningar
max_guesses = 6
num_guesses = 0

# fortsätter köra while-loop så länge antalet gissningar är mindre än max
while num_guesses < max_guesses:
    print(f'Du har {max_guesses - num_guesses} gissningar kvar.')

    # visa redan gissade bokstäver
    if guessed_letters:
        print(f'Redan gissade bokstäver: {Fore.RED}{", ".join(guessed_letters)}{Fore.RESET}')

    # be om en gissning
    guess = input('Gissa ett 5-bokstavsord: ').lower()

    # kolla om gissningen är rätt
    if guess == word:
        print(f'Rätt svar! Ordet var {word}.')
        break

    # om gissningen inte är rätt, visa vilka bokstäver som är rätt
    num_guesses += 1
    correct_letters = ''

    for i, letter in enumerate(guess):
        if letter == word[i]:
            correct_letters += f'{Fore.GREEN}{letter}{Fore.RESET}'
            if letter in guessed_letters:
                guessed_letters.remove(letter)
        elif letter in word and guess.count(letter) <= word.count(letter):
            if letter not in guessed_letters:
                correct_letters += f'{Fore.YELLOW}{letter}{Fore.RESET}'
                guessed_letters.append(letter)
                yellow_letters.append(letter)
            else:
                correct_letters += f'{Fore.RED}{letter}{Fore.RESET}'
        else:
            correct_letters += f'{Fore.RED}{letter}{Fore.RESET}'

    for letter in yellow_letters:
        if letter in guessed_letters:
            correct_letters = correct_letters.replace(letter, f'{Fore.YELLOW}{letter}{Fore.RESET}')

    print(f'Tyvärr, {guess} är inte rätt. Här är delvis rätt svar: {correct_letters}.')

    # lägg till gissningen till redan gissade bokstäver
    for letter in guess:
        if letter not in guessed_letters:
            guessed_letters.append(letter)

# om max antal gissningar har nåtts och ordet inte har gissats, visa svaret
if num_guesses == max_guesses:
    print(f'Du har inga gissningar kvar. Ordet var {word}.')
