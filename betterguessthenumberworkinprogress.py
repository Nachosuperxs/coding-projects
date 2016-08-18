from time import sleep
import random
def delay(x):
	sleep(x)
print "Welcome to guess the number!"
print
print "From which number to which number do you want to try to guess?"

def first_input():
	first = int(raw_input("Lowest number: "))
	if first > 50:
		print "That number is too high, it had to be less than 50"
		first_input()
	elif first >= 0:
		first_number = first
	else:
		print "This number is too low!, it has to be bigger or equal to zero!"
		first_input()

def last_input():
	last = int(raw_input("Highest number: "))
	if last > 100:
		print "That would be too hard, it had to be less than 100"
		last_input()
	elif last > first:
		last_number = last
	else:
		print "This number is too low!, it has to be bigger or equal to your first number!"
		last_input()

first_input()
last_input()

def number_generator():
 	number = random.randint(first_number(),last_number())
 	return number

number_generator()



























"""answer = raw_input("Do you want to roll the dice? ")
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
dice_function(answer)"""