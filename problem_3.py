"""
Description:
	This program calculates the largest prime factor
	of the number
Computations:
	prime factor = 0
	factor = 2
	while number > 1:
		if number % factor == 0:
			number = number / factor
			if prime factor < factor:
				prime factor = factor
			factor = 2
		else:
			factor++
"""

def main():
	print("Calculate the largest prime factor of the number")
	number = int(input("Enter the number: "))
	prime_factor = get_prime_factor(number)
	print("Largest prime factor of {} is {}".format(number, prime_factor))

def get_prime_factor(number):
	prime_factor = 0
	factor = 2

	while number > 1:
		if number % factor == 0:
			number /= factor			
			if prime_factor < factor:
				prime_factor = factor
			factor = 2
		else:
			factor += 1
	return prime_factor


if __name__ == '__main__':
	main()