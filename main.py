from pynput import keyboard
from roll_the_dice import load_dice, roll_all
from animation import animate_roll

def on_press(key):
    if key == keyboard.Key.space:
        animate_roll()
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
        print("Press esc to exit.")
    elif key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    dice = load_dice("dice.txt")
    print("Press space to roll.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join() 