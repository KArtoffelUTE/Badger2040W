import badger2040
import jpegdec
import os
import ujson
# ------------------------------
#   Display Setup
# ------------------------------

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

jpeg = jpegdec.JPEG(display.display)


# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

IMAGE_WIDTH = 104

COMPANY_HEIGHT = 30
DETAILS_HEIGHT = 20
NAME_HEIGHT = HEIGHT - COMPANY_HEIGHT - (DETAILS_HEIGHT * 2) - 2
TEXT_WIDTH = WIDTH - IMAGE_WIDTH - 1

COMPANY_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10

BADGE_PATH = "/badges/badge.txt"
CURRENT_BADGE = "/state/current_badge.json"

DEFAULT_TEXT = """mustelid inc
H. Badger
RP2040
2MB Flash
E ink
296x128px
/badges/badge.jpg
"""



# ------------------------------
#      Utility functions
# ------------------------------


# Reduce the size of a string until it fits within a given width
def truncatestring(text, text_size, width):
    while True:
        length = display.measure_text(text, text_size)
        if length > 0 and length > width:
            text = text[:-1]
        else:
            text += ""
            return text


# ------------------------------
#      Drawing functions
# ------------------------------

# Draw the badge, including user text
def draw_badge():
    display.set_pen(0)
    display.clear()

    # Draw badge image
    jpeg.open_file(badge_image)
    jpeg.decode(WIDTH - IMAGE_WIDTH, 0)

    # Draw a border around the image
    display.set_pen(0)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - 1, 0)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - IMAGE_WIDTH, HEIGHT - 1)
    display.line(WIDTH - IMAGE_WIDTH, HEIGHT - 1, WIDTH - 1, HEIGHT - 1)
    display.line(WIDTH - 1, 0, WIDTH - 1, HEIGHT - 1)

    # Uncomment this if a white background is wanted behind the company
    # display.set_pen(15)
    # display.rectangle(1, 1, TEXT_WIDTH, COMPANY_HEIGHT - 1)

    # Draw the company
    display.set_pen(15)  # Change this to 0 if a white background is used
    display.set_font("serif")
    display.text(company, LEFT_PADDING, (COMPANY_HEIGHT // 2) + 1, WIDTH, COMPANY_TEXT_SIZE)

    # Draw a white background behind the name
    display.set_pen(15)
    display.rectangle(1, COMPANY_HEIGHT + 1, TEXT_WIDTH, NAME_HEIGHT)

    # Draw the name, scaling it based on the available width
    display.set_pen(0)
    display.set_font("sans")
    name_size = 2.0  # A sensible starting scale
    while True:
        name_length = display.measure_text(name, name_size)
        if name_length >= (TEXT_WIDTH - NAME_PADDING) and name_size >= 0.1:
            name_size -= 0.01
        else:
            display.text(name, (TEXT_WIDTH - name_length) // 2, (NAME_HEIGHT // 2) + COMPANY_HEIGHT + 1, WIDTH, name_size)
            break

    # Draw a white backgrounds behind the details
    display.set_pen(15)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT * 2, TEXT_WIDTH, DETAILS_HEIGHT - 1)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT, TEXT_WIDTH, DETAILS_HEIGHT - 1)

    # Draw the first detail's title and text
    display.set_pen(0)
    display.set_font("sans")
    name_length = display.measure_text(detail1_title, DETAILS_TEXT_SIZE)
    display.text(detail1_title, LEFT_PADDING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), WIDTH, DETAILS_TEXT_SIZE)
    display.text(detail1_text, 5 + name_length + DETAIL_SPACING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), WIDTH, DETAILS_TEXT_SIZE)

    # Draw the second detail's title and text
    name_length = display.measure_text(detail2_title, DETAILS_TEXT_SIZE)
    display.text(detail2_title, LEFT_PADDING, HEIGHT - (DETAILS_HEIGHT // 2), WIDTH, DETAILS_TEXT_SIZE)
    display.text(detail2_text, LEFT_PADDING + name_length + DETAIL_SPACING, HEIGHT - (DETAILS_HEIGHT // 2), WIDTH, DETAILS_TEXT_SIZE)

    display.update()


# ------------------------------
#        Program setup
# ------------------------------

BADGE_DIR = "/badges"
badge_files = [f for f in os.listdir(BADGE_DIR) if f.endswith(".txt")]
badge_files.sort()  # alphabetisch sortieren


def load_badge(index):
    global company, name, detail1_title, detail1_text, detail2_title, detail2_text, badge_image

    path = BADGE_DIR + "/" + badge_files[index]
    with open(path, "r") as badge:
        company = badge.readline().strip()
        name = badge.readline().strip()
        detail1_title = badge.readline().strip()
        detail1_text = badge.readline().strip()
        detail2_title = badge.readline().strip()
        detail2_text = badge.readline().strip()
        badge_image = badge.readline().strip()

    # Texte kürzen
    company = truncatestring(company, COMPANY_TEXT_SIZE, TEXT_WIDTH)
    detail1_title = truncatestring(detail1_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
    detail1_text = truncatestring(detail1_text, DETAILS_TEXT_SIZE,
                                  TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail1_title, DETAILS_TEXT_SIZE))
    detail2_title = truncatestring(detail2_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
    detail2_text = truncatestring(detail2_text, DETAILS_TEXT_SIZE,
                                  TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail2_title, DETAILS_TEXT_SIZE))

    draw_badge()






# Create a new Badger and set it to update NORMAL
display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

jpeg = jpegdec.JPEG(display.display)
'''
# Open the badge file
try:
    badge = open(BADGE_PATH, "r")
except OSError:
    with open(BADGE_PATH, "w") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
    badge = open(BADGE_PATH, "r")

# Read in the next 6 lines
company = badge.readline()        # "mustelid inc"
name = badge.readline()           # "H. Badger"
detail1_title = badge.readline()  # "RP2040"
detail1_text = badge.readline()   # "2MB Flash"
detail2_title = badge.readline()  # "E ink"
detail2_text = badge.readline()   # "296x128px"
badge_image = badge.readline()    # /badges/badge.jpg

# Truncate all of the text (except for the name as that is scaled)
company = truncatestring(company, COMPANY_TEXT_SIZE, TEXT_WIDTH)

detail1_title = truncatestring(detail1_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
detail1_text = truncatestring(detail1_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail1_title, DETAILS_TEXT_SIZE))

detail2_title = truncatestring(detail2_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
detail2_text = truncatestring(detail2_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail2_title, DETAILS_TEXT_SIZE))
'''

# ------------------------------
#       Main program
# ------------------------------

def save_badge_index(value):
    data = {"current_badge": value}
    with open(CURRENT_BADGE, "w") as f:
        f.write(ujson.dumps(data))
        f.flush()
        os.sync()   # wichtig auf RP2040
def get_badge_index():
    try:
        with open(CURRENT_BADGE, "r") as f:
            data = ujson.loads(f.read())
            badge_index = data.get("current_badge", 0)
    except:
        badge_index = 0
    if badge_index < 0:
        badge_index = 0
    if badge_index >= len(badge_files):
        badge_index = len(badge_files) - 1
    return badge_index

#draw_badge()

load_badge(get_badge_index())
while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()
    
    if display.pressed(badger2040.BUTTON_UP):
        badge_index = (get_badge_index() - 1) % len(badge_files)
        save_badge_index(badge_index)
        load_badge(badge_index)
    elif display.pressed(badger2040.BUTTON_DOWN):
        badge_index = (get_badge_index() + 1) % len(badge_files)
        save_badge_index(badge_index)
        load_badge(badge_index)
    else:
        # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
        display.halt()

