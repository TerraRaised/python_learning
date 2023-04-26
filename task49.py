# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 22

    def __setattr__(self, attr, value):
        if attr == "age":
            pass
        elif attr == "name":
            self.name = value

    def print_attr(self):
        print(self.name, self.age)


person1 = Person
person1.name = "Brown"
person1.age = 33
person1.print_attr

person1.print_attr()