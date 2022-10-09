class Car:
    #this is class variable
    wheels = 4 #class name_space

    def __init__(self):
        #this is instance variable
        self.name = 'bmw'  #instance name_space
        self.mil = 10


c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 10

print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)
