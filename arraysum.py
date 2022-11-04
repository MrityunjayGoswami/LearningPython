list1 = [1,2,3,4,5]
target = 5
dic ={}
for i in list1:
    if i in dic:
        dic +=1
    else:
        dic[i] = 1
    if target-i in dic:
        print([i,target-i])
