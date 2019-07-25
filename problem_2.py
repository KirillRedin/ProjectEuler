"""
This program calculates the sum of all even Fibonacci 
numbers which does not exceed 4 000 000.
"""

def main():
	limit = int(input("Enter Fibonacci sequence limit: "))
	sequence = get_fibonacci_sequence(limit)
	print(get_sum_of_even(sequence))

def get_fibonacci_sequence(limit):
	sequence = [1, 2]
	while last_elements_sum(sequence, 2) <= limit:
		sequence.append(last_elements_sum(sequence, 2))
	return sequence

def last_elements_sum(list, num_of_elements):
	sum = 0
	for i in range(1, num_of_elements + 1):
		sum += list[-i]
	return sum

def get_sum_of_even(sequence):
	sum = 0
	for number in sequence:
		if number % 2 == 0:
			sum += number
	return sum

if __name__ == '__main__':
	main()