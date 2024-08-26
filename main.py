import msvcrt

from library.askforname import *
from library.tasklist import *
from utility.functions import *

while True:
	clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n2: TaskList" + "\n\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			askForName()
		elif option == "2":
			taskList()

	input("\nPress 'Enter' or 'Return' to go back")
