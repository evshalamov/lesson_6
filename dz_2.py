"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия
одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    __length = 0
    __width = 0

    def __init__(self, __length, __width, weight, depth):
        self._length = __length
        self._width = __width
        self.weight = weight
        self.depth = depth

    def mass(self):
        length = self._length
        width = self._width
        weight = self.weight
        depth = self.depth
        total = int(length * width * weight * depth / 1000)
        print(f"Масса асфальта\n {length} м * {width} м * {weight} кг * {depth} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()