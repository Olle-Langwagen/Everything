import sys
import numpy as np
import time
import random
import colorama
from colorama import Fore, Back, Style
from just_playback import Playback

#Declaring Variables
playerName = ""
hidingText = 0

#Colors
colorama.init()
print(Fore.LIGHTBLUE_EX + "Hej")
print(Fore.LIGHTBLACK_EX + "Hej")
print(Fore.LIGHTCYAN_EX + "Hej")
print(Fore.LIGHTGREEN_EX + "Hej")
print(Fore.LIGHTMAGENTA_EX + "Hej")
print(Fore.LIGHTYELLOW_EX + "Hej")
#Jan banans skapelse(randomMoves)
rand_move_fire = 0
rand_move_water = 0
rand_move_grass = 0

#RandomMoveList
rand_fire_move = 0
rand_water_move = 0
rand_grass_move = 0

#Music
playback = Playback()
playback.load_file("musicc.mp3")
playback.play()
playback.set_volume(1)
playback.loop_at_end(True)
#https://downloads.khinsider.com/game-soundtracks/album/pokemon-gameboy-sound-collection

#Opponent Names
opponent_names = ["Alder", "Blue", "Cynthia", "Diantha", "Drake", "Giovanni Giorgio", "Iris", "Lance", "Nate", "Professor Oak", "Red", "Steven", "Wallace", "Anabel", "Argenta", "Candice", "Dawn", "Lenora", "Misty", "Rosa", "Brock", "Mustard"]
random_opp_names = random.randrange(len(opponent_names))

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

# Delay printing
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

