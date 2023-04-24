# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.


class Triangle:
    def check(self, a, b, c):
        if a and b and c  > 0 and a + b > c and b + c > a and a + c > b:
            print("its ok")
        else:
            print("error, try again")

tri = Triangle()
tri.check( 2, 2, 3)