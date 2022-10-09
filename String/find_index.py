# This function checks if a value exist in a string
def find_index(string, key):
    for i in range(len(string)):
        if string[i] == key:
            print(i)



string, key = input("enter a string and key : ").split(".")
find_index(string, key)
