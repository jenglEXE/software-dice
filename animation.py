import os
import time
import random

FILL = "@"
PIP_PATTERNS = {
    1: [(1, 1)],
    2: [(0, 0), (2, 2)],
    3: [(0, 0), (1, 1), (2, 2)],
    4: [(0, 0), (0, 2), (2, 0), (2, 2)],
    5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
}

def build_die(value, cell_w=7, cell_h=4):
    pips = set(PIP_PATTERNS[value])
    lines = []
    for row in range(3):
        for sub_row in range(cell_h):
            line = ""
            is_pip_center = (sub_row == cell_h // 2)
            for col in range(3):
                if (row, col) in pips and is_pip_center:
                    pip_gap = cell_w // 3
                    hole = cell_w - 2 * pip_gap
                    line += FILL * pip_gap + " " * hole + FILL * pip_gap
                else:
                    line += FILL * cell_w
            lines.append(line)
    width = len(lines[0])
    border = "┌" + "─" * width + "┐"
    bottom = "└" + "─" * width + "┘"
    return [border] + ["│" + line + "│" for line in lines] + [bottom]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_roll():
    delays = [0.05, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3]
    for delay in delays:
        clear_screen()
        for line in build_die(random.randint(1, 6)):
            print(line)
        time.sleep(delay)
    clear_screen()