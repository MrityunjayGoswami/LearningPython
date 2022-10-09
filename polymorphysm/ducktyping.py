# Python program to demonstrate
# duck typing

class Specialstring:
	def __len__(self):
		return 10

# Driver's code
if __name__ == "__main__":

	string = Specialstring()
	print(len(string))
