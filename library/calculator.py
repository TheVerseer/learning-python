
def add(nums):
  sum = 0
  for n in nums:
    sum+=n
  return sum

def sub(nums):
  sum = 0
  for n in nums:
    sum-=n
  return sum

def div(nums):
  sum = 0
  for n in nums:
    sum/=n
  return sum

def mul(nums):
  sum = 0
  for n in nums:
    sum*=n
  return sum

def calculator():
	numbers = input("numbers (seperate with ','):")
	operator = input("operator to apply")
  
	numbers = numbers.replace(" ", "").split(",")
  
  
	if operator[1] == "+":
		print(f"sum: {add(numbers)}")
	elif operator[1] == "-":
		print(f"sum: {sub(numbers)}")
	elif operator[1] == "/":
		print(f"sum: {div(numbers)}")
	elif operator[1] == "*":
		print(f"sum: {mul(numbers)}")