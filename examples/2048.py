import badger2040

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

def start():
    display.set_update_speed(badger2040.UPDATE_NORMAL)
    display.set_pen(0)
    display.clear()
    display.update()
    
    display.set_update_speed(badger2040.UPDATE_FAST)
    
    board()
    display.update()
    
def board():
    WIDTH = badger2040.WIDTH # Speed 
    HEIGHT = badger2040.HEIGHT
    display.set_pen(15)
    display.rectangle(0, 0, WIDTH, HEIGHT)
    
    display.set_pen(0)
    display.line(0, 0, 0, HEIGHT)
    display.line(74, 0, 74, HEIGHT)
    display.line(148, 0, 148, HEIGHT)
    display.line(222, 0, 222, HEIGHT)
    display.line(295, 0, 295, HEIGHT)
    

start()
while True:
    display.keepalive()
    
    display.halt()