# Method resolation order
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Featue 1 is working")

class B:
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("Featue 2 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feature6(self):
        print("Featue 6 is working")


a1 = C()
a1.feature1()