#main program file

import chargen
import utility

if __name__ == "__main__":
    level = utility.dice(1, 6) - 3
    if level <= 0:
        level = 0
    character = chargen.Character(level)
    if character.level >= 1:
        print(f"{character.name}, Level {character.level} {character.sex} {character.race} {character.charclass} ({character.template.name})\nSTR {character.strength}, DEX {character.dexterity}, CON {character.constitution}, INT {character.intellect}, WIL {character.will}, CHA {character.charisma}\n{character.hp} HP; {character.armor.name} (AC {character.ac})")
    else:
        print(f"{character.name}, Level {character.level} {character.sex} {character.race} {character.charclass}\nSTR {character.strength}, DEX {character.dexterity}, CON {character.constitution}, INT {character.intellect}, WIL {character.will}, CHA {character.charisma}\n{character.hp} HP; {character.armor.name} (AC {character.ac})")
