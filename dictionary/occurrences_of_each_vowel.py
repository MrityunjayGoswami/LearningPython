word = input("enter any word : ")
vowels = ["a","e","i","o","u"]
dic = {}

for x in word:
    if x in vowels:
        dic[x] = dic.get(x,0)+1
for k,v in dic.items():
    print(k," occurred ",v," times.")