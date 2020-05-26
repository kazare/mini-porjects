# User will play rock, paper, scissors with the computer

# delcaring variables and importing random library
import random

rounds = 0
maxRounds = 6
userScore = 0
cpuScore = 0
options = ["rock", "paper", "scissors"]

print('''

	Welcome to rock, paper, scissors! Let's see who wins after %d rounds

	''' % maxRounds)

while rounds < maxRounds:
	cpu = random.choice(options)
	user = input("Please choose rock, paper, or scissors:")
	rounds += 1

	print("Computer chose: " + cpu)
	print("You chose: " + user)

	# if computer chooses rock
	if cpu == "rock":
		if user == "paper":
			print("Congrats! You won!! Paper beats rock!")
			userScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "scissors":
			print("You lost! Rock beats scissors")
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "rock":
			print("A tie!")
			userScore += 1
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))

	# if computer chooses paper
	elif cpu == "paper":
		if user == "scissors":
			print("Congrats! You won!! Scissors beats paper!")
			userScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "rock":
			print("You lost! Paper beats rock")
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "paper":
			print("A tie!")
			userScore += 1
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))

	# if computer chooses scissors
	elif cpu == "scissors":
		if user == "rock":
			print("Congrats! You won!! Rock beats scissors!")
			userScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "paper":
			print("You lost! Scissors beats paper")
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))
		if user == "scissors":
			print("A tie!")
			userScore += 1
			cpuScore += 1
			print("""
				You're score: {0}
				Computer's score: {1}
				""".format(userScore, cpuScore))

	if rounds == maxRounds:
		print('''

			Game over!

			''')
		if userScore > cpuScore:
			print("Congrats you won the game!")
		elif cpuScore > userScore:
			print("Sorry, the computer won. Better luck next time.")
		else:
			print(" The game ends in a tie! You both won!")
