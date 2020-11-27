#Kirdesh Kumar
#P13
#17/8/2020
# +------------------------
# | Text for various menus 
# +------------------------
main_text = ["New Game",\
             "Resume Game",\
#             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]



# Code your main program here

#========================================================================================#
############################-- IMPORTANT STUFF --#########################################
#========================================================================================#

import random
import sys
import pickle
import os
town_coord = [[0,0], [1, 3], [2, 5], [3, 1], [6, 4]]
Rat_King_coord = [7, 7]
all_coord = []
all_coord.extend(town_coord)
all_coord.append(Rat_King_coord)
global orb
orb = False
global day
day = 1

#========================================================================================#
########################-- STORE ITEMS AND THEIR PRICE --#################################
#========================================================================================#

potion = {'potion':5}
weapons = {'Normal Sword':20, 'Big Sword':35, 'Even Bigger Sword':50}
armours = {'Bronze Armour':20, 'Obsidion Armour':35, 'Meteor Armour':50}

#========================================================================================#
################################-- PLAYER CLASS --########################################
#========================================================================================#

#Using class and __init__ so that i do not need to call back to it whenever i need to use the
#information in other functions like attack and stuff and it is also easier to save.

class Player:
     def __init__(self, name):
             self.name = name
             self.maxhp = 25
             self.hp = self.maxhp             
             self.base_damage1 = 2
             self.base_damage2 = 5
             self.base_defence = 1
             self.coord = [0,0]
             self.coin = 10
             self.potion = 0
             self.weapon = ['Bare Hands']
             self.in_hand =['Bare Hands']
             self.armour = ['Clothes']
             self.armour_on = ['Clothes']

 
     @property
     def damage1(self):
          damage1 = self.base_damage1
          if self.in_hand == 'Bare Hands':
               damage1 += 0
          if self.in_hand == 'Normal Sword':
               damage1 += 1
          if self.in_hand == 'Big Sword':
               damage1 += 2
          if self.in_hand == 'Even Bigger Sword':
               damage1 += 3
          return damage1
     
     @property 
     def damage2(self):
          damage2 = self.base_damage2
          if self.in_hand == 'Bare Hands':
               damage2 += 0
          if self.in_hand == 'Normal Sword':
               damage2 += 1
          if self.in_hand == 'Big Sword':
               damage2 += 2
          if self.in_hand == 'Even Bigger Sword':
               damage2 += 3
          return damage2
     
     @property 
     def defence(self):
          defence = self.base_defence
          if self.armour_on == 'Clothes':
               defence += 0               
          if self.armour_on == 'Bronze Armour':
               defence += 1               
          if self.armour_on == 'Obsidion Armour':
               defence += 2               
          if self.armour_on == 'Meteor Armour':
               defence += 3
          return defence

#========================================================================================#
################################-- ENEMY CLASS --#########################################
#========================================================================================#

#>>>>>>>>>> CHIPMUNK CLASS <<<<<<<<<<#
class Chipmunk:
    def __init__(self, name):
        self.name = name
        self.maxhp = 12
        self.hp = self.maxhp
        self.damage1 = 2
        self.damage2 = 6
        self.defence = 1
        self.coindrop = 7
ChipmunkIG = Chipmunk('Chipmunk')



#>>>>>>>>>> GOPHER CLASS <<<<<<<<<<#
class Gopher:
    def __init__(self, name):
        self.name = name
        self.maxhp = 17
        self.hp = self.maxhp
        self.damage1 = 1
        self.damage2 = 4
        self.defence = 2
        self.coindrop = 12
GopherIG = Gopher('Gopher')



#>>>>>>>>>> RAT CLASS <<<<<<<<<<#
class Rat:
    def __init__(self, name):
        self.name = name
        self.maxhp = 10
        self.hp = self.maxhp
        self.damage1 = 1
        self.damage2 = 3
        self.defence = 1
        self.coindrop = 5
RatIG = Rat('Rat')



#>>>>>>>>>> JERBOA CLASS <<<<<<<<<<#
class Jerboa:
     def __init__(self, name):
          self.name = name
          self.maxhp = 7
          self.hp = self.maxhp
          self.damage1 = 5
          self.damage2 = 7
          self.defence = 1
          self.coindrop = 10
JerboaIG = Jerboa('Jerboa')



#>>>>>>>>>> BEAVER CLASS <<<<<<<<<<#
class Beaver:
     def __init__(self, name):
          self.name = name
          self.maxhp = 20
          self.hp = self.maxhp
          self.damage1 = 1
          self.damage2 = 3
          self.defence = 2
          self.coindrop = 14
BeaverIG = Beaver('Beaver')




#>>>>>>>>>> RODENT KING CLASS <<<<<<<<<<#
class Rat_King:
     def __init__(self, name):
        self.name = name
        self.maxhp = 30
        self.hp = self.maxhp
        self.damage1 = 8
        self.damage2 = 13
        self.defence = 5
Rat_KingIG = Rat_King('Rat King')

#========================================================================================#
##############################-- STARTING SCREEN --#######################################
#========================================================================================#

def Title_Screen():
     print('')
     print('Welcome to Ratventure!')
     print('----------------------')
     print('1) New Game')
     print('2) Resume Game')
     print('3) Exit Game')

     option = input('Enter Choice: ')

     if option == '1':
         new_game()

     elif option == '2':
          load()

     elif option == '3':
          print('')
          print('You Exited Ratventure')
          sys.exit()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Title_Screen()

#========================================================================================#
##################################-- NEW GAME --##########################################
#========================================================================================#

def new_game():
     print('')
     orb_location()
     print('Hello, what is your name?')
     option = input('>>> ')
     print('')
     print('You walk into the town and find 10 coins on the ground!') 
     print('Today is your lucky day! or is it....?')
     global PlayerIG
     PlayerIG = Player(option)
     Town_Menu()

#========================================================================================#
##################################-- TOWN MENU --#########################################
#========================================================================================#

def Town_Menu():
     print('')
     print('Day %i : You are in a town.' %day)
     print('1) View Character')
     print('2) View Map')
     print('3) Move')
     print('4) Rest')
     print('5) Store')
     print('6) Inventory')
     print('7) Save Game')
     print('8) Exit Game')

     option = input('Enter Choice: ')

     if option == '1':
          Character_info()
          Town_Menu()

     elif option == '2':          
          Map()         
          Town_Menu()

     elif option == '3':          
          Map()
          Move()

     elif option == '4':
          rest()
          Town_Menu()

     elif option == '5':
          store_options()
          Town_Menu()

     elif option == '6':
          inventory()
          Town_Menu

     elif option == '7':
          save()
          Town_Menu()

     elif option == '8':
          print('')
          print('You Exited Ratventure')
          sys.exit()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Town_Menu()

#========================================================================================#
#################################-- OUTDOOR MENU --#######################################
#========================================================================================#

def Outdoor_Menu():
     print('')
     print('Day %i: You are out in the open.' %day)
     print('1) View Character')
     print('2) View Map')
     print('3) Move')
     print('4) Sense Orb')
     print('5) Inventory')
     print('6) Exit Game')

     option = input('Enter Choice: ')

     if option == '1': 
         Character_info()
         Outdoor_Menu()

     elif option == '2':
          Map()
          Outdoor_Menu()

     elif option == '3':
          Map()
          Move()

     elif option == '4':
          if x == positionx and y == positiony:
               orb_found()
               Outdoor_Menu()

          else:
               orb_direction()
               Outdoor_Menu()


     elif option =='5':
          inventory()


     elif option == '6':
          print('')
          print('You Exited Ratventure')
          sys.exit()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Outdoor_Menu()
          
#========================================================================================#
################################-- PLAYER'S INFO --#######################################
#========================================================================================#

def Character_info():
     global orb
     print('')
     print('Name: %s' %PlayerIG.name)
     print('Damage: %i-%i' %(PlayerIG.damage1, PlayerIG.damage2))
     print('Defence: %i' %PlayerIG.defence)
     print('Health: %i' %PlayerIG.hp)
     print('Coins: %i' %PlayerIG.coin)
     print('Potions: %i' %PlayerIG.potion)

     if orb == True:
          print('You have the Orb of Power')
     else:
          pass

#========================================================================================#
##################################-- MAP --###############################################
#========================================================================================#

def Map():
    hero_location()
    print('')
    x, y = PlayerIG.coord[0], PlayerIG.coord[1]
    world_map[x][y] = '{:s}'.format(hero)
    m = ('+---+---+---+---+---+---+---+---+')
    Map = m + '\n'
    for j in range(8):
        for i in range(8):
            Map += '|{:^3s}'.format(world_map[j][i])
            if i == 7 and j != 7:
                Map += '|\n' + m + '\n'
            elif i == 7 and j == 7:
                Map += '|\n' + m
    print(Map)

#========================================================================================#
##################################-- MOVEMENT --##########################################
#========================================================================================#

#>>>>>>>>>> LEAVE LOCATION <<<<<<<<<<#
def leave_location():
     for a in all_coord:
          global leave
          if str(a) == str(Rat_King_coord) and str(a) == str(PlayerIG.coord):
               leave = 'K'
               break
          elif str(a) == str(PlayerIG.coord):
               leave = 'T'
               break
          else:
               leave = ' '


#>>>>>>>>>> HERO LOCATION <<<<<<<<<<#
def hero_location():
     for a in all_coord:
          global location
          global hero
          if str(a) == str(PlayerIG.coord) and str(a) == str(Rat_King_coord):
               location = 'rat king'
               hero = 'H/K'
               break
          elif str(a) == str(PlayerIG.coord):
               location = 'in a town'
               hero = 'H/T'
               break
          else:
               location = 'out in the open'
               hero = 'H'
     


#>>>>>>>>>> MOVEMENT <<<<<<<<<<#
def Move():
     global location, x, y, day
     leave_location()
     print('')
     print('W = up; A = left; S = down; D = right')
     move = input('Your move: ') 
     x,y = PlayerIG.coord[0],PlayerIG.coord[1]
     world_map[x][y] = '{:s}'.format(leave)
     
#>>>>>>>>> MOVE UP <<<<<<<<<<#
     x,y = PlayerIG.coord[0],PlayerIG.coord[1]
     if move == 'w':
         if x != 0:
             PlayerIG.coord[0] -= 1
         else:
              print('')
              print('Invalid option, Please select a valid option.')
              Move()
              
#>>>>>>>>> MOVE DOWN <<<<<<<<<<#
     elif move == 's':
         if x != 7:
             PlayerIG.coord[0] += 1
         else:
              print('')
              print('Invalid option, Please select a valid option.')
              Move()
              
#>>>>>>>>> MOVE LEFT <<<<<<<<<<#
     elif move == 'a':
         if y != 0:
             PlayerIG.coord[1] -= 1
         else:
              print('')
              print('Invalid option, Please select a valid option.')
              Move()
              
#>>>>>>>>> MOVE RIGHT <<<<<<<<<<#
     elif move == 'd':
         if y != 7:
             PlayerIG.coord[1] += 1
         else:
              print('')
              print('Invalid option, Please select a valid option.')
              Move()
              
#>>>>>>>>> INVALID OPTION <<<<<<<<<<#
     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Move()
     hero_location()
     x,y = PlayerIG.coord[0],PlayerIG.coord[1]
     world_map[x][y] = '{:s}'.format(hero)
     Map()
     day += 1
     locations()
     return PlayerIG.coord




#>>>>>>>>> LOCATIONS <<<<<<<<<<#
def locations():
     global location
     hero_location()
     if location == 'in a town':
          Town_Menu()
     elif location == 'out in the open':
          pre_fight()
     elif location == 'rat king':
          Rat_King()


#========================================================================================#
###################################-- RESTING --##########################################
#========================================================================================#

def rest():
     print('')
     global day
     PlayerIG.hp = PlayerIG.maxhp
     print('You are fully healed.')
     day += 1

#========================================================================================#
####################################-- STORE --###########################################
#========================================================================================#

#>>>>>>>>>> SHOP MENU <<<<<<<<<<#
def store_options():
     print('')
     print('Welcome to the shop')
     print('What would you like to buy?')
     print('1) Potions')
     print('2) Swords')
     print('3) Armours')
     print('4) Exit Store')

     option = input('Item number: ')

     if option == '1':
          potions()

     elif option == '2':
          Swords()

     elif option == '3':
          Armours()

     elif option == '4':
          Town_Menu()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          store_options()


#>>>>>>>>>> BUYING OF POTIONS <<<<<<<<<<#
def potions():
     print('')
     print('Would you like to buy a health potion?')
     print('1)Yes')
     print('2)No')

     option = input('Option number: ')

     if option == '1':
          option = 'potion'

          if option in potion:

               if PlayerIG.coin >= potion[option]:
                    PlayerIG.coin -= potion[option]
                    PlayerIG.potion += 1
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()

     elif option == '2':
          store_option()


     else:
          print('')
          print('Invalid option, Please select a valid option.')
          potions()

#>>>>>>>>>> BUYING OF SWORDS <<<<<<<<<<#
def Swords():
     print('')
     print('What sword would you like to buy?')
     print('1) Normal Sword')
     print('2) Big Sword')
     print('3) Even Bigger Sword')
     print('4) Return to store options')

     option = input('Option number: ')
     
     if option == '1':
          option = 'Normal Sword'

          if option in weapons:

               if PlayerIG.coin >= weapons[option]:
                    PlayerIG.coin -= weapons[option]
                    PlayerIG.weapon.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()

     elif option == '2':
          option = 'Big Sword'

          if option in weapons:

               if PlayerIG.coin >= weapons[option]:
                    PlayerIG.coin -= weapons[option]
                    PlayerIG.weapon.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()
          

     elif option == '3':
          option = 'Even Bigger Sword'

          if option in weapons:

               if PlayerIG.coin >= weapons[option]:
                    PlayerIG.coin -= weapons[option]
                    PlayerIG.weapon.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()
          

     elif option == '4':
          store_options()
          

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Swords()
          
               
#>>>>>>>>>> BUYING OF ARMOURS <<<<<<<<<<#
def Armours():
     print('')
     print('What armour would you like to buy?')
     print('1) Bronze Armour')
     print('2) Obsidion Armour')
     print('3) Meteor Armour')
     print('4) Return to store options')
     option = input('Option number: ')
     
     if option == '1':
          option = 'Bronze Armour'

          if option in armours:

               if PlayerIG.coin >= armours[option]:
                    PlayerIG.coin -= armours[option]
                    PlayerIG.armour.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()
          

     elif option == '2':
          option = 'Obsidion Armour'

          if option in armours:

               if PlayerIG.coin >= armours[option]:
                    PlayerIG.coin -= armours[option]
                    PlayerIG.armour.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()
          

     elif option == '3':
          option = 'Meteor Armour'

          if option in armours:

               if PlayerIG.coin >= armours[option]:
                    PlayerIG.coin -= armours[option]
                    PlayerIG.armour.append(option)
                    print('')
                    print('You have bought a %s' %option)
                    store_options()

               else:
                    print('')
                    print('You do not have enough coins')
                    store_options()

          else:
               store_options()
          

     elif option == '4':
          store_options()
          
     else:
          print('')
          print('Invalid option, Please select a valid option.')
          Armour()

#========================================================================================#
##################################-- INVENTORY --#########################################
#========================================================================================#

#>>>>>>>>>> INVENTORY MENU <<<<<<<<<<#
def inventory():
     print('')
     print('What would you like to do?')
     print('1) Look at current items')
     print('2) Equip Sword')
     print('3) Equip Armour')
     print('4) Exit inventory')

     option = input('Option number: ')

     if option == '1':
          look_inventory()

     elif option == '2':
          equip_sword()

     elif option == '3':
          equip_armour()

     elif option == '4':
          Town_Menu()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          inventory()

#>>>>>>>>>> EQUIPTING OF SWAORD <<<<<<<<<<#
def equip_sword():
     print('')
     print('What sword do you want to equip?')

     for weapons in PlayerIG.weapon:
          print(weapons)
          print('')

     option = input('Type in the Weapon name or "exit" to go back to inventory: ')

     if option == PlayerIG.in_hand:
          print('')
          print('You already have the %s equipped.' %option)
          inventory()

     elif option == 'exit':
          inventory()

     elif option in PlayerIG.weapon:
          PlayerIG.in_hand = option
          print('')
          print('You have equipped the %s.' %option)
          inventory()

     else:
          print('')
          print('You do not have the %s in your inventory' %option)
          equip_sword()
     



#>>>>>>>>>> EQUIPTING OF ARMOUR <<<<<<<<<<#
def equip_armour():
     print('')
     print('What armour do you want to equip?')

     for armours in PlayerIG.armour:
          print('')
          print(armours)

     option = input('Type in the Weapon name or "exit" to go back to inventory: ')

     if option == PlayerIG.armour_on:
          print('')
          print('You already have the %s equipped.' %option)
          inventory()

     elif option == 'exit':
          inventory()

     elif option in PlayerIG.armour:
          PlayerIG.armour_on = option
          print('')
          print('You have equipped the %s.' %option)
          inventory()

     else:
          print('')
          print('You do not have the %s in your inventory' %option)
          equip_armour()
     




#>>>>>>>>>> VIEWING INVENTORY <<<<<<<<<<#
def look_inventory():
     print('')
     print('You have these items in your inventory')

     for weapons in PlayerIG.weapon:
          print('')
          print(weapons)

     for armours in PlayerIG.armour:
          print('')
          print(armours)

     if orb == True:
          print('')
          print('Orb of Power')

     inventory()
     
#========================================================================================#
#################################-- SAVING GAME --########################################
#========================================================================================#

#saving in binary

def save():
          with open('savefile', 'wb') as f:

               pickle.dump(PlayerIG, f)

               pickle.dump(orb, f)

               pickle.dump(town_coord, f)

               pickle.dump(day, f)

               print('')
               print('Game has been saved')

#========================================================================================#
#################################-- LOADING GAME --#######################################
#========================================================================================#

def load():
     if os.path.exists('savefile') == True:
            with open('savefile', 'rb') as f:

                global PlayerIG
                PlayerIG = pickle.load(f)

                global orb
                orb = pickle.load(f)

                global town_coord
                town_coord = pickle.load(f)

                global day
                day = pickle.load(f)
                Town_Menu()
     else:
          print('')
          print('There are no save files')
          Title_Screen()

#========================================================================================#
##########################-- CHOOSING OF NORMAL ENEMY --##################################
#========================================================================================#

def pre_fight():
     global enemy

     enemy_choosing = random.randint(1,5)

     if enemy_choosing == 1:
          enemy = RatIG

     elif enemy_choosing == 2:
          enemy = ChipmunkIG

     elif enemy_choosing == 3:
          enemy = JerboaIG

     elif enemy_choosing == 4:
          enemy = BeaverIG

     else:
          enemy = GopherIG

     fight()

#========================================================================================#
################################-- NORMAL BATTLE --#######################################
#========================================================================================#

#>>>>>>>>>> FIGHT MENU OF NORMAL ENEMY <<<<<<<<<<#
def fight():
     print('')
     print('Encounter! - %s' %enemy.name)
     print('Damage: %i-%i' %(enemy.damage1, enemy.damage2))
     print('Defence: %i' %enemy.defence)
     print('Hp: %i' %enemy.hp)
     print('1) Attack')
     print('2) Potion')
     print('3) Run')

     option = input('Enter Choice: ')

     if option == '1':
          attack()

     elif option == '2':
          Potion()

     elif option == '3':
          run()

     else:
          print('')
          print('Invalid option, Please select a valid option.')
          fight()
          
          


#>>>>>>>>>> ATTACK OF NORMAL ENEMY <<<<<<<<<<#
def attack():
     global enemy
     Pattack = random. randint(PlayerIG.damage1, PlayerIG.damage2)
     Eattack = random. randint(enemy.damage1, enemy.damage2)
     Pdamage = Pattack - enemy.defence
     Edamage = Eattack - PlayerIG.defence
     enemy.hp -= Pdamage
     print('')
     print('You deal %i damage to the %s' %(Pdamage, enemy.name))

     if enemy.hp <= 0:
          print('')
          print('The %s is dead! You are victorious!' %enemy.name)
          print('')
          print('You looted the enemy and found %i coins' %enemy.coindrop)
          PlayerIG.coin += enemy.coindrop
          enemy.hp = enemy.maxhp
          Outdoor_Menu()

     if Edamage <= 0:
          print('The %s did not deal any damage!' %enemy.name)
          print('')
          print('You have %i HP left.' %PlayerIG.hp)
     else:
          PlayerIG.hp -= Edamage
          print('')
          print('Ouch! The %s hit you for %i damage!' %(enemy.name, Edamage))
          print('')
          print('You have %i HP left.' %PlayerIG.hp)

     if PlayerIG.hp <= 0:
          print('')
          print('You have failed to defeat the %s!' %enemy.name)
          print('')
          print('You are dead!')
          sys.exit()

     else:
         fight()



#>>>>>>>>>> RUN OF NORMAL ENEMY <<<<<<<<<<#
def run():
     global enemy
     run_chance = random.randint(1, 2)

     if run_chance == 1:
         print('')
         print('You ran and hide!')
         enemy.hp = enemy.maxhp
         print('')
         print('Day %i: You are out in the open.' %day)
         print('1) View Character')
         print('2) View Map')
         print('3) Move')
         print('4) Sense Orb')
         print('5) Exit Game')

         while True:

              option = input('Enter Choice: ')

              if option == '1':
                   Character_info()
                   attack()

              elif option == '2':
                   Map()
                   attack()

              elif option == '3':
                   Map()
                   Move()
                   break

              elif option == '4':

                   if x == positionx and y == positiony:
                        orb_found()
                        attack()

                   else:
                        orb_direction()
                        attack()

              elif option == '5':
                   print('')
                   print('You Exited Ratventure')
                   sys.exit()

              else:
                   print('')
                   print('Invalid option, Please select a valid option.')
                   fight()
     else:
         print('')
         print('You failed to run away!')
         Eattack = random. randint(enemy.damage1, enemy.damage2)
         Edamage = Eattack - PlayerIG.defence
         if Edamage <= 0:
               print('The %s did not deal any damage!' %enemy.name)
               print('')
               print('You have %i HP left.' %PlayerIG.hp)
         else:
               PlayerIG.hp -= Edamage
               print('')
               print('Ouch! The %s hit you for %i damage!' %(enemy.name, Edamage))
               print('')
               print('You have %i HP left.' %PlayerIG.hp)
         PlayerIG.hp -= Edamage
         print('')
         print('Ouch! The %s hit you for %i damage!' %(enemy.name, Edamage))
         print('')
         print('You have %i HP left.' %PlayerIG.hp)

         if PlayerIG.hp <= 0:
              print('')
              print('You have failed to defeat the %s!' %enemy.name)
              print('')
              print('You are dead!')
              sys.exit()

         else:
              fight()

#========================================================================================#
#################################-- KING BATTLE --########################################
#========================================================================================#

#>>>>>>>>>> FIGHT MENU OF RODENT KING <<<<<<<<<<#
def Rat_King():
     if PlayerIG.coord == Rat_King_coord:
          print('')
          print('Encounter! - %s' %Rat_KingIG.name)
          print('Damage: %i-%i' %(Rat_KingIG.damage1, Rat_KingIG.damage2))
          print('Defense: %i' %Rat_KingIG.defence)
          print('Hp: %i' %Rat_KingIG.hp)
          print('1) Attack')
          print('2) Potion')
          print('3) Run')

          option = input('Enter Choice: ')

          if option == '1':

               global orb
               if orb == True:
                    Fight()

               else:
                    Basically_dead()

          elif option == '2':
               King_potion()

          elif option == '3':
               Run()

          else:
               print('')
               print('Invalid option, Please select a valid option.')
               Rat_King()
     else:
          pass

#>>>>>>>>>> ATTACK OF RODENT KING <<<<<<<<<<#
def Fight():
      Pattack = random. randint(PlayerIG.damage1, PlayerIG.damage2)
      Eattack = random. randint(Rat_KingIG.damage1, Rat_KingIG.damage2)
      Pdamage = Pattack - Rat_KingIG.defence
      Edamage = Eattack - PlayerIG.defence
      Rat_KingIG.hp -= Pdamage
      print('')
      print('You deal %i damage to the Rat King' %Pdamage)

      if Rat_KingIG.hp <= 0:
           Rat_KingIG.hp = Rat_KingIG.maxhp
           print('')
           print('The Rat King is dead! You are victorious!')
           Title_Screen()          

      PlayerIG.hp -= Edamage
      print('')
      print('Ouch! The Rat King hit you for %i damage!' %Edamage)
      print('')
      print('You have %i HP left.' %PlayerIG.hp)

      if PlayerIG.hp <= 0:
           print('')
           print('You have failed to defeat the Rat King!')
           print('')
           print('You are dead!')
           sys.exit()

      else:
           Rat_King()

           
#>>>>>>>>>> ATTACK OF RODENT KING WITHOUT ORB <<<<<<<<<<#    
def Basically_dead():
      print('')
      print('You do not have the Orb of Power - the Rat King is immune!')
      print('')
      print('You deal 0 damage to the Rat King')

      Eattack = random. randint(Rat_KingIG.damage1, Rat_KingIG.damage2)
      Edamage = Eattack - PlayerIG.defence
      PlayerIG.hp -= Edamage

      print('')
      print('Ouch! The Rat King hit you for %i damage!' %Edamage)
      print('')
      print('You have %i HP left.' %PlayerIG.hp)

      if PlayerIG.hp <= 0:
           print('')
           print('You have failed to defeat the Rat King!')
           print('')
           print('You are dead!')
           sys.exit()

      else:
           Rat_King()

#>>>>>>>>>> RUN OF RODENT KING <<<<<<<<<<#
def Run():
     run_chance = random.randint(1, 2)
     if run_chance == 1:
          print('')
          print('You ran and hide!')
          Rat_KingIG.hp = Rat_KingIG.maxhp
     
          print('')
          print('Day %i: You are out in the open.' %day)
          print('1) View Character')
          print('2) View Map')
          print('3) Move')
          print('4) Sense Orb')
          print('5) Exit Game')

          option = input('Enter Choice: ')

          if option == '1': 
               Character_info()
               Fight()

          elif option == '2':
               Map()
               Fight()

          elif option == '3':
               Map()
               Move()

          elif option == '4':          

               if x == positionx and y == positiony:
                    orb_found()
                    Fight()

               else:
                    orb_direction()
                    Fight()

          elif option == '5':
               print('')
               print('You Exited Ratventure')
               sys.exit()

          else:
               print('')
               print('Invalid option, Please select a valid option.')
               Run()

     else:
          print('')
          print('You failed to run away!')
          Eattack = random. randint(enemy.damage1, enemy.damage2)
          Edamage = Eattack - PlayerIG.defence
          PlayerIG.hp -= Edamage
          print('')
          print('Ouch! The %s hit you for %i damage!' %(enemy.name, Edamage))
          print('')
          print('You have %i HP left.' %PlayerIG.hp)

          if PlayerIG.hp <= 0:
               print('')
               print('You have failed to defeat the %s!' %enemy.name)
               print('')
               print('You are dead!')
               sys.exit()

          else:
               fight()


#========================================================================================#
#################################-- ORB OF POWER --#######################################
#========================================================================================#

#>>>>>>>>>> ORB OF POWER PLACEMENT <<<<<<<<<<#
def orb_location():
     global positionx
     positionx = random.randint(4,7)

     global positiony
     positiony = random.randint(4,7)



#>>>>>>>>>> ORB OF POWER DIRECTION <<<<<<<<<<#
def orb_direction():
     global orb
     global orb, day, positonx, positiony
     day += 1

     if orb == True:
          print('')
          print('You have already found the Orb of Power')
     else:
          if x < positionx and y == positiony:
               print('')
               print('You sense that the Orb of Power is to the SOUTH')

          elif x > positionx and y == positiony:
               print('')
               print('You sense that the Orb of Power is to the NORTH')

          elif x == positionx and y < positiony:
               print('')
               print('You send that the Orb of Power is to the EAST')

          elif x == positionx and y > positiony:
               print('')
               print('You send that the Orb of Power is to the WEST')

          elif x < positionx and y < positiony:
               print('')
               print('You sense that the Orb of Power is to the SOUTH-EAST')

          elif x < positionx and y > positiony:
               print('')
               print('You sense that the Orb of Power is to the SOUTH-WEST')

          elif x > positionx and y < positiony:
               print('')
               print('You sense that the Orb of Power is to the NORTH-EAST')

          elif x > positionx and y > positiony:
               print('')
               print('You sense that the Orb of Power is to the NORTH-EAST')

          else:
               Outdoor_Menu()

#>>>>>>>>>> FINDING THE ORB OF POWER <<<<<<<<<<#
def orb_found():
     global orb
     orb = True

     print('')
     print('You found the Orb of Power!')

     PlayerIG.base_damage1 = PlayerIG.base_damage1 + 5
     PlayerIG.base_damage2 = PlayerIG.base_damage2 + 5
     print('')
     print('Your attack increases by 5!')

     PlayerIG.base_defence = PlayerIG.base_defence + 5
     print('')
     print('Your defence increases by 5!')

#========================================================================================#
#################################-- HEALTH POTION --######################################
#========================================================================================#


def Potion():
    if PlayerIG.potion == 0:
        print('')
        print('you do not have any potions')
        attack()

    else:
        PlayerIG.hp += 10
        PlayerIG.potion -= 1

        if PlayerIG.hp > PlayerIG.maxhp:
             PlayerIG.hp = PlayerIG.maxhp
             print('')
             print('You drank a potion')
             print('')
             print('You gained 10 Hp')
             fight()



def King_potion():
     if PlayerIG.potion == 0:
          print('')
          print('You do not have any potions')
          Fight()
     else:
          PlayerIG.hp += 10
          PlayerIG.potion -= 1

          if PlayerIG.hp > PlayerIG.maxhp:
               PlayerIG.hp = PlayerIG.maxhp
               print('')
               print('You drank a potion')
               print('')
               print('You gained 10 Hp')
               Rat_King()







Title_Screen()






















