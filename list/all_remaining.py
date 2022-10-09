data = [10,20,30,3,5,8,6,2]
if 10 in data:
    data.remove(10)
print(data)

data.pop(0)
print(data)

data.reverse()
print("reverse",data)

data.sort()
print("sor : ",data)

data.sort(reverse=True)
print(data)

clone_data = data[:]
print("data : ",id(data))
print("cloned data : ",id(clone_data))

copy_data = data.copy()
print("data : ",id(data))
print("copied data : ",id(copy_data))
