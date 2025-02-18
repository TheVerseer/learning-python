import os

from library.askforname import *
from library.tasklist import *
from library.calculator import *
from library.shutdown import *

from utility.functions import *

while True:
	clearScreen()

	inputString: str = "Select a Module:\n\n1: AskForName\n2: TaskList\n3: Calculator\n4: Scheduled Shutdown" + "\n\nModule: "
	option: str = input(inputString)
	
	if option.isdigit():
		if option == "1":
			askForName()
		elif option == "2":
			taskList()
		elif option == "3":
			calculator()
		elif option == "4":
			shutdown()
	
	if option == "4":
		input("\nPress 'Enter' or 'Return' to go back and cancel shutdown")
		os.system("shutdown -a")
	else:
		input("\nPress 'Enter' or 'Return' to go back")
