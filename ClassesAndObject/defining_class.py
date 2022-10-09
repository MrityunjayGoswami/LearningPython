class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is : ",self.cpu, self.ram)

comp1 = Computer('i5','8gb')
comp2 = Computer('i7','32gb')

Computer.config(comp1)
Computer.config(comp2)

comp1.config()