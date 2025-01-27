# character generation code

import utility
import random


class Character:
    def __init__(self, level):
        self.level = level
        self.hp = 1
        self.weapon = "Default"
        self.armor = "Default"
        self.ac = 0
        self. damage = 0
        self.class_type = "Martial"
        self.sex = random.choice(["Male", "Female"])
        self.generate_abilities()
        self.class_type_chooser()
        self.race_chooser()
        self.class_chooser()
        self.hp_gen()

    def generate_abilities(self):
        self.strength = utility.dice(3, 6)
        self.dexterity = utility.dice(3, 6)
        self.constitution = utility.dice(3, 6)
        self.intellect = utility.dice(3, 6)
        self.will = utility.dice(3, 6)
        self.charisma = utility.dice(3, 6)
        modifier_dict = {3: -3, 4: -2, 5: -2, 6: -1, 7: -1, 8: -1, 9: 0,
                         10: 0, 11: 0, 12: 0, 13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3}
        self.strength_modifier = modifier_dict[self.strength]
        self.dexterity_modifier = modifier_dict[self.dexterity]
        self.constitution_modifier = modifier_dict[self.constitution]
        self.intellect_modifier = modifier_dict[self.intellect]
        self.will_modifier = modifier_dict[self.will]
        self.charisma_modifier = modifier_dict[self.charisma]

    def class_type_chooser(self):
        self.ability_dict = {"strength": self.strength, "dexterity": self.dexterity,
                             "constitution": self.constitution, "intellect": self.intellect, "will": self.will, "charisma": self.charisma}
        if max(self.ability_dict, key=self.ability_dict.get) == "strength":
            self.class_type = "Martial"
        elif max(self.ability_dict, key=self.ability_dict.get) == "constitution":
            self.class_type = "Explorer"
        elif max(self.ability_dict, key=self.ability_dict.get) == "dexterity":
            self.class_type = "Criminal"
        elif max(self.ability_dict, key=self.ability_dict.get) == "intellect":
            self.class_type = "Arcane"
        elif max(self.ability_dict, key=self.ability_dict.get) == "will":
            self.class_type == "Divine"
        elif max(self.ability_dict, key=self.ability_dict.get) == "charisma":
            self.class_type = "Social"
        else:
            self.class_type = random.choice(["Martial", "Criminal", "Social"])

    def race_chooser(self):
        tentative_race = random.choice(
            ["Human", "Human", "Elf", "Dwarf", "Nobiran", "Zaharan"])
        if tentative_race == "Dwarf" and self.constitution >= 9:
            self.race = "Dwarf"
        elif tentative_race == "Elf":
            self.race = "Elf"
        elif tentative_race == "Nobiran" and self.strength >= 11 and self.constitution >= 11 and self.dexterity >= 11 and self.intellect >= 11 and self.will >= 11 and self.charisma >= 11:
            self.race = "Nobiran"
        elif tentative_race == "Zaharan" and self.intellect >= 9 and self.will >= 9 and self.charisma >= 9:
            self.race = "Zaharan"
        else:
            self.race = "Human"

    def class_chooser(self):
        if self.level == 0:
            self.class_category = random.choice(["Laborer", "Artisan", "Artisan", "Merchant", "Merchant",
                                                "Specialist", "Hosteller", "Entertainer", "Mercenary", "Mercenary", "Ecclestiac", "Magician"])
            normal_man_dict = {"Laborer": ["Barber", "Bath Attendant", "Bricklayer", "Cook", "Dockworker", "Launderer", "Rower", "Gongfarmer", "Hawker", "Stablehand", "Servant", "Prostitute", "Ratcatcher", "Roofer", "Sailor", "Scullion", "Woodcutter", "Teamster", "Tavenworker", "Unskilled Laborer"], "Artisan": ["Clothmaker", "Cobbler", "Confectioner", "Cooper", "Coppersmith", "Ropemaker", "Decorative Artist", "Florist", "Gemcutter", "Glassworker", "Goldsmith", "Hornworker", "Illuminator", "Jeweler", "Locksmith", "Mason", "Parchmentmaker", "Perfumer", "Potter", "Saddler", "Scribe", "Shipwright", "Silversmith", "Spinner", "Tailor", "Tanner", "Taxidermist", "Tinker", "Wainwright", "Weaponsmith", "Wheelwright"], "Merchant": ["Bookseller", "Chandler", "Coppermonger", "Cornmonger", "Draper", "Fishmonger", "Fripperer", "Furrier", "Greengrocer", "Horsemonger", "Ironmonger", "Lawyer", "Lumbermonger", "Mercer", "Oilmonger", "Skinner",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "Poulterer", "Salter", "Vintner"], "Specialist": ["Alchemist", "Animal Trainer", "Artillerist", "Engineer", "Healer", "Marshal", "Navigator", "Quartermaster", "Sage", "Siege Engineer", "Ship Captain"], "Hosteller": ["Brothelkeeper", "Cantinakeeper", "Innkeeper", "Tavernkeeper"], "Entertainer": ["Actor", "Dancer", "Musician", "Singer", "Carouser"], "Mercenary": ["Light Infantry", "Heavy Infantry", "Slinger", "Bowman", "Crossbowman", "Composite Bowman", "Longbowman", "Light Cavalry", "Mounted Crossbowman", "Horse Archer", "Medium Cavalry", "Heavy Cavalry", "Cataphract Cavalry", "Camel Archer", "Camel Lancer"], "Ecclestiac": ["Missionary", "Anchorite", "Heretic", "Medician", "Inquisitor", "Oracle", "Sacred Courtesan", "Seminarian", "Village Witch"], "Magician": ["Apprentice Mage", "Apprentice Warlock", "Astrologer", "Augur", "Charlatan", "Failed Apprentice", "Hedge Magician", "Occultist", "Prestidigitator"]}
            self.charclass = random.choice(
                normal_man_dict[self.class_category])
        elif self.level > 0:
            if self.race == "Nobiran":
                self.charclass = "Wonderworker"
            elif self.race == "Zaharan":
                self.charclass = "Ruinguard"
            elif self.class_type == "Martial":
                if self.race == "Human":
                    self.charclass = random.choice(
                        ["Fighter", "Barbarian", "Paladin"])
                elif self.race == "Dwarf":
                    self.charclass = "Vaultguard"
                elif self.race == "Elf":
                    self.charclass = "Spellsword"
            elif self.class_type == "Explorer" and self.race == "Human":
                self.charclass = "Explorer"
            elif self.class_type == "Criminal":
                if self.race == "Human":
                    self.charclass = random.choice(["Thief", "Assassin"])
                elif self.race == "Dwarf":
                    self.charclass = "Vaultguard"
                elif self.race == "Elf":
                    self.charclass == "Nightblade"
            elif self.class_type == "Arcane":
                if self.race == "Human":
                    self.charclass = random.choice(["Mage", "Warlock"])
                elif self.race == "Dwarf":
                    self.charclass = "Vaultguard"
                elif self.race == "Elf":
                    self.charclass = random.choice(
                        ["Spellsword", "Nightblade"])
            elif self.class_type == "Divine":
                if self.race == "Human":
                    if self.sex == "Male":
                        self.charclass = random.choice(["Crusader", "Shaman"])
                    elif self.sex == "Female":
                        self.charclass = random.choice(
                            "Crusader", "Bladedancer", "Priestess", "Witch")
                elif self.race == "Dwarf":
                    self.charclass = "Craftpriest"
            elif self.class_type == "Social":
                self.charclass = random.choice(["Venturer", "Bard"])
            else:
                if self.race == "Human":
                    self.charclass = random.choice(["Fighter", "Thief"])
                elif self.race == "Dwarf":
                    self.charclass = random.choice(
                        ["Vaultguard", "Craftpriest"])
                elif self.race == "Elf":
                    self.charclass = random.choice(
                        ["Spellsword", "Nightblade"])

    def hp_gen(self):
        class_hd_dict = {"Fighter": 8, "Explorer": 6, "Thief": 4, "Mage": 4, "Crusader": 6, "Venturer": 6, "Assassin": 6, "Barbarian": 8, "Bard": 4, "Bladedancer": 6, "Paladin": 8,
                         "Priestess": 4, "Shaman": 6, "Warlock": 4, "Witch": 4, "Craftpriest": 4, "Vaultguard": 8, "Nightblade": 6, "Spellsword": 6, "Wonderworker": 4, "Ruinguard": 6}
        if self.level == 0:
            self.hp = utility.dice(1, 6) + self.constitution_modifier
            if self.hp < 1:
                self.hp = 1
        elif self.level >= 1:
            self.hp = utility.dice(self.level, class_hd_dict[self.charclass]) + self.constitution_modifier * self.level