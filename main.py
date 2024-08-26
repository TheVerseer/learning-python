import keyboard

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

	print("\nPress 'Enter' or 'Return' to go back \nPress 'Esc' to exit")
	while True:
		if keyboard.is_pressed('enter'):
			exit = False
			break
		elif keyboard.is_pressed('esc'):
			exit = True
			break

	if exit:
		break
