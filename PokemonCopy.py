import sys
import numpy as np
import time
import random

#Colors
CLIGHTGREEN = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'

#Randomized ATTACK Stats
    #Gen 1 Starters Evolution 1
Rand_ATK1 = random.randrange(2, 6)
Rand_ATK2 = random.randrange(2, 6)
Rand_ATK3 = random.randrange(2, 6)

    #Gen 1 Starters Evolution 2
Rand_ATK4 = random.randrange(6, 10)
Rand_ATK5 = random.randrange(6, 10)
Rand_ATK6 = random.randrange(6, 10)

    #Gen 1 Starters Evolution 3
Rand_ATK7 = random.randrange(10, 13)
Rand_ATK8 = random.randrange(10, 13)
Rand_ATK9 = random.randrange(10, 13)

print(CRED + "\nSTART/DEV\n" + CEND)
print("ATTACK_EVs ", Rand_ATK1, Rand_ATK2, Rand_ATK3, Rand_ATK4, Rand_ATK5, Rand_ATK6, Rand_ATK7, Rand_ATK8, Rand_ATK9)
print(CRED + "\nEND/DEV\n" + CEND)


# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print(CLIGHTGREEN + "-----POKÉMON BATTLE-----" + CEND)
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print(CRED + "\nVS" + CEND)
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                money = np.random.choice(5000)
                delay_print(f"\nOpponent paid you ${money}.\n")
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            #for i, x in enumerate(Pokemon2.moves):
                #print(f"{i+1}.", x)
            #index = int(input('Pick a move: '))
            index = random.randrange(1, 5)
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                money = np.random.choice(5000)
                delay_print(f"\nYou paid your opponent ${money}.\n")
                break

if __name__ == '__main__':
    #Create Pokemon
    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':49, 'DEFENSE':49})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK':1, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':Rand_ATK3, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':Rand_ATK4, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': Rand_ATK5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':60, 'DEFENSE':62})

    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':Rand_ATK7, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': Rand_ATK8, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':80, 'DEFENSE':82})
    
    # Get them to fight
    opponent = random.randrange(1, 10)
    if opponent == 1:
        opponent = Charmander
    if opponent == 2:
        opponent = Squirtle
    if opponent == 3:
        opponent = Bulbasaur
    if opponent == 4:
        opponent = Charmeleon
    if opponent == 5:
        opponent = Wartortle
    if opponent == 6:
        opponent = Ivysaur
    if opponent == 7:
        opponent = Charizard
    if opponent == 8:
        opponent = Blastoise
    if opponent == 9:
        opponent = Venusaur
    
    Charizard.fight(opponent)