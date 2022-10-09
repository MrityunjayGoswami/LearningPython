class A:
    def feature1(self):
        print("Featue 1 is working")
    def feature2(self):
        print("Featue 2 is working")

class B(A):
    def feature3(self):
        print("Featue 3 is working")
    def feature4(self):
        print("Featue 4 is working")

class C(B):
    def feature5(self):
        print("Featue 5 is working")

"""above is multilevel level inheritence"""

"""and below is multiple inheritence"""

class C(A,B):
    def feature6(self):
        print("Featue 6 is working")


c1 = C()
b1 = B()