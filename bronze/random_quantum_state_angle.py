# your function is here
from math import cos, sin, pi
from random import randrange
def random_quantum_state():
    angle = randrange(360) / 360 * pi
    state = [cos(angle), sin(angle)]
    return state
