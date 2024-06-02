

import pgzrun

import random
'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
TITLE = "fruit collector"
WIDTH = 500
HEIGHT = 500

message = ""



apol = Actor("apple")

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
def draw():
    screen.clear()
    screen.fill(color = "pink")
    apol.draw()

def place_zeapple():
    apol.x = random.randint(55, WIDTH-40)
    apol.y = random.randint(55, HEIGHT-40)

def on_mouse_down(pos):
    global message
    if apol.collidepoint(pos):
        message = "one fruit in the basket!"
        place_zeapple()
    else:
        message = "come on! more fruit!"

place_zeapple()


pgzrun.go()