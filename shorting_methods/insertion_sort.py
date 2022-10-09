data_list = [50, 40, -10, 30, 20, 12, 15]
l = len(data_list)

for i in range(1,l):
    j = i-1
    key = data_list[i]
    while j >= 0 and key<data_list[j]:
        data_list[j+1] = data_list[j]
        j -=1
    data_list[j+1] = key
    print(data_list)

print("final : ",data_list)