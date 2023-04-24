# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.



class Pet():
    def __init__(self, name, weight, hunger):
        self.name = name
        self.weight = weight
        self.hunger = hunger

    def info(self):
        print("name ", self.name)
        print("weight ", self.weight)
        print("hunger ", self.hunger)

    def hungry(self):
        print("how is my pet doing")
        if self.hunger < 5:
            print("feed me")
        elif self.hunger > 10:
            print("im ok")

    def feed(self):
        print("feeding pet with sausage")
        self.hunger = self.hunger + 3


cat = Pet("Barsik", 2, 12)
dog = Pet("Barbos", 4, 2)


cat.info()
dog.info()

cat.hungry()
dog.hungry()

dog.feed()
dog.feed()
dog.feed()
dog.feed()

dog.hungry()