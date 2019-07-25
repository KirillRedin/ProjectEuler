"""
This program calculates the sum of all the multiplies
of 3 or 5 below 1000
"""

def main():
	bounds = tuple(input("Enter bounds: "))
	count_multiplies_sum(bounds)

def count_multiplies_sum(bounds):
	sum = 0 
	for number in range(bounds[0], bounds[1]):
		if number % 3 == 0 or number % 5 == 0:
			sum += number
	print(sum)

if __name__ == '__main__':
	main()