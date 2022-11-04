# lambda arguments : expression
from functools import reduce
add10 = lambda x : x+10
print(add10(1))

mult = lambda x,y : x*y
print(mult(2,3))

a = [1,2,3,4,5]

b =  map(lambda x:x*2,a)
print(list(b))

product_a =  reduce(lambda x,y : x*y, a)
print(int(product_a))