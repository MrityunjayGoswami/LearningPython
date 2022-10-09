def count(string,word):
    list = string.split()
    dic = {}
    for i in list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in list:
        if word == i:
            print(dic[word])
            break
        else:
            print("this word is not present in string so can't be counted")



string = input("enter a string : ")
word = input("enter a word  : ")
count(string,word)