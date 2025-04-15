class Animol:
    def __init__(self,name,type,mass):
        self.name=name
        self.type=type
        self.mass=mass
a=Animol('Maks',"Cat","10 kg")
b=Animol("barsik",'Dog',"25 kg")

print("name:",a.name)
print("name:",b.name)
print(vars(a))
print(vars(b))
