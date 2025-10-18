import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def r(self):
        # Радиус-вектор: sqrt(x² + y²)
        return math.sqrt(self._x**2 + self._y**2)
    
    @r.setter
    def r(self, value):
        # Сохраняем угол, меняем радиус
        current_angle = self.a
        self._x = value * math.cos(current_angle)
        self._y = value * math.sin(current_angle)
    
    @property
    def a(self):
        # Угол в радианах
        if self._x == 0 and self._y == 0:
            return 0
        return math.atan2(self._y, self._x)
    
    @a.setter
    def a(self, value):
        # Сохраняем радиус, меняем угол
        current_radius = self.r
        self._x = current_radius * math.cos(value)
        self._y = current_radius * math.sin(value)
