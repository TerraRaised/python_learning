#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda
from functools import reduce
lst = [123, 234, 345, 456]
print([reduce(lambda x, y: x+y, map(int, str(el))) for el in lst])
