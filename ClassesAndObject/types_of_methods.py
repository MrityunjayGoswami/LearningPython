class Student:
    school = 'mit'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1 = Student(10,12,13)
s2  = Student(20,21,23)

print(s1.avg())