import random

exit = False
print ("--- Dice Generator ---")
while (exit == False):
	print ("The random dice number is " , random.randint(1,6))
	yeno = input("Would you like to Roll again Y/N ")
	if (yeno == "Y" or yeno == "y" or yeno == "Yes" or yeno == "YES" or yeno == "yes"):
		exit = False
	elif (yeno == "N" or yeno == "n" or yeno == "No" or yeno == "NO" or yeno == "no"):
		exit = True
	else:
		print("Yes or No wasn't entered so we will roll again")
