class Car:
    def __init__(self,car_tupe,car_color,car_speed,car_age=2025):
        self.tupe=car_tupe
        self.color=car_color
        self.speed=car_speed
        self.age=car_age
class Human:
    def __init__(self,human_name,human_colorskin,human_mass):
        self.name=human_name
        self.colorskin=human_colorskin
        self.mass=human_mass
cobalt=Car("x 100", "dark","3000",)
print(cobalt.tupe)
print(cobalt.color)
print(cobalt.speed)
print(cobalt.age)
print(vars(cobalt))
