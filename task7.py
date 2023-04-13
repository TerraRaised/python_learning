# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

print("input X")
x = int(input())
print("input Y")
y = int(input())
print("input Z")
z = int(input())

if x > y and x > z:
    print("Наибольшее число ", x)
elif y > x and y > z:
    print("Наибольшее число ", y)
elif z > x and z > x:
    print("Наибольшее число ", z)
else:
    print("Числа равны")