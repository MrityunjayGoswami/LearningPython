x = input("enter : ")
count = 0
b=3
while b>0:
    for i in x:
        count = count + int(i)
    x = str(count)
    count = 0
    b = b-1

print("your mulank is :",x)
