from utility.functions import *

def createTaskList():
	tasklist: list = []

	def handleOp1():
		taskname = input("task name: ")
		taskdesc = input("task description: ")
		clearScreen()
		print(f"└── added {taskname} \n")
		taskfinal = [taskname, taskdesc]
		tasklist.insert(1, taskfinal)

	def handleOp2():
		clearScreen()
		taskname = input("task name to remove: ")
		for task in tasklist:
			if task[0].lower() == taskname.lower():
				tasklist.remove(task)

	def handleOp3():
		clearScreen()
		for task in tasklist:
			print(f"{task[0]} :: {task[1]}")
		print("\n\n")

	def handleOp4():
		source: str = ""
   
		for task in tasklist:
			source + f"{task[0]}:\n		{task[1]}"
   
		createFile("bin\TaskList.txt", source)

	clearScreen()
	while True:
		option: str = input("1: add task\n2: remove task\n3: list tasks\n4: generate .txt\n\ninput: ")
		print()
		if option.isdigit and option == "1":
			handleOp1()
		elif option.isdigit and option == "2":
			handleOp2()
		elif option.isdigit and option == "3":
			handleOp3()
		elif option.isdigit and option == "4":
			handleOp4()

