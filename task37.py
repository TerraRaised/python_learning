

#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import time, datetime

def hello():
    print("Hello world")
    global name
    name = "hello "

def goodbye():
    print("Goodbye world")
    global name
    name = "goodbye "

def wrapper(func):
    fd = open("data.log", "a")
    global counter
    counter = 0
    counter += 1
    call = time.localtime()
    call_str = time.strftime("%d.%m.%Y %H:%M", call)
    log_str = name + str(counter) + " " + call_str
    print(log_str)
    fd.write(log_str)

 #   print(call_str)

print("input number of recursions: ")
x = int(input())
while x > 0:
    wrapper(goodbye())
    x -= 1