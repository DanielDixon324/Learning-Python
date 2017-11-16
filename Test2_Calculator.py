def add (num1, num2):
	return num1 + num2
def sub (num1, num2):
	return num1 - num2
def mult (num1, num2):
	return num1 * num2
def divid (num1, num2):
	return num1 / num2	
	
	
	
Operand1 = int(input("Enter the first number "))
Operator1 = input("Enter the Operator e.g. - + / * ")
Operand2 = int(input("Enter the Second number "))

if Operator1 == "Times" or Operator1 == "*" or Operator1 == "times" or Operator1 == "multiply" or Operator1 == "x":
	print(mult(Operand1, Operand2))
elif Operator1 == "Minus" or Operator1 == "-" or Operator1 == "minus" or Operator1 == "subtract" :
	print(sub(Operand1, Operand2))
elif Operator1 == "Plus" or Operator1 == "+" or Operator1 == "plus":
	print(add(Operand1, Operand2))
elif Operator1 == "Divide" or Operator1 == "/" or Operator1 == "divide" :
	print(divid(Operand1, Operand2))
else :
	print ("That is not a viable operator")
