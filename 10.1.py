class Worker:
    def __init__(self,name,age,balase):
        self.name=name
        self.age=age
        self.balase=balase
class Admin(Worker):
    def __init__(self,name,age,balase ):
        super().__init__(name,age,balase)
        print(f"Cgbcjr {self.name},{self.age},{self.balase}")


