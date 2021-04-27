# Game #1
# A simple Python3 game

from tkinter import *

#Adding a window for the game
tk = Tk()
tk.title("Game#1")
tk.resizable(0, 0)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
canvas.pack()
