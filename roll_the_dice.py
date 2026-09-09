import random
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_dice(filepath=None):
    if filepath is None:
        filepath = resource_path("dice.txt")

    with open(filepath, "r") as f:
        lines = f.readlines()

    dice = {"[DIE1]": [], "[DIE2]": [], "[DIE3]": []}
    current = None

    for line in lines:
        line = line.strip()
        if line in dice:
            current = line
        elif line and current:
            dice[current].append(line)

    return dice

def roll(dice, die_key):
    return random.choice(dice[die_key])

def roll_all(dice):
    d1 = roll(dice, "[DIE1]")
    d2 = roll(dice, "[DIE2]")
    d3 = roll(dice, "[DIE3]")
    return d1, d2, d3

