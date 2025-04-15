
class Human:
    def __init__(self,human_name,human_text,human_like=0):
        self.name=human_name
        self.text=human_text
        self.like=human_like
    def add_like(self):
        self.like+=1
        return self.like

a1=Human("sdcs","ascasc",12)
print(vars(a1))

print(a1.add_like())
