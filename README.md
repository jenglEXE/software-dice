# Software Dice

A software-flavored take on Simone Giertz's build-brief dice. Instead of material/object/property for physical builds, these three dice roll an interface paradigm, a category of program, and a friendly creative modifier — giving you a random software project brief to build.

Rolls three animated ASCII dice side by side in a retro-styled terminal window, then reveals your build brief.

## How it works

- **Die 1 — Interface/Runtime paradigm**: CLI tool, web app, desktop GUI, bot, browser extension, API/backend, etc.
- **Die 2 — Object/Category**: data tool, game, automation, generator, tracker, simulator, etc.
- **Die 3 — Modifier**: a friendly, non-restrictive flavor/constraint to make the build a bit more interesting.

Press **Space** to roll (or reroll). Press **Esc** to exit.

## Requirements

- Python 3.x
- [PySide6](https://pypi.org/project/PySide6/)

Install with:

```
pip install PySide6
```

## Running it

```
python main.py
```

## Project structure

- `main.py` — entry point; launches the GUI
- `gui.py` — the PySide6 window, keyboard handling, and animation sequencing
- `roll_the_dice.py` — loads `dice.txt` and rolls each die
- `animation.py` — builds the ASCII dice face art
- `dice.txt` — the three banks of roll options (`[DIE1]`, `[DIE2]`, `[DIE3]`)