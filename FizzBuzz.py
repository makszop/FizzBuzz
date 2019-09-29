'''
Write a script to implement the game "Fizz Buzz".
Counting from 1 to 100, print each number in turn, on a new line.
BUT...
 * If the number is divisible by 3, or contains a digit 3,
    print "Fizz" instead of the number.
 * Similarly, for 5s, print "Buzz".
 * If both the "3" and "5" conditions, "Fizz Buzz".
'''

def checFizzBuzz(number, mod):
	''' Main method to perform check and return False or True
	    Method takes two parameters:
		@number: a integer to check if is divisible by @mod
	    @mod: a divider
	    return False when @number is not a integer
	    return True when @number is divisible by @mod or @mod is in @number
	    otherwise return False
	'''
	if type(number) != type(int()):
		return False
	if number%mod == 0 or str(mod) in str(number):
		return True
	else:
		return False

def run(x):
	''' Main run function to start iteration from 1 to x
	    Method takes only parameter:
		@x: which is max in range from 1 to x
	'''
	for i in range(1,x+1):
		if checFizzBuzz(number=i, mod=3) and checFizzBuzz(number=i, mod=5):
			print("Fizz Buzz")
		elif checFizzBuzz(number=i, mod=3):
			print("Fizz")
		elif checFizzBuzz(number=i, mod=5):
			print("Buzz")
		else:
			print(i)

if __name__ == '__main__':
	run(100)
