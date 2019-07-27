"""
Decription:
	This program calculates the smallest
	positive number that is evenly divisible
	by all of the numbers from 1 to 20
Computations:
	dividers (structure is {divider: amount})
	for each number from 1 to 20:
		if not all dividers of number in dividers:
			add missing dividers to dividers
	
	number = 1
	for each divider in dividers:
		number = number * divider ^ amount
"""

def main():
	print("Calculate the smallest positive number that is evenly divisible "\
		"by all numbers in a range")
	largest_num = int(input("Enter the largest number: "))
	lowest_num = int(input("Enter the lowest number: "))
	result = get_smallest_common_number(lowest_num, largest_num)
	print("Smallest positive number that is evenly divisible by all of the "\
		"numbers from {} to {} is {}".format(lowest_num, largest_num, result))
	
def get_smallest_common_number(lowest_num, largest_num):
	# First: get all dividers of future smallest evenly divisible number and
	# their amount
	dividers_dict = get_dividers_in_range(lowest_num, largest_num)
	# Second: multiply all dividers. Amount of each divider is it's power.
	result = 1
	for (divider, amount) in dividers_dict.items():
		result *= divider ** amount
	return result

def get_dividers_in_range(lowest_num, largest_num):
	dividers_dict = {}	
	
	for number in range(lowest_num, largest_num + 1):
		dividers = get_dividers(number) # Get dividers of current number
		# Traversing dividers of current number
		for (divider, amount) in dividers.items(): 
			# If current divider in dict is missing or it's amount is less
			# than amount in current number, then ... 
			if dividers_dict.get(divider, 0) < amount: 
				# New amount of current divider in dict will be amount from
				# current number
				dividers_dict[divider] = amount 
	print("All dividers are: ", dividers_dict)
	return dividers_dict
		
def get_dividers(number):
	dividers_dict = {1: 1}
	
	while number > 1:
		step  = 1
		i = 2
		# I decided to use custom loop to modify step after first iteration
		while i <= number: 
			if i == 3:
				# We can use step = 2 after firt iteration to skip all even
				# numbers exept for 2 itself
				step = 2 
			
			if number % i == 0:
				dividers_dict[i] = dividers_dict.get(i, 0) + 1
				number /= i
				break
			
			i += step
	return dividers_dict
			
if __name__ == '__main__':
	main()