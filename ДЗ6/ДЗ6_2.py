
class Road:
    _length = 0
    _width = 0
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, thickness, mass_part):
         return self._length * self._width * mass_part * thickness /1000


r = Road(20, 5000)
print(f"Вы создали объект класса с шириной - {r._length }, и длиной - {r._width}")
mass = r.mass( 25, 5)
print(f"Масса дороги {int(mass)}")