from tkinter import *
from Ant import Ant
from AntCell import AntCell
import random
import time

tk = Tk()
tk.title("Langton's Ant")

canvas = Canvas(tk, width=1500, height=700)
canvas.pack()

cells = []
universal_color = 'blue'

for x in range(0, 1400, 10):
    for y in range(0, 700, 10):
        cell = AntCell(canvas, x, y, 10)
        cells.append(cell)

seconds = 0
timer_heading = canvas.create_text(1430, 10, text='Timer (s):')
timer_txt = canvas.create_text(1420, 40, text=seconds)

ant = Ant()

chosen = random.choice(cells)
chosen.change_color(universal_color)

init_time = time.time()


def mainLoop(c):
    while True:
        tk.update()
        tk.update_idletasks()
        time.sleep(0.0001)

        if c.color == universal_color:
            ant.change_direction(-1)
        if c.color == '':
            ant.change_direction(1)

        if ant.direction == 0:
            c = cells[cells.index(c) - 1]
        if ant.direction == 1:
            c = cells[cells.index(c) + 70]
        if ant.direction == 2:
            c = cells[cells.index(c) + 1]
        if ant.direction == 3:
            c = cells[cells.index(c) - 70]
        # chosen = chosen.move(chosen, cells)
        # chosen = cells[cells.index(chosen) + 1]   will now equal move()

        if c.color == '':
            c.change_color(universal_color)
        else:
            c.change_color('')

        seconds = time.time() - init_time
        canvas.itemconfig(timer_txt, text=int(seconds))

        tk.update()
        tk.update_idletasks()
        time.sleep(0.01)
