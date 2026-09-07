"""Roll the dice for a build brief you unimaginative fuckwad"""
import random
from pynput import keyboard

#Remove when done:
    #Die Legend:
    # DIE1 = Interface/Runtime paradigm
    # DIE2 = Object/Category
    # DIE3 = Property (friendly/creative flavor, non-restrictive)


def roll(dice, die_key):
    return random.choice(dice[die_key])

def roll_all(dice):
    d1 = roll(dice, "[DIE1]")
    d2 = roll(dice, "[DIE2]")
    d3 = roll(dice, "[DIE3]")
    return d1, d2, d3

def on_press(key):
    if key == keyboard.Key.space:
        die1_choice, die2_choice, die3_choice = roll_all(dice)

        print(f"""
 Rolls:
--------------- 
 Interface/Runtime paradigm: {die1_choice}
---------------
 Object/Category: {die2_choice}
---------------
 Modifier (friendly/creative flavor): {die3_choice}""")
        print("Press space to roll again.")
        print("Press esc to exit. ")

    elif key == keyboard.Key.esc:  
        return False

if __name__ == "__main__":
    with open("dice.txt", "r") as f:
        lines = f.readlines()

    dice = {"[DIE1]": [], "[DIE2]": [], "[DIE3]": []}
    current = None

    for line in lines:
        line = line.strip()
        if line in dice:
            current = line
        elif line and current:
            dice[current].append(line)



    print("Press space to roll.")
    
    with keyboard.Listener(on_press=on_press) as listener:  
        listener.join()

