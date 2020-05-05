import random

def random_quantum_state():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    length = (a ** 2 + b ** 2)**(1/2)
    return [a / length, b / length]
