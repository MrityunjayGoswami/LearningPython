data_list = [50, 40, -10, 30, 20, 12, 15]
l = len(data_list)

for i in range(l):
    for j in range(0, l-i-1):
        if data_list[j] > data_list[j+1]:
            data_list[j], data_list[j+1] = data_list[j+1], data_list[j]

print(data_list)
print("\nSecond Largest number of list is : ",data_list[-2])

