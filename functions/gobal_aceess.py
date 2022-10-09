a=10 #global variable
def f1():
    a=777 #local variable
    print(a)
    print(globals()['a'])
f1()