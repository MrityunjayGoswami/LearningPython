def factorial(number):
    result = 1
    while number>=1:
        result = result*number
        number = number-1
    return result

number = int(input("Eneter the number to find factorial : "))
fact = factorial(number)
print(fact)