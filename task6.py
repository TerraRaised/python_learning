# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

print("input A")
a = int(input())
print("input B")
b = int(input())
print("input C")
c = int(input())
x = int(b)
b = a
c = x
a = c
print("A = ", a)
print("B = ", b)
print("C = ", c)