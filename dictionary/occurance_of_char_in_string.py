word = input("enter any word : ")
dic = {}
for x in word:
    dic[x] =dic.get(x,0)+1

for k,v in dic.items():
    print(k," occured ",v," times ")