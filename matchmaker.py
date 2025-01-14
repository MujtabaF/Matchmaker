#LIBRARIES
import random
import time
from tkinter import Tk, Button, DISABLED

#SYMBOLS
def show_symbol(x, y):
    global first
    global previousX, previousY
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()


    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x ,y]['command'] = DISABLED
        first = True

#GUI
root = Tk()
root.title('Match these weirdos')
root.resizable(width=False, height=False)

#DICTIONARIES AND VARIABLES
buttons = {}
first = True
previousX = 0
PreviousY = 0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',\
           u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',\
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',\
           u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2718', u'\u2718']

random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), \
                        width=6, height=3)
        button.grid(column = x, row = y, padx = 15, pady = 15)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

root.mainloop()
        
                    
           

