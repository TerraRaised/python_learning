# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

print("input A")
a = int(input())
print("input B")
b = int(input())
print("input C")
c = int(input())
print("AC = ", abs(a-c))
print("BC = ", abs(b-c))
print("AC + BC = ", abs(a-c) + abs(b-c))

