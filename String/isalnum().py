def alphanum(string):

    for i in string:
        if type(i) != int or type(i) != str:
            print("it is not a alpha numeric string")
            break
        else:
            print("it is a alpha numeric string")


string = input("enter the string : ")
alphanum(string)