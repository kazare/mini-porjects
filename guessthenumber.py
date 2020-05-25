# User will guess the number

import random

# declaring variables
numToGuess = random.randint(1, 20)
tries = 0
maxTries = 6

print('Secret number %d' % numToGuess)

print("Welcome to the number guessing game!")

# create loop so user can make multiple guesses
while tries < maxTries:
	guess = int(input("Please input a number: "))
	tries += 1

	# if user's guess is too high
	if guess > numToGuess:
		print('''
Your guess is too high.
Number of guesses left: {0}
You just tried: {1}
			'''.format(maxTries - tries, guess))

	# if user's guess is too low
	if guess < numToGuess:
		print('''
Your guess is too low.
Number of guesses left: {0}
You just tried: {1}
			'''.format(maxTries - tries, guess))

	# if user's guess is correct show statment and then end loop
	if guess == numToGuess:
		print('''
You're correct! The number is {0}
It took you {1} tries!
		'''.format(numToGuess, tries))
		break

	# if user uses up all of their max tries and then end loop
	if tries == maxTries:
		print('''
Sorry time is up!
The number was %d
			''' % numToGuess)
		break
