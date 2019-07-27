"""
This program calculates the sum of all the multiples
of 3 or 5 below 1000
"""

def main():
	print("Calculate the sum of all the multiples of 3 or 5 in a range")
	largest_num = int(input("Enter the largest number: "))
	lowest_num = int(input("Enter the lowest number: "))
	
	sum_of_3 = count_multiples_sum(largest_num, lowest_num, 3)
	sum_of_5 = count_multiples_sum(largest_num, lowest_num, 5)
	# Count sum of multiples of 15 to exclude repeating numbers
	sum_of_15 = count_multiples_sum(largest_num, lowest_num, 15)
	
	sum = sum_of_3 + sum_of_5 - sum_of_15
	print("The sum of all the multiples of 3 or 5 in the [{}, {}] interval "\
		"is {}".format(lowest_num, largest_num, sum))

def count_multiples_sum(largest_num, lowest_num, number):
	all_multiples_amount = largest_num // number
	excluded_multiples_amount = (lowest_num - 1) // number
	multiples_amount = all_multiples_amount - excluded_multiples_amount
	max_multiple = all_multiples_amount * number
	min_multiple = (excluded_multiples_amount + 1) * number
	multiples_sum = (min_multiple + max_multiple) * multiples_amount / 2
	return multiples_sum

# Deprecated because of complexity
def count_multiples_sum_depr(largest_num, lowest_num):
	sum = 0 
	for number in range(lowest_num, largest_num + 1):
		if number % 3 == 0 or number % 5 == 0:
			sum += number
	return sum

if __name__ == '__main__':
	main()