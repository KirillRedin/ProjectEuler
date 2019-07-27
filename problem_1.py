"""
This program calculates the sum of all the multiplies
of 3 or 5 below 1000
"""

def main():
	print("Calculate the sum of all the multiplies of 3 or 5 in an interval")
	largest_num = int(input("Enter the largest number: "))
	lowest_num = int(input("Enter the lowest number: "))
	sum = count_multiplies_sum(largest_num, lowest_num)
	print("The sum of all the multiplies of 3 or 5 in the [{}, {}] interval "\
		"is {}".format(lowest_num, largest_num, sum))

def count_multiplies_sum(largest_num, lowest_num):
	sum = 0 
	for number in range(lowest_num, largest_num + 1):
		if number % 3 == 0 or number % 5 == 0:
			sum += number
	return sum

if __name__ == '__main__':
	main()