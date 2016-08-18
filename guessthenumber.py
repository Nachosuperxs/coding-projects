from time import sleep
import random
def delay(x):
	sleep(x)
print "Welcome to guess the number!"
print
print "You only have 3 tries"
print
answer = int(raw_input("From 1 to 10, which is the number? "))
number = random.randint(1,10)
total = 2
def another(try_again):
	if try_again.upper() == "YES":
		answer = int(raw_input("From 1 to 10, which is the number? "))
                number = random.randint(1,10)
		guessing(answer,number,total)
	elif try_again.upper() == "NO":
		print "Shutting Down..."
		delay(1.5)
		exit()
	else:
		try_again = raw_input("Do you want to try again?")
		another(try_again)
def guessing(answer,number,total):

	if number == answer:
		print "You have won!"
		input("ENTER to EXIT")
	elif total == 0:
		print
		print "Missed again! unfortunately, you have run out of tries, you lose!"
		print
		try_again = raw_input("Do you want to try again?")
		another(try_again)
	else:
		print
		print "You missed! Try again!"
		total = total - 1
		answer = int(raw_input("From 1 to 10, which is the number? "))
		guessing(answer,number,total)
guessing(answer,number,total)	

