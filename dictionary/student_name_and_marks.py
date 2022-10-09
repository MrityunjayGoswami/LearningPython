n = int(input("Enter number of students : "))
dic = {}
for i in range(n):
    name = input("Enter name of the student : ")
    marks = input("Enter marks of the student : ")
    dic[name] = marks

print(dic)
while True:
    name = input("Enter student name to get marks : ")
    marks = dic.get(name,-1)
    if marks == -1:
        print("Student not found")
    else:
        print("The marks of ",name,"is : ",marks)
    option = input("do you want any other students marks [yes|no] : ")
    if option == "no":
        break
print("Thanks for using this application")
