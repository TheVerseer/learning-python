#rom library.askforname import *
#from library.clearscreen import *

#from main.functions import *

while True:
	#clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n" + "\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			print('what')
			#askForName()

	print("\nPress 'Enter' or 'Return' to go back \nPress 'Esc' to exit")
