import badger2040

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
badger2040.system_speed(badger2040.SYSTEM_FAST)
display.set_thickness(2)

display.line(0, 0, 296, 128)


while (true):
    display.keepalive()
    
    display.halt()