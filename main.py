import msvcrt

from library.askforname import *
from library.clearscreen import *

from utility.functions import *

while True:
	exit: bool = False
	clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n" + "\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			askForName()

	print("\nPress 'Enter' or 'Return' to go back \nPress 'Esc' and 'Enter' to exit")

	while True:
		ch = msvcrt.getch()
		if ch == b'\r' or ch == b'\n':
			break
		elif ch == b'\x1b':
			exit = True
			break

	if exit:
		break
