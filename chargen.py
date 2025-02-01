# character generation code

import utility
import random
import json
import equipment


class Template:
    def __init__(self, equipment_dict):
        self.name = "Default"
        self.equipment_dict = equipment_dict
        self.armor = self.equipment_dict["Tunic"]
        self.weapon = self.equipment_dict["Staff"]
        self.proficiencies = {}
        self.equipment = {}


class Character:
    def __init__(self, level):
        self.load_equipment()
        self.level = level
        self.shield = False
        self.hp = 1
        self.weapon = self.equipment_dict["Staff"]
        self.armor = self.equipment_dict["Tunic"]
        self.ac = 0
        self. damage = "1d6"
        self.class_type = "Martial"
        self.sex = random.choice(["Male", "Female"])
        self.generate_abilities()
        self.class_type_chooser()
        self.race_chooser()
        self.class_chooser()
        self.hp_gen()
        self.name_gen()
        self.load_templates()
        self.proficiency_string = ", ".join (self.proficiencies)
        self.equipment_string = ", ".join (self.equipment)

    def load_equipment(self):
        with open("data/equipment.json", "r") as equipment_file:
            self.equipment_source_dict = json.load(equipment_file)
        self.equipment_dict = {}
        for item in self.equipment_source_dict:
            self.equipment_dict[self.equipment_source_dict[item]
                                ["name"]] = equipment.Item()
            self.equipment_dict[self.equipment_source_dict[item]
                                ["name"]].name = self.equipment_source_dict[item]["name"]
            self.equipment_dict[self.equipment_source_dict[item]["name"]].damage = self.equipment_source_dict[item]["damage"]
            self.equipment_dict[self.equipment_source_dict[item]
                                ["name"]].type = self.equipment_source_dict[item]["type"]
            self.equipment_dict[self.equipment_source_dict[item]
                                ["name"]].ac = self.equipment_source_dict[item]["ac"]
            self.equipment_dict[self.equipment_source_dict[item]["name"]
                                ].encumbrance = self.equipment_source_dict[item]["encumbrance"]
            if self.equipment_source_dict[item]["magical"] == "True":
                self.equipment_dict[self.equipment_source_dict[item]
                                    ["name"]].magical = True
            elif self.equipment_source_dict[item]["magical"] == "False":
                self.equipment_dict[self.equipment_source_dict[item]
                                    ["name"]].magical = False

    def load_templates(self):
            if self.level >= 1:
                with open("data/char_database.json", "r") as template_file:
                    self.template_source_dict = json.load(template_file)
                roll = utility.dice(3, 6)
                self.template = Template(self.equipment_dict)
                self.template.name = self.template_source_dict[self.charclass]["templates"][str(
                    roll)]["name"]
                if "armor" in self.template_source_dict[self.charclass]["templates"][str(roll)].keys():
                    self.armor = self.equipment_dict[self.template_source_dict[self.charclass]["templates"][str(
                        roll)]["armor"]]
                else:
                    pass
                self.ac = self.armor.ac
                if "weapon" in self.template_source_dict[self.charclass]["templates"][str(roll)]:
                    self.weapon = self.equipment_dict[self.template_source_dict[self.charclass]["templates"][str(
                        roll)]["weapon"]]
                else:
                    pass
                self.damage = self.weapon.damage
                if "shield" in self.template_source_dict[self.charclass]["templates"][str(roll)]:
                    if self.template_source_dict[self.charclass]["templates"][str(roll)]["shield"] == "True":
                        self.shield = True
                    else:
                        self.shield = False
                else:
                    self.shield = False
                self.ac = self.armor.ac
                if self.shield:
                    self.ac += 1
                self.proficiencies = self.template_source_dict[self.charclass]["templates"][str(
                    roll)]["proficiencies"]
                self.equipment = self.template_source_dict[self.charclass]["templates"][str(
                    roll)]["equipment"]
            else:
                with open("data/zero_level_database.json", "r") as template_file:
                    self.template_source_dict = json.load(template_file)
                self.template = Template(self.equipment_dict)
                self.template.name = random.choice(list(self.template_source_dict[self.charclass].keys()))
                if "armor" in self.template_source_dict[self.charclass][self.template.name]:
                    self.armor = self.equipment_dict[self.template_source_dict[self.charclass][self.template.name]["armor"]]
                else:
                    pass
                if "weapon" in self.template_source_dict[self.charclass][self.template.name]:
                    self.weapon = self.equipment_dict[self.template_source_dict[self.charclass][self.template.name]["weapon"]]
                else:
                    pass
                if "shield" in self.template_source_dict[self.charclass][self.template.name]:
                    if self.template_source_dict[self.charclass][self.template.name]["shield"] == "True":
                        self.shield = True
                    else:
                        self.shield = False
                else:
                    self.shield = False
                self.ac = self.armor.ac
                if self.shield:
                    self.ac += 1
                self.damage = self.weapon.damage
                self.proficiencies = {}
                self.equipment = ""
                self.charclass = self.template.name

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
            ["Human", "Human", "Human", "Human", "Human", "Human", "Elf", "Dwarf", "Nobiran", "Zaharan"])
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
            self.class_category = random.choice(["Laborer", "Artisan", "Merchant",
                                                "Specialist", "Hosteller", "Entertainer", "Mercenary", "Mercenary", "Mercenary", "Mercenary", "Mercenary", "Ecclestiac", "Magician"])
            self.charclass = self.class_category
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
                    self.charclass = "Nightblade"
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
            self.hp = utility.dice(
                self.level, class_hd_dict[self.charclass]) + self.constitution_modifier * self.level
            if self.hp < 1:
                self.hp = 1

    def name_gen(self):
        if self.race == "Human":
            if self.sex == "Male":
                self.name = utility.random_line("data/malenames.txt")
            elif self.sex == "Female":
                self.name = utility.random_line("data/femalenames.txt")
        elif self.race == "Dwarf":
            if self.sex == "Male":
                self.name = utility.random_line("data/dwarfmalenames.txt")
            elif self.sex == "Female":
                self.name = utility.random_line("data/dwarffemalenames.txt")
        elif self.race == "Elf":
            if self.sex == "Male":
                self.name = utility.random_line("data/elfmalenames.txt")
            elif self.sex == "Female":
                self.name = utility.random_line("data/elffemalenames.txt")
        elif self.race == "Zaharan":
            if self.sex == "Male":
                self.name = utility.random_line("data/zaharanmalenames.txt")
            elif self.sex == "Female":
                self.name = utility.random_line("data/zaharanfemalenames.txt")
        else:
            if self.sex == "Male":
                self.name = utility.random_line("data/malenames.txt")
            elif self.sex == "Female":
                self.name = utility.random_line("data/femalenames.txt")
