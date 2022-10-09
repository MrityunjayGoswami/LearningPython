def text_center(string, num):
    half = num//2

    if num % 2 == 0:
        if num > len(string):
            result = " "*half + string + " "*half
            print(result)
        else:
            print(string)
    else:
        print("enter a evan number because to center something you have to give equal space both sides")

string = input("enter a string : ")
num = int(input("enter a even number : "))
text_center(string,num)