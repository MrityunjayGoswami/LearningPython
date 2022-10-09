string = "hello how are u भारत"
print("ascii : ",string.isascii())

dec = "1000"
print("decimal: ",dec.isdecimal())

digit = "1234"
print("digit : ", digit.isdigit())

print("identifier : ",string.isidentifier())

print("Lower? : ",string.islower())

print("numeric : ",string.isnumeric())

print("printable : ",string.isprintable())

whitespace = "     fh  "
print("isspace() : ",whitespace.isspace())

title = "This Is America"
print("istitle() : ",string.istitle())
print("istitle() : ",title.istitle())

upper1 = "Heloo how are you"
upper2 = "HELLO HOW ARE YOU"
print("isupper() : ",upper1.isupper())
print("isupper()2 : ", upper2.isupper())

iterable_string = ("how","are","you")
print(".join() : ","#".join(iterable_string))

just = "how"
print("!just : ",just.ljust(20),"are you")

print("lower : ",upper2.lower())

strip = "    hello    "
print("lstrip() : ",strip.lstrip(),"hello")

translate = "hello how are you"
table = translate.maketrans("h","x")
print("translate",translate.translate(table))

part = "i could eat banana all day"
print("partition : ",part.partition("banana"))

print("replace() : ",part.replace("banana","apple"))
