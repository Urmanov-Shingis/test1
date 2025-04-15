class Persona:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=Persona('Maks',"44")
b=Persona("barsik",'66')

print("name:",a.name)
print("age:",a.age)
print(vars(a))

print("name:",b.name)
print("age:",b.age)
print(vars(b))



