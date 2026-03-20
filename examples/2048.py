import badger2040

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

board = [ "2", " ", " ", " ",
          "4", " ", " ", " ",
          " ", " ", "32", " ",
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
    display.text("2", 30, 5, scale=3) # fuer 4 Stellige Zahlen: 5,5 fuer 1 stellige zahlen: 30,5 fuer drei: 20,5 fuer zwei: 23,5
    display.text("4", 104, 5, scale=3)
    display.text("8", 178, 5, scale=3)
    display.text("16", 248, 5, scale=3)
    
    display.text("32", 23, 37, scale=3)
    display.text("64", 97, 37, scale=3)
    display.text("128", 166, 37, scale=3)
    display.text("256", 237, 37, scale=3)
    
    display.text("512", 20, 69, scale=3)
    display.text("1024", 82, 69, scale=3)
    display.text("2048", 153, 69, scale=3)
    display.text("4096", 225, 69, scale=3)
    
    display.text("8192", 8, 101, scale=3) 
    display.update()
    
    for i, number in enumerate(board):
        print(number)
        

print("HI")

start()
numbers()
while True:
    display.keepalive()
    
    display.halt()