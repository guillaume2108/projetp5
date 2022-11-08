# import core
#
# def setup():
#     print("setup START----")
#     core.WINDOW_SIZE = [400, 400]
#     print("setup END------")
#
#
# def run():
#         print("running")
#         core.Draw.rect((255, 0, 0,), (100, 100, 100, 300), 1)
#
#
#
# core.main(setup,run)
import random
from pygame.math import Vector2, Vector3
import core


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 600]

    core.memory("bobPosition", Vector2(0, 0))
    core.memory("origine",Vector2(400,300))
    core.memory("bobHistorique",[])

    print("Setup END-----------")




def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("bobPosition", Vector2(0, 0))

    #DESSIN
    core.Draw.circle((255,0,0),core.memory("bobPosition") + core.memory("origine"),10)

    #DEPLACEMENT
    vel = Vector2(random.randint(-10, 10), random.randint(-10, 10))
    core.memory("bobHistorique").append(vel.length())
    posx = core.memory("bobPosition").x + vel.x
    posy = core.memory("bobPosition").y + vel.y
    core.memory("bobPosition", Vector2(posx, posy))
    s = sum(core.memory("bobHistorique"))
    n = len(core.memory("bobHistorique"))
    print("moyenne", s/n)
    core.printMemory()





core.main(setup, run)
