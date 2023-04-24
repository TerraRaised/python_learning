# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square

    def set_color(self):
        print("input color")
        color = str(input())
        self.color = color

    def print_color(self):
        print(self.color)

    def set_square(self):
        print("input square")
        square = float(input())
        self.square = square

    def print_square(self):
        print(self.square)

circle = Shape("blue", 3)

circle.set_color()
circle.print_color()
circle.print_square()