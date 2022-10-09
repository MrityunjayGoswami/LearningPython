def add_sub(a,b):
    add = a+b
    sub = a-b
    return add,sub

add = int(input("enter the values : "))
sub = int(input())
x,y = add_sub(add,sub)
print("Addition is ",x,"and subtraction is",y)