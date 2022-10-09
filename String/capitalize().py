x = input("enter a string : ")

result = ""

for i in range(len(x)):
    if i == 0:
        result = result + x[i].upper()
    if i != 0:
        result = result + x[i].lower()

print(result)

