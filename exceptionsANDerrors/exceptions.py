x =-5

# if x<0:
#     raise Exception('x should be positive')
#assert(x>=0), 'x is not positive'

try:
    x = 5/0
    b = x+'b'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("evrything is good")
finally:
    print("it will always run")