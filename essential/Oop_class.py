class Person:
	def __init__(self, name , age):
		self.name = name
		self.age = age

	# pass
	def print_person(self):
		print(self.name, " is ", self.age)


john = Person("John", 26)
lucy = Person("Lucy", 22)


john.print_person()
lucy.print_person()