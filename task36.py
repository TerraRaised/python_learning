#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.
import time

def hello():
    print("Hello world")

def wrapper(func):
    start = time.time_ns()
    func
    end = time.time_ns()
    print("Operation time: ", end-start, "ns")


wrapper(hello())
