import Json
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

#lists that are more convinent for python than JSON

races = ["elf", "dwarf", "human",
 "fae", "beast_creature"]
ethnciity = ["German", "Egyptian", "Greek",
"celtic", "Persian", "Semite", "black", "asian"]
gender = ["male", "female", "neutral", "unknown"]
places = ["Egypt", "Germany", "Gaul", "Iberia", "britan", "subsaharan africa",
"North Africa", "India", "east asia", "an unknown land"
]

# qualitative values of a character

class character_description:
    def _init_ (self, first_name, last_name, hair_color, eye_color, height, weight,
     gender, from1, race, ethnicity, health):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.gender = gender
        self.from1 = from1
        self.race = race
        self.ethnicity = ethnicity
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
# quantitative values of a character
class character_stats:
    def _init_ (self,str,dex,int,wis,fort):
        self.str = str
        self.dex = dex
        self.int = _int
        self.wis = wis
        self.fort = fort


# creates random character
class random_character(character_description, character_stats):
    def _init_ (self, first_name, last_name, hair_color, eye_color, height,money, inventory,
     weight, gender, from1, race, ethnicity,first_name, last_name, hair_color,
      eye_color, height, weight, gender, from1, race, ethnicity):
        self.money = money
        self.inventory = inventory
        self.weapons = weapons
        self.armour = armour
        random_character.__init__(self, first_name, last_name, hair_color,
        eye_color, height, weight, gender, from1, race, ethnicity,first_name, last_name,
         hair_color, eye_color, height, weight, gender, from1, race, ethnicity, health)
    def description():
        self.first_name = ""
        self.last_name = ""
        self.hair_color =  color["standard_colors"][randrange(0,10)]
        self.eye_color =  color['basic_colors'][randrange(0,6)]
        self.height = str(random.randrange(130, 250) + "cm")
        self.weight = str(random.randrange(40, 100) + "kg")
        self.from1 = places[random.randrange(0,10)]
        self.race = races[random.randrange(0,5)]
        self.ethnicity = ethnciity[random.randrange(0,6)]
    def stat_creation(self, str, dex, int, wis, fort):
        self.str = randrange(0,21)
        self.dex = randrange(0,21)
        self.int = randrange(0,21)
        self.wis = randrange(0,21)
        self.fort = randrange(0,21)
        self.health = randrange(33)
    def inventory(self, inventory, armour, weapons):
        self.weapons = cost.weapons.weapon[randrange(len(cost.weapons.weapon)]
        self.armour = cost.defense.helmet[randrange(len(cost.defense.helment))],
        cost.defense.breat_plate[randrange(len(cost.defense.breast_plate))],
        cost.defense.leggings[randrange(len(cost.defense.leggings))],
        cost.defense.boots[randrange(len(cost.defense.boots))],
        cost.defense.sheild[randrange(len(cost.defense.sheild))]

#use for main characters

class main_character(character_description, character_stats):
    def _init_ (self,self, first_name, last_name, hair_color, eye_color, height, weight,
    gender, from1, race, ethnicity,first_name, last_name, hair_color, eye_color, height, weight,
     gender, from1, race, ethnicity ,money, inventory):
        main_character._init_(self, first_name, last_name, hair_color, eye_color, height, weight, gender, from1, race, ethnicity,first_name, last_name, hair_color, eye_color, height, weight, gender, from1, race, ethnicity)
        self.money = money
        self.inventory = inventory

    def storage():
        self.inventory =  [3]
        self.money = [range(7000)]
