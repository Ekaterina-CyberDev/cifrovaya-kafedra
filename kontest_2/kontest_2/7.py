import random

class Cat:
    def __init__(self, alive):
        self._alive = alive
    
    def is_alive(self):
        return self._alive

class Box:
    def open(self):
        # Случайно определяем, жив кот или мертв
        is_alive = random.choice([True, False])
        return Cat(is_alive)