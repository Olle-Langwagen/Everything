import sys
import numpy as np
import time
import random
import colorama
from colorama import Fore, Back, Style
from just_playback import Playback

pokemonHealth = 20

#Opponent Names
opponent_names = ["Alder", "Blue", "Cynthia", "Diantha", "Drake", "Giovanni Giorgio", "Iris", "Lance", "Nate", "Professor Oak", "Red", "Steven", "Wallace", "Anabel", "Argenta", "Candice", "Dawn", "Lenora", "Misty", "Rosa", "Brock", "Mustard"]
random_opp_names = random.randrange(len(opponent_names))

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
# Long Delay Print
def long_delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)

class Pokemon:

   
    def __init__(self, name, types, moves, EVs, health):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        #self.specialattack = EVs["SPATTACK"]
        #self.specialdefense = EVs["SPDEFENSE"]
        self.defense = EVs['DEFENSE']
        self.speed = EVs["SPEED"]
        self.health = health
        self.healthnumber = pokemonHealth # Amount of health

    def showPokemon(fight):
        showPokemon = 1
        if showPokemon == 1:
            delay_print("These are your pokemon:\n")
            time.sleep(0.2)
            
            time.sleep(0.2)
            delay_print("These are your opponents pokemon:\n")
            time.sleep(0.2)
            
            showPokemon = showPokemon -2
    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
        

        # Print fight information
        print(Fore.LIGHTGREEN_EX + "\n-----POKÉMON BATTLE-----" + Fore.RESET)
        print(Fore.CYAN + "\nAsh Ketchup" + Fore.RESET)
        print(f"{self.name}")
        print("LVL:", 3*(1+np.mean([self.attack,self.defense])))
        time.sleep(0.5)
        print(Fore.RED + "\nVS\n" + Fore.RESET)
        time.sleep(0.5)
        print(Fore.CYAN + opponent_names[random_opp_names] + Fore.RESET)
        print(f"{Pokemon2.name}")
        print("LVL:", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(1)

        #Print the health of each pokemon
        print(f"\n{self.name}\t\tHEALTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
        time.sleep(2)

        #Updated Type Advantages
        attack_advantage = {"Fire":["Grass"], "Water":["Fire"], "Grass":["Water"], "Fire":["Bug"], "Bug":["Grass"]}
        if self.types in attack_advantage[Pokemon2.types]:  #Pokemon2 is strong
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts super effective!\n'
        elif Pokemon2.types in attack_advantage[self.types]: #Pokemon2 is weak
            self.attack *= 2
            self.defense *= 2
            string_1_attack = '\nIts super effective!'
            string_2_attack = '\nIts not very effective...\n'
        else: #No type advantage
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts not very effective...\n'
            
        # Fight Sequence
        # Continue while pokemon still have health
        while (self.healthnumber > 0) and (Pokemon2.healthnumber > 0):
            
            if self.speed > Pokemon2.speed:

                print(f"Go {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                print("5. Run")

                index = int(input('Pick a move: '))
                if index == 1 or 2 or 3 or 4:
                    pass
                if index == 5:
                    delay_print("You ran away from the threat\n")
                    time.sleep(1)
                    long_delay_print(Fore.LIGHTMAGENTA_EX + "Pussy")
                    time.sleep(0.5)
                    break

                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)

                # Determine damage
                Pokemon2.healthnumber -= self.attack
                Pokemon2.health = Pokemon2.healthnumber

                # Add back bars plus defense boost
                for j in range(int(Pokemon2.healthnumber+.1*Pokemon2.defense)):
                    Pokemon2.health += 1

                # Check to see if Pokemon fainted
                if Pokemon2.healthnumber <= 0:
                    delay_print(Fore.GREEN + "\n..." + Pokemon2.name + ' fainted.' + Fore.RESET)
                    money = np.random.choice(5000)
                    delay_print(f"\nOpponent paid you ${money}.\n")
                    break
                time.sleep(1)
                print(f"\n{self.name}\t\tHEALTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
                time.sleep(.5)

                  # Pokemon2s turn
                print(f"Go {Pokemon2.name}!")
                index = random.randrange(1, 5)
                delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_2_attack)

                # Determine damage
                self.healthnumber -= Pokemon2.attack
                self.health = self.healthnumber

                # Add back bars plus defense boost
                for j in range(int(self.healthnumber+.1*self.defense)):
                    self.health += 1

                # Check to see if Pokemon fainted
                if self.healthnumber <= 0:
                    delay_print(Fore.RED + "\n..." + self.name + ' fainted.' + Fore.RESET)
                    money = np.random.choice(500000)
                    delay_print(f"\nYou paid your opponent ${money}.\n")
                    break
                time.sleep(1)
                print(f"\n{self.name}\t\tHEALTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
                time.sleep(.5)

            if self.speed < Pokemon2.speed:
                # Pokemon2s turn
                print(f"Go {Pokemon2.name}!")
                index = random.randrange(1, 5)
                delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_2_attack)

                # Determine damage
                self.healthnumber -= Pokemon2.attack
                self.health = self.healthnumber

                # Add back bars plus defense boost
                for j in range(int(self.healthnumber+.1*self.defense)):
                    self.health += 1

                # Check to see if Pokemon fainted
                if self.healthnumber <= 0:
                    delay_print(Fore.RED + "\n..." + self.name + ' fainted.' + Fore.RESET)
                    money = np.random.choice(500000)
                    delay_print(f"\nYou paid your opponent ${money}.\n")
                    break
                time.sleep(1)
                print(f"\n{self.name}\t\tHEALTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
                time.sleep(.5)

                print(f"Go {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                print("5. Run")

                index = int(input('Pick a move: '))
                if index == 5:
                    delay_print("You ran away from the threat\n")
                    time.sleep(1)
                    long_delay_print(Fore.LIGHTMAGENTA_EX + "Pussy")
                    time.sleep(0.5)
                    break

                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)

                # Determine damage
                Pokemon2.healthnumber -= self.attack
                Pokemon2.health = Pokemon2.healthnumber

                # Add back bars plus defense boost
                for j in range(int(Pokemon2.healthnumber+.1*Pokemon2.defense)):
                    Pokemon2.health += 1

                # Check to see if Pokemon fainted
                if Pokemon2.healthnumber <= 0:
                    delay_print(Fore.GREEN + "\n..." + Pokemon2.name + ' fainted.' + Fore.RESET)
                    money = np.random.choice(5000)
                    delay_print(f"\nOpponent paid you ${money}.\n")
                    break
                time.sleep(1)
                print(f"\n{self.name}\t\tHEALTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
                time.sleep(.5)
           
           

#Create Pokemons and randomization + start fight sequence
if __name__ == '__main__':

    #Randomized move for each pokémon
    rand_move_fire = ['Ember', 'Fire Spin', 'Fire Blast', 'Fire Punch', 'Flamethrower']
    rand_move_water = ['Bubblebeam', 'Crabhammer', 'Bubble', 'Surf', 'Water Gun', 'Hydro Pump', "Clamp", "Waterfall"]
    rand_move_grass = ['Vine Wip', 'Razor Leaf', 'Solar Beam', 'Leech Seed', 'Bullet Seed', 'Frenzy Plant']
    rand_move_bug = ["Leech Life", "Pin Missile", "String Shot", "Twineedle"]
    rand_move_flying = ["Drill Peck", "Fly", "Gust", "Peck", "Sky Attack", "Wing Attack"]
    rand_move_normal = ["Body Slam", "Tackle", "Spike Cannon", "Hyper Fang", "Headbutt"]
    #rand_move_poison = ["Acid", "Poison Sting", "Sludge", "Smog"]
    rand_move_electric = ["Thunder", "Thunder Punch", "Thunder Shock", "Thunder Wave", "Thunderbolt"]
    rand_move_ground = ["Bone Club", "Bonemerang", "Dig", "Earthquake", "Sand Attack"]
    rand_move_fight = ["Double Kick", "Karate Chop", "Low Kick", "Rolling Kick", "Seismic Toss", "Submission"]
    rand_move_psychic = ["Confusion", "Kinesis", "Psybeam", "Psychic", "Psywave"]
    #rand_move_ice = ["Aurora Beam", "Blizzard", "Ice Beam", "Ice Punch"]
    #Create pokemons for player
    #Starters
    Charmander = Pokemon(Fore.RED + 'Charmander' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4) ,{'ATTACK':5.2, 'DEFENSE':4.3, "SPEED":100}, 40)
    Squirtle = Pokemon(Fore.BLUE + 'Squirtle' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':4.8, 'DEFENSE':6.5, "SPEED":110}, 35)
    Bulbasaur = Pokemon(Fore.GREEN + 'Bulbasaur' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':4.9, 'DEFENSE':4.9, "SPEED":70}, 45)
    Caterpie = Pokemon(Fore.LIGHTGREEN_EX + "Caterpie" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":3, "DEFENSE":3.5, "SPEED": 120}, 40)

    Charmander.fight(Bulbasaur)