class Math1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addi(self):
        print(f"Сложения = {self.a}+{self.b}={self.a+self.b}")
    def subs(self):
        print(f"Разность = {self.a}-{self.b}={self.a - self.b}")
    def multi(self):
        print(f"Пройзводная = {self.a}*{self.b}={self.a * self.b}")
    def devi(self):
        print(f"Деления = {self.a}/{self.b}={self.a /self.b}")

m=Math1(4,5)
m.multi()
m.devi()
m.addi()
m.subs()

class Car:
    def __init__(self,color,type,year):
        self.color=color
        self.type=type
        self.year=year
    def start(self):
        print("Автомобиль заведен")
    def stop(self):
        print("Автомобиль заглушен")
    def set_year(self, year):
        self.year = year
        print(f"Год выпуска установлен: {self.year}")
    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля установлен: {self.type}")
    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")
car1 = Car("белый", "хэтчбек", 2018)
car1.start()
car1.set_year(2020)
car1.set_type("седан")
car1.set_color("черный")
car1.stop()

class Student:
    def init(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
    def Name1(self):
        return self.name
    def Age1(self):
        return self.age
    def GroupNumber1(self):
        return self.groupNumber
    def NameAge1(self, name, age):
        self.name = name
        self.age = age
    def GroupNumber2(self, groupNumber):
        self.groupNumber = groupNumber
student1 = Student()
student1.NameAge1("Ali", 17)
student1.GroupNumber2("11B")
print("Студент 1:")
print("Имя:", student1.Name1())
print("Возраст:", student1.Age1())
print("Группа:", student1.GroupNumber1())
