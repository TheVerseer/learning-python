import os

from library.askforname import *
from library.tasklist import *
from library.calculator import *

from utility.functions import *

if not checkFileExists("bin"):
	os.makedirs("bin")

while True:
	clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n2: TaskList\n3: Calculator" + "\n\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			askForName()
		elif option == "2":
			taskList()
		elif option == "3":
			calculator()

	input("\nPress 'Enter' or 'Return' to go back")
