from time import sleep
import random
def delay(x):
	sleep(x)
print "Welcome to the dice roll simulator"

def number_generator():
 	dice = random.randint(1,6)
 	return dice

answer = raw_input("Do you want to roll the dice? ")
def dice_function(answer):
	if answer.upper() == "YES":
		delay(0.5)
		print
		print number_generator()
		print
		answer = raw_input("Do you want to roll the dice again? ")
		dice_function(answer)
	elif answer.upper() == "NO":
		delay(0.5)
		print "Shutting down..."
		delay(1)
		exit()
	else:
		delay(0.5)
		answer = raw_input("I can't understand that, do you want to roll the dice? ")
		dice_function(answer)
dice_function(answer)