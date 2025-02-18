import os

from utility.functions import *

def shutdown():
    clearScreen()

    #while True:
    clearScreen()

    option = input("Input a time value until shutdown (seconds): ")
	
    os.system(f"shutdown -s -t {option}")
        
        #input(f"\nShutting down in {option} seconds, press enter to cancel")
        #os.system("shutdown -a") 