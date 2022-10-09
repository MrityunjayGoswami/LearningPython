non_sorted_list = [200, 10, 2, -1, 34, -100, 99,1]

size = len(non_sorted_list)
for i in range(size):
    for j in range(1, size):
        if non_sorted_list[i] > non_sorted_list[j]:
            val = non_sorted_list[i]
            non_sorted_list[i] = non_sorted_list[j]

            non_sorted_list[j] = val
    print(non_sorted_list)
non_sorted_list.append(non_sorted_list.pop(0))

print("\n final : ",non_sorted_list)
