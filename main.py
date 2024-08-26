from modules.askforname import *
from modules.clearscreen import *

while True:
	clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n" + "\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			askForName()

	input("\nPress 'Enter' or 'Return' to go back \nPress 'Esc' to exit\n")
	