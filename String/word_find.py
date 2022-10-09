string = input("enter a string : ")
word = input("enter what do you want to search : ")
spilitted = string.split(" ")

for i in spilitted:
    if i == word:
        print(i)
        break
    else:
        print("word is not in string")
        break
