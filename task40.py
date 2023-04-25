

# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

import calendar

def dates(year, month):
    lst = calendar.monthrange(year, month)
    print(lst)
    x = lst[1]
    print(x)
    days = [i for i in range(x+1)]
    print(days)

dates(2023, 9)