# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

print("input four digit number")
x = str(input())
rev = x[::-1]
y = bool(True)
print(rev)
if x == rev:
    print(y)
else:
    print(not(y))
