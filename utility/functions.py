import os

def clearScreen():
    if os.name == 'posix':  # Linux or macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print("Unsupported OS")

def createFile(name: str = "Untitled.txt", source: str = "Hello world?"):
    with open(name, "w") as file:
        file.write(source)