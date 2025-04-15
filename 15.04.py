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