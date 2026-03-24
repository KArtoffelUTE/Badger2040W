import badger2040
import random

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT
SCALE = 3

g_board = [ " ", " ", " ", " ",
            " ", " ", " ", " ",
            " ", " ", " ", " ",
            " ", " ", " ", " ",]

def start():
    display.set_update_speed(badger2040.UPDATE_NORMAL)
    display.set_pen(0)
    display.clear()
    display.update()
    
    display.set_update_speed(badger2040.UPDATE_FAST)
    
    draw_board()
    display.update()
    
def draw_board():
    WIDTH = badger2040.WIDTH # Speed 
    HEIGHT = badger2040.HEIGHT
    display.set_pen(15)
    display.rectangle(0, 0, WIDTH, HEIGHT)
    
    display.set_pen(0)
    display.line(0, 0, 0, HEIGHT) # Vertical lines
    display.line(74, 0, 74, HEIGHT)
    display.line(148, 0, 148, HEIGHT)
    display.line(222, 0, 222, HEIGHT)
    display.line(295, 0, 295, HEIGHT)
    
    display.line(0, 0, WIDTH, 0) # Horizontal Lines
    display.line(0, 32, WIDTH, 32)
    display.line(0, 64, WIDTH, 64)
    display.line(0, 96, WIDTH, 96)
    display.line(0, 127, WIDTH, 127)

def numbers():
    board = g_board
    display.set_pen(0)
    for i, number in enumerate(board):
        print(number)
        lenght = len(number)
        width = display.measure_text(number, scale=3)
        box_width = 74
        x1 = box_width - width
        x = int(x1 / 2)
        if i == 0:
            display.text(number, x, 5, scale=3)
        elif i == 1:
            display.text(number, x+74, 5, scale=3)
        elif i == 2:
            display.text(number, x+74*2, 5, scale=3)
        elif i == 3:
            display.text(number, x+74*3+2, 5, scale=3)
            
        elif i == 4:
            display.text(number, x, 37, scale=3)
        elif i == 5:
            display.text(number, x+74, 37, scale=3)
        elif i == 6:
            display.text(number, x+74*2, 37, scale=3)
        elif i == 7:
            display.text(number, x+74*3+2, 37, scale=3)
            
        elif i == 8:
            display.text(number, x, 69, scale=3)
        elif i == 9:
            display.text(number, x+74, 69, scale=3)
        elif i == 10:
            display.text(number, x+74*2, 69, scale=3)
        elif i == 11:
            display.text(number, x+74*3+2, 69, scale=3)
            
        elif i == 12:
            display.text(number, x, 101, scale=3)
        elif i == 13:
            display.text(number, x+74, 101, scale=3)
        elif i == 14:
            display.text(number, x+74*2, 101, scale=3)
        elif i == 15:
            display.text(number, x+74*3+2, 101, scale=3)

def pick_two_distinct(values):
    first = random.choice(values)
    second = random.choice(values)
    while second == first:
        second = random.choice(values)
    return first, second

def fill_board_start():
    global g_board
    nothing = []
    for i, number in enumerate(g_board):
        if number == " ":
            nothing.append(i)
    
    a, b = pick_two_distinct(nothing)
    
    g_board[a] = random.choice(["2", "4"])
    g_board[b] = random.choice(["2", "4"])

def move_up():
    global g_board

    for col in range(4):
    # Indizes der Spalte
        idx = [col, col+4, col+8, col+12]
        # Werte der Spalte holen
        col_vals = [g_board[i] for i in idx]
        # 1. Leere entfernen
        filtered = [v for v in col_vals if v != " "]
        # 2. Mergen
        merged = []
        skip = False
        for i in range(len(filtered)):
            if skip:
                skip = False
                continue

            if i+1 < len(filtered) and filtered[i] == filtered[i+1]:
                merged.append(str(int(filtered[i]) * 2))
                skip = True
            else:
                merged.append(filtered[i])

        # 3. Wieder auffüllen
        while len(merged) < 4:
            merged.append(" ")

        # 4. Zurückschreiben
        for i, val in zip(idx, merged):
            g_board[i] = val
        
def move_down():
    global g_board
    
    for col in range(4):
        idx = [col, col+4, col+8, col+12]
        col_vals = [g_board[i] for i in idx]
        
        filtered = [v for v in col_vals if v != " "]
        
        merged = []
        skip = False
        for i in range(len(filtered)):
            if skip:
                skip = False
                continue
            
            if i+1 < len(filtered) and filtered[i] == filtered[i+1]:
                merged.append(str(int(filtered[i]) * 2))
                skip = True
            else:
                merged.append(filtered[i])
        
        while len(merged) < 4:
            merged.insert(0, " ")
        
        for i, val in zip(idx, merged):
            g_board[i] = val
        

print("HI")

start()
fill_board_start()
numbers()
display.update()
while True:
    display.keepalive()
    
    if display.pressed(badger2040.BUTTON_UP):
        move_up()
        display.set_pen(15)
        display.clear()
        draw_board()
        numbers()
        display.update()
    elif display.pressed(badger2040.BUTTON_DOWN):
        move_down()
        display.set_pen(15)
        display.clear()
        draw_board()
        numbers()
        display.update()
    
    display.halt()