s = {10,20,30}
i = {60,70,80}

s.update(i,range(5))
print(s)

b = s.copy()
print(id(b),id(s))