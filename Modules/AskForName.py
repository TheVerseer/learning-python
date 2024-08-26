from modules.clearscreen import *

def askForName():
    namelist: list = []

    finished: bool = False

    clearScreen()
    while not finished:
        option: str = input("1: add name\n2: say hi\n\ninput: ")
        print()
        if option.isdigit and option == "1":
            name = input("name: ")
            print(f"└── added {name} \n")
            namelist.insert(1, name)
        elif option.isdigit and option == "2":
            finished = True
            for name in namelist:
                print("Hi,", name)
            namelist = []
