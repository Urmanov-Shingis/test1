class Car:
    def turnof(self):
        return  "вкл машин"
    def turnon(self):
        return "откл маши"
class Damas(Car):
    def move(self):
        return "нет тормозит"
t=Car()

Damas.turnof()
Damas.move()
