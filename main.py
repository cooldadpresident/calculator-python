def read_number(text_number, text_error):
	while True:
		try:
			number = float(input(text_number))
			return number
		except ValueError:
			print(text_error)
		else:
			return number
		
def another_excercise():
	while True:
		answer = input("Do you want another one? yes / no").lower()
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		print("Answer yes or no")
		
def make_operation(a, b):
	while True:
		print('1 - addition')
		print('2 - subtraction')
		print('3 - multiplication')
		print('4 - Division')
		
		try:
			input = int(input('Enter number for Artihmetic Operation'))
		
			match input:
				case 1:
					return a + b
				case 2:
					return a - b
				case 3:
					return a * b
				case 4:
					if b != 0:
						return a / b
					else:
						print('Cannot divide by null')
						continue
				case _:
					print('Enter number from 1 to 4')
					continue	
		except ValueError:
			print('Invalid input')
			continue
	