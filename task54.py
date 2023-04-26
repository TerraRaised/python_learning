# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым чи отрезкуслом, но не принадлежит [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')

#todo:
# Сделайте функцию get_weekday() статической в классе Helper
def get_week_day(number):
    try:
        if number % 1 != 0:
            raise TypeError
        elif number > 7:
            raise ValueError
        elif number < 1:
            raise ValueError
        else:
            if number == 1:
                print("monday")
            elif number == 2:
                print("tuesday")
            elif number == 3:
                print("wednesday")
            elif number == 4:
                print("thursday")
            elif number == 5:
                print("friday")
            elif number == 6:
                print("saturday")
            elif number == 7:
                print("sunday")
    except ValueError as ve:
        print("Аргумент не принадлежит требуемому диапазону")
    except TypeError as te:
        print("Аргумент не является целым числом")

print("input day of the week")
number = float(input())
get_week_day(number)