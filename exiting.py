bye = raw_input("Type EXIT to quit the game ")

def exit_program(bye):
	if bye.upper() == "EXIT":
		exit()
	else:
		try_again = raw_input("Type EXIT to quit the game")
		exit_program(try_again)
		
exit_program(bye)