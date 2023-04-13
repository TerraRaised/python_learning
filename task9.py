# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

print("input year")
year = int(input())
year = str(year)
if len(year) <= 2:
    print("1 century")
elif len(year) == 3:
    print(int(year[0]) + 1, "century")
elif len(year) == 4:
    print(10*int(year[0]) + int(year[1]) + 1, "century")