class Human:
    def __init__(self,human_name,human_balans=0):
        self.name=human_name
        self.balans=human_balans
    def add_balans(self,n):
        n=input("Vog")
        self.balans+=n
        return self.balans

a1=Human("sdcs",1)
print(vars(a1))