# Create the class
class Pokemon:

   
    def __init__(self, name, types, moves, EVs, health= Fore.GREEN + '====================' + Fore.RESET):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars
    """
    playerName = input("Choose your name: ")
    delay_print("Thank you for entering your fake name\n")
    time.sleep(0.2)
    delay_print("Your real name is obviously Ash Ketchup\n")
    time.sleep(0.2)
    delay_print("Your team includes 3 pokemon that will fight your opponent\n")
    time.sleep(0.2)
    delay_print("You will be able to switch pokemon whenever you wish\n")
    time.sleep(0.2)
    """

    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
        #Questions for player
        showPokemon = 1
        if showPokemon == 1:
            delay_print("These are your pokemon:\n")
            time.sleep(0.2)
            print("1. ", playerrName, "\n2. ", playerrName1, "\n3. ", playerrName2)
            time.sleep(0.2)
            delay_print("These are your opponents pokemon:\n")
            time.sleep(0.2)
            print("1. ", opponentName, "\n2. ", opponentName1, "\n3. ", opponentName2)
            showPokemon = showPokemon -2

        # Print fight information
        print(Fore.LIGHTGREEN_EX + "\n-----POKÉMON BATTLE-----" + Fore.RESET)
        print(Fore.CYAN + "\nAsh Ketchup" + Fore.RESET)
        print(f"{self.name}")
        #print("TYPE/", self.types)
        #print("ATTACK/", self.attack)
        #print("DEFENSE/", self.defense)
        print("LVL:", 3*(1+np.mean([self.attack,self.defense])))
        time.sleep(0.5)
        print(Fore.RED + "\nVS\n" + Fore.RESET)
        time.sleep(0.5)
        print(Fore.CYAN + opponent_names[random_opp_names] + Fore.RESET)
        print(f"{Pokemon2.name}")
        #print("TYPE/", Pokemon2.types)
        #print("ATTACK/", Pokemon2.attack)
        #print("DEFENSE/", Pokemon2.defense)
        print("LVL:", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(1)

        #Print the health of each pokemon
        print(f"\n{self.name}\t\tHEALTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
        time.sleep(2)

        # Consider type advantages
        """
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...\n'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    #self.attack /= 2
                    #self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!\n'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    #Pokemon2.attack /= 2
                    #Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...\n'
        """

        #Updated Type Advantages (in progress/funkar inte alls/jag rebuildar den/bättre mechanics/actual type advantages)
        attack_advantage = {"Fire":["Grass"], "Water":["Fire"], "Grass":["Water"], "Fire":["Bug"], "Water":["Ground"], "Electric":["Water"], "Electric":["Flying"], "Grass":["Ground"], "Fighting":["Normal"], "Ground":["Fire"], "Ground":["Electric"], "Flying":["Grass"], "Flying":["Fighting"], "Flying":["Bug"], "Psychic":["Fighting"], "Bug":["Grass"], "Bug":["Psychic"], "Normal":["Fighting"]}
        if self.types in attack_advantage[Pokemon2.types]:  #Pokemon2 is strong
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts super effective!\n'
        elif Pokemon2.types in attack_advantage[self.types]: #Pokemon2 is weak
            self.attack *= 2
            self.defense *= 2
            #Pokemon2.attack /= 2
            #Pokemon2.defense *= 3
            string_1_attack = '\nIts super effective!'
            string_2_attack = '\nIts not very effective...\n'
        else: #No type advantage
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts not very effective...\n'
            





        # Fight Sequence
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            
            activePokemon = 0
            yourPokemon1 = 1
            yourPokemon2 = 1 
            yourPokemon3 = 1

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            print("5. Run")
            print("6. Switch pokemon to ", playerrName)
            print("7. Switch pokemon to ", playerrName1)
            print("8. Switch pokemon to ", playerrName2)

            index = int(input('Pick a move: '))
            if index == 5:
                delay_print("You ran away from the threat\n")
                time.sleep(1)
                long_delay_print(Fore.LIGHTMAGENTA_EX + "Pussy")
                time.sleep(0.5)
                break
            if index == 6:
                player.fight(opponent)
                activePokemon = yourPokemon1
            if index == 7:
                player1.fight(opponent)
                activePokemon = yourPokemon2
            if index == 8:
                player2.fight(opponent)
                activePokemon = yourPokemon3

            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = Fore.GREEN + "" + Fore.RESET

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += Fore.GREEN + "=" + Fore.RESET

            time.sleep(1)
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print(Fore.GREEN + "\n..." + Pokemon2.name + ' fainted.' + Fore.RESET)
                money = np.random.choice(5000)
                delay_print(f"\nOpponent paid you ${money}.\n")
                break

            # Pokemon2s turn
            print(f"Go {Pokemon2.name}!")
            #UNCOMMENT om du vill inte vill ha randomized moves
            #for i, x in enumerate(Pokemon2.moves):
                #print(f"{i+1}.", x)
            #index = int(input('Pick a move: '))
            index = random.randrange(1, 5)
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = Fore.GREEN + "" + Fore.RESET

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += Fore.GREEN + "=" + Fore.RESET

            time.sleep(1)
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print(Fore.RED + "\n..." + self.name + ' fainted.' + Fore.RESET)
                activePokemon = 0
                print(yourPokemon1, yourPokemon2, yourPokemon3)
                #if()
                #money = np.random.choice(500000)
                #delay_print(f"\nYou paid your opponent ${money}.\n")
                #break
            #player1.fight(opponent1)
            if yourPokemon1 & yourPokemon2 & yourPokemon3 == 0:
                break
            randplayerpokemon1 = [Vulpix.name, Ninetales.name, Growlithe.name, Arcanine.name, Ponyata.name, Rapidash.name, Magmar.name]
            print(random.sample(randplayerpokemon1, 1))
            randguy = str(randplayerpokemon1)
            print(randguy)

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
    Charmander = Pokemon(Fore.RED + 'Charmander' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4) ,{'ATTACK':5.2, 'DEFENSE':4.3})
    Squirtle = Pokemon(Fore.BLUE + 'Squirtle' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':4.8, 'DEFENSE':6.5})
    Bulbasaur = Pokemon(Fore.GREEN + 'Bulbasaur' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':4.9, 'DEFENSE':4.9})
    Charmeleon = Pokemon(Fore.RED + 'Charmeleon' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4),{'ATTACK':6.4, 'DEFENSE':5.8})
    Wartortle = Pokemon(Fore.BLUE + 'Wartortle' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':6.3, 'DEFENSE':8})
    Ivysaur = Pokemon(Fore.GREEN + 'Ivysaur\t' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':6.2, 'DEFENSE':6.3})
    Charizard = Pokemon(Fore.RED + 'Charizard' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':8.4, 'DEFENSE':7.8})
    Blastoise = Pokemon(Fore.BLUE + 'Blastoise' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':8.3, 'DEFENSE':10})
    Venusaur = Pokemon(Fore.GREEN + 'Venusaur' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':8.2, 'DEFENSE':8.3})

    #Fire pokemons
    Vulpix = Pokemon(Fore.RED + 'Vulpix' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':4.1, 'DEFENSE':4})
    Ninetales = Pokemon(Fore.RED + 'Ninetales' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':7.6, 'DEFENSE':6.5})
    Growlithe = Pokemon(Fore.RED + 'Growlithe' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':7, 'DEFENSE':4.5})
    Arcanine = Pokemon(Fore.RED + 'Arcanine' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':11, 'DEFENSE':8})
    Ponyata = Pokemon(Fore.RED + 'Ponyata' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':5.5, 'DEFENSE':6.5})
    Rapidash = Pokemon(Fore.RED + 'Rapidash' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':10, 'DEFENSE':7})
    Magmar = Pokemon(Fore.RED + 'Magmar' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':9.5, 'DEFENSE':5.7})
    Flareon = Pokemon(Fore.RED + 'Flareon' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':13, 'DEFENSE':6})
    Moltres = Pokemon(Fore.RED + 'Moltres' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':10, 'DEFENSE':9})

    #Water
    Psyduck = Pokemon(Fore.BLUE + 'Psyduck' + Fore.RESET, 'Water', random.sample(rand_move_water, 4), {'ATTACK':5.2, 'DEFENSE':4.8})
    Golduck = Pokemon(Fore.BLUE + 'Golduck' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':8.2, 'DEFENSE':7.8})
    Poliwag = Pokemon(Fore.BLUE + 'Poliwag' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':5, 'DEFENSE':4})
    Poliwhirl = Pokemon(Fore.BLUE + 'Poliwhirl' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':6.5, 'DEFENSE':6.5})
    Poliwrath = Pokemon(Fore.BLUE + 'Poliwrath' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':9.5, 'DEFENSE':9.5})
    Krabby = Pokemon(Fore.BLUE + 'Krabby' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':10.5, 'DEFENSE':9})
    Kingler = Pokemon(Fore.BLUE + 'Kingler' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':13, 'DEFENSE':11.5})
    Staryu = Pokemon(Fore.BLUE + 'Staryu' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':4.5, 'DEFENSE':5.5})
    Starmie = Pokemon(Fore.BLUE + 'Starmie' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':7.5, 'DEFENSE':8.5})
    Magikarp = Pokemon(Fore.BLUE + 'Magikarp' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':1, 'DEFENSE':5.5})
    Gyarados = Pokemon(Fore.BLUE + 'Gyarados' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':12.5, 'DEFENSE':7.9})

    #Grass
    Oddish = Pokemon(Fore.GREEN + 'Oddish' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':5, 'DEFENSE':5.5})
    Gloom = Pokemon(Fore.GREEN + 'Gloom' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':6.5, 'DEFENSE':7})
    Vileplume = Pokemon(Fore.GREEN + 'Vileplume' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':8, 'DEFENSE':8.5})
    Paras = Pokemon(Fore.GREEN + 'Paras' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':7, 'DEFENSE':5.5})
    Parasect = Pokemon(Fore.GREEN + 'Parasect' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9.5, 'DEFENSE':8})
    Bellsprout = Pokemon(Fore.GREEN + 'Bellsprout' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':7.5, 'DEFENSE':3.5})
    Weepinbell = Pokemon(Fore.GREEN + 'Weepinbell' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9, 'DEFENSE':5})
    Victrebell = Pokemon(Fore.GREEN + 'Victrebell' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':10.5, 'DEFENSE':6.5})
    Exeggcute = Pokemon(Fore.GREEN + 'Exeggcute' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':4, 'DEFENSE':8})
    Exeggutor = Pokemon(Fore.GREEN + 'Exeggutor' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9.5, 'DEFENSE':8.5})
    Tangela = Pokemon(Fore.GREEN + 'Tangela' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':5.5, 'DEFENSE':11.5})

    #Bug
    Caterpie = Pokemon(Fore.LIGHTGREEN_EX + "Caterpie" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":3, "DEFENSE":3.5})
    Metapod = Pokemon(Fore.LIGHTGREEN_EX + "Metapod" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":2, "DEFENSE":5.5})
    Butterfree = Pokemon(Fore.LIGHTGREEN_EX + "Butterfree" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":4.5, "DEFENSE":5})
    Weedle = Pokemon(Fore.LIGHTGREEN_EX + "Weedle" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":3.5, "DEFENSE":3})
    Kakuna = Pokemon(Fore.LIGHTGREEN_EX + "Kakuna" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":2.5, "DEFENSE":5})
    Beedrill = Pokemon(Fore.LIGHTGREEN_EX + "Beedrill" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":9, "DEFENSE":4})
    Scyther = Pokemon(Fore.LIGHTGREEN_EX + "Scyther" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":11, "DEFENSE":8})
    Pinsir = Pokemon(Fore.LIGHTGREEN_EX + "Pinsir" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":12.5, "DEFENSE":10})

    #Flying
    Pidgey = Pokemon(Fore.CYAN + "Pidgey" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":4.5, "DEFENSE":4})
    Pidgeotto= Pokemon(Fore.CYAN + "Pidgeotto" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":6, "DEFENSE":5.5})
    Pidgeot = Pokemon(Fore.CYAN + "Pidgeot" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":8, "DEFENSE":7.5})
    Spearow = Pokemon(Fore.CYAN + "Spearow" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":6, "DEFENSE":3})
    Fearow = Pokemon(Fore.CYAN + "Fearow" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":9, "DEFENSE":6.5})
    Aerodactyl = Pokemon(Fore.CYAN + "Aerodactyl" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":10.5, "DEFENSE":6.5})

    #Normal
    Rattata = Pokemon(Fore.LIGHTBLACK_EX + "Rattata" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.6, "DEFENSE":3.5})
    Raticate = Pokemon(Fore.LIGHTBLACK_EX + "Raticate" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":8.1, "DEFENSE":6})
    Meowth = Pokemon(Fore.LIGHTBLACK_EX + "Meowth" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":4.5, "DEFENSE":3.5})
    Persian = Pokemon(Fore.LIGHTBLACK_EX + "Persian" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":7, "DEFENSE":6.5})
    Lickitung = Pokemon(Fore.LIGHTBLACK_EX + "Lickitung" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.5, "DEFENSE":7.5})
    Kangaskhan = Pokemon(Fore.LIGHTBLACK_EX + "Kangaskhan" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":9.5, "DEFENSE":8})
    Tauros = Pokemon(Fore.LIGHTBLACK_EX + "Tauros" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":10, "DEFENSE":9.5})
    Eevee = Pokemon(Fore.LIGHTBLACK_EX + "Eevee" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.5, "DEFENSE":5})
    Porygon = Pokemon(Fore.LIGHTBLACK_EX + "Porygon" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":6, "DEFENSE":7})
    Snorlax = Pokemon(Fore.LIGHTBLACK_EX + "Snorlax" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":6.5, "DEFENSE":11})

    #Electric
    Pikachu = Pokemon(Fore.LIGHTYELLOW_EX + "Pikachu" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":5.5, "DEFENSE":4})
    Raichu = Pokemon(Fore.LIGHTYELLOW_EX + "Raichu" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":9, "DEFENSE":5.5})
    Voltorb = Pokemon(Fore.LIGHTYELLOW_EX + "Voltorb" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":3, "DEFENSE":5})
    Electrode = Pokemon(Fore.LIGHTYELLOW_EX + "Electrode" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":5, "DEFENSE":7})
    Electabuzz = Pokemon(Fore.LIGHTYELLOW_EX + "Electabuzz" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":8.3, "DEFENSE":5.7})
    Jolteon = Pokemon(Fore.LIGHTYELLOW_EX + "Jolteon" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":6.5, "DEFENSE":6})
    Zapdos = Pokemon(Fore.LIGHTYELLOW_EX + "Zapdos" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":9, "DEFENSE":8.5})

    #Ground
    Sandshrew = Pokemon(Fore.YELLOW + "Sandshrew" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":7.5, "DEFENSE":8.5})
    Sandslash = Pokemon(Fore.YELLOW + "Sandslash" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":10, "DEFENSE":11})
    Dugtrio = Pokemon(Fore.YELLOW + "Dugtrio" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":10, "DEFENSE":5})
    Rhyhorn = Pokemon(Fore.YELLOW + "Rhyhorn" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":8.5, "DEFENSE":9.5})
    Rhydon = Pokemon(Fore.YELLOW + "Rhydon" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":13, "DEFENSE":12})

    #Fighting
    Mankey = Pokemon(Fore.WHITE + "Mankey" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":8, "DEFENSE":3.5})
    Primeape = Pokemon(Fore.WHITE + "Primeape" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10.5, "DEFENSE":6})
    Machop = Pokemon(Fore.WHITE + "Machop" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":8, "DEFENSE":5})
    Machoke = Pokemon(Fore.WHITE + "Machoke" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10, "DEFENSE":7})
    Machamp = Pokemon(Fore.WHITE + "Machamp" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":13, "DEFENSE":8})
    Hitmonlee = Pokemon(Fore.WHITE + "Hitmonlee" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":12, "DEFENSE":5.3})
    Hitmonchan = Pokemon(Fore.WHITE + "Hitmonchan" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10.5, "DEFENSE":7.9})

    #Psychic
    Hypno = Pokemon(Fore.LIGHTMAGENTA_EX + "Hypno" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":7.3, "DEFENSE":7})
    Mewtwo = Pokemon(Fore.LIGHTMAGENTA_EX + "Mewtwo" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":11, "DEFENSE":9})
    Mew = Pokemon(Fore.LIGHTMAGENTA_EX + "Mew" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":10, "DEFENSE":10})
    




    #Create Pokemon for opponent
    #Starters
    Charmander1 = Pokemon(Fore.RED + 'Charmander' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4) ,{'ATTACK':5.2, 'DEFENSE':4.3})
    Squirtle1 = Pokemon(Fore.BLUE + 'Squirtle' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':4.8, 'DEFENSE':6.5})
    Bulbasaur1 = Pokemon(Fore.GREEN + 'Bulbasaur' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':4.9, 'DEFENSE':4.9})
    Charmeleon1 = Pokemon(Fore.RED + 'Charmeleon' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4),{'ATTACK':6.4, 'DEFENSE':5.8})
    Wartortle1 = Pokemon(Fore.BLUE + 'Wartortle' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':6.3, 'DEFENSE':8})
    Ivysaur1 = Pokemon(Fore.GREEN + 'Ivysaur\t' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':6.2, 'DEFENSE':6.3})
    Charizard1 = Pokemon(Fore.RED + 'Charizard' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':8.4, 'DEFENSE':7.8})
    Blastoise1 = Pokemon(Fore.BLUE + 'Blastoise' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':8.3, 'DEFENSE':10})
    Venusaur1 = Pokemon(Fore.GREEN + 'Venusaur' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':8.2, 'DEFENSE':8.3})

    #Fire pokemons
    Vulpix1 = Pokemon(Fore.RED + 'Vulpix' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':4.1, 'DEFENSE':4})
    Ninetales1 = Pokemon(Fore.RED + 'Ninetales' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':7.6, 'DEFENSE':6.5})
    Growlithe1 = Pokemon(Fore.RED + 'Growlithe' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':7, 'DEFENSE':4.5})
    Arcanine1 = Pokemon(Fore.RED + 'Arcanine' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':11, 'DEFENSE':8})
    Ponyata1= Pokemon(Fore.RED + 'Ponyata' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':5.5, 'DEFENSE':6.5})
    Rapidash1 = Pokemon(Fore.RED + 'Rapidash' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':10, 'DEFENSE':7})
    Magmar1 = Pokemon(Fore.RED + 'Magmar' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':9.5, 'DEFENSE':5.7})
    Flareon1 = Pokemon(Fore.RED + 'Flareon' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':13, 'DEFENSE':6})
    Moltres1 = Pokemon(Fore.RED + 'Moltres' + Fore.RESET, 'Fire', random.sample(rand_move_fire, 4), {'ATTACK':10, 'DEFENSE':9})

    #Water
    Psyduck1 = Pokemon(Fore.BLUE + 'Psyduck' + Fore.RESET, 'Water', random.sample(rand_move_water, 4), {'ATTACK':5.2, 'DEFENSE':4.8})
    Golduck1 = Pokemon(Fore.BLUE + 'Golduck' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':8.2, 'DEFENSE':7.8})
    Poliwag1= Pokemon(Fore.BLUE + 'Poliwag' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':5, 'DEFENSE':4})
    Poliwhirl1 = Pokemon(Fore.BLUE + 'Poliwhirl' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':6.5, 'DEFENSE':6.5})
    Poliwrath1 = Pokemon(Fore.BLUE + 'Poliwrath' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':9.5, 'DEFENSE':9.5})
    Krabby1 = Pokemon(Fore.BLUE + 'Krabby' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':10.5, 'DEFENSE':9})
    Kingler1 = Pokemon(Fore.BLUE + 'Kingler' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':13, 'DEFENSE':11.5})
    Staryu1 = Pokemon(Fore.BLUE + 'Staryu' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':4.5, 'DEFENSE':5.5})
    Starmie1 = Pokemon(Fore.BLUE + 'Starmie' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':7.5, 'DEFENSE':8.5})
    Magikarp1 = Pokemon(Fore.BLUE + 'Magikarp' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':1, 'DEFENSE':5.5})
    Gyarados1 = Pokemon(Fore.BLUE + 'Gyarados' + Fore.RESET, 'Water', random.sample(rand_move_water, 4),{'ATTACK':12.5, 'DEFENSE':7.9})

    #Grass
    Oddish1 = Pokemon(Fore.GREEN + 'Oddish' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':5, 'DEFENSE':5.5})
    Gloom1 = Pokemon(Fore.GREEN + 'Gloom' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':6.5, 'DEFENSE':7})
    Vileplume1 = Pokemon(Fore.GREEN + 'Vileplume' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':8, 'DEFENSE':8.5})
    Paras1 = Pokemon(Fore.GREEN + 'Paras' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':7, 'DEFENSE':5.5})
    Parasect1 = Pokemon(Fore.GREEN + 'Parasect' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9.5, 'DEFENSE':8})
    Bellsprout1 = Pokemon(Fore.GREEN + 'Bellsprout' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':7.5, 'DEFENSE':3.5})
    Weepinbell1 = Pokemon(Fore.GREEN + 'Weepinbell' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9, 'DEFENSE':5})
    Victrebell1 = Pokemon(Fore.GREEN + 'Victrebell' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':10.5, 'DEFENSE':6.5})
    Exeggcute1 = Pokemon(Fore.GREEN + 'Exeggcute' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':4, 'DEFENSE':8})
    Exeggutor1 = Pokemon(Fore.GREEN + 'Exeggutor' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':9.5, 'DEFENSE':8.5})
    Tangela1 = Pokemon(Fore.GREEN + 'Tangela' + Fore.RESET, 'Grass', random.sample(rand_move_grass, 4),{'ATTACK':5.5, 'DEFENSE':11.5})

    #Bug
    Caterpie1 = Pokemon(Fore.LIGHTGREEN_EX + "Caterpie" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":3, "DEFENSE":3.5})
    Metapod1 = Pokemon(Fore.LIGHTGREEN_EX + "Metapod" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":2, "DEFENSE":5.5})
    Butterfree1 = Pokemon(Fore.LIGHTGREEN_EX + "Butterfree" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":4.5, "DEFENSE":5})
    Weedle1= Pokemon(Fore.LIGHTGREEN_EX + "Weedle" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":3.5, "DEFENSE":3})
    Kakuna1 = Pokemon(Fore.LIGHTGREEN_EX + "Kakuna" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":2.5, "DEFENSE":5})
    Beedrill1 = Pokemon(Fore.LIGHTGREEN_EX + "Beedrill" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":9, "DEFENSE":4})
    Scyther1 = Pokemon(Fore.LIGHTGREEN_EX + "Scyther" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":11, "DEFENSE":8})
    Pinsir1 = Pokemon(Fore.LIGHTGREEN_EX + "Pinsir" + Fore.RESET, "Bug", random.sample(rand_move_bug, 4), {"ATTACK":12.5, "DEFENSE":10})

    #Flying
    Pidgey1 = Pokemon(Fore.CYAN + "Pidgey" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":4.5, "DEFENSE":4})
    Pidgeotto1 = Pokemon(Fore.CYAN + "Pidgeotto" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":6, "DEFENSE":5.5})
    Pidgeot1 = Pokemon(Fore.CYAN + "Pidgeot" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":8, "DEFENSE":7.5})
    Spearow1 = Pokemon(Fore.CYAN + "Spearow" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":6, "DEFENSE":3})
    Fearow1 = Pokemon(Fore.CYAN + "Fearow" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":9, "DEFENSE":6.5})
    Aerodactyl1 = Pokemon(Fore.CYAN + "Aerodactyl" + Fore.RESET, "Flying", random.sample(rand_move_flying, 4), {"ATTACK":10.5, "DEFENSE":6.5})

    #Normal
    Rattata1 = Pokemon(Fore.LIGHTBLACK_EX + "Rattata" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.6, "DEFENSE":3.5})
    Raticate1 = Pokemon(Fore.LIGHTBLACK_EX + "Raticate" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":8.1, "DEFENSE":6})
    Meowth1 = Pokemon(Fore.LIGHTBLACK_EX + "Meowth" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":4.5, "DEFENSE":3.5})
    Persian1 = Pokemon(Fore.LIGHTBLACK_EX + "Persian" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":7, "DEFENSE":6.5})
    Lickitung1 = Pokemon(Fore.LIGHTBLACK_EX + "Lickitung" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.5, "DEFENSE":7.5})
    Kangaskhan1 = Pokemon(Fore.LIGHTBLACK_EX + "Kangaskhan" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":9.5, "DEFENSE":8})
    Tauros1 = Pokemon(Fore.LIGHTBLACK_EX + "Tauros" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":10, "DEFENSE":9.5})
    Eevee1= Pokemon(Fore.LIGHTBLACK_EX + "Eevee" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":5.5, "DEFENSE":5})
    Porygon1 = Pokemon(Fore.LIGHTBLACK_EX + "Porygon" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":6, "DEFENSE":7})
    Snorlax1 = Pokemon(Fore.LIGHTBLACK_EX + "Snorlax" + Fore.RESET, "Normal", random.sample(rand_move_normal, 4), {"ATTACK":6.5, "DEFENSE":11})

    #Electric
    Pikachu1 = Pokemon(Fore.LIGHTYELLOW_EX + "Pikachu" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":5.5, "DEFENSE":4})
    Raichu1 = Pokemon(Fore.LIGHTYELLOW_EX + "Raichu" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":9, "DEFENSE":5.5})
    Voltorb1 = Pokemon(Fore.LIGHTYELLOW_EX + "Voltorb" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":3, "DEFENSE":5})
    Electrode1 = Pokemon(Fore.LIGHTYELLOW_EX + "Electrode" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":5, "DEFENSE":7})
    Electabuzz1 = Pokemon(Fore.LIGHTYELLOW_EX + "Electabuzz" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":8.3, "DEFENSE":5.7})
    Jolteon1 = Pokemon(Fore.LIGHTYELLOW_EX + "Jolteon" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":6.5, "DEFENSE":6})
    Zapdos1 = Pokemon(Fore.LIGHTYELLOW_EX + "Zapdos" + Fore.RESET, "Electric", random.sample(rand_move_electric, 4), {"ATTACK":9, "DEFENSE":8.5})

    #Ground
    Sandshrew1 = Pokemon(Fore.YELLOW + "Sandshrew" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":7.5, "DEFENSE":8.5})
    Sandslash1 = Pokemon(Fore.YELLOW + "Sandslash" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":10, "DEFENSE":11})
    Dugtrio1 = Pokemon(Fore.YELLOW + "Dugtrio" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":10, "DEFENSE":5})
    Rhyhorn1 = Pokemon(Fore.YELLOW + "Rhyhorn" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":8.5, "DEFENSE":9.5})
    Rhydon1 = Pokemon(Fore.YELLOW + "Rhydon" + Fore.RESET, "Ground", random.sample(rand_move_ground, 4), {"ATTACK":13, "DEFENSE":12})

    #Fighting
    Mankey1 = Pokemon(Fore.WHITE + "Mankey" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":8, "DEFENSE":3.5})
    Primeape1 = Pokemon(Fore.WHITE + "Primeape" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10.5, "DEFENSE":6})
    Machop1 = Pokemon(Fore.WHITE + "Machop" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":8, "DEFENSE":5})
    Machoke1 = Pokemon(Fore.WHITE + "Machoke" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10, "DEFENSE":7})
    Machamp1 = Pokemon(Fore.WHITE + "Machamp" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":13, "DEFENSE":8})
    Hitmonlee1 = Pokemon(Fore.WHITE + "Hitmonlee" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":12, "DEFENSE":5.3})
    Hitmonchan1 = Pokemon(Fore.WHITE + "Hitmonchan" + Fore.RESET, "Fighting", random.sample(rand_move_fight, 4), {"ATTACK":10.5, "DEFENSE":7.9})

    #Psychic
    Hypno1 = Pokemon(Fore.LIGHTMAGENTA_EX + "Hypno" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":7.3, "DEFENSE":7})
    Mewtwo1 = Pokemon(Fore.LIGHTMAGENTA_EX + "Mewtwo" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":11, "DEFENSE":9})
    Mew1 = Pokemon(Fore.LIGHTMAGENTA_EX + "Mew" + Fore.RESET, "Psychic", random.sample(rand_move_psychic, 4), {"ATTACK":10, "DEFENSE":10})


    random_opponent_pokemon = random.sample(range(9), 3)
    random_player_pokemon = random.sample(range(85), 3)
    
    #Opponent Randomization
    
    if hidingText == 0:
        #opponent = random_opponent_pokemon[0]
        opponent = Raichu1
        opponentName = "Raichu"
        if opponent == 0:
            opponent = Charmander1
            opponentName = Fore.RED + 'Charmander' + Fore.RESET
        if opponent == 1:
            opponent = Squirtle1
            opponentName = Fore.BLUE + 'Squirtle' + Fore.RESET
        if opponent == 2:
            opponent = Bulbasaur1
            opponentName = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if opponent == 3:
            opponent = Charmeleon1
            opponentName = Fore.RED + 'Charmeleon' + Fore.RESET
        if opponent == 4:
            opponent = Wartortle1
            opponentName = Fore.BLUE + 'Wartortle' + Fore.RESET
        if opponent == 5:
            opponent = Ivysaur1
            opponentName = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if opponent == 6:
            opponent = Charizard1
            opponentName = Fore.RED + 'Charizard' + Fore.RESET
        if opponent == 7:
            opponent = Blastoise1
            opponentName = Fore.BLUE + 'Blastoise' + Fore.RESET
        if opponent == 8:
            opponent = Venusaur1
            opponentName = Fore.GREEN + 'Venusaur' + Fore.RESET
    
    if hidingText == 0:
        #opponent1 = random_opponent_pokemon[1]
        opponent1 = Sandshrew1
        opponentName1 = "Sandshrew"
        if opponent1 == 0:
            opponent1 = Charmander1
            opponentName1 = Fore.RED + 'Charmander' + Fore.RESET
        if opponent1 == 1:
            opponent1 = Squirtle1
            opponentName1 = Fore.BLUE + 'Squirtle' + Fore.RESET
        if opponent1 == 2:
            opponent1 = Bulbasaur1
            opponentName1 = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if opponent1 == 3:
            opponent1 = Charmeleon1
            opponentName1 = Fore.RED + 'Charmeleon' + Fore.RESET
        if opponent1 == 4:
            opponent1 = Wartortle1
            opponentName1 = Fore.BLUE + 'Wartortle' + Fore.RESET
        if opponent1 == 5:
            opponent1 = Ivysaur1
            opponentName1 = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if opponent1 == 6:
            opponent1 = Charizard1
            opponentName1 = Fore.RED + 'Charizard' + Fore.RESET
        if opponent1 == 7:
            opponent1 = Blastoise1
            opponentName1 = Fore.BLUE + 'Blastoise' + Fore.RESET
        if opponent1 == 8:
            opponent1 = Venusaur1
            opponentName1 = Fore.GREEN + 'Venusaur' + Fore.RESET

    if hidingText == 0:
        #opponent2 = random_opponent_pokemon[2]
        opponent2 = Mew1
        opponentName2 = "Mew"
        if opponent2 == 0:
            opponent2 = Charmander1
            opponentName2 = Fore.RED + 'Charmander' + Fore.RESET
        if opponent2 == 1:
            opponent2 = Squirtle1
            opponentName2 = Fore.BLUE + 'Squirtle' + Fore.RESET
        if opponent2 == 2:
            opponent2 = Bulbasaur1
            opponentName2 = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if opponent2 == 3:
            opponent2 = Charmeleon1
            opponentName2 = Fore.RED + 'Charmeleon' + Fore.RESET
        if opponent2 == 4:
            opponent2 = Wartortle1
            opponentName2 = Fore.BLUE + 'Wartortle' + Fore.RESET
        if opponent2 == 5:
            opponent2 = Ivysaur1
            opponentName2 = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if opponent2 == 6:
            opponent2 = Charizard1
            opponentName2 = Fore.RED + 'Charizard' + Fore.RESET
        if opponent2 == 7:
            opponent2 = Blastoise1
            opponentName2 = Fore.BLUE + 'Blastoise' + Fore.RESET
        if opponent2 == 8:
            opponent2 = Venusaur1
            opponentName2 = Fore.GREEN + 'Venusaur' + Fore.RESET
    
    
    #Player randomization
    if hidingText == 0:
        player = random_player_pokemon[0]
        if player == 0:
            player = Charmander
            playerrName = Fore.RED + 'Charmander' + Fore.RESET
        if player == 1:
            player = Squirtle
            playerrName = Fore.BLUE + 'Squirtle' + Fore.RESET
        if player == 2:
            player = Bulbasaur
            playerrName = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if player == 3:
            player = Charmeleon
            playerrName = Fore.RED + 'Charmeleon' + Fore.RESET
        if player == 4:
            player = Wartortle
            playerrName = Fore.BLUE + 'Wartortle' + Fore.RESET
        if player == 5:
            player = Ivysaur
            playerrName = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if player == 6:
            player = Charizard
            playerrName = Fore.RED + 'Charizard' + Fore.RESET
        if player == 7:
            player = Blastoise
            playerrName = Fore.BLUE + 'Blastoise' + Fore.RESET
        if player == 8:
            player = Venusaur
            playerrName = Fore.GREEN + 'Venusaur' + Fore.RESET

        #Fire
        if player == 9:
            player = Vulpix
            playerrName = Fore.RED + 'Vulpix' + Fore.RESET
        if player == 10:
            player = Ninetales
            playerrName = Fore.RED + 'Ninetales' + Fore.RESET
        if player == 11:
            player = Growlithe
            playerrName = Fore.RED + 'Growlithe' + Fore.RESET
        if player == 12:
            player = Arcanine
            playerrName = Fore.RED + 'Arcanine' + Fore.RESET
        if player == 13:
            player = Ponyata
            playerrName = Fore.RED + 'Ponyata' + Fore.RESET
        if player == 14:
            player = Rapidash
            playerrName = Fore.RED + 'Rapidash' + Fore.RESET
        if player == 15:
            player = Magmar
            playerrName = Fore.RED + 'Magmar' + Fore.RESET
        if player == 16:
            player = Flareon
            playerrName = Fore.RED + 'Flareon' + Fore.RESET
        if player == 17:
            player = Moltres
            playerrName = Fore.RED + 'Moltres' + Fore.RESET

        #Water
        if player == 18:
            player = Psyduck
            playerrName = Fore.BLUE + 'Psyduck' + Fore.RESET
        if player == 19:
            player = Golduck
            playerrName = Fore.BLUE + 'Golduck' + Fore.RESET
        if player == 20:
            player = Poliwag
            playerrName = Fore.BLUE + 'Poliwag' + Fore.RESET
        if player == 21:
            player = Poliwhirl
            playerrName = Fore.BLUE + 'Poliwhirl' + Fore.RESET
        if player == 22:
            player = Poliwrath
            playerrName = Fore.BLUE + 'Poliwrath' + Fore.RESET
        if player == 23:
            player = Krabby
            playerrName = Fore.BLUE + 'Krabby' + Fore.RESET
        if player == 24:
            player = Kingler
            playerrName = Fore.BLUE + 'Kingler' + Fore.RESET
        if player == 25:
            player = Staryu
            playerrName = Fore.BLUE + 'Staryu' + Fore.RESET
        if player == 26:
            player = Starmie
            playerrName = Fore.BLUE + 'Starmie' + Fore.RESET
        if player == 27:
            player = Magikarp
            playerrName = Fore.BLUE + 'Magikarp' + Fore.RESET
        if player == 28:
            player = Gyarados
            playerrName = Fore.BLUE + 'Gyarados' + Fore.RESET
        
        #Grass
        if player == 29:
            player = Oddish
            playerrName = Fore.GREEN + 'Oddish' + Fore.RESET
        if player == 30:
            player = Gloom
            playerrName = Fore.GREEN + 'Gloom' + Fore.RESET
        if player == 31:
            player = Vileplume
            playerrName = Fore.GREEN + 'Vileplume' + Fore.RESET
        if player == 32:
            player = Paras
            playerrName = Fore.GREEN + 'Paras' + Fore.RESET
        if player == 33:
            player = Parasect
            playerrName = Fore.GREEN + 'Parasect' + Fore.RESET
        if player == 34:
            player = Bellsprout
            playerrName = Fore.GREEN + 'Bellsprout' + Fore.RESET
        if player == 35:
            player = Weepinbell
            playerrName = Fore.GREEN + 'Weepinbell' + Fore.RESET
        if player == 36:
            player = Victrebell
            playerrName = Fore.GREEN + 'Victrebell' + Fore.RESET
        if player == 37:
            player = Exeggcute
            playerrName = Fore.GREEN + 'Exeggcute' + Fore.RESET
        if player == 38:
            player = Exeggutor
            playerrName = Fore.GREEN + 'Exeggutor' + Fore.RESET
        if player == 39:
            player = Tangela
            playerrName = Fore.GREEN + 'Tangela' + Fore.RESET

        #Bug
        if player == 40:
            player = Caterpie
            playerrName = Fore.LIGHTGREEN_EX + 'Caterpie' + Fore.RESET
        if player == 41:
            player = Metapod
            playerrName = Fore.LIGHTGREEN_EX + 'Metapod' + Fore.RESET
        if player == 42:
            player = Butterfree
            playerrName = Fore.LIGHTGREEN_EX + 'Butterfree' + Fore.RESET
        if player == 43:
            player = Weedle
            playerrName = Fore.LIGHTGREEN_EX + 'Weedle' + Fore.RESET
        if player == 44:
            player = Kakuna
            playerrName = Fore.LIGHTGREEN_EX + 'Kakuna' + Fore.RESET
        if player == 45:
            player = Beedrill
            playerrName = Fore.LIGHTGREEN_EX + 'Beedrill' + Fore.RESET
        if player == 46:
            player = Scyther
            playerrName = Fore.LIGHTGREEN_EX + 'Scyther' + Fore.RESET
        if player == 47:
            player = Pinsir
            playerrName = Fore.LIGHTGREEN_EX + 'Pinsir' + Fore.RESET

        #Flying
        if player == 48:
            player = Pidgey
            playerrName = Fore.CYAN + 'Pidgey' + Fore.RESET
        if player == 49:
            player = Pidgeotto
            playerrName = Fore.CYAN + 'Pidgeotto' + Fore.RESET
        if player == 50:
            player = Pidgeot
            playerrName = Fore.CYAN + 'Pidgeot' + Fore.RESET
        if player == 51:
            player = Spearow
            playerrName = Fore.CYAN + 'Spearow' + Fore.RESET
        if player == 52:
            player = Fearow
            playerrName = Fore.CYAN + 'Fearow' + Fore.RESET
        if player == 53:
            player = Aerodactyl
            playerrName = Fore.CYAN + 'Aerodactyl' + Fore.RESET
        
        #Normal
        if player == 54:
            player = Rattata
            playerrName = Fore.LIGHTBLACK_EX + 'Rattata' + Fore.RESET
        if player == 55:
            player = Raticate
            playerrName = Fore.LIGHTBLACK_EX + 'Raticate' + Fore.RESET
        if player == 56:
            player = Meowth
            playerrName = Fore.LIGHTBLACK_EX + 'Meowth' + Fore.RESET
        if player == 57:
            player = Persian
            playerrName = Fore.LIGHTBLACK_EX + 'Persian' + Fore.RESET
        if player == 58:
            player = Lickitung
            playerrName = Fore.LIGHTBLACK_EX + 'Lickitung' + Fore.RESET
        if player == 59:
            player = Kangaskhan
            playerrName = Fore.LIGHTBLACK_EX + 'Kangaskhan' + Fore.RESET
        if player == 60:
            player = Tauros
            playerrName = Fore.LIGHTBLACK_EX + 'Tauros' + Fore.RESET
        if player == 61:
            player = Eevee
            playerrName = Fore.LIGHTBLACK_EX + 'Eevee' + Fore.RESET
        if player == 62:
            player = Porygon
            playerrName = Fore.LIGHTBLACK_EX + 'Porygon' + Fore.RESET
        if player == 63:
            player = Snorlax
            playerrName = Fore.LIGHTBLACK_EX + 'Snorlax' + Fore.RESET

        #Electric
        if player == 64:
            player = Pikachu
            playerrName = Fore.LIGHTYELLOW_EX + 'Pikachu' + Fore.RESET
        if player == 65:
            player = Raichu
            playerrName = Fore.LIGHTYELLOW_EX + 'Raichu' + Fore.RESET
        if player == 66:
            player = Voltorb
            playerrName = Fore.LIGHTYELLOW_EX + 'Voltorb' + Fore.RESET
        if player == 67:
            player = Electrode
            playerrName = Fore.LIGHTYELLOW_EX + 'Electrode' + Fore.RESET
        if player == 68:
            player = Electabuzz
            playerrName = Fore.LIGHTYELLOW_EX + 'Electabuzz' + Fore.RESET
        if player == 69:
            player = Jolteon
            playerrName = Fore.LIGHTYELLOW_EX + 'Jolteon' + Fore.RESET
        if player == 70:
            player = Zapdos
            playerrName = Fore.LIGHTYELLOW_EX + 'Zapdos' + Fore.RESET
        
        #Ground
        if player == 71:
            player = Sandshrew
            playerrName = Fore.YELLOW + 'Sandshrew' + Fore.RESET
        if player == 72:
            player = Sandslash
            playerrName = Fore.YELLOW + 'Sandslash' + Fore.RESET
        if player == 73:
            player = Dugtrio
            playerrName = Fore.YELLOW + 'Dugtrio' + Fore.RESET
        if player == 74:
            player = Rhyhorn
            playerrName = Fore.YELLOW + 'Rhyhorn' + Fore.RESET
        if player == 75:
            player = Rhydon
            playerrName = Fore.YELLOW + 'Rhydon' + Fore.RESET
        
        #Fighting
        if player == 76:
            player = Mankey
            playerrName = Fore.YELLOW + 'Mankey' + Fore.RESET
        if player == 77:
            player = Primeape
            playerrName = Fore.YELLOW + 'Primeape' + Fore.RESET
        if player == 78:
            player = Machop
            playerrName = Fore.YELLOW + 'Machop' + Fore.RESET
        if player == 79:
            player = Machoke
            playerrName = Fore.YELLOW + 'Machoke' + Fore.RESET
        if player == 80:
            player = Machamp
            playerrName = Fore.YELLOW + 'Machamp' + Fore.RESET
        if player == 81:
            player = Hitmonlee
            playerrName = Fore.YELLOW + 'Hitmonlee' + Fore.RESET
        if player == 82:
            player = Hitmonchan
            playerrName = Fore.YELLOW + 'Hitmonchan' + Fore.RESET
        
        #Psychic
        if player == 83:
            player = Hypno
            playerrName = Fore.LIGHTMAGENTA_EX + 'Hypno' + Fore.RESET
        if player == 84:
            player = Mewtwo
            playerrName = Fore.LIGHTMAGENTA_EX + 'Mewtwo' + Fore.RESET
        if player == 85:
            player = Mew
            playerrName = Fore.LIGHTMAGENTA_EX + 'Mew' + Fore.RESET
    
    if hidingText == 0:
        player1 = random_player_pokemon[1]
        if player1 == 0:
            player1 = Charmander
            playerrName1 = Fore.RED + 'Charmander' + Fore.RESET
        if player1 == 1:
            player1 = Squirtle
            playerrName1 = Fore.BLUE + 'Squirtle' + Fore.RESET
        if player1 == 2:
            player1 = Bulbasaur
            playerrName1 = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if player1 == 3:
            player1 = Charmeleon
            playerrName1 = Fore.RED + 'Charmeleon' + Fore.RESET
        if player1 == 4:
            player1 = Wartortle
            playerrName1 = Fore.BLUE + 'Wartortle' + Fore.RESET
        if player1 == 5:
            player1 = Ivysaur
            playerrName1 = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if player1 == 6:
            player1 = Charizard
            playerrName1 = Fore.RED + 'Charizard' + Fore.RESET
        if player1 == 7:
            player1 = Blastoise
            playerrName1 = Fore.BLUE + 'Blastoise' + Fore.RESET
        if player1 == 8:
            player1 = Venusaur
            playerrName1 = Fore.GREEN + 'Venusaur' + Fore.RESET
        
        #Fire
        if player1 == 9:
            player1 = Vulpix
            playerrName1 = Fore.RED + 'Vulpix' + Fore.RESET
        if player1 == 10:
            player1 = Ninetales
            playerrName1 = Fore.RED + 'Ninetales' + Fore.RESET
        if player1 == 11:
            player1 = Growlithe
            playerrName1 = Fore.RED + 'Growlithe' + Fore.RESET
        if player1 == 12:
            player1 = Arcanine
            playerrName1 = Fore.RED + 'Arcanine' + Fore.RESET
        if player1== 13:
            player1 = Ponyata
            playerrName1 = Fore.RED + 'Ponyata' + Fore.RESET
        if player1 == 14:
            player1 = Rapidash
            playerrName1 = Fore.RED + 'Rapidash' + Fore.RESET
        if player1 == 15:
            player1 = Magmar
            playerrName1 = Fore.RED + 'Magmar' + Fore.RESET
        if player1 == 16:
            player1 = Flareon
            playerrName1 = Fore.RED + 'Flareon' + Fore.RESET
        if player1 == 17:
            player1 = Moltres
            playerrName1 = Fore.RED + 'Moltres' + Fore.RESET

        #Water
        if player1 == 18:
            player1= Psyduck
            playerrName1 = Fore.BLUE + 'Psyduck' + Fore.RESET
        if player1 == 19:
            player1 = Golduck
            playerrName1 = Fore.BLUE + 'Golduck' + Fore.RESET
        if player1 == 20:
            player1 = Poliwag
            playerrName1 = Fore.BLUE + 'Poliwag' + Fore.RESET
        if player1 == 21:
            player1 = Poliwhirl
            playerrName1 = Fore.BLUE + 'Poliwhirl' + Fore.RESET
        if player1 == 22:
            player1 = Poliwrath
            playerrName1 = Fore.BLUE + 'Poliwrath' + Fore.RESET
        if player1 == 23:
            player1 = Krabby
            playerrName1 = Fore.BLUE + 'Krabby' + Fore.RESET
        if player1 == 24:
            player1 = Kingler
            playerrName1 = Fore.BLUE + 'Kingler' + Fore.RESET
        if player1 == 25:
            player1 = Staryu
            playerrName1 = Fore.BLUE + 'Staryu' + Fore.RESET
        if player1 == 26:
            player1 = Starmie
            playerrName1 = Fore.BLUE + 'Starmie' + Fore.RESET
        if player1 == 27:
            player1 = Magikarp
            playerrName1 = Fore.BLUE + 'Magikarp' + Fore.RESET
        if player1 == 28:
            player1 = Gyarados
            playerrName1 = Fore.BLUE + 'Gyarados' + Fore.RESET
        
        #Grass
        if player1 == 29:
            player1 = Oddish
            playerrName1 = Fore.GREEN + 'Oddish' + Fore.RESET
        if player1 == 30:
            player1 = Gloom
            playerrName1 = Fore.GREEN + 'Gloom' + Fore.RESET
        if player1 == 31:
            player1 = Vileplume
            playerrName1 = Fore.GREEN + 'Vileplume' + Fore.RESET
        if player1== 32:
            player1 = Paras
            playerrName1 = Fore.GREEN + 'Paras' + Fore.RESET
        if player1 == 33:
            player1 = Parasect
            playerrName1 = Fore.GREEN + 'Parasect' + Fore.RESET
        if player1 == 34:
            player1 = Bellsprout
            playerrName1 = Fore.GREEN + 'Bellsprout' + Fore.RESET
        if player1 == 35:
            player1 = Weepinbell
            playerrName1 = Fore.GREEN + 'Weepinbell' + Fore.RESET
        if player1 == 36:
            player1 = Victrebell
            playerrName1 = Fore.GREEN + 'Victrebell' + Fore.RESET
        if player1 == 37:
            player1 = Exeggcute
            playerrName1 = Fore.GREEN + 'Exeggcute' + Fore.RESET
        if player1 == 38:
            player1 = Exeggutor
            playerrName1 = Fore.GREEN + 'Exeggutor' + Fore.RESET
        if player1 == 39:
            player1 = Tangela
            playerrName1= Fore.GREEN + 'Tangela' + Fore.RESET

        #Bug
        if player1 == 40:
            player1 = Caterpie
            playerrName1 = Fore.LIGHTGREEN_EX + 'Caterpie' + Fore.RESET
        if player1 == 41:
            player1 = Metapod
            playerrName1 = Fore.LIGHTGREEN_EX + 'Metapod' + Fore.RESET
        if player1 == 42:
            player1 = Butterfree
            playerrName1 = Fore.LIGHTGREEN_EX + 'Butterfree' + Fore.RESET
        if player1 == 43:
            player1 = Weedle
            playerrName1 = Fore.LIGHTGREEN_EX + 'Weedle' + Fore.RESET
        if player1 == 44:
            player1 = Kakuna
            playerrName1 = Fore.LIGHTGREEN_EX + 'Kakuna' + Fore.RESET
        if player1 == 45:
            player1 = Beedrill
            playerrName1 = Fore.LIGHTGREEN_EX + 'Beedrill' + Fore.RESET
        if player1 == 46:
            player1 = Scyther
            playerrName1 = Fore.LIGHTGREEN_EX + 'Scyther' + Fore.RESET
        if player1 == 47:
            player1= Pinsir
            playerrName1 = Fore.LIGHTGREEN_EX + 'Pinsir' + Fore.RESET

        #Flying
        if player1 == 48:
            player1 = Pidgey
            playerrName1 = Fore.CYAN + 'Pidgey' + Fore.RESET
        if player1 == 49:
            player1 = Pidgeotto
            playerrName1 = Fore.CYAN + 'Pidgeotto' + Fore.RESET
        if player1 == 50:
            player1 = Pidgeot
            playerrName1 = Fore.CYAN + 'Pidgeot' + Fore.RESET
        if player1 == 51:
            player1 = Spearow
            playerrName1 = Fore.CYAN + 'Spearow' + Fore.RESET
        if player1 == 52:
            player1 = Fearow
            playerrName1 = Fore.CYAN + 'Fearow' + Fore.RESET
        if player1 == 53:
            player1 = Aerodactyl
            playerrName1 = Fore.CYAN + 'Aerodactyl' + Fore.RESET
        
        #Normal
        if player1 == 54:
            player1 = Rattata
            playerrName1 = Fore.LIGHTBLACK_EX + 'Rattata' + Fore.RESET
        if player1 == 55:
            player1 = Raticate
            playerrName1 = Fore.LIGHTBLACK_EX + 'Raticate' + Fore.RESET
        if player1 == 56:
            player1 = Meowth
            playerrName1 = Fore.LIGHTBLACK_EX + 'Meowth' + Fore.RESET
        if player1 == 57:
            player1 = Persian
            playerrName1 = Fore.LIGHTBLACK_EX + 'Persian' + Fore.RESET
        if player1 == 58:
            player1 = Lickitung
            playerrName1 = Fore.LIGHTBLACK_EX + 'Lickitung' + Fore.RESET
        if player1 == 59:
            player1 = Kangaskhan
            playerrName1 = Fore.LIGHTBLACK_EX + 'Kangaskhan' + Fore.RESET
        if player1 == 60:
            player1 = Tauros
            playerrName1 = Fore.LIGHTBLACK_EX + 'Tauros' + Fore.RESET
        if player1 == 61:
            player1 = Eevee
            playerrName1 = Fore.LIGHTBLACK_EX + 'Eevee' + Fore.RESET
        if player1== 62:
            player1 = Porygon
            playerrName1 = Fore.LIGHTBLACK_EX + 'Porygon' + Fore.RESET
        if player1 == 63:
            player1 = Snorlax
            playerrName1 = Fore.LIGHTBLACK_EX + 'Snorlax' + Fore.RESET

        #Electric
        if player1 == 64:
            player1 = Pikachu
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Pikachu' + Fore.RESET
        if player1 == 65:
            player1 = Raichu
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Raichu' + Fore.RESET
        if player1 == 66:
            player1 = Voltorb
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Voltorb' + Fore.RESET
        if player1 == 67:
            player1 = Electrode
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Electrode' + Fore.RESET
        if player1 == 68:
            player1 = Electabuzz
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Electabuzz' + Fore.RESET
        if player1 == 69:
            player1 = Jolteon
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Jolteon' + Fore.RESET
        if player1 == 70:
            player1 = Zapdos
            playerrName1 = Fore.LIGHTYELLOW_EX + 'Zapdos' + Fore.RESET
        
        #Ground
        if player1 == 71:
            player1 = Sandshrew
            playerrName1 = Fore.YELLOW + 'Sandshrew' + Fore.RESET
        if player1 == 72:
            player1 = Sandslash
            playerrNam1e = Fore.YELLOW + 'Sandslash' + Fore.RESET
        if player1 == 73:
            player1 = Dugtrio
            playerrName1 = Fore.YELLOW + 'Dugtrio' + Fore.RESET
        if player1 == 74:
            player1 = Rhyhorn
            playerrName1 = Fore.YELLOW + 'Rhyhorn' + Fore.RESET
        if player1== 75:
            player1 = Rhydon
            playerrName1 = Fore.YELLOW + 'Rhydon' + Fore.RESET
        
        #Fighting
        if player1 == 76:
            player1 = Mankey
            playerrName1 = Fore.YELLOW + 'Mankey' + Fore.RESET
        if player1 == 77:
            player1 = Primeape
            playerrName1 = Fore.YELLOW + 'Primeape' + Fore.RESET
        if player1 == 78:
            player1 = Machop
            playerrName1 = Fore.YELLOW + 'Machop' + Fore.RESET
        if player1 == 79:
            player1 = Machoke
            playerrName1 = Fore.YELLOW + 'Machoke' + Fore.RESET
        if player1 == 80:
            player1 = Machamp
            playerrName1 = Fore.YELLOW + 'Machamp' + Fore.RESET
        if player1 == 81:
            player1 = Hitmonlee
            playerrName1 = Fore.YELLOW + 'Hitmonlee' + Fore.RESET
        if player1 == 82:
            player1 = Hitmonchan
            playerrName1 = Fore.YELLOW + 'Hitmonchan' + Fore.RESET
        
        #Psychic
        if player1 == 83:
            player1= Hypno
            playerrName1 = Fore.LIGHTMAGENTA_EX + 'Hypno' + Fore.RESET
        if player1 == 84:
            player1 = Mewtwo
            playerrName1 = Fore.LIGHTMAGENTA_EX + 'Mewtwo' + Fore.RESET
        if player1 == 85:
            player1 = Mew
            playerrName1 = Fore.LIGHTMAGENTA_EX + 'Mew' + Fore.RESET

    if hidingText == 0:
        player2 = random_player_pokemon[2]
        if player2 == 0:
            player2 = Charmander
            playerrName2 = Fore.RED + 'Charmander' + Fore.RESET
        if player2 == 1:
            player2 = Squirtle
            playerrName2 = Fore.BLUE + 'Squirtle' + Fore.RESET
        if player2 == 2:
            player2 = Bulbasaur
            playerrName2 = Fore.GREEN + 'Bulbasaur' + Fore.RESET
        if player2 == 3:
            player2 = Charmeleon
            playerrName2 = Fore.RED + 'Charmeleon' + Fore.RESET
        if player2 == 4:
            player2 = Wartortle
            playerrName2 = Fore.BLUE + 'Wartortle' + Fore.RESET
        if player2 == 5:
            player2 = Ivysaur
            playerrName2 = Fore.GREEN + 'Ivysaur' + Fore.RESET
        if player2 == 6:
            player2 = Charizard
            playerrName2 = Fore.RED + 'Charizard' + Fore.RESET
        if player2 == 7:
            player2 = Blastoise
            playerrName2 = Fore.BLUE + 'Blastoise' + Fore.RESET
        if player2 == 8:
            player2 = Venusaur
            playerrName2 = Fore.GREEN + 'Venusaur' + Fore.RESET

        #Fire
        if player2 == 9:
            player2 = Vulpix
            playerrName2 = Fore.RED + 'Vulpix' + Fore.RESET
        if player2 == 10:
            player2 = Ninetales
            playerrName2 = Fore.RED + 'Ninetales' + Fore.RESET
        if player2 == 11:
            player2 = Growlithe
            playerrName2 = Fore.RED + 'Growlithe' + Fore.RESET
        if player2 == 12:
            player2 = Arcanine
            playerrName2 = Fore.RED + 'Arcanine' + Fore.RESET
        if player2 == 13:
            player2 = Ponyata
            playerrName2 = Fore.RED + 'Ponyata' + Fore.RESET
        if player2 == 14:
            player2 = Rapidash
            playerrName2 = Fore.RED + 'Rapidash' + Fore.RESET
        if player2 == 15:
            player2 = Magmar
            playerrName2 = Fore.RED + 'Magmar' + Fore.RESET
        if player2 == 16:
            player2 = Flareon
            playerrNam2 = Fore.RED + 'Flareon' + Fore.RESET
        if player2 == 17:
            player2 = Moltres
            playerrName2 = Fore.RED + 'Moltres' + Fore.RESET

        #Water
        if player2 == 18:
            player2 = Psyduck
            playerrName2 = Fore.BLUE + 'Psyduck' + Fore.RESET
        if player2 == 19:
            player2 = Golduck
            playerrName2 = Fore.BLUE + 'Golduck' + Fore.RESET
        if player2 == 20:
            player2 = Poliwag
            playerrName2 = Fore.BLUE + 'Poliwag' + Fore.RESET
        if player2 == 21:
            player2 = Poliwhirl
            playerrName2 = Fore.BLUE + 'Poliwhirl' + Fore.RESET
        if player2 == 22:
            player2 = Poliwrath
            playerrName2 = Fore.BLUE + 'Poliwrath' + Fore.RESET
        if player2 == 23:
            player2 = Krabby
            playerrName2 = Fore.BLUE + 'Krabby' + Fore.RESET
        if player2 == 24:
            player2 = Kingler
            playerrName2 = Fore.BLUE + 'Kingler' + Fore.RESET
        if player2 == 25:
            player2 = Staryu
            playerrName2 = Fore.BLUE + 'Staryu' + Fore.RESET
        if player2 == 26:
            player2 = Starmie
            playerrName2 = Fore.BLUE + 'Starmie' + Fore.RESET
        if player2 == 27:
            player2 = Magikarp
            playerrName2 = Fore.BLUE + 'Magikarp' + Fore.RESET
        if player2 == 28:
            player2 = Gyarados
            playerrName2 = Fore.BLUE + 'Gyarados' + Fore.RESET
        
        #Grass
        if player2 == 29:
            player2 = Oddish
            playerrName2 = Fore.GREEN + 'Oddish' + Fore.RESET
        if player2 == 30:
            player2 = Gloom
            playerrName2 = Fore.GREEN + 'Gloom' + Fore.RESET
        if player2 == 31:
            player2 = Vileplume
            playerrName2 = Fore.GREEN + 'Vileplume' + Fore.RESET
        if player2 == 32:
            player2 = Paras
            playerrName2 = Fore.GREEN + 'Paras' + Fore.RESET
        if player2 == 33:
            player2 = Parasect
            playerrName2 = Fore.GREEN + 'Parasect' + Fore.RESET
        if player2 == 34:
            player2 = Bellsprout
            playerrName2 = Fore.GREEN + 'Bellsprout' + Fore.RESET
        if player2 == 35:
            player2 = Weepinbell
            playerrName2 = Fore.GREEN + 'Weepinbell' + Fore.RESET
        if player2 == 36:
            player2 = Victrebell
            playerrName2 = Fore.GREEN + 'Victrebell' + Fore.RESET
        if player2 == 37:
            player2 = Exeggcute
            playerrName2 = Fore.GREEN + 'Exeggcute' + Fore.RESET
        if player2 == 38:
            player2 = Exeggutor
            playerrName2 = Fore.GREEN + 'Exeggutor' + Fore.RESET
        if player2 == 39:
            player2 = Tangela
            playerrName2= Fore.GREEN + 'Tangela' + Fore.RESET

        #Bug
        if player2 == 40:
            player2 = Caterpie
            playerrName2 = Fore.LIGHTGREEN_EX + 'Caterpie' + Fore.RESET
        if player2 == 41:
            player2 = Metapod
            playerrName2 = Fore.LIGHTGREEN_EX + 'Metapod' + Fore.RESET
        if player2 == 42:
            player2 = Butterfree
            playerrName2 = Fore.LIGHTGREEN_EX + 'Butterfree' + Fore.RESET
        if player2 == 43:
            player2 = Weedle
            playerrName2 = Fore.LIGHTGREEN_EX + 'Weedle' + Fore.RESET
        if player2 == 44:
            player2 = Kakuna
            playerrName2 = Fore.LIGHTGREEN_EX + 'Kakuna' + Fore.RESET
        if player2 == 45:
            player2 = Beedrill
            playerrName2 = Fore.LIGHTGREEN_EX + 'Beedrill' + Fore.RESET
        if player2 == 46:
            player2 = Scyther
            playerrName2 = Fore.LIGHTGREEN_EX + 'Scyther' + Fore.RESET
        if player2 == 47:
            player2 = Pinsir
            playerrName2 = Fore.LIGHTGREEN_EX + 'Pinsir' + Fore.RESET

        #Flying
        if player2 == 48:
            player2 = Pidgey
            playerrName2 = Fore.CYAN + 'Pidgey' + Fore.RESET
        if player2 == 49:
            player2 = Pidgeotto
            playerrName2 = Fore.CYAN + 'Pidgeotto' + Fore.RESET
        if player2 == 50:
            player2 = Pidgeot
            playerrName2 = Fore.CYAN + 'Pidgeot' + Fore.RESET
        if player2 == 51:
            player2 = Spearow
            playerrName2 = Fore.CYAN + 'Spearow' + Fore.RESET
        if player2 == 52:
            player2 = Fearow
            playerrName2 = Fore.CYAN + 'Fearow' + Fore.RESET
        if player2 == 53:
            player2 = Aerodactyl
            playerrName2 = Fore.CYAN + 'Aerodactyl' + Fore.RESET
        
        #Normal
        if player2 == 54:
            player2 = Rattata
            playerrName2 = Fore.LIGHTBLACK_EX + 'Rattata' + Fore.RESET
        if player2 == 55:
            player2 = Raticate
            playerrName2 = Fore.LIGHTBLACK_EX + 'Raticate' + Fore.RESET
        if player2 == 56:
            player2 = Meowth
            playerrName2 = Fore.LIGHTBLACK_EX + 'Meowth' + Fore.RESET
        if player2 == 57:
            player2 = Persian
            playerrName2 = Fore.LIGHTBLACK_EX + 'Persian' + Fore.RESET
        if player2 == 58:
            player2 = Lickitung
            playerrName2 = Fore.LIGHTBLACK_EX + 'Lickitung' + Fore.RESET
        if player2 == 59:
            player2 = Kangaskhan
            playerrName2 = Fore.LIGHTBLACK_EX + 'Kangaskhan' + Fore.RESET
        if player2 == 60:
            player2 = Tauros
            playerrName2 = Fore.LIGHTBLACK_EX + 'Tauros' + Fore.RESET
        if player2 == 61:
            player2 = Eevee
            playerrName2 = Fore.LIGHTBLACK_EX + 'Eevee' + Fore.RESET
        if player2 == 62:
            player2 = Porygon
            playerrName2 = Fore.LIGHTBLACK_EX + 'Porygon' + Fore.RESET
        if player2 == 63:
            player2 = Snorlax
            playerrName2 = Fore.LIGHTBLACK_EX + 'Snorlax' + Fore.RESET

        #Electric
        if player2 == 64:
            player2 = Pikachu
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Pikachu' + Fore.RESET
        if player2 == 65:
            player2 = Raichu
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Raichu' + Fore.RESET
        if player2 == 66:
            player2 = Voltorb
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Voltorb' + Fore.RESET
        if player2 == 67:
            player2 = Electrode
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Electrode' + Fore.RESET
        if player2 == 68:
            player2 = Electabuzz
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Electabuzz' + Fore.RESET
        if player2 == 69:
            player2 = Jolteon
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Jolteon' + Fore.RESET
        if player2 == 70:
            player2 = Zapdos
            playerrName2 = Fore.LIGHTYELLOW_EX + 'Zapdos' + Fore.RESET
        
        #Ground
        if player2 == 71:
            player2 = Sandshrew
            playerrName2 = Fore.YELLOW + 'Sandshrew' + Fore.RESET
        if player2 == 72:
            player2 = Sandslash
            playerrName2 = Fore.YELLOW + 'Sandslash' + Fore.RESET
        if player2 == 73:
            player2 = Dugtrio
            playerrName2 = Fore.YELLOW + 'Dugtrio' + Fore.RESET
        if player2 == 74:
            player2 = Rhyhorn
            playerrName2 = Fore.YELLOW + 'Rhyhorn' + Fore.RESET
        if player2 == 75:
            player2 = Rhydon
            playerrName2 = Fore.YELLOW + 'Rhydon' + Fore.RESET
        
        #Fighting
        if player2 == 76:
            player2 = Mankey
            playerrName2 = Fore.YELLOW + 'Mankey' + Fore.RESET
        if player2 == 77:
            player2 = Primeape
            playerrName2 = Fore.YELLOW + 'Primeape' + Fore.RESET
        if player2 == 78:
            player2 = Machop
            playerrName2 = Fore.YELLOW + 'Machop' + Fore.RESET
        if player2 == 79:
            player2 = Machoke
            playerrName2 = Fore.YELLOW + 'Machoke' + Fore.RESET
        if player2 == 80:
            player2 = Machamp
            playerrName2 = Fore.YELLOW + 'Machamp' + Fore.RESET
        if player2 == 81:
            player2 = Hitmonlee
            playerrName2 = Fore.YELLOW + 'Hitmonlee' + Fore.RESET
        if player2 == 82:
            player2 = Hitmonchan
            playerrName2 = Fore.YELLOW + 'Hitmonchan' + Fore.RESET
        
        #Psychic
        if player2 == 83:
            player2 = Hypno
            playerrName2 = Fore.LIGHTMAGENTA_EX + 'Hypno' + Fore.RESET
        if player2 == 84:
            player2 = Mewtwo
            playerrName2 = Fore.LIGHTMAGENTA_EX + 'Mewtwo' + Fore.RESET
        if player2 == 85:
            player2 = Mew
            playerrName2 = Fore.LIGHTMAGENTA_EX + 'Mew' + Fore.RESET
    
    #If opponent has same pokemon = reroll
    """
    while player == opponent:
        player = random.randrange(1, 10)
        print(Fore.RED + "Same pokémon, rerolling" + Fore.RESET)
    """
    #Fight sequence
    player.fight(opponent)