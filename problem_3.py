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
	# We can exclude all even factors and then travers factors with step = 2
	if number % 2 == 0:
		prime_factor = 2
		while number % 2 == 0:
			number /= 2
	else:
		prime_factor = 1
		
	factor = 3	
	while number > 1 :
		if number % factor == 0:
			number /= factor
			prime_factor = factor
		else:
			factor += 2
	return prime_factor

if __name__ == '__main__':
	main()