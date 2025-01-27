#main program file

import chargen
import utility

if __name__ == "__main__":
    level = utility.dice(1, 6) - 3
    if level <= 0:
        level = 0
    character = chargen.Character(level)
    print(f"Level {character.level} {character.sex} {character.race} {character.charclass}. {character.hp} HP. STR {character.strength}, DEX {character.dexterity}, CON {character.constitution}, INT {character.intellect}, WIL {character.will}, CHA {character.charisma}")
