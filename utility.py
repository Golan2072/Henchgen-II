#general utility code

import random
import os
import platform


def yn():
    query = True
    while query:
        answer = input("Y/N: ")
        if answer.lower() == "y" or "yes":
            return True
            break
        if answer.lower() == "n" or "no":
            return False
            break
        else:
            print("Invalid Answer")


def dice(n, sides):
    die = 0
    roll = 0
    while die < n:
        roll = roll + random.randint(1, sides)
        die += 1
    return roll


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def random_line(filename):
    with open(filename, "r") as line_list:
        line = random.choice(line_list.readlines())
        line = line.strip()
    return line
