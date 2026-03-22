import badger2040

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT
SCALE = 3

g_board = [ "1024", "4", "128", "32",
          "32", "64", "128", "256",
          "512", "1024", "2048", "4096",
          "8192", "1024", "2048", "4096",]

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
    
    display.update()
        
        

print("HI")

start()
numbers()
while True:
    display.keepalive()
    
    display.halt()