class Animol:
    def __init__(self,make_sound):
        self.make_sound=make_sound

class Dog(Animol):
    def __init__(self,name,make_sound):
        self.name=name
        super.__init__(make_sound)

    def speak(self):
        print(f"{self.name}  говорит -{self.make_sound}")

class Cat(Animol):
    def __init__(self,name1,make_sound):
        self.name1=name1
        super.__init__(make_sound)
    def speak(self):
        print(f"{self.name1}  говорит - {self.make_sound}")

class Cow(Animol):
    def __init__(self,name2,make_sound):
        self.name2=name2
        super.__init__(make_sound)
    def speak(self):
        print(f"{self.name2}  говорит -{self.make_sound}")

d=Dog('Niki',"avvv")
d.speak()