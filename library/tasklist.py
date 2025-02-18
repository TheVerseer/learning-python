from utility.functions import *

def taskList():
	allTasks = []
	listname: str = ""
			
	def handleOp1():
		taskname = input("task name: ")
		taskdesc = input("task description: ")
		clearScreen()
		print(f"└── added {taskname} \n")
		
		allTasks.insert(1, [taskname, taskdesc])

	def handleOp2():
		clearScreen()
		taskname = input("task name to remove: ")
		for task in allTasks:
			if task[0].lower() == taskname.lower():
				allTasks.remove(task)

	def handleOp3():
		clearScreen()
		for task in allTasks:
			print(f"{task[0]}: {task[1]}")
		print("\n")

	def handleOp4():
		source: str = ""
   
		for task in allTasks:
			source = f"{source}{task[0]}:\n  {task[1]}\n\n"

		#createFile(f"bin/{listname}.txt", source)
		createFile(f"{listname}.txt", source)

	clearScreen()
	while True:
		if listname == "":
			givenInput = input("list name: ")
			#if checkFileExists(f"bin/{givenInput}.txt"):
			if checkFileExists(f"{givenInput}.txt"):
				print(f"'{givenInput}.txt' already exists, try a different name")
			else:
				print(f"'{givenInput}' list created\n")
				listname = givenInput
		else:
			option: str = input("1: add task\n2: remove task\n3: list tasks\n4: load .txt\n\noption: ")
			if option.isdigit and option == "1":
				handleOp1()
			elif option.isdigit and option == "2":
				handleOp2()
			elif option.isdigit and option == "3":
				handleOp3()
			elif option.isdigit and option == "4":
				handleOp4()
				break
