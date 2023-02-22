import random
import time

pos_x = 0
pos_y = 0

bg_colors = [random.randrange (15), random.randrange (15), random.randrange (15)]
text_colors = [random.randrange (15), random.randrange (15), random.randrange (15)]

def inputs_render():
    pen (bg_colors[0], bg_colors[1], bg_colors[2])
    clear ()
    cursor (pos_x, pos_y)
    pen (text_colors[0], text_colors[1], text_colors[2])
    text ("hello, world!")
    flip ()


while True:
    led (random.randrange (100), random.randrange (100), random.randrange (100))
    inputs_render ()
    
    if button (A):
        text_colors = [random.randrange (15), random.randrange (15), random.randrange (15)]
        inputs_render ()
    
    if button (B):
        bg_colors = [random.randrange (15), random.randrange (15), random.randrange (15)]
        inputs_render ()

    if button (LEFT):
        pos_x -= 10
        if pos_x < 0:
            pos_x = 0
    elif button (RIGHT):
        pos_x += 10
        if pos_x > 200:
            pos_x = 200
    if button (UP):
        pos_y -= 10
        if pos_y < 0:
            pos_y = 0
    elif button (DOWN):
        pos_y += 10
        if pos_y > 200:
            pos_y = 200
        
    time.sleep_ms (150)


