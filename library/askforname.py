from utility.functions import *

def askForName():
    namelist: list = []

    clearScreen()
    while True:
        option: str = input("1: add name\n2: say hi\n\noption: ")
        print()
        if option.isdigit and option == "1":
            name = input("name: ")
            clearScreen()
            print(f"└── added {name} \n")
            namelist.insert(1, name)
        elif option.isdigit and option == "2":
            clearScreen()
            for name in namelist:
                print("Hi,", name)
            namelist = []
            break