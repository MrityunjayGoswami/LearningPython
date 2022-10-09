rfind = "Hello you how are you are"
print("rfind : ",rfind.rfind("are"))

print("rindex : ",rfind.rindex("are"))

print("rpartition : ",rfind.rpartition("you"))

split = "apple, banana, cherry"
print("rsplit() : ",split.rsplit(", "))

split_lines =  "thanku for the music.\nWelcome to the jungle."
print("splitlines", split_lines.splitlines())

print("starts_with : ",rfind.startswith("Hello"))

strip = "    banana    "
print("that is ",strip.strip(),"and apple")

swap = "HeLLo My namE is PeteR Sam"
print("swapcase : ", swap.swapcase())

print("Title : ",swap.title())

my_dict = {83:80}
print("translate : ",swap.translate(my_dict))

print("upper : ",swap.upper())

txt = "50"
print("zfill : ",txt.zfill(10))