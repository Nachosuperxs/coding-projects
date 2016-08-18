from time import sleep
def delay(x):
	sleep(x)
print "Welcome to the menu of text-adventure-game!"
delay(0.5)
print "You will now see some options"
delay(0.5)
name = raw_input("What is your name? ")
delay(0.5)
name = name.title()
delay(0.5)
if name.upper() == "JOSE":
	print "Hello Admin!"
else:
	print "Nice you meet you " + name + "!"
delay(1)
print "Welcome to..."
delay(1)
def main_menu():
	print
	print "00------------------------------00"
	print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|"
	print "|                                |"
	print "|         TEXT ADVENTURE         |"
	print "|                                |"
	print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|"
	print "00------------------------------00"
	delay(0.5)
	print
	print
	print "NEW GAME"
	print
	print "CREDITS"
	print
	print "EXIT"
	print
delay(0.5)
main_menu()
option = raw_input("Select option ")
def menu(option):
	if option.upper() == "NEW GAME":
		print "The game isn't finished dum dum"
		delay(1)
		exit()
	elif option.upper() == "CREDITS":
                print
		print "This game was created by Jose Ignacio Rodriguez Labra"
		print ""
		print "This is his first game to experiment with the wonders of Python!"
		print ""
		exit_credits = raw_input("Press ENTER to go back to the menu ")
		main_menu()
		option = raw_input("Select option ")
		menu(option)
	elif option.upper() == "EXIT":
		def sure_to_exit():
                        print
			sure_exit = raw_input("Are you sure you want to exit the game? ")
			if sure_exit.upper() == "YES":
				exit()
			elif sure_exit.upper() == "NO":
				print
				main_menu()
				option = raw_input("Select option ")
				menu(option)
			else:
				sure_to_exit()
		sure_to_exit()
	else:
		option = raw_input("I didn't understand. Your options are: NEW GAME, CREDITS, and EXIT ")
		menu(option)
menu(option)
