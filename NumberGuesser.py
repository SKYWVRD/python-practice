import random

playGame = True
secretNumber = random.randint(0, 100)
playerAnswer = 0
maxTry = 5
win = False
attempt = 0

print("Guess the positive integer between 0 & 100")

while(playGame and attempt<maxTry):
	try:
		playerAnswer = int(input("Guess: "))

		if(playerAnswer == secretNumber):
			playGame = False
			win = True
		elif(playerAnswer > 100 or playerAnswer < 0):
			print("That is not in the range given")
		elif(playerAnswer > secretNumber):
			print("Too high")
		elif(playerAnswer < secretNumber):
			print("Too low")

		attempt = attempt + 1
	except:
		print("That is not an integer try again")

if(win):
	print("WELL PLAYED")
	
elif(not win):
	print("YOU LOSE, THE ANSWER WAS:", secretNumber)
