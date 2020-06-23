import random

exit = False
valid = False

while(not valid):
	try:
		diceNumber = int(input("How many dice do you want to throw?: "))
		total = 0
		valid = True
	except:
		print("Not a valid number")


while(not exit):
	response = input("Push Enter to generate random dice numbers")
	for x in range(diceNumber):
		result = random.randint(1, 6)
		print(result)
		total = total + result
		
	print("Total for dice roles is:", total)
