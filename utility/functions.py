import os

def checkFileExists(dir: str):
    return os.path.exists(dir)

def clearScreen():
    if os.name == 'posix':  # Linux or macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print("Unsupported OS")

def createFile(name: str = "Untitled.txt", source: str = ""):
    with open(name, "w") as file:
        file.write(source)