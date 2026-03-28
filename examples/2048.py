import badger2040
import random
import time

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
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

def fill_board():
    global g_board
    nothing = []
    for i, number in enumerate(g_board):
        if number == " ":
            nothing.append(i)
    a = random.choice(nothing)
    print(a)
    g_board[a] = random.choice(["2", "4"])

def compress_and_merge(line):
    # Remove spaces
    nums = [x for x in line if x != " "]

    merged = []
    skip = False

    for i in range(len(nums)):
        if skip:
            skip = False
            continue

        if i+1 < len(nums) and nums[i] == nums[i+1]:
            merged.append(str(int(nums[i]) * 2))
            skip = True
        else:
            merged.append(nums[i])

    # Fill with spaces
    while len(merged) < 4:
        merged.append(" ")

    return merged


def move_up(change_board):
    for col in range(4):
    # Indizes der Spalte
        idx = [col, col+4, col+8, col+12]
        # Werte der Spalte holen
        line = [change_board[i] for i in idx]
        # 2. Mergen
        merged = compress_and_merge(line)

        # 4. Zurückschreiben
        for i, val in zip(idx, merged):
            change_board[i] = val
        
def move_down(change_board):
    for col in range(4):
        idx = [col, col+4, col+8, col+12]
        line = [change_board[i] for i in idx]
        
        merged = compress_and_merge(list(reversed(line)))
        merged.reverse()
        
        for i, val in zip(idx, merged):
            change_board[i] = val

def move_right(change_board):
    for row in range(4):
        idx = [row*4 + i for i in range(4)]
        line = [change_board[i] for i in idx]
        
        merged = compress_and_merge(list(reversed(line)))
        merged.reverse()
        
        for i, val in zip(idx, merged):
            change_board[i] = val
        
def move_left(change_board):
    for row in range(4):
        idx = [row*4 + i for i in range(4)]
        line = [change_board[i] for i in idx]
        
        merged = compress_and_merge(line)
        
        for i, val in zip(idx, merged):
            change_board[i] = val

def board_changed(old, new):
    return old != new

def no_moves():
    global g_board
    test_board = g_board.copy()
    move_up(test_board)
    move_down(test_board)
    move_right(test_board)
    move_left(test_board)
    if board_changed(g_board, test_board):
        return False
    else:
        return True
    

    
    
print("HI")

start()
fill_board_start()
numbers()
display.update()
while True:
    display.keepalive()
    
    if display.pressed(badger2040.BUTTON_UP):
        old = g_board.copy()
        move_up(g_board)
        if board_changed(old, g_board):
            fill_board()
            display.set_pen(15)
            display.clear()
            draw_board()
            numbers()
            display.update()
    elif display.pressed(badger2040.BUTTON_DOWN):
        old = old = g_board.copy()
        move_down(g_board)
        if board_changed(old, g_board):
            fill_board()
            display.set_pen(15)
            display.clear()
            draw_board()
            numbers()
            display.update()
    elif display.pressed(badger2040.BUTTON_C):
        old = g_board.copy()
        move_right(g_board)
        if board_changed(old, g_board):
            fill_board()
            display.set_pen(15)
            display.clear()
            draw_board()
            numbers()
            display.update()
    elif display.pressed(badger2040.BUTTON_A):
        old = g_board.copy()
        move_left(g_board)
        if board_changed(old, g_board):
            fill_board()
            display.set_pen(15)
            display.clear()
            draw_board()
            numbers()
            display.update()
    elif display.pressed(badger2040.BUTTON_A) and display.pressed(badger2040.BUTTON_C):
        while(True):
            display.keepalive()
            display.halt()
    if no_moves():
        display.set_pen(15)
        display.rectangle(0, 0, WIDTH, HEIGHT)
        display.set_pen(0)
        display.set_font("bitmap8")
        display.text("Game Over", 0, 0, scale=5)
        display.text("press b for new game", 0, 100, scale=2)
        display.update()
        while not display.pressed(badger2040.BUTTON_B):
                time.sleep(0.05)
        start()
        fill_board_start()
        numbers()
        display.update()
       
    
    