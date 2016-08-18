answer = raw_input("Are you happy? ")

def question(answer):
	if answer.upper() == "YES":
		print "Awesome!"
		again = raw_input("Do you want to try again? ")
		try_again(again)
	elif answer.upper() == "NO":
		print "Shucks man :("
		again = raw_input("Do you want to try again? ")
		try_again(again)
	else:
		answer = raw_input("What? ")
		question(answer)

def try_again(again):
	if again.upper() == "YES":
		answer = raw_input("Are you happy? ")
		question(answer)
	elif again.upper() == "NO":
		raw_input("Press Enter to exit!")
	else:
		answer = raw_input("What??? ")
		try_again(answer)		

question(answer)