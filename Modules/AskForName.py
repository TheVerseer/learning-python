from Modules.ClearScreen import *

def askForName():
    namelist: list = []

    finished: bool = False

    print()
    clear_screen()
    while not finished:
        option: str = input("1: add name\n2: say hi\n\ninput: ")
        if option.isdigit and option == "1":
            name = input("name: ")
            print("└── added "+name)
            namelist.insert(1, name)
            print()
        elif option.isdigit and option == "2":
            finished = True
            for name in namelist:
                print("Hi,", name)
            print()
            namelist = []
