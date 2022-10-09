data_list = [50, 40, -10, 30, 20, 12, 15]

l = len(data_list)

for i in range(l):
    min = i
    for j in range(i+1,l):
        if data_list[min] > data_list[j]:
            min = j

    data_list[i],data_list[min] = data_list[min],data_list[i]

print(data_list)
