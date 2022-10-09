#thi function checks if string ends with given value
def endswith(string, value):
    if string[-1] == value:
        print("yes this string ends with this value")
    else:
        print("nope this string does not ends with this value")


string = input("enter a string : ")
value = input("enter a value : ")
endswith(string, value)

# one line code:
print(string.endswith(value))