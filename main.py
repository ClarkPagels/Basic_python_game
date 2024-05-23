import json
import Character
import random

colorFile = open('colors.json', 'r')
color = json.load(colorFile)
colorFile.close()

costFile = open('cost.json', 'r')
cost = json.load(costFile)
colorFile.close()

nameFile = open('fist-names.json')
name = json.load(nameFile)
nameFile.close()

placeFile = open('places.json')
place = json.load(placeFile)
placeFile.close()



print("welcome to my game, time for an adventure")

class Character1(object):
    name        = ''
    strength    = 0
    health      = 0
    wisdom      = 0
    dexterity   = 0
    points      = 20
    _attributes = ['name', 'strength', 'health', 'wisdom', 'dexterity', 'points']
    money = 10000
    def __init__(self, name):
        assert self.valid_name(name)
        self.name = name
    def add_points(self):
        accepted = ['strength', 'health', 'wisdom', 'dexterity']
        accepted_dict = dict(enumerate(accepted, start=1))
        prompt = "\nWhich attribute?\n\t" + "\n\t".join("%d. %s"%n for n in accepted_dict.items())+"\n?"
        attribute = False
        while attribute not in accepted:
            attribute = raw_input(prompt)
            try:
                attribute = accepted_dict[int(attribute)]
            except:
                print "Input was invalid. Please enter either an attribute or its corresponding number"
        amount = None
        while type(amount) != int or amount > self.points:
            try:
                amount = int(raw_input("By how much?"))
                assert amount <= self.points
            except AssertionError:
                print "You do not have that many points remaining"
            except:
                print "You must enter an integer amount"
        self.__setattr__(attribute, self.__getattribute__(attribute) + amount)
        self.points -= amount
    def __str__(self):
        return "\n".join("%s\t:\t%s"%(n, self.__getattribute__(n)) for n in self._attributes)
    @staticmethod
    def valid_name(name):
        if bool(name) and type(name) == str:
            return True
        else:
            return False
    def class()
class basic_character():
    def
if __name__ == "__main__":
    running = True
    print "Create a character! You have points to assign to strength, health, wisdom, and dexterity."
    name = ''
    while not Character.valid_name(name):
        name = raw_input("Please enter your character's name:")
    CHAR = Character(name)
    OPTIONS_LIST = ["Add points", "Remove points", "See current attributes", "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while running:
        CHOICE = raw_input(PROMPT)
        try:
            CHOICE = int(CHOICE)
        except:
            pass
        if CHOICE in OPTIONS_DICT.keys():
            CHOICE = OPTIONS_DICT[CHOICE]
        if CHOICE == "Add points":
            CHAR.add_points()
        elif CHOICE == "Remove points":
            raise NotImplementedError()
        elif CHOICE == "See current attributes":
            print CHAR
        elif CHOICE == "Exit":
            running = False
# the initial construction of character
gender = str(input("what is your gender"))
race = str(input("what is your race?" +" German, Egyptian, Greek," +"
"celtic, Persian, Semite,"+"black, or asian are teh acceptable races"))
eye_color = str(input("what is your hair color?"))
hair_color = str(input("what is your hair color"))
# all the stages of a fightt
class fight(object):
    #INITIVATIVE section of code


    def initiative(enemy):
        character_role = randrange(20) + character.dex() - 10
        enemy_role = randrange(20) + Character.enemy.stat_creation(dex) -10
        print("your role initiative is " + character_role + " and your foe's row is " + enemy_role)
        while character.health() or if enemy
        if character_role > enemy_role:
            print("you go first")
            n = 0
        elif character_role == enemy_role:
            if character.dex() > Character.random_character.stat_creation(dex):
                n = 0
                print("it's your turn")
            if character.dex() == Character.random_character.stat_creation(dex):
                print("it's your turn")
            else:
                n = 1
                print("its the enemy's turn")
        else:
            n = 1
            print("it's the enemy's turn")
    while enemy.health or character.health > 0:
    #CHance of getting hit by the enemy and enemy's chance of hitting player
        def hit(enemy, player):
            player = Character1.dex()
            player_success = (randrange(20) + player) - (randrange(20) + enemy )
            n = True
            if player_success > 0:
                n = True
                print("you succeed")
            else:
                n = False
                print("you fail")
        def damage():
            if
    else:
        if enemy.health == 0:
            print(enemy + "lies slain on the field of battle.")
        else:
            print("game over")



print(gender)
print(race)
print(eye_color)
print(hair_color)
print(eye_color)

print("hello good hero now is the time for adventure")
print( "you must now go on your quest to serve the emporer.")
print("or you may serve others")
print("we will see")
def main():
    
