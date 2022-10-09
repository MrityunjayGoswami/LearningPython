class Computer:

    def __init__(self):
        self.name = 'amit'
        self.age = 23

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c1.age = 24
c2 = Computer()
if c1.compare(c2):
    print("they are same")
else:
    print("they are not same")