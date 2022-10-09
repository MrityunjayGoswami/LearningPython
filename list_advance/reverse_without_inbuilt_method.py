data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
reversed_list = []
x = len(data_list)

for i in range(x):
    reversed_list.append(data_list[x-i-1])

print(reversed_list)