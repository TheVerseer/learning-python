from modules.askforname import *
from modules.clearscreen import *

inputString: str = "Select a Module:\n\n1: AskForName\n" + "\nModule: "
option: str = input(inputString)

if option.isdigit():
	if option == "1":
		askForName()
