"""
Description:
	This program outputs the largest palindrome
	made from the product of two 3-digit numbers
Computations:
	largest palindrome
	for i from largest num to lowest num:
		for j from largest num to lowest num:
			if i * j < largest palindrome:
				next i iteration
			else if i * j is palindrome:
				largest palindrome = i * j
"""

def main():
	largest_num = int(input("Enter largest number: "))
	lowest_num = int(input("Enter lowest number: "))
	largest_palindrome = get_largest_palindrome(largest_num, lowest_num)
	print("{} * {} = {}".format(largest_palindrome[0], largest_palindrome[1], largest_palindrome[2]))

def get_largest_palindrome(largest_num, lowest_num):
	largest_palindrome = 0
	first_number = 0
	second_number = 0

	for i in range(largest_num, lowest_num - 1, -1):
		for j in range(largest_num, lowest_num - 1, -1):
			product = i * j
			if product < largest_palindrome:
				break
			elif is_palindrome(product):
				largest_palindrome = product
				first_number = i
				second_number = j
	return (first_number, second_number, largest_palindrome)

def is_palindrome(number):
	return str(number) == str(number)[::-1]

if __name__ == '__main__':
	main()