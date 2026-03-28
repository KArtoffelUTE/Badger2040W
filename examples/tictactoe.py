import badger2040
import time

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT
IMAGE_WIDTH = 104

WIN_LINES = [
        [0, 1, 2],  # Reihe 1
        [3, 4, 5],  # Reihe 2
        [6, 7, 8],  # Reihe 3
        [0, 3, 6],  # Spalte 1
        [1, 4, 7],  # Spalte 2
        [2, 5, 8],  # Spalte 3
        [0, 4, 8],  # Diagonale
        [2, 4, 6]   # Diagonale
            ]

def new_start():
    global current_position, board, board2, move
    current_position = 1
    board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }
    move = 1
    board2 = [ " ", " ", " ",
               " ", " ", " ",
               " ", " ", " "]
    display.set_update_speed(badger2040.UPDATE_NORMAL)
    display.set_pen(0)
    display.clear()
    display.update()
    display.set_update_speed(badger2040.UPDATE_FAST)
    draw_board()
    draw_position(current_position)
    draw_marks()
    display.update()
    
def draw_board():
    display.set_pen(15)
    display.rectangle(0, 0, WIDTH, HEIGHT)

    display.set_pen(0)
    display.line(99, 0, 99, 128)
    display.line(197, 0, 197, 128)
    display.line(0, 43, 296, 43)
    display.line(0, 85, 296, 85)

def draw_marks():
    for pos, mark in board.items():
        if mark == "X":
            draw_X(pos)
        elif mark == "O":
            draw_O(pos)
            
def add_mark():
    global current_position, move
    if board.get(current_position) == " ":
        if move  not in (2, 4, 6, 8):
            mark = "O"
        else:
            mark = "X"
        move += 1
        board2[current_position -1] = mark
        board[current_position] = mark

def check_winner():
    for a, b, c in WIN_LINES:
        if board2[a] != " " and board2[a] == board2[b] == board2[c]:
            return board2[a]
    return None

def check_draw():
    return all(field != " " for field in board2) and check_winner() is None

def draw_position(new_position):
    global current_position
    current_position = new_position
    display.set_pen(12)
    if new_position == 1:
        display.rectangle(0, 0, 98, 42)
    elif new_position == 2:
        display.rectangle(100, 0, 97, 42)
    elif new_position == 3:
        display.rectangle(199, 0, 98, 42)
    elif new_position == 4:
        display.rectangle(0, 44, 98, 41)
    elif new_position == 5:
        display.rectangle(100, 44, 97, 41)
    elif new_position == 6:
        display.rectangle(199, 44, 98, 41)
    elif new_position == 7:
        display.rectangle(0, 87, 98, 41)
    elif new_position == 8:
        display.rectangle(100, 87, 97, 41)
    elif new_position == 9:
        display.rectangle(199, 87, 98, 41)

def draw_X(position):
    display.set_pen(0)
    if position == 1:
        display.line(0, 0, 98, 42)
        display.line(98, 0, 0, 42)
    elif position == 2:
        display.line(100, 0, 197, 42)
        display.line(197, 0, 100, 42)
    elif position == 3:
        display.line(199, 0, 297, 42)
        display.line(297, 0, 199, 42)
    elif position == 4:
        display.line(0, 44, 98, 85)
        display.line(98, 44, 0, 85)
    elif position == 5:
        display.line(100, 44, 197, 85)
        display.line(197, 44, 100, 85)
    elif position == 6:
        display.line(199, 44, 297, 85)
        display.line(297, 44, 199, 85)
    elif position == 7:
        display.line(0, 87, 98, 128)
        display.line(98, 87, 0, 128)
    elif position== 8:
        display.line(100, 87, 197, 128)
        display.line(197, 87, 100, 128)
    elif position == 9:
        display.line(199, 87, 297, 128)
        display.line(297, 87, 199, 128)

def draw_O(position):
    display.set_pen(0)    
    if position == 1:
        display.circle(49, 21, 20)
        display.set_pen(15)
        display.circle(49, 21, 19)
    elif position == 2:
        display.circle(147, 21, 20)
        display.set_pen(15)
        display.circle(147, 21, 19)
    elif position == 3:
        display.circle(248, 21, 20)
        display.set_pen(15)
        display.circle(248, 21, 19)
    elif position == 4:
        display.circle(49, 64, 20)
        display.set_pen(15)
        display.circle(49, 64, 19)
    elif position == 5:
        display.circle(147, 64, 20)
        display.set_pen(15)
        display.circle(147, 64, 19)
    elif position == 6:
        display.circle(248, 64, 20)
        display.set_pen(15)
        display.circle(248, 64, 19)
    elif position == 7:
        display.circle(49, 106, 20)
        display.set_pen(15)
        display.circle(49, 106, 19)
    elif position == 8:
        display.circle(147, 106, 20)
        display.set_pen(15)
        display.circle(147, 106, 19)
    elif position == 9:
        display.circle(248, 106, 20)
        display.set_pen(15)
        display.circle(248, 106, 19)

new_start()
needs_update = False
time.sleep(0.3)
while (display.pressed(badger2040.BUTTON_A) or
       display.pressed(badger2040.BUTTON_B) or
       display.pressed(badger2040.BUTTON_C) or
       display.pressed(badger2040.BUTTON_UP) or
       display.pressed(badger2040.BUTTON_DOWN)):
    display.keepalive()
    time.sleep(0.05)
while True:
    display.keepalive()
    

    if display.pressed(badger2040.BUTTON_DOWN) and current_position < 7:
        draw_board()
        draw_position(current_position + 3)
        draw_marks()
        needs_update = True
    elif display.pressed(badger2040.BUTTON_UP) and current_position > 3:
        draw_board()
        draw_position(current_position - 3)
        draw_marks()
        needs_update = True
    elif display.pressed(badger2040.BUTTON_C) and current_position % 3 != 0:
        draw_board()
        draw_position(current_position + 1)
        draw_marks()
        needs_update = True
    elif display.pressed(badger2040.BUTTON_A) and current_position not in (1, 4, 7):
        draw_board()
        draw_position(current_position - 1)
        draw_marks()
        needs_update = True
    elif display.pressed(badger2040.BUTTON_B):
        add_mark()
        draw_board()
        draw_position(current_position)
        draw_marks()
        display.update()
        if check_winner() == "X":
            display.set_pen(15)
            display.rectangle(0, 0, WIDTH, HEIGHT)
            display.set_pen(0)
            display.set_font("bitmap8")
            display.text("X won", 0, 0, scale=10)
            display.text("press b for new game", 0, 100, scale=2)
            display.update()
            while not display.pressed(badger2040.BUTTON_B):
                display.keepalive()
                time.sleep(0.02)
            new_start()
        elif check_winner() == "O":
            display.set_pen(15)
            display.rectangle(0, 0, WIDTH, HEIGHT)
            display.set_pen(0)
            display.set_font("bitmap8")
            display.text("O won", 0, 0, scale=10)
            display.text("press b for new game", 0, 100, scale=2)
            display.update()
            while not display.pressed(badger2040.BUTTON_B):
                display.keepalive()
                time.sleep(0.02)
            new_start()
        if check_draw():
            display.set_pen(15)
            display.rectangle(0, 0, WIDTH, HEIGHT)
            display.set_pen(0)
            display.set_font("bitmap8")
            display.text("Draw", 0, 0, scale=10)
            display.text("press b for new game", 0, 100, scale=2) 
            display.update()
            while not display.pressed(badger2040.BUTTON_B):
                display.keepalive()
                time.sleep(0.02)
            new_start()

    if needs_update:
        display.update()
        needs_update = False
